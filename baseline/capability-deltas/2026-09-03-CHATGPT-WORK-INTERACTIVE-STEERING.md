# Capability Delta — ChatGPT Work interactive steering

**Status:** CANDIDATE evidence/impact record — reconciled to promoted Native Work Transition  
**Date:** 2026-09-03  
**Purpose:** Bind one product delta to the smallest supported system consequence. This is not a new workflow, architecture layer or Work Contract.

## Delta

Current ChatGPT Work product behavior supports interactive steering during execution: Work can expose progress, ask questions and accept Human direction while the task is running. Separately, a previously observed Chat UI route for continuing from Chat into Work is no longer visible in the observed surface; underlying removal of the capability is not established by that UI observation alone.

## Evidence status

- Interactive Work steering: `CONFIRMED_PRODUCT_CHANGE` based on current OpenAI product/release documentation reviewed on 2026-09-03.
- Missing prior three-dot Chat→Work action: `OBSERVED_SURFACE_CHANGE`; capability removal is not established.

This record intentionally does not freeze a specific UI path as a durable system requirement.

## Affected assumption and owner

A Chat→Work model that distinguishes Chat and Work by **interactivity** or treats Work as a primarily silent downstream executor is no longer reliable.

The legitimate owner of the affected transition semantics is the promoted `baseline/NATIVE-WORK-TRANSITION.md` on authoritative `main@7cd5b5490f67638e5eb6d85ff1fbb62cfabb1f4f` (blob `a33285e59c6b836e1bbea4ef662a46cf94b90676`). This record does not define a parallel handoff or Work Contract.

## Classification

`EXTERNAL_CAPABILITY_DELTA`

Primary dependency: Chat/Project → Work transition semantics, routed to their existing authoritative owner.

## Bounded disposition

- Interactive Work steering: originally `CANDIDATE_SEMANTIC_CHANGE`; the change is now absorbed by the promoted Native Work Transition on `main@7cd5b5490f67638e5eb6d85ff1fbb62cfabb1f4f`. Its explicit ordinary-interaction, material re-entry and UI-independent transition semantics, together with the protected-commitment, operational-autonomy and no-silent-mutation rules, cover the acceptance constraints. No additional Chat→Work semantic change remains pending from this episode.
- Missing prior three-dot Chat→Work action: `TEST`. It remains an unresolved surface observation. No capability-removal or architecture claim follows unless stronger evidence establishes a material underlying impact.

PR #51 is promoted and read back at the authoritative identity above. This PR #50 record now binds to that promoted source rather than the former Candidate head.

## System integration

The generic intake, persistence threshold and termination rule remain owned by `baseline/SYSTEM-LEARNING.md`. This episode warrants one bounded record because it affected a concrete transition assumption and documents its routing to the authoritative owner; it creates no standing Capability Watch, ledger or monitoring subsystem.

## Claim limit

This record establishes only a bounded interpretation of the reviewed product state, its absorption by the promoted Native Work Transition and the remaining UI test. It does not establish that every account/surface exposes identical Work behavior; that the previously observed Chat→Work UI action was permanently removed; that underlying transition capability is absent; that PR #50 has been accepted or merged; that the revised Global CI is installed or active; or that the Native Work Transition is behaviorally validated.
