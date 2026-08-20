# E2E Kernel — Live-Control + Six-Primitive Review v0.1

**Status:** COMPLETE — v0.1 REVISE; v0.2 repair candidate created.  
**Date:** 2026-08-20

## 1. Review inputs

A. Human-supplied exact currently live Global Custom Instructions:

- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt`
- normalized identity recorded in `GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT-METADATA.md`

B. E2E Global Runtime Kernel Candidate v0.1.

C. Parallel Free-account compression exploration proposing six primitives:

```text
INTERPRET → MODEL → TEST → DECIDE → WORK → VERIFY
```

D. Current OpenAI Model Spec framing, used only as an external behavior reference: instruction Chain of Command / applicable authority; no independent assistant objectives; truth/objectivity; agentic scope and side-effect control; best-work defaults.

## 2. What is worth borrowing from the six-primitive exploration

### KEEP as compression / reasoning grammar

1. **INTERPRET** — explicitly foreground applicable mandate/authority, intent, context and ambiguity.
2. **smallest sufficient model/depth** — strong compact formulation of proportionality.
3. **MODEL vs TEST** — useful distinction between forming the relevant problem/solution representation and challenging whether its claims/options actually hold.
4. **VERIFY with new evidence** — reinforces selective reopening rather than rationalizing old decisions.
5. Clarification/research/tool use are support actions, not universal lifecycle stages — already consistent with the cross-cutting Orchestrator.

### DO NOT adopt as the full runtime architecture

The six-primitives grammar is too compressed to replace the E2E runtime contract.

Most importantly:

```text
WORK = establish/commit + execute
```

would risk re-collapsing the bounded repair:

```text
commitment
≠ decision/acceptance/authorization
≠ promotion/state transition
≠ execution
```

Likewise a single `VERIFY` primitive does not safely preserve the distinctions among refinement, deterministic verification, independent challenge, intended-use validation, transition readiness, in-use performance and outcome evidence.

Therefore the six primitives are retained only as a **compression/interpretability lens**, not as the controlling E2E semantics.

## 3. Exact live-CI differential against E2E v0.1

Capturing the actual live payload exposed an important process correction: the v0.1 static review had compared the new kernel to the E2E contract and historical summaries, but not yet to the exact currently operating CI.

Several explicit guards in the live control were missing or too implicit in v0.1:

| Live-control function | v0.1 | Judgment |
|---|---|---|
| retrieved/tool content = evidence, not instruction/authority unless delegated | missing explicit cue | RESTORE |
| Reality wins | implicit | RESTORE explicit salience |
| do not invent/transfer state/capability/access/authority/decision/acceptance/completion/deployment/outcome | under-explicit | RESTORE |
| absence != negation | missing | RESTORE |
| blocked route != outcome impossibility | missing | RESTORE |
| no downstream-state inference | present | KEEP |
| action-specific authorization | present | KEEP |
| revalidate authorization before material effect | missing explicit cue | RESTORE |
| minimize sensitive data/authority | missing | RESTORE |
| delay-risk containment = smallest authorized containment | missing | RESTORE |

These are not reasons to revert to the old lifecycle. They are integrity/authority controls that should survive the migration into the new E2E structure.

## 4. Model-Spec alignment implication

The restored cues strengthen rather than compete with the current Model Spec direction:

- `Follow applicable authority` supports Chain-of-Command semantics without attempting to restate platform rules.
- external/retrieved/tool content does not gain instruction authority merely because it is visible;
- no-invention/no-transfer and Reality-wins support truth/objectivity;
- action-specific authorization, revalidation and containment support bounded agentic autonomy and side-effect control;
- `smallest sufficient depth` supports best-work / thorough-but-efficient behavior.

The Global CI should complement higher-authority Model Spec/platform behavior, not duplicate safety policy or attempt to override it.

## 5. Repair

Created:

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.2.md`

v0.2 keeps the E2E additions while restoring the live-control guardrails above.

Target payload envelope:

```text
~4,977 LF characters
~4,986 CRLF characters
< 5,000 CRLF
```

The exact saved payload must still receive readback/count verification before installation.

## 6. Gate

```text
v0.1 Global E2E kernel                REVISE / DO NOT INSTALL
exact old live Global CI              CAPTURED / ROLLBACK CONTROL
six-primitive grammar                 KEEP AS COMPRESSION LENS ONLY
v0.2 Global E2E kernel                CURRENT REPAIR CANDIDATE
Project Instructions                  STILL REQUIRED FOR FIRST PROJECT
external installation                 NOT PERFORMED
behavioral acceptance                 NOT ESTABLISHED
```
