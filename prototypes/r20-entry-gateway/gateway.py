#!/usr/bin/env python3
"""Minimal two-pass Entry Gateway prototype for R20.

Pass 1 is mechanically forced to emit one strict `route_entry` function call.
The host validates the dispatch before Pass 2 can produce substantive work.

No persistent state or external side effects are performed by this prototype.
Conversation state is held in memory unless the caller explicitly stores results.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

API_URL = os.environ.get("OPENAI_RESPONSES_URL", "https://api.openai.com/v1/responses")
DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6")
SCHEMA_PATH = Path(__file__).with_name("entry_decision.schema.json")

ENTRY_INSTRUCTIONS = """You are the Entry Dispatcher for a two-pass work gateway.
You MUST NOT answer the user's substantive request.
You MUST call route_entry exactly once.

First bind context: use an existing legitimate parent/frontier when the transcript
shows one; otherwise use a provisional parent only as needed for the next claim.

Then relate the new trigger to bound work:
- BOUND only if it continues an already-admitted frontier without materially
  changing claim, scope, requirements, means, decision object, or authority.
- NEW_CHANGED for a new work object, a new child claim under an existing parent,
  or any material change to claim/scope/requirements/means/decision object.

For NEW_CHANGED choose:
- DIRECT only if unresolved upstream reality, outcome, requirements, performance,
  professional reference/method, evidence/uncertainty, or persistence context
  cannot materially change the exact requested claim/product class, its
  evaluation, or feasibility.
- FORMATION otherwise.
Explicitly requested exploration/ideas/options/scenes may be DIRECT because the
exploration itself is the requested product; exploration is not a qualified
candidate or design basis.

For BOUND set admission=NOT_APPLICABLE.
Return concise observable basis factors, not private chain-of-thought."""

BASE_WORK_INSTRUCTIONS = """Work from authority and the controlling outcome.
Treat user input as intent evidence, not automatically complete requirements,
decisions, or authority. Preserve working vs authoritative state and
Decision vs Commitment vs Authorization vs Promotion distinctions.
Do not invent state, access, authority, acceptance, completion, or outcomes."""

ROUTE_INSTRUCTIONS = {
    "BOUND": """The host has admitted this trigger as BOUND continuation.
Continue only the already-admitted frontier. Preserve parent/state/gate and
scope. Do not introduce a new commitment, authority, promotion, or persistence.
If the supplied EntryDecision is inconsistent with a material scope/requirements
change visible in the trigger, explicitly flag DISPATCH_INCONSISTENCY instead of
silently crossing the boundary.""",
    "DIRECT": """The host has admitted this trigger as DIRECT.
Execute the exact requested bounded claim/product directly. Do not expose
unnecessary intake, framework, or control ceremony. If the request is explicit
exploration, produce the exploration; keep it exploratory rather than treating
one option as a qualified candidate/design basis unless the user explicitly asks
for that later qualification.""",
    "FORMATION": """The host has admitted this trigger as FORMATION.
