# Runtime Control Split — Placement Review v0.3

**Status:** STATIC PLACEMENT REVIEW — CANDIDATE  
**Date:** 2026-08-20  
**Candidate:** `realization/RUNTIME-CONTROL-SPLIT-CANDIDATE-v0.3.md`

## Review question

> Can the current 19-function incumbent ledger be preserved as **available semantics** without requiring all 19 functions to remain permanently salient in the Global CI?

This review does not claim behavioral superiority. It checks for unowned semantic deletion and inappropriate placement only.

## Placement tie-out

| ID | Existing function | v0.3 placement | Verdict |
|---|---|---|---|
| F01 outcome over wording / input boundary | Kernel | KEEP GLOBAL |
| F02 B.6 bounded macro / closure | Task-local Professional Method | REMOVE GLOBAL DETAIL |
| F03 Work Object / receiving context / Performance Model | Method + State when material | CONDITIONAL |
| F04 existing-system recovery | Kernel trigger + Method/State detail | KEEP TRIGGER |
| F05 qualified reference/reuse | Kernel method trigger + local method | KEEP TRIGGER |
| F06 alternatives / simpler-no-action / peer split | Task-local Professional Method | CONDITIONAL |
| F07 epistemic challenge / uncertainty | Task-local Professional Method | CONDITIONAL |
| F08 decomposition / parent integration | Task-local Method/State | CONDITIONAL |
| F09 recipient maturity / AI-resolvable repair | Method + Assurance | CONDITIONAL |
| F10 realization / use / outcome chain | Method + Assurance | CONDITIONAL |
| F11 Human-AI/tool composition | Kernel Human-boundary + local Method | KEEP BOUNDARY |
| F12 authoritative state / retrieve-before-ask | Kernel + task-local State | KEEP GLOBAL INVARIANT |
| F13 no-invention / typed non-equivalence | Kernel invariant; detailed taxonomy local | KEEP GLOBAL CORE |
| F14 persistence / authorization / containment | Kernel authority boundary + task-local State | KEEP BOUNDARY |
| F15 claim-bound assurance / FAIL-UNVERIFIED | Kernel assurance trigger + task-local Assurance | KEEP TRIGGER |
| F16 selective reopening / preservation | Kernel preserve rule + State/Assurance | KEEP CORE |
| F17 parent continuity / promotion-readback | Task-local State for persistent/system work | CONDITIONAL |
| F18 minimum frontier / VoI / robustness / commitment | Task-local Professional Method | CONDITIONAL |
| F19 runtime mapping / handoff / boundary economics | Kernel handoff trigger + task-local Method/State | KEEP TRIGGER |

## Findings

```text
Functions discarded from the system             0 / 19
Functions required permanently global            6 core/boundary groups
Functions moved to conditional task-local use    13 detail/mechanism groups
New architecture objects                         0
New mandatory artifacts                          0
New agent/store/Skill topology                    0
```

The exact count of globally resident wording is not itself a target. The important correction is that **global residence is no longer used as the proof of semantic preservation**.

## Prior-decision correction

The incumbent-first PR #4 audit was correct to reject an unproven compression rollout. Its `0 relocation justified` result was an evidence state for that rollout decision, not an architecture invariant that every mechanism must remain permanently global.

The later reviewed Solution-Forming CI v0.2 preserved all 19 functions globally and passed static regression, but it also states:

```text
envelope saturated
behavioral superiority not established
external installation not performed
```

Therefore its installation target is not protected by accepted/runtime evidence.

The earlier R6 `CI-shadow-v0.2` is relevant qualified prior evidence because it had already demonstrated a conservative pattern of keeping global **triggers/boundaries** while moving detailed mechanisms to conditional/retrievable method. v0.3 restores that distinction with a clearer Method / State / Assurance activation model.

## Static verdict

```text
Accepted architecture reopened                  NO
Semantic deletion identified                    NO
Global-residence assumption retained            NO
Conditional activation made explicit            YES
Simple-work collapse preserved                  YES
Formal artifact/Human review still possible     YES, when material
Behavioral superiority                          NOT ESTABLISHED
External runtime installation                   NOT PERFORMED
```

**STATIC PLACEMENT VERDICT: PASS AS CANDIDATE.**

Next evidence must be behavioral. The next test should compare actual work under the live incumbent versus the split-kernel candidate, with special attention to both failure directions:

- **over-activation:** meta-work, ceremony, needless reopening;
- **under-activation:** missing professional method, stale/wrong state, weak assurance or missing Human control when material.