# ADR-0003 — Normalized vNext Requirements Baseline v0.2

**Status:** ACCEPTED / ACTIVE — PR #18 authorized, merged at `b355ed63ad94d6456a6913cac079458238067921` and read back on `main`  
**Date:** 2026-08-24  
**Decision owner:** Human repository owner

## Context

`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` was the prior controlling solution-neutral Requirements baseline adopted through ADR-0002 and is now retained as historical Qualified Prior evidence.

Subsequent real-use and Runtime evidence established a legitimate Requirements-reopen trigger without establishing a Target-Architecture gap:

- premature solution/formation failures;
- professional-method activation failures;
- Exploration-readiness learning;
- Human-attention and AI-resolvable-work burden;
- State/Parent/Authority control failures;
- over-orchestration and high end-to-end latency;
- need for broader Whole-System Economics;
- need for stronger provider/surface isolation and portability;
- need to make evidence-bound learning/change explicit.

A first R01–R30 formation candidate recovered the broader semantic space but mixed Core Requirements, Conditional Requirements, interpretation rules and Runtime concerns. A bounded normalization and adversarial de-bias review produced the smaller v0.2 Candidate:

```text
5 Interpretation Rules
14 Core Requirements
7 Conditional Requirements
central non-equivalences
```

The Human accepted that normalized Candidate as the Requirements Design Basis on 2026-08-24. The acceptance did not itself authorize repository write, Promotion, architecture change or Runtime Solution Formation.

## Decision

PR #18 and its containing package were explicitly authorized, merged at `b355ed63ad94d6456a6913cac079458238067921` and read back on `main`. Therefore:

1. adopt `foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md` as the controlling solution-neutral Requirements baseline;
2. classify `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` as:
   - `SUPERSEDED AS CONTROLLING REQUIREMENTS BASELINE`;
   - `RETAINED IMMUTABLY AS HISTORICAL QUALIFIED PRIOR`;
3. retain `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md` as the controlling conceptual architecture:
   - compatibility with Requirements v0.2 is recorded in `evidence/REQUIREMENTS-v0.1-to-v0.2-RECONCILIATION-v0.1.md`;
   - no architecture semantic change or reopen is accepted by this decision;
4. retain ADR-0002 as historical accepted decision:
   - its adoption of Requirements v0.1 is superseded by this ADR;
   - its adoption of Target Architecture v0.2 and its architecture reopen discipline remain in force;
5. open Runtime Solution Formation as the next eligible Work frontier after this repository Promotion/readback reconciliation;
6. accept no Runtime, Skill, Project, UI, Agent topology, provider allocation, implementation or external action.

## Supersession and retirement semantics

```text
Requirements v0.1
  repository file                 RETAIN
  historical decision/evidence    RETAIN
  controlling Requirements role   SUPERSEDED

ADR-0002
  historical decision             RETAIN
  Requirements-v0.1 adoption      SUPERSEDED BY ADR-0003
  Target-Architecture adoption    RETAIN
  architecture reopen discipline  RETAIN

Target Architecture v0.2
  controlling architecture        RETAIN
  compatibility with v0.2 Req.    REQUALIFIED / PASS
  architecture reopen             NO

R01–R30 formation candidate
  semantic learning               RETAINED THROUGH v0.2
  separate baseline/status        NONE / SUPERSEDED PACKAGING

earlier ΔR candidates
  reconciliation evidence         RETAINED IN FORMATION HISTORY
  controlling status              NONE
```

No file is deleted, moved or rewritten merely to erase prior history.

## Acceptance boundary

Acceptance means only:

> Requirements v0.2 is sufficiently coherent, solution-neutral, lineage-reconciled, de-biased and compatible with the accepted Target Architecture to serve as the current Requirements Design Basis for subsequent solution work.

Acceptance does not mean:

- the Requirement set is eternally complete;
- the Target Architecture is behaviorally superior;
- Runtime effectiveness or Human–AI synergy is established;
- a particular Runtime topology is selected;
- a Skill, Agent, Project, provider or state architecture is accepted;
- concrete Performance budgets are established;
- any external or persistent Runtime action is authorized.

## Consequences

Following the authorized merge and readback:

1. Requirements v0.2 controls subsequent Architecture/Realization evaluation;
2. Requirements v0.1 remains available for lineage and regression analysis;
3. Target Architecture v0.2 stays closed absent a named architecture reopen trigger;
4. Runtime Solution Formation becomes the next legitimate frontier;
5. future Runtime candidates must be evaluated against v0.2 rather than against the R01–R30 formation packaging or fragmented deltas;
6. later evidence may reopen only the affected Requirement or dependent design scope.

## Pre-merge verification

Before the merge decision, the package was checked to:

- verify 5 IR / 14 CR / 7 CCR with unique IDs;
- verify complete v0.1 treatment map;
- verify complete v0.2 → Target Architecture compatibility map;
- verify no provider-specific solution or Runtime topology is accepted;
- verify no Runtime, Skill, UI or external action is included;
- verify `CURRENT.md`, `README.md` and `foundation/SYSTEM-OF-INTEREST.md` use consistent authority wording;
- verify the package branch is based on the merged/read-back PR #17 state, `main@5e3c84309b3c59da4ba8bde7748c66eaa41d802f`;
- run a bounded adversarial review of the exact PR head in both directions:
  - what material Requirement is missing?
  - what has been added only because of recent failures or control bias?
  - what is actually a mechanism rather than a Requirement?
  - what would create unnecessary future meta-work?
- require PASS or bounded repair before the Human merge decision.

## Post-merge readback

Completed after PR #18 merge:

- merge SHA recorded as `b355ed63ad94d6456a6913cac079458238067921`;
- exact `main` Requirements v0.2 readback PASS;
- v0.2 is controlling and v0.1 is superseded only in its controlling role;
- Target Architecture v0.2 remains accepted/closed;
- this bounded authority reconciliation updates stale Candidate wording only;
- Runtime Solution Formation becomes eligible after the corresponding `CURRENT.md` reconciliation is read back.

---
