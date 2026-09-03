# Capability Delta — ChatGPT Work interactive steering

**Status:** CURRENT evidence/impact record on authoritative `main`; CANDIDATE off `main`  
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

The legitimate owner of the affected transition semantics is the promoted `baseline/NATIVE-WORK-TRANSITION.md` on current authoritative `main@d42a1b06614dd9510838750a85ce9690e42e93b5` (blob `a33285e59c6b836e1bbea4ef662a46cf94b90676`; introduced by PR #51 merge `7cd5b5490f67638e5eb6d85ff1fbb62cfabb1f4f`). This record does not define a parallel handoff or Work Contract.

## Classification

`EXTERNAL_CAPABILITY_DELTA`

Primary dependency: Chat/Project → Work transition semantics, routed to their existing authoritative owner.

## Bounded disposition

- Interactive Work steering: originally `CANDIDATE_SEMANTIC_CHANGE`; the change is now absorbed by the promoted Native Work Transition on `main@7cd5b5490f67638e5eb6d85ff1fbb62cfabb1f4f`. Its explicit ordinary-interaction, material re-entry and UI-independent transition semantics, together with the protected-commitment, operational-autonomy and no-silent-mutation rules, cover the acceptance constraints. No additional Chat→Work semantic change remains pending from this episode.
- Missing prior three-dot Chat→Work action: `TEST`. It remains an unresolved surface observation. No capability-removal or architecture claim follows unless stronger evidence establishes a material underlying impact.

PR #51 and PR #50 are promoted. Post-promotion readback binds this record to current `main@d42a1b06614dd9510838750a85ce9690e42e93b5`.

## System integration

The generic intake, persistence threshold and termination rule remain owned by `baseline/SYSTEM-LEARNING.md`. This episode warrants one bounded record because it affected a concrete transition assumption and documents its routing to the authoritative owner; it creates no standing Capability Watch, ledger or monitoring subsystem.

## Claim limit

This record establishes only a bounded interpretation of the reviewed product state, its absorption by the promoted Native Work Transition, the promotion of PR #50 and the remaining UI test. A separate 2026-09-03 product-surface readback established exact installed identity of the revised Global CI; that identity does not prove activation in every session. This record does not establish that every account/surface exposes identical Work behavior; that the previously observed Chat→Work UI action was permanently removed; that underlying transition capability is absent; or that the Native Work Transition is generally behaviorally validated.
