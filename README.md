# Human–AI Work System Next

> Lineage-aware reconstruction and realization program for a reference-grounded, empirically testable Human–AI Work System.

## Start here

**[`CURRENT.md`](CURRENT.md) is the controlling repository program/navigation pointer.**

Use it to determine:
- the parent System of Interest and parent program;
- which conceptual baseline is accepted;
- which prior designs remain Qualified Priors;
- which artifacts/branches are historical or non-controlling;
- the current development program and gate.

Do not infer current state from the newest-looking filename or from a historical artifact's embedded `Next` / `Current gate` section.

## Status

**ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / ARCHITECTURE → RUNTIME / OPERATING REALIZATION**

PR #3 was merged on 2026-08-19. Under ADR-0002, that merge accepts `Concerns & Requirements v0.1` and `Target Architecture v0.2` within their explicit scope and moves the repository from architecture formation into runtime/operating realization.

## Parent System of Interest

The default focal System of Interest is the **Human–AI Work System**:

> the socio-technical configuration of Human actor(s), AI capabilities, tools/workflows, relevant methods, state/knowledge, authority/control mechanisms and interfaces that jointly perform the work.

Boundary selection is claim-relative. Technical/runtime claims may focus a narrower subsystem while preserving its interfaces to the parent Work System; persistent operating/organizational claims may widen scope when the mechanism requires it.

See [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md).

## Parent program

The repository-level parent work is to develop, realize and evaluate a general Human–AI Work System that improves real professional work by composing Human judgment and agency, AI capabilities, tools, methods, state/knowledge, authority, assurance and operating mechanisms appropriately for the situation.

The development path is:

```text
Purpose / Problem / System of Interest
+ External reference landscape
+ Qualified prior / real-use evidence
↓
Concerns & Requirements
↓
Conceptual discrimination / architecture
↓
Verification / falsification
↓
Accepted conceptual architecture
↓
Runtime / Operating Realization
↓
Behavioral + implementation evaluation
↓
Evidence-driven improvement / selective reopen
```

Current position:

```text
System / SoI foundation              ✓
References + evidence                ✓ baseline established
Concerns & Requirements              ✓ accepted via PR #3
Conceptual architecture              ✓ Target Architecture v0.2 accepted
Runtime / Operating Realization      ← CURRENT PROGRAM
Behavioral effectiveness             not yet established
```

A current child topic never replaces this parent program by recency alone.

## Accepted conceptual baseline

### Normative baseline
- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md) — 11 Concerns / 13 Core Requirements / 7 Conditional Requirements.
- [`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md) — accepted conceptual architecture.
- [`decisions/ADR-0002-target-conceptual-baseline.md`](decisions/ADR-0002-target-conceptual-baseline.md) — acceptance boundary, consequences and reopen triggers.
- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md) — parent problem and claim-relative SoI/boundary.
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — lineage, reuse, reopening and architecture-change discipline.
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md) — behavioral/economic/state/authority/transition evaluation discipline.

The baseline files created in PR #3 retain pre-merge `PROPOSED` headers as provenance. ADR-0002 defines explicit merge as acceptance; PR #3 is merged. `CURRENT.md` records current status so historical metadata does not become a competing program pointer.

### Structural commitments

Target Architecture v0.2 requires only three structural commitments:

```text
A. DISTINCT RESPONSIBILITIES
   Strategic / Operating / Work / Execution / Learning-Change

B. DISTRIBUTED TYPED STATE
   authoritative state remains with legitimate owners/stores;
   working context is composed as needed

C. ADAPTIVE WORK-SELECTION CONTRACT
   for admitted/triggered work, select the minimum justified next work
   while preserving reality, requirements, state, dependencies,
   professional quality, capability/authority/runtime reality,
   assurance, uncertainty and net value
```

These do **not** mandate five runtime layers, a central DWM store, one Work Graph, a B.6 stage machine, a Semantic Compiler subsystem, a fixed Human-in-the-loop design or a specific Project/Skill/agent topology.

## Current program — Architecture → Runtime / Operating Realization

The current problem is not to invent more conceptual architecture. It is to realize the accepted semantics in the actual operating environment.

Relevant realization carriers may include:
- Human roles/judgment/authority;
- AI models and actual product behavior;
- Custom / Project Instructions and context surfaces;
- tools, Apps, deterministic systems and workflows;
- authoritative state stores and working context;
- Skills/capabilities and reusable methods;
- Projects/contexts and execution environments;
- permissions, identity, action paths and handoffs;
- operating practices, evaluation and learning/change mechanisms.

Carrier existence is not architectural necessity. A mechanism must earn its place by satisfying a real requirement or closing a demonstrated realization gap with acceptable total-system cost.

### Current realization gate

> **Recover the actual current whole-system realization and map its material coverage/gaps against the accepted Target Architecture before changing realization.**

That means incumbent-first:

```text
accepted baseline
+ actual current runtime / operating state
+ qualified predecessor behavior and failure evidence
↓
what is already satisfied?
what is materially unmet / unreliable / unowned?
↓
smallest justified realization delta
↓
evaluation against the best realistic incumbent
```

CI compression, Skill creation, Project restructuring, agents, additional state machinery or other carrier-specific work is not a default objective.

## Qualified Prior Designs / evidence lineage

High-priority qualified predecessors remain closed-but-reopenable within their accepted scope:

- `AI-native-Operating-Model` v0.2 — whole/persistent-system responsibility architecture and cross-cutting semantics;
- `human-ai-work-architecture` v1.3.1 — personal-work architecture description, state/authority/runtime-context/assurance precision;
- `Human-AI-Work-System` later B.6/Core/runtime line — Professional Work, adaptive decision/realization and real-use/failure evidence;
- `PAOS` — minimum-complexity/native-surface counter-design.

Prior designs are not universal truth, but neither are they open-by-default. Reuse and reopening follow the architecture method and ADR-0002.

## Repository areas

### Current state / foundation / method
- [`CURRENT.md`](CURRENT.md)
- [`foundation/SYSTEM-OF-INTEREST.md`](foundation/SYSTEM-OF-INTEREST.md)
- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md)
- [`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md)
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md)
- [`architecture/ARCHITECTURE-PRINCIPLES-v0.1.md`](architecture/ARCHITECTURE-PRINCIPLES-v0.1.md)
- [`decisions/ADR-0001-reconstruction-bootstrap.md`](decisions/ADR-0001-reconstruction-bootstrap.md)
- [`decisions/ADR-0002-target-conceptual-baseline.md`](decisions/ADR-0002-target-conceptual-baseline.md)
- [`evaluation/EVALUATION-STRATEGY.md`](evaluation/EVALUATION-STRATEGY.md)

