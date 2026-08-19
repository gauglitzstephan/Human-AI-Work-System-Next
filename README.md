# Human–AI Work System Next

> Lineage-aware reconstruction program for a reference-grounded, empirically testable Human–AI Work System.

## Start here

**[`CURRENT.md`](CURRENT.md) is the controlling repository state pointer.**

Use it to determine:
- what the current bootstrap decisions are;
- which prior designs are treated as Qualified Priors;
- which intermediate artifacts are historical/non-controlling;
- what the active next gate is.

Do not infer current development state from the newest-looking filename or from a historical artifact's embedded `Next` / `Current gate` section.

## Status

**BOOTSTRAP / PRE-ARCHITECTURE / DIFFERENTIAL RECONCILIATION**

This repository is not another blank-slate architecture branch. It preserves qualified prior designs, reconciles architecture types, and creates new architecture only where a genuine unresolved delta remains.

## Working intent

Develop or select a general Human–AI Work System that improves real professional work by composing Human judgment and agency, AI capabilities, tools, knowledge, state and existing processes appropriately for the situation — and that scales from one Human + AI to larger Human–AI organizations without architecture rewrite.

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

## Core reconstruction artifacts

### Current state / foundation / method
- [`CURRENT.md`](CURRENT.md) — controlling state/navigation pointer
- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md) — v0.3 lineage-aware / closure-synced
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — v0.2 lineage-corrected
- [`architecture/ARCHITECTURE-PRINCIPLES-v0.1.md`](architecture/ARCHITECTURE-PRINCIPLES-v0.1.md)
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md) — lineage-corrected bootstrap ADR
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md)

### Differential / lineage reconciliation
- [`architecture/PRIOR-ARCHITECTURE-DIFFERENTIAL-REVIEW-v0.1.md`](architecture/PRIOR-ARCHITECTURE-DIFFERENTIAL-REVIEW-v0.1.md)
- [`architecture/LAYER-VIEW-WORKCONTROL-RUNTIME-CORRESPONDENCE-v0.1.md`](architecture/LAYER-VIEW-WORKCONTROL-RUNTIME-CORRESPONDENCE-v0.1.md)
- [`architecture/DELTA-01-02-PERSONAL-OPERATING-ARCHITECTURE-SOI-REVIEW-v0.1.md`](architecture/DELTA-01-02-PERSONAL-OPERATING-ARCHITECTURE-SOI-REVIEW-v0.1.md)
- [`architecture/DELTA-03-VIEW-CONTROL-PLANE-RECONCILIATION-v0.1.md`](architecture/DELTA-03-VIEW-CONTROL-PLANE-RECONCILIATION-v0.1.md)
- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md) — v0.2 with I0–I4 status classes
- [`evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md`](evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md)
- [`evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md`](evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md)
- [`evidence/PREDECESSOR-INVENTORY-v0.1.md`](evidence/PREDECESSOR-INVENTORY-v0.1.md)

### Reference stream
- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — v0.3 working coverage baseline; its historical `Current gate` is not the project-state pointer
- [`references/SEED-REFERENCE-REGISTER.md`](references/SEED-REFERENCE-REGISTER.md)
- [`references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md`](references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md)
- [`references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md`](references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md)
- [`references/REFERENCE-MAP-RED-TEAM-v0.1.md`](references/REFERENCE-MAP-RED-TEAM-v0.1.md)
- [`references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md`](references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md)
- [`references/CROSS-REFERENCE-SYNTHESIS-DISCRIMINATION-v0.1.md`](references/CROSS-REFERENCE-SYNTHESIS-DISCRIMINATION-v0.1.md) — retained intermediate synthesis; later deltas supersede parts of its candidate dispositions
- [`references/FRONTIER-USER-CHALLENGE-v0.1.md`](references/FRONTIER-USER-CHALLENGE-v0.1.md)

## Leading type-correct architecture interpretation

