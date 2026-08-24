#!/usr/bin/env python3
"""Run offline negative controls for the ChatGPT-native Episode Runtime Kernel."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from validate_packets import (
    PacketStop,
    validate_episode,
    validate_qualification,
    validate_return,
)


CASES_PATH = Path(__file__).with_name("runtime_cases.json")


def _set_path(document: dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    current = document
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = value


def _run(case: dict[str, Any], data: dict[str, Any]) -> dict[str, str]:
    episode = copy.deepcopy(data["base_episode"])
    returned = copy.deepcopy(data["base_return"])
    qualification = copy.deepcopy(data["base_qualification"])
    targets = {"episode": episode, "return": returned, "qualification": qualification}
    for mutation in case["mutations"]:
        _set_path(targets[mutation["target"]], mutation["path"], mutation["value"])

    try:
        if case["kind"] == "episode":
            validate_episode(episode)
        elif case["kind"] == "return":
            validate_return(episode, returned)
        elif case["kind"] == "qualification":
            validate_qualification(episode, returned, qualification)
        else:
            return {"status": "HARNESS_ERROR", "reason": "UNKNOWN_CASE_KIND"}
    except PacketStop as exc:
        return {"status": "STOP", "reason": exc.reason}
    return {"status": "PASS"}


def main() -> int:
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    failures = 0
    for case in data["cases"]:
        actual = _run(case, data)
        expected = case["expect"]
        passed = actual == expected
        if not passed:
            failures += 1
        print(
            f"{case['id']}: {'PASS' if passed else 'FAIL'} "
            f"expected={expected} actual={actual}"
        )
    print(f"\nFixture verdict: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    print("Claim: static packet and invariant regression only; native runtime behavior remains unverified.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

