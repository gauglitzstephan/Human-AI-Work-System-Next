# Human–AI Work System Next

> Reconstruction program for a reference-grounded, empirically testable Human–AI Work System.

## Status

**BOOTSTRAP / PRE-ARCHITECTURE**

This repository intentionally does **not** begin by copying the architecture of the predecessor repository or by assuming that concepts such as a Work Engine, DWM, Semantic Compiler, Work Graph, or any prior lifecycle belong in the new system.

The immediate objective is to establish a sound basis from which the architecture can be derived.

## Working intent

Develop a general Human–AI Work System that improves real professional work by composing human judgment and agency, AI capabilities, tools, knowledge, state, and existing processes appropriately for the situation.

This intent is provisional until the System of Interest, stakeholder concerns, operational context, and performance model are qualified.

## Epistemic stance

The reconstruction uses three evidence streams:

1. **External knowledge** — state of the art, standards, research, reference architectures, and productive systems.
2. **Internal evidence** — predecessor repository, real work traces, prior evaluations, successes, failures, and other implemented workflows.
3. **First-principles reasoning** — purpose, constraints, mechanisms, trade-offs, and deductions that follow from the problem itself.

None of these streams is sufficient alone. References are evidence, not authority for this system; prior architecture is knowledge capital, not a baseline requirement; plausible deductions remain hypotheses until adequately supported.

## Bootstrap work products

- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md) — provisional problem, mission, boundary, stakeholders, outcomes, and performance concerns.
- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — reference families and the questions each should answer.
- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md) — internal evidence sources and harvesting rules.
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — how evidence becomes concerns, requirements, alternatives, views, and architecture decisions.
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md) — how architectural and behavioral claims will be tested.
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md) — rationale for a clean reconstruction rather than direct refactoring.

## Current non-decisions

The following are **not yet established**:

- the final System of Interest boundary;
- whether `Work Engine` is the correct name, abstraction, or subsystem boundary;
- whether `Capabilities` and `Environment` are architectural components or views;
- the final lifecycle or work-state model;
- the runtime implementation (Custom Instructions, skills, agents, deterministic orchestration, or combinations);
- the final evaluation suite;
- which predecessor concepts survive, change level, or are rejected.

## Reconstruction flow

```text
Purpose / Problem / Operational Context
                +
     External reference landscape
                +
         Internal evidence
                ↓
      Concerns and requirements
                ↓
        Conceptual alternatives
                ↓
     Architecture viewpoints/views
                ↓
        Candidate architecture
                ↓
     Verification / falsification
                ↓
       Accepted architecture
                ↓
       Runtime realization
```

The governing rule is: **do not promote a concept into the architecture merely because it is plausible, familiar, or previously useful. Establish its role, scope, mechanism, evidence, and architectural placement first.**
