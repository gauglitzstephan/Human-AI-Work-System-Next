# Human–AI Work System Next

> Reconstruction program for a reference-grounded, empirically testable Human–AI Work System.

## Status

**BOOTSTRAP / PRE-ARCHITECTURE**

This repository intentionally does **not** begin by copying the predecessor architecture or by assuming that `Work Engine`, DWM, Semantic Compiler, Work Graph, prior lifecycle stages, Skills, agents or any current product surface belong in the final system.

## Working intent

Develop a general Human–AI Work System that improves real professional work by composing human judgment and agency, AI capabilities, tools, knowledge, state and existing processes appropriately for the situation.

This intent remains provisional until the System of Interest, stakeholder concerns, operational context and performance model are qualified.

## Epistemic stance

The reconstruction triangulates:

1. **External knowledge** — state of the art, standards, research, reference architectures and productive systems.
2. **Internal evidence** — predecessor repository, real work traces, prior evaluations, successes/failures and implemented workflows.
3. **First-principles reasoning** — purpose, mechanisms, constraints, alternatives and trade-offs.

None is sufficient alone.

```text
reference ≠ requirement
prior architecture ≠ truth
plausible deduction ≠ validated mechanism
current product capability ≠ system invariant
```

## Bootstrap work products

### Foundation and method
- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md)
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md)
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md)
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md)

### External knowledge stream
- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — **v0.3 working coverage baseline:** 17 Reference Families + 16 conditional Coverage Lenses; explicitly not architecture.
- [`references/SEED-REFERENCE-REGISTER.md`](references/SEED-REFERENCE-REGISTER.md) — verified bootstrap anchors and remaining verification frontier.
- [`references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md`](references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md)
- [`references/REFERENCE-MAP-RED-TEAM-v0.1.md`](references/REFERENCE-MAP-RED-TEAM-v0.1.md)
- [`references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md`](references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md) — resolves the first four disputed areas.
- [`references/FRONTIER-USER-CHALLENGE-v0.1.md`](references/FRONTIER-USER-CHALLENGE-v0.1.md)

### Internal evidence stream
- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md)
- [`evidence/PREDECESSOR-INVENTORY-v0.1.md`](evidence/PREDECESSOR-INVENTORY-v0.1.md)

## Reference Map v0.3 delta

The first Anchor & Conflict Sweep supports:

- **R7 expanded** to `Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research`;
- **R16 promoted:** `Strategic Management, Strategy Formation & Strategic Renewal`;
- **R17 promoted:** `Project, Programme, Portfolio, Initiative & Management Control`;
- **L15 promoted:** `Strategy / Portfolio / Initiative Coherence`;
- **L16 promoted:** `Organizational Persistence / Institutionalization`.

Important boundary:

```text
Strategy ≠ local decision quality
Strategy ≠ portfolio management
Portfolio management ≠ Work Engine
Intelligence ≠ strategy ownership
stored knowledge ≠ organizational persistence
```

## Current non-decisions

Still **not established**:

- final System of Interest boundary;
- final nested focal units;
- whether `Work Engine` is a subsystem, control policy, viewpoint, runtime loop or another construct;
- whether `Capabilities` / `Environment` are structural components;
- lifecycle/work-state model;
- runtime realization;
- which predecessor concepts survive, change level or are rejected.

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

**Do not design the Work Engine yet.**

Reference coverage is now sufficiently broad to stop adding topics by intuition. The next work is **synthesis and discrimination**:

1. broaden external Anchor & Conflict verification across the remaining highest-discrimination families;
2. build a cross-reference synthesis by `concern → competing mechanisms → evidence → boundary conditions → conflict → transfer implication`;
3. build the high-priority predecessor evidence matrix in parallel;
4. use the two streams to qualify SoI boundary, focal units and performance concerns;
5. derive `CONCERNS-AND-REQUIREMENTS v0.1` only then.

The governing rule remains: **a concept earns architectural placement only after its problem, mechanism, scope, evidence, alternatives, trade-offs and level are sufficiently established.**