### Lineage / differential evidence
- [`architecture/PRIOR-ARCHITECTURE-DIFFERENTIAL-REVIEW-v0.1.md`](architecture/PRIOR-ARCHITECTURE-DIFFERENTIAL-REVIEW-v0.1.md)
- [`architecture/LAYER-VIEW-WORKCONTROL-RUNTIME-CORRESPONDENCE-v0.1.md`](architecture/LAYER-VIEW-WORKCONTROL-RUNTIME-CORRESPONDENCE-v0.1.md)
- [`architecture/DELTA-01-02-PERSONAL-OPERATING-ARCHITECTURE-SOI-REVIEW-v0.1.md`](architecture/DELTA-01-02-PERSONAL-OPERATING-ARCHITECTURE-SOI-REVIEW-v0.1.md)
- [`architecture/DELTA-03-VIEW-CONTROL-PLANE-RECONCILIATION-v0.1.md`](architecture/DELTA-03-VIEW-CONTROL-PLANE-RECONCILIATION-v0.1.md)
- [`evidence/EVIDENCE-MAP.md`](evidence/EVIDENCE-MAP.md)
- [`evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md`](evidence/PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md)
- [`evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md`](evidence/PRIOR-ARCHITECTURE-RECONCILIATION-MATRIX-v0.1.md)
- [`evidence/PREDECESSOR-INVENTORY-v0.1.md`](evidence/PREDECESSOR-INVENTORY-v0.1.md)
- [`reviews/BOOTSTRAP-CLOSURE-REVIEW-v0.1.md`](reviews/BOOTSTRAP-CLOSURE-REVIEW-v0.1.md)

### Reference stream
- [`references/REFERENCE-MAP.md`](references/REFERENCE-MAP.md) — working coverage/reference evidence; historical embedded gate text does not control current program state.
- [`references/SEED-REFERENCE-REGISTER.md`](references/SEED-REFERENCE-REGISTER.md)
- [`references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md`](references/REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md)
- [`references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md`](references/REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md)
- [`references/REFERENCE-MAP-RED-TEAM-v0.1.md`](references/REFERENCE-MAP-RED-TEAM-v0.1.md)
- [`references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md`](references/REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md)
- [`references/CROSS-REFERENCE-SYNTHESIS-DISCRIMINATION-v0.1.md`](references/CROSS-REFERENCE-SYNTHESIS-DISCRIMINATION-v0.1.md)
- [`references/FRONTIER-USER-CHALLENGE-v0.1.md`](references/FRONTIER-USER-CHALLENGE-v0.1.md)

## Historical development state

The bootstrap `Δ4 Adaptive Work-Control → Δ5 Architecture/runtime semantic compilation → Δ6 Knowledge Capital` sequence was superseded as the controlling architecture-development program by PR #3 / ADR-0002. Those artifacts remain evidence and lineage; they are not deleted or rewritten merely to remove historical `Next` language.

Closed/unmerged PRs and candidate branches are likewise non-controlling unless independently re-qualified and promoted.

## Epistemic / change stance

```text
reference ≠ requirement
qualified prior ≠ universal truth
qualified prior ≠ open-by-default
raw internal evidence ≠ accepted design
architecture acceptance ≠ runtime installation
runtime installation ≠ behavioral effectiveness
candidate existence ≠ promotion
```

Foundational architecture is closed by default. New evidence should produce the narrowest supported repair; architecture reopens only under a named ADR-0002 trigger.
