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

### Foundation and method

- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md) — provisional problem, mission, competing boundary hypotheses, stakeholders, outcomes, and performance concerns.
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — how concerns, references, evidence, alternatives, views, and decisions become architecture.
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md) — how conceptual, behavioral, economic, Human–AI, state, transition, and robustness claims will be tested.
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md) — rationale for reconstruction rather than direct refactoring.

### External knowledge stream

- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — reference families and the questions each should answer.
- [`references/SEED-REFERENCE-REGISTER.md`](references/SEED-REFERENCE-REGISTER.md) — first verified source register covering architecture, concept definition, AI assurance, agents/orchestration, and Human–AI collaboration.

### Internal evidence stream

- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md) — internal evidence sources, evidence strength, and harvesting rules.
- [`evidence/PREDECESSOR-INVENTORY-v0.1.md`](evidence/PREDECESSOR-INVENTORY-v0.1.md) — first-pass inventory of high-value architecture, runtime, falsification, and real-use evidence in `Human-AI-Work-System`.

## Current non-decisions

The following are **not yet established**:

- the final System of Interest boundary;
- whether `Work Engine` is the correct name, abstraction, subsystem, control policy, or viewpoint;
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

## Current gate

Do **not** design the Work Engine yet.

The next decision-relevant work is to build two linked matrices:

1. **Reference synthesis by concern/mechanism** — what the strongest external disciplines say about the same underlying concerns, including conflicts and transfer limits.
2. **Predecessor evidence matrix** — `problem → reference basis → mechanism → architectural placement → evidence → counterevidence → dependencies → confidence → candidate disposition` for the high-priority predecessor sources.

Those matrices should then produce the first qualified set of stakeholder/system concerns and candidate requirements. Only after that do we define architecture viewpoints and compare conceptual architecture alternatives.

The governing rule is: **do not promote a concept into the architecture merely because it is plausible, familiar, or previously useful. Establish its role, scope, mechanism, evidence, alternatives, and architectural placement first.**
