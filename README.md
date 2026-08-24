# Human–AI Work System Next

> Build a Human–AI Work System that turns real needs into intended-use-sufficient working solutions with strong reality, state, authority, quality and Human-agency control — without unnecessary meta-work.

## Start here

**[`main/CURRENT.md`](CURRENT.md) is the controlling repository state and operating entry point.**

A `CURRENT.md` copy read on an unmerged branch is Candidate state. It becomes controlling only when that exact state is present on `main` after an authorized merge and readback. Do not infer current program state from historical `Next` sections, newest-looking files, old installation bundles, chat history, or closed/unmerged branches.

## Current status

```text
Target Architecture v0.2                         ACCEPTED / KEEP CLOSED
Static E2E Work Architecture                     REPOSITORY-PROMOTED / KEEP CLOSED
Runtime deployment + interaction-control repair  REPOSITORY-PROMOTED via PR #13
Repository hygiene/state reconciliation           REPOSITORY-PROMOTED via PR #14
R21 product/carrier + real-use reconciliation     REPOSITORY-PROMOTED EVIDENCE via PR #16 / READBACK PASS

Promoted Global Runtime                          v0.5
Active external Global                           v0.5 / persistent UI readback PASS
Repository-promoted Project baseline             v0.4
Live Project payload                             v0.5 CANDIDATE / UI content readback PASS / UNPROMOTED
material-work-entry                              v0.6-candidate / external Personal Skill / UNPROMOTED

R20 active repair                                CLOSED
R21 repository convergence                       COMPLETE via PR #16
Post-R21 authority-state reconciliation           COMPLETE via PR #17 / READBACK PASS
Requirements v0.1                               CONTROLLING ON main UNTIL LATER PROMOTION
Requirements v0.2                               HUMAN-ACCEPTED DESIGN BASIS / BRANCH CANDIDATE
Requirements package branch                     reconcile/vnext-requirements-v0.2
Next                                             EXACT-HEAD REVIEW + DRAFT PR; NO MERGE/PROMOTION
```

PR #16 reconciled native Product/Carrier mapping, version-scoped R21 real-use evidence, the live-versus-promoted Project-carrier distinction, and candidate lineage. It did **not** change the live Runtime, Project UI, installed Skill, static architecture, or any Runtime/Skill Promotion state.

PR #17 subsequently reconciled the post-R21 repository authority surfaces on `main`. The current Requirements package starts from that exact merged/read-back state and changes no Runtime, Skill, Project UI or static architecture.

## Authority and transition rules

```text
main/CURRENT.md
= controlling repository program state

Repository evidence persisted on main
≠ Runtime behavior
≠ UI installation
≠ Skill or Runtime Promotion
≠ architecture acceptance/change

Unmerged branch / PR / external Skill candidate
= Working or Candidate state

Persistence
≠ Promotion

Next
= continue only the currently bound legitimate frontier
≠ acceptance, authorization, merge, promotion, scope change or new commitment
```

Any later status change requires its own evidence, decision/authority, write path, readback and reconciliation.

## Requirements baseline transition

The controlling Requirements baseline on `main` remains:

- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md) — controlling until an explicitly authorized later merge and readback.

This branch adds, as Candidate state only:

- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md) — Human-accepted normalized Requirements Design Basis;
- [`evidence/REQUIREMENTS-v0.1-to-v0.2-RECONCILIATION-v0.1.md`](evidence/REQUIREMENTS-v0.1-to-v0.2-RECONCILIATION-v0.1.md) — lineage, de-bias, known-failure and architecture-compatibility evidence;
- [`decisions/ADR-0003-vnext-requirements-baseline-v0.2.md`](decisions/ADR-0003-vnext-requirements-baseline-v0.2.md) — proposed authority/supersession transition.

```text
branch / Draft PR
→ v0.2 remains Candidate; v0.1 remains controlling

authorized merge + main readback
→ v0.2 may become controlling
→ v0.1 may become superseded only in its controlling role
→ Target Architecture v0.2 remains accepted and closed
```