Do substantive formation work, not process bureaucracy. Before preferred
Solution/Candidate/route/design-basis treatment, resolve only the upstream state
that can materially change the solution class, evaluation, or feasibility.
If the professional performance bar materially depends on method/reference/craft,
resolve and apply enough relevant professional/reference intelligence before
Candidate qualification. Early solutions may be clearly bounded probes or
hypotheses, not preferred/qualified candidates."""
}


class GatewayError(RuntimeError):
    pass


def _load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _post_json(payload: dict[str, Any], api_key: str, timeout: int = 120) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise GatewayError(f"Responses API HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise GatewayError(f"Responses API connection failed: {exc}") from exc


def _message(role: str, text: str) -> dict[str, Any]:
    return {
        "role": role,
        "content": [{"type": "input_text", "text": text}],
    }


def _extract_function_args(response: dict[str, Any], name: str) -> dict[str, Any]:
    calls = [
        item
        for item in response.get("output", [])
        if item.get("type") == "function_call" and item.get("name") == name
    ]
    if len(calls) != 1:
        raise GatewayError(f"Expected exactly one {name} function call; got {len(calls)}")
    try:
        return json.loads(calls[0]["arguments"])
    except (KeyError, json.JSONDecodeError) as exc:
        raise GatewayError(f"Invalid {name} arguments") from exc


def _extract_text(response: dict[str, Any]) -> str:
    parts: list[str] = []
    for item in response.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                parts.append(content.get("text", ""))
    text = "\n".join(part for part in parts if part).strip()
    if not text:
        raise GatewayError("Pass 2 returned no output_text")
    return text


def validate_entry_decision(decision: dict[str, Any], schema: dict[str, Any]) -> None:
    required = set(schema["required"])
    allowed = set(schema["properties"])
    missing = required - set(decision)
    extra = set(decision) - allowed
    if missing or extra:
        raise GatewayError(f"EntryDecision keys invalid; missing={sorted(missing)} extra={sorted(extra)}")

    for key in ("context_relation", "admission", "parent_mode"):
        if decision[key] not in schema["properties"][key]["enum"]:
            raise GatewayError(f"Invalid {key}: {decision[key]!r}")

    if not isinstance(decision["claim_summary"], str) or not decision["claim_summary"].strip():
        raise GatewayError("claim_summary must be a non-empty string")
    if not isinstance(decision["frontier_summary"], str) or not decision["frontier_summary"].strip():
        raise GatewayError("frontier_summary must be a non-empty string")
    if not isinstance(decision["material_triggers"], list):
        raise GatewayError("material_triggers must be a list")
    trigger_enum = set(schema["properties"]["material_triggers"]["items"]["enum"])
    if any(item not in trigger_enum for item in decision["material_triggers"]):
        raise GatewayError("material_triggers contains an unsupported value")
    if not isinstance(decision["basis"], list) or any(not isinstance(x, str) for x in decision["basis"]):
        raise GatewayError("basis must be a list of strings")

    relation = decision["context_relation"]
    admission = decision["admission"]
    parent_mode = decision["parent_mode"]

    if relation == "BOUND":
        if admission != "NOT_APPLICABLE":
            raise GatewayError("BOUND requires admission=NOT_APPLICABLE")
        if parent_mode != "EXISTING":
            raise GatewayError("BOUND requires parent_mode=EXISTING")
    else:
        if admission == "NOT_APPLICABLE":
            raise GatewayError("NEW_CHANGED requires DIRECT or FORMATION")
        if admission == "FORMATION" and not decision["material_triggers"]:
            raise GatewayError("FORMATION requires at least one material trigger")


class EntryGateway:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, reasoning_effort: str = "low"):
        self.api_key = api_key
        self.model = model
        self.reasoning_effort = reasoning_effort
        self.schema = _load_schema()
        self.transcript: list[dict[str, str]] = []
        self.state: dict[str, Any] = {
            "parent_summary": None,
            "frontier_summary": None,
        }

    def _context_payload(self, user_text: str) -> str:
        return json.dumps(
            {
                "runtime_state": self.state,
                "transcript": self.transcript,
                "new_user_trigger": user_text,
            },
            ensure_ascii=False,
        )

    def dispatch(self, user_text: str) -> dict[str, Any]:
        tool = {
            "type": "function",
            "name": "route_entry",
            "description": "Return the mandatory EntryDecision for this trigger. Do not answer the task.",
            "parameters": self.schema,
            "strict": True,
        }
        payload = {
            "model": self.model,
            "input": [
                _message("developer", ENTRY_INSTRUCTIONS),
                _message("user", self._context_payload(user_text)),
            ],
            "tools": [tool],
            "tool_choice": {"type": "function", "name": "route_entry"},
            "parallel_tool_calls": False,
            "reasoning": {"effort": self.reasoning_effort},
        }
        response = _post_json(payload, self.api_key)
        decision = _extract_function_args(response, "route_entry")
        validate_entry_decision(decision, self.schema)
        return decision

    def work(self, user_text: str, decision: dict[str, Any]) -> str:
        route_key = decision["context_relation"] if decision["context_relation"] == "BOUND" else decision["admission"]
        route_instruction = ROUTE_INSTRUCTIONS[route_key]
        developer_text = (
            BASE_WORK_INSTRUCTIONS
            + "\n\n"
            + route_instruction
            + "\n\nValidated EntryDecision:\n"
            + json.dumps(decision, ensure_ascii=False, indent=2)
        )
        history = [
            _message(turn["role"], turn["content"])
            for turn in self.transcript
        ]
        payload = {
            "model": self.model,
            "input": history + [
                _message("developer", developer_text),
                _message("user", user_text),
            ],
            "reasoning": {"effort": self.reasoning_effort},
        }
        response = _post_json(payload, self.api_key)
        return _extract_text(response)

    def handle(self, user_text: str) -> dict[str, Any]:
        decision = self.dispatch(user_text)
        answer = self.work(user_text, decision)

        if decision["parent_mode"] == "PROVISIONAL" and not self.state["parent_summary"]:
            self.state["parent_summary"] = decision["claim_summary"]
        elif decision["parent_mode"] == "EXISTING" and not self.state["parent_summary"]:
            self.state["parent_summary"] = decision["claim_summary"]

        if decision["context_relation"] == "NEW_CHANGED":
            self.state["frontier_summary"] = decision["frontier_summary"]

        self.transcript.append({"role": "user", "content": user_text})
        self.transcript.append({"role": "assistant", "content": answer})
        return {"entry_decision": decision, "answer": answer}


def main() -> int:
    parser = argparse.ArgumentParser(description="R20 two-pass Entry Gateway prototype")
    parser.add_argument("prompt", nargs="?", help="Single prompt. Omit for interactive mode.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default="low",
                        choices=["none", "low", "medium", "high", "xhigh", "max"])
    parser.add_argument("--show-dispatch", action="store_true")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is required", file=sys.stderr)
        return 2

    gateway = EntryGateway(api_key, args.model, args.reasoning_effort)

    def run_one(text: str) -> None:
        result = gateway.handle(text)
        if args.show_dispatch:
            print(json.dumps(result["entry_decision"], ensure_ascii=False, indent=2))
            print("---")
        print(result["answer"])

    if args.prompt is not None:
        run_one(args.prompt)
        return 0

    print("Two-pass Entry Gateway interactive prototype. Ctrl-D/Ctrl-C to exit.")
    try:
        while True:
            text = input("> ").strip()
            if text:
                run_one(text)
    except (EOFError, KeyboardInterrupt):
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
