# ADR-0002 — Target Conceptual Architecture Baseline v0.2

**Status:** PROPOSED — acceptance occurs only if the containing PR is explicitly accepted and merged  
**Date:** 2026-08-19  
**Decision owner:** Human repository owner

## Context

The reconstruction program initially produced architecture too early and later corrected itself through:

- Reference Map / reference-depth calibration;
- Q1–Q8 synthesis and Qualified-Prior tie-out;
- solution-neutral Concerns & Requirements derivation;
- Requirements Quality Audit;
- mapping of qualified prior architectures against those requirements;
- Architecture Necessity & Scope Discrimination;
- Minimal-Rival Discrimination for responsibility partition, shared state and adaptive work control;
- Target Architecture synthesis;
- adversarial semantic-regression / failure-case audit;
- bounded repairs for evidence-qualified reuse, semantic preservation through implementation, detection-capable assurance, shared-state legibility, transition integrity and scope/packaging.

The result is not a combination of predecessor repositories. It is a requirements-derived candidate that reuses predecessor mechanisms only where they remain necessary or evidentially justified.

## Decision

If this ADR is accepted and merged, adopt:

1. `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` as the controlling solution-neutral architecture-driver baseline; and
2. `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md` as the controlling conceptual Human–AI Work System architecture baseline.

The conceptual baseline has three structural commitments:

```text
A. distinct responsibility classes
   Strategic / Operating / Work / Execution / Learning-Change

B. distributed typed state
   authoritative state remains with legitimate owners/stores;
   integrated work-state projections are conditional

C. one adaptive work-selection contract for admitted/triggered work
   selecting the minimum justified next work while preserving valid state,
   dependency integrity, professional quality, authority, runtime reality,
   assurance, uncertainty and net value
```

The five responsibility distinctions do not mandate a five-layer runtime or physical subsystem topology.

A Dynamic Work Model, explicit Work Graph, B.6 macro projection, Semantic Compiler label/policy, PAOS surface topology and the predecessor eight-view scheme remain available qualified mechanisms/projections/profiles where useful, but are not universal architecture objects required by this decision.

Cross-cutting Reality/State, Capability/Authority/Agency, Professional Quality/Claim and Value/Realization/Change groupings are explanatory invariant groupings, not additional modules or a new ontology.

## Superseded controlling development frame

If merged, this decision supersedes the bootstrap `CURRENT.md` framing that treated `Δ4 Adaptive Work-Control`, `Δ5 Architecture → runtime semantic compilation` and `Δ6 Knowledge Capital ownership/promotion` as the controlling remaining architecture program.

The prior bootstrap/differential documents remain historical evidence and Qualified-Prior reconciliation records. They are not deleted or rewritten.

This supersession does **not** assert that their individual findings were false. It means their delta sequence is no longer the controlling architecture-development program after the independent requirements-derived synthesis.

## Acceptance boundary

Acceptance means only:

> The Requirements v0.1 and Target Architecture v0.2 are sufficiently coherent, solution-neutral/requirements-traceable, semantically complete against known failure classes and qualified prior mechanisms, and proportionate enough to serve as the conceptual baseline for subsequent realization work.

Acceptance does **not** mean:

- runtime implementation or deployment;
- behavioral effectiveness or Human–AI synergy;
- cross-domain empirical generality;
- optimality of every naming/grouping choice;
- acceptance of one DWM, Work Graph, lifecycle, Semantic Compiler subsystem, agent topology, state store, Skill topology, Project layout, Surface topology or instruction format;
- acceptance of any external action or persistent system mutation.

## Consequences

After acceptance:

1. foundational architecture expansion is closed by default;
2. architecture changes require a named reopen trigger from the baseline;
3. the next program becomes **Architecture → Runtime / Operating Realization**, explicitly separate from conceptual architecture design;
4. realization must preserve material baseline semantics without copying the full architecture into every runtime;
5. real-use/behavioral evidence may later reopen the baseline when a material failure cannot be represented or repaired locally.

## Reopen triggers

Reopen only for a material named trigger:

- changed System-of-Interest / intended claim;
- new external evidence materially contradicting the baseline;
- repeated/consequential real-use failure not cleanly representable or repairable;
- materially simpler rival satisfying the same requirements at lower burden;
- implementation/runtime impossibility or systematic semantic loss;
- unowned requirement / semantic regression / hidden mandatory structure discovered;
- material responsibility/authority contradiction;
- newly established legitimate concern/requirement.

A new framework, elegant terminology, isolated anomalous response or mere implementation preference is not sufficient.

## Verification before merge

Before merge, verify only:

- Requirements file contains all 11 Concerns, 13 Core Requirements and 7 Conditional Requirements;
- Target Architecture traces every Core Requirement and owns all Conditional Requirements;
- the six adversarial-audit repairs are explicit;
- no runtime/deployment claim is accidentally accepted;
- `CURRENT.md` correctly points to this baseline and demotes the old delta sequence to historical status;
- no CI/Actions run is required for this documentation-only conceptual baseline change.