No branch content authorizes merge, Requirements Promotion, prior-baseline retirement, Runtime/Skill/UI change or Runtime Solution Formation.

## Accepted conceptual baseline

[`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md) retains three structural commitments:

```text
DISTINCT RESPONSIBILITIES
DISTRIBUTED TYPED STATE
ADAPTIVE WORK SELECTION
```

These are responsibilities/contracts, not mandatory runtime layers, agents, stores, ontologies or stage machines. Static architecture stays closed unless a named Runtime/real-use trigger or legitimate requirement/scope change establishes a reason to reopen it.

## Current Runtime realization

Canonical semantic source:

- [`realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`](realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md)

Repository-promoted compiled views:

- [`realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`](realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md) — Global Custom Instructions view
- [`realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`](realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md) — System Development Project baseline
- [`realization/E2E-INSTALLATION-BUNDLE-v0.4.md`](realization/E2E-INSTALLATION-BUNDLE-v0.4.md) — repository-promoted external-transition bundle
- [`realization/README.md`](realization/README.md) — realization navigation and lineage

The live System Development Project contains the branch-origin v0.5 Candidate payload by Human UI content readback. That deployment fact is recorded truthfully while the repository-promoted Project baseline remains v0.4. No rollback, UI edit or Promotion follows from the divergence alone.

Do **not** select earlier Global, Project or Installation-Bundle versions for installation unless `CURRENT.md` explicitly re-promotes them.

## Runtime control model

Keep distinct:

```text
Work Function
≠ Control Operator
≠ Method
≠ Provider
≠ Surface / Environment
≠ State / Knowledge Carrier
≠ Boundary Contract
```

and:

```text
Decision
≠ Commitment
≠ Authorization
≠ Handoff
≠ Execution
≠ Provider Return
≠ Human-facing Control Return
≠ Promotion / State Transition
```

## R21 evidence

Primary and secondary records are indexed in [`evaluation/e2e-real-use/README.md`](evaluation/e2e-real-use/README.md).

Key reconciliation records:

- [`evaluation/e2e-real-use/E2E-04-R21-2026-08-22-MATERIAL-WORK-ENTRY-v0.5-v0.6-REAL-USE-SYNTHESIS.md`](evaluation/e2e-real-use/E2E-04-R21-2026-08-22-MATERIAL-WORK-ENTRY-v0.5-v0.6-REAL-USE-SYNTHESIS.md) — version-scoped synthesis and bounded disposition
- [`evaluation/e2e-real-use/E2E-04-R21-2026-08-22-LIVE-PROJECT-IDENTITY-READBACK.md`](evaluation/e2e-real-use/E2E-04-R21-2026-08-22-LIVE-PROJECT-IDENTITY-READBACK.md) — live v0.5 Candidate carrier identity versus promoted v0.4 baseline
- [`evaluation/e2e-real-use/E2E-01-R21-2026-08-22-EV-WAIT-DECISION-v0.6.md`](evaluation/e2e-real-use/E2E-01-R21-2026-08-22-EV-WAIT-DECISION-v0.6.md) — current-evidence WAIT decision and bounded re-entry contract
- [`evaluation/e2e-real-use/E2E-04-R21-2026-08-22-PERSONAL-INFORMATION-SYSTEM-v0.6.md`](evaluation/e2e-real-use/E2E-04-R21-2026-08-22-PERSONAL-INFORMATION-SYSTEM-v0.6.md) — System-Boundary Discovery and bootstrap evidence

Positive records remain claim- and version-scoped. They do not constitute complete v0.6 qualification or establish broader real-use outcomes.

## Current monitoring frontier

Observe, rather than manufacture, the remaining claims when genuine work naturally exercises them:

- provider return → Parent rebind;
- bounded negative control;
- active monitoring execution where separately authorized.

R20 repair and R21 repository convergence are closed. Their remaining genuine-use monitoring is non-blocking for this bounded Requirements Candidate. Reopen only on material counterevidence or a legitimate new requirement. This branch authorizes no UI action, Skill/Runtime repair, architecture change, merge or Promotion.