```text
RESPONSIBILITY ARCHITECTURE
→ Strategic / Operating / Work / Execution / Learning

ARCHITECTURE DESCRIPTION VIEWS
→ Mission & Outcome / Work Process / Information & State /
  Capability & Resource / Interaction & Authority /
  Quality & Assurance / Governance & Learning /
  Execution Context & Integration

CROSS-CUTTING INTEGRITY CONTRACTS
→ Reality & Provenance
→ Authority / Governance / Security
→ Assurance & Risk
→ Performance / Economics / Value
→ Knowledge / Configuration / Change

WITHIN WORK ARCHITECTURE
→ Work Object / Work Product / conditional Work Units / Work Graph
→ optional adaptive next-work control

RUNTIME / OPERATING PROFILE
→ context-specific minimal realization (e.g. PAOS-like)
```

The categories above are different architecture object types, not peer layers.

## Architecture principles now active for reconstruction

Key principles include:

- optimize the whole Human–AI work system;
- responsibility/role before actor binding;
- scale-invariant semantics, scale-conditional structures;
- persistent Operating Architecture distinct from episodic Work;
- economics and Human attention as architecture inputs;
- layers/views/control/runtime remain type-correct;
- capability/access/authority/accountability remain distinct;
- persistent ownership only where divergence matters;
- simple work collapses aggressively;
- design for actor substitution, extensibility and portability;
- preserve material semantics through runtime compression;
- qualified prior architecture is closed-but-reopenable.

## Differential results to date

### Δ1 — Personal/general Operating Architecture

**Resolved provisionally:** retain Operating Architecture as a scale-invariant responsibility class. Generalize `organization/roles` to `role/responsibility → actor binding`; enterprise-specific mechanisms are conditional.

### Δ2 — System-of-Interest boundary

**Resolved provisionally:** do not promote a permanent `SoI-P / SoI-E` taxonomy. Use claim-relative boundary selection. Human–AI Work System is the default focal SoI for work/outcome claims; focus narrower technical or wider organizational scope only when the claim requires it.

### Δ3 — Views vs Control Planes

**Resolved provisionally:** retain the five responsibility layers and eight accepted Views. Retain the five Control Plane semantics but represent them in Next as cross-cutting **Integrity Contracts / lenses**, not a third peer decomposition.

No new top-level responsibility layer or View is currently justified.

## Provisionally inherited common semantics

Unless a named reopen trigger appears, stop first-principles re-derivation of:

- request/input ≠ complete requirement;
- authoritative reality before material redesign;
- Work Object / Work Product / Working State distinctions;
- conditional Work Units / Work Graph decomposition;
- Human/AI/tool/workflow allocation by effective capability/context/authority;
- capability ≠ access ≠ authority ≠ verified performance;
- internal readiness gate ≠ Human Gate;
- technical completion ≠ professional fitness ≠ acceptance ≠ use ≠ outcome ≠ value;
- explicit ownership/promotion for persistent Operating patterns/state;
- execution-context dependence of actual capability/state;
- governed Learning without silent mutation authority;
- aggressive collapse for simple work;
- architecture acceptance ≠ runtime installation ≠ behavioral effectiveness.

## Remaining genuine architecture delta

1. **Δ4 Adaptive Work-Control value** — does Semantic Compiler / Work-Control policy materially improve behavior over accepted Work Architecture + PAOS-like conditional routing?
2. **Δ5 Architecture→runtime semantic compilation** — how are load-bearing semantics preserved under severe active-context/salience constraints?
3. **Δ6 Knowledge Capital ownership/promotion** — where do reusable knowledge, Work patterns, Skills/capabilities, Operating patterns and authoritative state live and transition?

## Current gate

**Do not create new top-level architecture by default. Do not create a peer Work Engine layer.**

After the bootstrap PR closes, start a new branch / PR for:

> **Δ4 Adaptive Work-Control Differential Review**

Compare:

```text
accepted Work Architecture only
vs
Work Architecture + Semantic Compiler / adaptive Work-Control
vs
PAOS-style minimal conditional routing
```

The question is empirical and architectural: whether an explicit adaptive controller adds unique behavioral value after its semantic and coordination cost is included.
