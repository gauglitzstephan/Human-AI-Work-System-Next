#!/usr/bin/env python3
"""Deterministic validator for native Episode, Return, and Qualification packets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SAFE_OPERATIONS = {"READ", "ANALYZE", "DRAFT_EPHEMERAL", "VALIDATE", "RETURN"}
REQUIRED_BLOCKS = {
    "PERSISTENT_WRITE",
    "EXTERNAL_ACTION",
    "APPLICATION_PRODUCTION",
    "SUBMISSION_OR_RELEASE",
    "PROMOTION",
}
PILOT_METHOD_STATUSES = {"QUALIFIED", "CANDIDATE", "PILOT_ONLY"}
PILOT_CAPABILITY_STATUSES = {"QUALIFIED", "PILOT_ONLY"}

EPISODE_KEYS = {
    "episode_id", "parent", "trigger", "work_unit", "work_basis", "method",
    "provider", "assurance", "authorization", "inputs", "requirements",
    "output_contract", "return_condition", "claim", "effects",
}
PARENT_KEYS = {
    "work_object", "outcome", "controlling_source", "state_version", "gate",
    "active_frontier",
}
TRIGGER_KEYS = {"kind", "summary", "continues_active_frontier"}
WORK_UNIT_KEYS = {
    "id", "work_function", "transformation", "child_to_parent_contribution",
}
METHOD_KEYS = {"id", "source", "status", "fit"}
PROVIDER_KEYS = {"id", "surface", "capability_status"}
ASSURANCE_KEYS = {"provider_id", "mode", "capability_status"}
AUTHORIZATION_KEYS = {
    "basis", "actor", "allowed_operations", "write_path", "blocked_transitions",
}
CLAIM_KEYS = {"intended", "allowed_return_claims"}
EFFECT_KEYS = {"mode", "promotion_allowed"}

RETURN_KEYS = {
    "episode_id", "parent_state_version_seen", "provider_id", "work_performed",
    "output", "child_to_parent_contribution", "evidence_used", "method_applied",
    "assumptions", "blockers", "assurance_applied", "supported_claim", "readiness",
    "operations_performed", "writes_performed", "external_actions_performed",
    "parent_status_claim", "promotion_claim", "human_or_authority_need",
    "recommended_frontier",
}

QUALIFICATION_KEYS = {
    "episode_id", "parent_state_version_rebound", "evaluator_id", "mode",
    "claim_evaluated", "evidence_used", "checks", "failures", "verdict",
    "supported_claim", "parent_status_claim", "promotion_claim",
}


class PacketStop(ValueError):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


def _object(value: Any, reason: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise PacketStop(reason)
    return value


def _exact_keys(value: dict[str, Any], keys: set[str], reason: str) -> None:
    if set(value) != keys:
        raise PacketStop(reason)


def _text(value: Any, reason: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise PacketStop(reason)
    return value.strip()


def _strings(value: Any, reason: str, *, nonempty: bool = False) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise PacketStop(reason)
    if nonempty and not value:
        raise PacketStop(reason)
    return value


def validate_episode(packet: Any) -> dict[str, Any]:
    episode = _object(packet, "EPISODE_NOT_OBJECT")
    _exact_keys(episode, EPISODE_KEYS, "EPISODE_FIELDS_INVALID")

    _text(episode["episode_id"], "EPISODE_ID_MISSING")
    parent = _object(episode["parent"], "PARENT_NOT_OBJECT")
    _exact_keys(parent, PARENT_KEYS, "PARENT_FIELDS_INVALID")
    for key in PARENT_KEYS:
        _text(parent[key], f"PARENT_{key.upper()}_MISSING")

    trigger = _object(episode["trigger"], "TRIGGER_NOT_OBJECT")
    _exact_keys(trigger, TRIGGER_KEYS, "TRIGGER_FIELDS_INVALID")
    if trigger["kind"] not in {"REQUEST", "CONTINUATION", "AUTHORIZATION"}:
        raise PacketStop("TRIGGER_KIND_INVALID")
    _text(trigger["summary"], "TRIGGER_SUMMARY_MISSING")
    if not isinstance(trigger["continues_active_frontier"], bool):
        raise PacketStop("TRIGGER_RELATION_INVALID")

    work_unit = _object(episode["work_unit"], "WORK_UNIT_NOT_OBJECT")
    _exact_keys(work_unit, WORK_UNIT_KEYS, "WORK_UNIT_FIELDS_INVALID")
    for key in WORK_UNIT_KEYS:
        _text(work_unit[key], f"WORK_UNIT_{key.upper()}_MISSING")

    if episode["work_basis"] != "PILOT_TEST":
        raise PacketStop("WORK_BASIS_NOT_PILOT")

    method = _object(episode["method"], "METHOD_NOT_OBJECT")
    _exact_keys(method, METHOD_KEYS, "METHOD_FIELDS_INVALID")
    _text(method["id"], "METHOD_ID_MISSING")
    _text(method["source"], "METHOD_SOURCE_MISSING")
    if method["status"] == "UNAVAILABLE":
        raise PacketStop("METHOD_UNAVAILABLE")
    if method["status"] == "UNVERIFIED":
        raise PacketStop("METHOD_UNVERIFIED")
    if method["status"] not in PILOT_METHOD_STATUSES:
        raise PacketStop("METHOD_NOT_ADMITTED")
    if method["status"] in {"CANDIDATE", "PILOT_ONLY"} and method["fit"] != "ESTABLISHED_FOR_PILOT":
        raise PacketStop("METHOD_PILOT_FIT_MISSING")
    if method["status"] == "QUALIFIED" and method["fit"] not in {"ESTABLISHED", "ESTABLISHED_FOR_PILOT"}:
        raise PacketStop("METHOD_FIT_MISSING")

    provider = _object(episode["provider"], "PROVIDER_NOT_OBJECT")
    _exact_keys(provider, PROVIDER_KEYS, "PROVIDER_FIELDS_INVALID")
    _text(provider["id"], "PROVIDER_ID_MISSING")
    if provider["surface"] not in {"CHAT", "WORK", "CODEX", "TOOL", "HUMAN"}:
        raise PacketStop("PROVIDER_SURFACE_INVALID")
    if provider["capability_status"] == "UNAVAILABLE":
        raise PacketStop("PROVIDER_UNAVAILABLE")
    if provider["capability_status"] == "UNVERIFIED":
        raise PacketStop("PROVIDER_UNVERIFIED")
    if provider["capability_status"] not in PILOT_CAPABILITY_STATUSES:
        raise PacketStop("PROVIDER_NOT_ADMITTED")

    assurance = _object(episode["assurance"], "ASSURANCE_NOT_OBJECT")
    _exact_keys(assurance, ASSURANCE_KEYS, "ASSURANCE_FIELDS_INVALID")
    _text(assurance["provider_id"], "ASSURANCE_PROVIDER_MISSING")
    if assurance["provider_id"] == provider["id"]:
        raise PacketStop("ASSURANCE_NOT_SEPARATED")
    if assurance["mode"] not in {"DETERMINISTIC", "SEPARATE_CONTEXT", "INDEPENDENT", "RECIPIENT_USE"}:
        raise PacketStop("ASSURANCE_MODE_INVALID")
    if assurance["capability_status"] == "UNAVAILABLE":
        raise PacketStop("ASSURANCE_UNAVAILABLE")
    if assurance["capability_status"] == "UNVERIFIED":
        raise PacketStop("ASSURANCE_UNVERIFIED")
    if assurance["capability_status"] not in PILOT_CAPABILITY_STATUSES:
        raise PacketStop("ASSURANCE_NOT_ADMITTED")

    authorization = _object(episode["authorization"], "AUTHORIZATION_NOT_OBJECT")
    _exact_keys(authorization, AUTHORIZATION_KEYS, "AUTHORIZATION_FIELDS_INVALID")
    if authorization["basis"] not in {
        "EXPLICIT_ACTION_AUTHORIZATION", "PARENT_WORK_BASIS", "CONTINUATION_TRIGGER"
    }:
        raise PacketStop("AUTHORIZATION_BASIS_INVALID")
    if authorization["basis"] == "CONTINUATION_TRIGGER":
        raise PacketStop("CONTINUATION_NOT_AUTHORITY")
    _text(authorization["actor"], "AUTHORIZATION_ACTOR_MISSING")
    allowed_operations = set(_strings(
        authorization["allowed_operations"], "ALLOWED_OPERATIONS_INVALID", nonempty=True
    ))
    if not allowed_operations.issubset(SAFE_OPERATIONS):
        raise PacketStop("EFFECT_OPERATION_REQUESTED")
    if authorization["write_path"] is not None:
        raise PacketStop("WRITE_PATH_FORBIDDEN")
    blocked = set(_strings(
        authorization["blocked_transitions"], "BLOCKED_TRANSITIONS_INVALID", nonempty=True
    ))
    if not REQUIRED_BLOCKS.issubset(blocked):
        raise PacketStop("EFFECT_BLOCKS_INCOMPLETE")

    if trigger["kind"] == "CONTINUATION" and not trigger["continues_active_frontier"]:
        raise PacketStop("CONTINUATION_FRONTIER_DRIFT")
    if trigger["kind"] == "CONTINUATION" and work_unit["id"] != parent["active_frontier"]:
        raise PacketStop("CONTINUATION_FRONTIER_DRIFT")

    _strings(episode["inputs"], "INPUTS_INVALID")
    _strings(episode["requirements"], "REQUIREMENTS_INVALID", nonempty=True)
    _text(episode["output_contract"], "OUTPUT_CONTRACT_MISSING")
    _text(episode["return_condition"], "RETURN_CONDITION_MISSING")

    claim = _object(episode["claim"], "CLAIM_NOT_OBJECT")
    _exact_keys(claim, CLAIM_KEYS, "CLAIM_FIELDS_INVALID")
    _text(claim["intended"], "INTENDED_CLAIM_MISSING")
    _strings(claim["allowed_return_claims"], "RETURN_CLAIMS_INVALID", nonempty=True)

    effects = _object(episode["effects"], "EFFECTS_NOT_OBJECT")
    _exact_keys(effects, EFFECT_KEYS, "EFFECT_FIELDS_INVALID")
    if effects["mode"] != "DISABLED":
        raise PacketStop("EFFECT_MODE_NOT_DISABLED")
    if effects["promotion_allowed"] is not False:
        raise PacketStop("PROMOTION_DISABLED")

    return episode


def validate_return(episode_packet: Any, return_packet: Any) -> dict[str, Any]:
    episode = validate_episode(episode_packet)
    returned = _object(return_packet, "RETURN_NOT_OBJECT")
    _exact_keys(returned, RETURN_KEYS, "RETURN_FIELDS_INVALID")

    if returned["episode_id"] != episode["episode_id"]:
        raise PacketStop("RETURN_EPISODE_MISMATCH")
    if returned["parent_state_version_seen"] != episode["parent"]["state_version"]:
        raise PacketStop("RETURN_STALE_PARENT")
    if returned["provider_id"] != episode["provider"]["id"]:
        raise PacketStop("RETURN_PROVIDER_MISMATCH")
    if returned["method_applied"] != episode["method"]["id"]:
        raise PacketStop("RETURN_METHOD_MISMATCH")
    _text(returned["work_performed"], "RETURN_WORK_MISSING")
    _text(returned["child_to_parent_contribution"], "RETURN_CONTRIBUTION_MISSING")
    for key in (
        "evidence_used", "assumptions", "blockers", "assurance_applied",
        "human_or_authority_need",
    ):
        _strings(returned[key], f"RETURN_{key.upper()}_INVALID")
    if returned["supported_claim"] not in episode["claim"]["allowed_return_claims"]:
        raise PacketStop("RETURN_CLAIM_OUT_OF_SCOPE")
    if returned["readiness"] not in {"COMPLETE_FOR_RETURN", "PARTIAL", "BLOCKED"}:
        raise PacketStop("RETURN_READINESS_INVALID")
    operations = set(_strings(
        returned["operations_performed"], "RETURN_OPERATIONS_INVALID"
    ))
    if not operations.issubset(set(episode["authorization"]["allowed_operations"])):
        raise PacketStop("RETURN_OPERATION_NOT_AUTHORIZED")
    writes = _strings(returned["writes_performed"], "RETURN_WRITES_INVALID")
    actions = _strings(
        returned["external_actions_performed"], "RETURN_EXTERNAL_ACTIONS_INVALID"
    )
    if writes or actions:
        raise PacketStop("RETURN_EFFECT_CLAIM")
    if returned["parent_status_claim"] is not None:
        raise PacketStop("RETURN_PARENT_STATUS_CLAIM")
    if returned["promotion_claim"] is not False:
        raise PacketStop("RETURN_PROMOTION_CLAIM")
    _text(returned["recommended_frontier"], "RETURN_FRONTIER_MISSING")
    return returned


def validate_qualification(
    episode_packet: Any,
    return_packet: Any,
    qualification_packet: Any,
) -> dict[str, Any]:
    episode = validate_episode(episode_packet)
    returned = validate_return(episode, return_packet)
    qualification = _object(qualification_packet, "QUALIFICATION_NOT_OBJECT")
    _exact_keys(qualification, QUALIFICATION_KEYS, "QUALIFICATION_FIELDS_INVALID")

    if qualification["episode_id"] != episode["episode_id"]:
        raise PacketStop("QUALIFICATION_EPISODE_MISMATCH")
    if qualification["parent_state_version_rebound"] != episode["parent"]["state_version"]:
        raise PacketStop("QUALIFICATION_STALE_PARENT")
    if qualification["evaluator_id"] != episode["assurance"]["provider_id"]:
        raise PacketStop("QUALIFICATION_PROVIDER_MISMATCH")
    if qualification["evaluator_id"] == returned["provider_id"]:
        raise PacketStop("ASSURANCE_NOT_SEPARATED")
    if qualification["mode"] != episode["assurance"]["mode"]:
        raise PacketStop("QUALIFICATION_MODE_MISMATCH")
    if qualification["claim_evaluated"] != episode["claim"]["intended"]:
        raise PacketStop("QUALIFICATION_CLAIM_MISMATCH")
    _strings(qualification["evidence_used"], "QUALIFICATION_EVIDENCE_INVALID")
    _strings(qualification["checks"], "QUALIFICATION_CHECKS_MISSING", nonempty=True)
    failures = _strings(qualification["failures"], "QUALIFICATION_FAILURES_INVALID")
    if qualification["verdict"] not in {"PASS", "FAIL", "UNVERIFIED"}:
        raise PacketStop("QUALIFICATION_VERDICT_INVALID")
    if qualification["verdict"] == "PASS" and failures:
        raise PacketStop("QUALIFICATION_PASS_WITH_FAILURES")
    if qualification["verdict"] == "PASS" and qualification["supported_claim"] != episode["claim"]["intended"]:
        raise PacketStop("QUALIFICATION_SUPPORTED_CLAIM_MISMATCH")
    _text(qualification["supported_claim"], "QUALIFICATION_SUPPORTED_CLAIM_MISSING")
    if qualification["parent_status_claim"] is not None:
        raise PacketStop("QUALIFICATION_PARENT_STATUS_CLAIM")
    if qualification["promotion_claim"] is not False:
        raise PacketStop("QUALIFICATION_PROMOTION_CLAIM")
    return qualification


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate native Episode Runtime packets")
    sub = parser.add_subparsers(dest="kind", required=True)
    episode_parser = sub.add_parser("episode")
    episode_parser.add_argument("episode", type=Path)
    return_parser = sub.add_parser("return")
    return_parser.add_argument("episode", type=Path)
    return_parser.add_argument("provider_return", type=Path)
    qualification_parser = sub.add_parser("qualification")
    qualification_parser.add_argument("episode", type=Path)
    qualification_parser.add_argument("provider_return", type=Path)
    qualification_parser.add_argument("qualification", type=Path)
    args = parser.parse_args()

    try:
        if args.kind == "episode":
            validate_episode(_load(args.episode))
        elif args.kind == "return":
            validate_return(_load(args.episode), _load(args.provider_return))
        else:
            validate_qualification(
                _load(args.episode),
                _load(args.provider_return),
                _load(args.qualification),
            )
    except (OSError, json.JSONDecodeError, PacketStop) as exc:
        reason = exc.reason if isinstance(exc, PacketStop) else f"INPUT_ERROR: {exc}"
        print(json.dumps({"status": "STOP", "reason": reason}))
        return 1

    print(json.dumps({"status": "PASS", "claim": f"{args.kind.upper()}_PACKET_INTEGRITY"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

