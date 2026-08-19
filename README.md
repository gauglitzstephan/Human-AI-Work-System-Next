# Human–AI Work System Next

> Lineage-aware reconstruction program for a reference-grounded, empirically testable Human–AI Work System.

## Status

**BOOTSTRAP / PRE-ARCHITECTURE / LINEAGE RECONCILIATION**

This repository is not another blank-slate architecture branch.

Its job is to recover and reconcile the substantial existing Human–AI architecture lineage, preserve qualified prior knowledge, identify genuine conflicts/gaps, and create new architecture only where prior designs plus current evidence are insufficient.

## Working intent

Develop or select a general Human–AI Work System that improves real professional work by composing human judgment and agency, AI capabilities, tools, knowledge, state and existing processes appropriately for the situation.

## Epistemic stance

The reconstruction uses four distinct inputs:

1. **External knowledge** — research, standards, reference architectures and productive systems.
2. **Qualified Prior Designs** — bounded prior architecture decisions with sufficient reference, review/falsification and acceptance to be closed-but-reopenable.
3. **Raw internal / real-use evidence** — work traces, failures, corrections, runtime and implementation evidence.
4. **First-principles reasoning** — purpose, mechanisms, constraints, alternatives and trade-offs.

```text
reference ≠ requirement
qualified prior ≠ universal truth
qualified prior ≠ open-by-default
raw internal evidence ≠ accepted design
current product capability ≠ system invariant
```

## Bootstrap work products

### Foundation and method
- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md)
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — **v0.2 lineage-corrected**
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md)
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md)

### Reference stream
- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — v0.3 working coverage baseline
- [`references/SEED-REFERENCE-REGISTER.md`](references/SEED-REFERENCE-REGISTER.md)
- [`references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md`](references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md)
- [`references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md`](references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md)
- [`references/REFERENCE-MAP-RED-TEAM-v0.1.md`](references/REFERENCE-MAP-RED-TEAM-v0.1.md)
- [`references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md`](references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md)
- [`references/FRONTIER-USER-CHALLENGE-v0.1.md`](references/FRONTIER-USER-CHALLENGE-v0.1.md)

### Lineage / evidence stream
- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md) — **v0.2 with I0–I4 status classes**
- [`evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md`](evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md)
- [`evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md`](evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md)
- [`evidence/PREDECESSOR-INVENTORY-v0.1.md`](evidence/PREDECESSOR-INVENTORY-v0.1.md)

## Central process correction

The relevant predecessor estate is broader than `Human-AI-Work-System` alone.

High-priority priors include:

- `AI-native-Operating-Model` — accepted five-layer/five-control-plane foundation with Work Architecture and Work Units;
- `human-ai-work-architecture` — accepted v1.3.1 semantics and execution-context architecture;
- `Human-AI-Work-System` — current Core/B.6/Semantic Compiler/runtime line and real-use evidence;
- `PAOS` — minimum-kernel/native-surface counter-design;
- `Personal-AI-Operating-Model` — HAPS/PAWS/AMM reconstruction research;
- persistence/workspace repositories — promotion/state counter-design lineage.

A prior accepted question is reopened only with a named trigger: changed SoI, new external evidence, new real-use failure, stronger rival, material prior conflict, implementation impossibility, or evidence that the prior was not actually qualified.

## Reclassification of Q1–Q3

The first Cross-Reference synthesis is retained as useful research but is **not treated as wholly novel derivation**.

- Work Units / Work Graph / Work→Outcome semantics were already substantially developed and qualified.
- Strategy/Operating/Work/Execution separation already exists in the accepted AI-native Operating Model.
- PAOS already supplies a serious minimal counter-design against universal formal Work Objects.
- `nested claim-relative SoIs` may be an incremental boundary repair and remains to be compared against the prior models.
- F0–F4 and SC/PC/WC/OC are candidate normalization/views until they demonstrate incremental value over existing structures.

## Current non-decisions

Still not established:

- which prior architecture becomes the parent representation;
- whether five layers, eight views, Core/B.6, PAOS or a synthesis is the best representation;
- whether `Work Engine` adds a distinct mechanism beyond accepted Work Architecture + Semantic Compiler + simple routing;
- final SoI model;
- final runtime realization.

## Corrected reconstruction flow

```text
Recover predecessor lineage
        ↓
Classify: raw evidence / candidate / qualified prior / runtime / counter-design
        ↓
Reconcile qualified priors
RETAIN / REFINE / RELOCATE / MERGE / SUPERSEDE / REJECT / OPEN-CONFLICT
        ↓
Identify genuine reopen triggers, conflicts and gaps
        ↓
Use external references + current real evidence to discriminate only those
        ↓
Qualified concerns / requirements
        ↓
Architecture delta or selection
        ↓
Behavioral / implementation evaluation
```

## Current gate

**Do not continue Q4–Q8 as blank-slate synthesis. Do not design the Work Engine.**

Next work:

> **Prior Architecture Differential Review v0.1**

Compare the four strongest competing representations:

1. `AI-native-Operating-Model` accepted five-layer/five-control-plane model;
2. `human-ai-work-architecture` accepted eight-view model;
3. `Human-AI-Work-System` Core/B.6 + Semantic Compiler candidate;
4. `PAOS` minimum-kernel/native-surface rival.

Determine:

- whether they are alternative architectures or orthogonal views/realizations;
- which questions each uniquely solves;
- where they conflict;
- which accepted semantics are common and can be frozen;
- what the **actual unresolved architecture delta** is.

Only that delta should drive further Cross-Reference Synthesis.
