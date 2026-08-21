#!/usr/bin/env python3
"""R20 dispatch + work eval harness for the two-pass Entry Gateway."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from gateway import DEFAULT_MODEL, EntryGateway, GatewayError

CASES_PATH = Path(__file__).with_name("r20_cases.json")


def load_cases() -> dict:
    return json.loads(CASES_PATH.read_text(encoding="utf-8"))


def validate_cases(data: dict) -> None:
    valid_relations = {"BOUND", "NEW_CHANGED"}
    valid_admissions = {"NOT_APPLICABLE", "DIRECT", "FORMATION"}
    if not isinstance(data.get("cases"), list) or not data["cases"]:
        raise ValueError("cases must be a non-empty list")
    ids = set()
    for case in data["cases"]:
        if case["id"] in ids:
            raise ValueError(f"duplicate case id: {case['id']}")
        ids.add(case["id"])
        if not case.get("turns"):
            raise ValueError(f"{case['id']} has no turns")
        for turn in case["turns"]:
            expect = turn["expect"]
            if expect["context_relation"] not in valid_relations:
                raise ValueError(f"{case['id']}: invalid context_relation")
            if expect["admission"] not in valid_admissions:
                raise ValueError(f"{case['id']}: invalid admission")
            if expect["context_relation"] == "BOUND" and expect["admission"] != "NOT_APPLICABLE":
                raise ValueError(f"{case['id']}: BOUND must expect NOT_APPLICABLE")
            if expect["context_relation"] == "NEW_CHANGED" and expect["admission"] == "NOT_APPLICABLE":
                raise ValueError(f"{case['id']}: NEW_CHANGED must expect DIRECT or FORMATION")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run R20 Entry Gateway evals")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default="low",
                        choices=["none", "low", "medium", "high", "xhigh", "max"])
    parser.add_argument("--validate-only", action="store_true",
                        help="Validate harness/cases without calling the API.")
    parser.add_argument("--json-out", type=Path,
                        help="Optional path for the complete eval record.")
    args = parser.parse_args()

    data = load_cases()
    validate_cases(data)
    if args.validate_only:
        print(f"PASS: {len(data['cases'])} eval cases validated")
        return 0

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is required", file=sys.stderr)
        return 2

    record = {
        "eval_version": data.get("version"),
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "cases": [],
    }
    failures = 0

    for case in data["cases"]:
        print(f"\n== {case['id']} ==")
        gateway = EntryGateway(api_key, args.model, args.reasoning_effort)
        case_record = {"id": case["id"], "turns": []}
        for index, turn in enumerate(case["turns"], start=1):
            try:
                result = gateway.handle(turn["prompt"])
                decision = result["entry_decision"]
                expected = turn["expect"]
                dispatch_pass = (
                    decision["context_relation"] == expected["context_relation"]
                    and decision["admission"] == expected["admission"]
                )
                if not dispatch_pass:
                    failures += 1
                print(
                    f"turn {index}: "
                    f"{decision['context_relation']}/{decision['admission']} "
                    f"expected {expected['context_relation']}/{expected['admission']} "
                    f"=> {'PASS' if dispatch_pass else 'FAIL'}"
                )
                case_record["turns"].append(
                    {
                        "prompt": turn["prompt"],
                        "expect": expected,
                        "entry_decision": decision,
                        "dispatch_pass": dispatch_pass,
                        "dispatch_meta": result["dispatch_meta"],
                        "work_meta": result["work_meta"],
                        "answer": result["answer"],
                    }
                )
            except GatewayError as exc:
                failures += 1
                print(f"turn {index}: ERROR {exc}")
                case_record["turns"].append(
                    {
                        "prompt": turn["prompt"],
                        "expect": turn["expect"],
                        "error": str(exc),
                        "dispatch_pass": False,
                    }
                )
                break
        record["cases"].append(case_record)

    record["completed_at"] = datetime.now(timezone.utc).isoformat()
    record["dispatch_failures"] = failures
    record["dispatch_verdict"] = "PASS" if failures == 0 else "FAIL"

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote eval record: {args.json_out}")

    print(f"\nDispatch verdict: {record['dispatch_verdict']} ({failures} failures)")
    print("Final-answer behavioral quality is intentionally retained in the record for separate claim-matched review.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
