# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / RUNTIME REALIZATION ENTRY RESTORED  
**Date:** 2026-08-20  
**Acceptance:** PR #3 explicitly accepted and merged as `0b2dc8f3d369cc5d0e5c8ec502449ccf11c7464e`

## 1. Controlling conceptual baseline

These files are controlling for the accepted conceptual baseline:

1. `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`
2. `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`
3. `decisions/ADR-0002-target-conceptual-baseline.md`
4. `architecture/ARCHITECTURE-METHOD.md`
5. `evaluation/EVALUATION-STRATEGY.md`

The embedded `PROPOSED` wording in the first three files is pre-merge metadata. PR #3 was explicitly accepted and merged; that merge is the acceptance event defined by those files.

Foundational architecture is closed by default and reopens only through the named triggers in ADR-0002.

## 2. Required parent bind for Runtime / Operating Realization

The next program remains:

> **Architecture → Runtime / Operating Realization**

It is **not** a blank-slate runtime design.

Before any realization child work, bind all of:

```text
PARENT OUTCOME
realize the accepted Target Architecture without material semantic loss
and without degrading already-qualified professional work behavior

PARENT STATE / GATE
Target Architecture v0.2 accepted; foundational architecture closed by default

QUALIFIED RUNTIME PREDECESSOR
`gauglitzstephan/Human-AI-Work-System` runtime lineage,
including the B.6/Core v0.5 line, global CI v0.6.x history,
full historical function / Protected-Salience regression evidence,
and the documented v0.6.3 compression-debt failure

CURRENT INCUMBENT RUNTIME
Human-confirmed current ~4,981-character Custom Instructions
+ current product/runtime behavior

ALLOWED OPERATION
recover and compare first; preserve qualified predecessor/runtime behavior;
change only a specifically demonstrated realization delta

NOT ALLOWED BY DEFAULT
clean-sheet runtime design
CI compression as an objective
carrier relocation by architectural preference
re-derivation of qualified predecessor mechanisms
```

If any part of this parent bind is unclear, recover it before proposing a new realization state.

## 3. Failed realization branch — PR #4

Draft PR #4 (`realization/architecture-runtime-operating-v0.1`) is **FAILED / NON-CONTROLLING**.

### First divergence

The first invalid step is **R1**, not R2.

R1 started Runtime Realization without first binding the qualified runtime predecessor and current incumbent. It introduced the unqualified objective that implementation should be smaller than the conceptual architecture and derived a `thin-global / strong-context` direction from it.

That violated the already controlling continuation rule:

```text
Next / continuation
→ bind parent Work Object / outcome + state + gate
→ bind child contribution + allowed operation
→ child ≠ implicit root
→ recover if unclear
```

R2–R6 were downstream of that incorrectly bound parent and therefore do not establish controlling realization decisions.

### Disposition

```text
R1 platform observations                    evidence only
R1 thin-global direction                    failed hypothesis
R2 Global-kernel minimal DEFAULT/PROMOTE     invalid downstream disposition
R3 G1–G6                                    non-controlling analysis
R4 carrier/5-clause CI                       rejected
R5 1,199-char CI                             rejected
R6 2,067-char CI                             rejected
PR #4                                        historical failure evidence only
```

Nothing from PR #4 may override the accepted baseline, qualified runtime predecessor, current incumbent runtime, or existing evaluation/change-control rules unless independently re-qualified through the correct parent/gate.

## 4. Current allowed work frontier

The first legitimate Runtime Realization operation is strictly differential:

```text
Accepted Target Architecture v0.2
+ bound qualified runtime predecessor
+ exact current incumbent runtime
→ identify only material realization deltas not already satisfied
→ preserve everything else
```

A proposed delta must state:

- the exact unmet architecture/runtime claim;
- the predecessor/current behavior being preserved;
- the evidence that a change is needed;
- the smallest changed scope;
- the evaluation needed before promotion.

No new runtime object, Skill, Project topology, instruction rewrite, state store, agent, workflow or compression target is admitted merely because it is plausible or available.

## 5. Evaluation / promotion rule

Use `evaluation/EVALUATION-STRATEGY.md` and the predecessor runtime regression evidence.

The incumbent is the control. A changed realization is promoted only if evidence supports its claimed delta and there is no material non-compensatory regression in professional outcome quality, state/authority integrity, Human burden/agency, recipient/use fitness, transition behavior or other applicable protected semantics.

## 6. Reopen rule

Foundational architecture reopens only through ADR-0002 triggers. Runtime realization problems are repaired at runtime/operating scope unless evidence demonstrates that a required conceptual semantic cannot be represented or preserved.
