# System of Interest — Foundation v0.3

**Status:** PROVISIONAL / PRE-ARCHITECTURE / LINEAGE-AWARE  
**Purpose:** Define the problem and claim-relative system boundary while preserving qualified predecessor architecture rather than re-deriving it.  
**Current basis:** predecessor lineage/reconciliation + Reference Map v0.3 + Reference Envelope calibration + Δ1/Δ2 differential review.

This document is not the final architecture.

---

# 1. Problem statement

General-purpose AI can perform many isolated cognitive and production tasks well. Reliable professional work, however, depends on the coupled configuration of Human judgment and agency, AI capabilities, tools, methods, authoritative state, interfaces, authority, assurance, receiving context and downstream use.

The problem is therefore:

> **How can Human and AI capabilities be composed into a scalable work system that improves professional quality, real-world outcomes and work economics while preserving reality contact, justified Human authority/agency, proportional complexity, recoverability and learning?**

The target is not maximum AI autonomy and not a universal visible workflow.

---

# 2. Default System of Interest

For claims about professional-work performance, quality, economics, Human agency, transition or outcomes, the default System of Interest is:

> **Human–AI Work System** — the socio-technical configuration of Human actor(s), AI capabilities, tools/workflows, relevant methods, state/knowledge, authority/control mechanisms and interfaces that jointly perform the work.

This is consistent with qualified prior architecture in `human-ai-work-architecture` and the whole-work-system optimization principle in `AI-native-Operating-Model`.

## Claim-relative boundary rule

Do **not** maintain a mandatory permanent `SoI-P / SoI-E` taxonomy.

Select the focal system/entity relative to the claim:

```text
work / outcome claim
→ Human–AI Work System is focal

technical / runtime / security / V&V claim
→ focus the relevant engineered subsystem/system element
  while preserving interfaces to the parent Work System

persistent operating / organizational claim
→ widen focus to the Operating system/organization where that scale
  materially changes the mechanism
```

Use the smallest boundary that preserves the mechanism and responsibility needed for the claim.

Explicit nested SoI types should be introduced only if ordinary parent/subsystem notation repeatedly fails to keep material claims distinct.

---

# 3. Personal scale is a minimum non-trivial operating context

A single Human working with AI is not identical to a legal or social organization. But once heterogeneous capabilities are coordinated over time, organization-like operating responsibilities already exist:

- purpose/value and prioritization;
- role/responsibility allocation;
- capability selection/substitution;
- authoritative state and Knowledge Capital;
- recurring work patterns/interfaces;
- authority and external-action boundaries;
- scarce resource allocation and opportunity cost;
- assurance/risk/recovery;
- learning, promotion and retirement.

Therefore:

> **Operating Architecture is treated as a scale-invariant responsibility class. Institutional realization mechanisms are conditional.**

At personal scale one Human may bind many legitimate ownership roles. At larger scale those same roles can bind to multiple Humans, teams, AI actors, tools or workflows without redefining the underlying responsibility semantics.

See `architecture/DELTA-01-02-PERSONAL-OPERATING-ARCHITECTURE-SOI-REVIEW-v0.1.md`.

---

# 4. Mission — provisional

Develop, select or reconcile a general Human–AI Work System architecture that:

1. supports high-quality professional work across heterogeneous tasks;
2. scales from one Human + AI to larger Human–AI organizations without architecture rewrite;
3. keeps persistent Operating responsibilities distinct from episodic Work and concrete Execution;
4. composes actors by capability, authority and economics rather than title or technology;
5. allows simple work to collapse to direct execution;
6. preserves material semantics through runtime realization;
7. learns and changes without discarding qualified prior knowledge or silently mutating authoritative state.

---

# 5. Intended performance concerns

The system should improve, where material:

- **Outcome effectiveness and value**;
- **professional/intended-use quality**;
- **reality and epistemic integrity**;
- **work economics** — Human attention/time/energy, AI/tool cost, latency, coordination, rework, maintenance and opportunity cost;
- **Human capability, agency and authorship**;
- **authority/accountability integrity**;
- **robustness, recoverability and adaptability**;
- **transition, adoption and in-use performance**;
- **portability and avoidable dependency/lock-in**.

These remain performance concerns, not a final metric suite.

---

# 6. Scale-invariant role model — candidate contract

Architecture should define responsibility before actor binding.

```text
Role / Responsibility
→ purpose
→ obligations
→ required capability
→ decision/action rights
→ accountability / acceptance
→ interfaces

Actor Binding
→ Human | AI | Human+AI | Tool | Workflow | Team | External Actor
→ verified capability
→ access
→ granted authority
→ current constraints
```

A Human may hold many roles. A future AI/workflow may take over a production responsibility without inheriting Human values, commitment authority, risk acceptance or acceptance rights.

This candidate is an architectural abstraction, not a mandatory runtime object.

---

# 7. Persistent Operating vs episodic Work

Qualified prior architecture already supports this distinction.

## Persistent Operating responsibilities

Only things that must remain coherent across Work Episodes belong to persistent Operating Architecture, such as:

- capability portfolio and performance expectations;
- role/authority bindings;
- authoritative state / Knowledge Capital;
- accepted recurring patterns/processes;
- platform/interfaces and permissions;
- economics/capacity;
- risk/control mechanisms;
- lifecycle/change ownership.

## Episodic Work responsibilities

A concrete Work Episode uses current reality and the persistent operating context to:

- form/confirm the Work Object and intended outcome;
- choose professional method/evidence;
- create Work Products;
- decompose conditionally into Work Units/Work Graph;
- allocate Human/AI/tool functions;
- execute/integrate;
- assure the claimed readiness;
- transition toward use/outcome where required.

One-off work does not become Operating state merely because it was useful. Institutionalization is a separate authorized transition.

---

# 8. Work scales — recovered semantics, not a new mandatory taxonomy

Prior architectures already distinguish local operations, Work Episodes, persistent initiatives/projects, portfolios and the configured Work System.

These scales should remain semantically distinct where they change:

- purpose/owner;
- persistence;
- state/completion;
- authority/acceptance;
- dependencies;
- resource allocation/opportunity cost;
- outcome horizon;
- monitoring/reopen conditions.

Do not promote the provisional labels `F0–F4` into a new canonical ontology unless they add decision value beyond the existing concepts.

The complete **Work Episode** remains a strong default evaluation/control scope for bounded professional work, while simple direct work may collapse operationally to one response/action.

---

# 9. Qualified prior architecture status

The reconstruction currently treats the following as high-priority closed-but-reopenable priors:

1. `AI-native-Operating-Model` v0.2 — five responsibility layers + five cross-cutting control planes;
2. `human-ai-work-architecture` v1.3.1 — eight architecture views and accepted Work/State/Authority/Execution-context semantics;
3. `Human-AI-Work-System` — later Work/Core/B.6/Semantic Compiler/runtime line and real-use evidence;
4. `PAOS` — minimum-kernel/native-surface counter-design.

Their common semantics are provisionally inherited rather than re-derived absent a named reopen trigger.

---

# 10. Architecture principles

The current reconstruction is constrained by `architecture/ARCHITECTURE-PRINCIPLES-v0.1.md`.

Especially relevant here:

- optimize the whole Human–AI work system;
- responsibility/role before actor;
- scale-invariant semantics, scale-conditional structures;
- persistent Operating vs episodic Work;
- economics as architecture input;
- type-correct separation of layers/views/control/runtime;
- capability/access/authority separation;
- proportionality and latent complexity;
- actor substitution/extensibility/portability;
- preserve material semantics through realization;
- accepted prior architecture is closed-but-reopenable.

---

# 11. Remaining genuine architecture deltas

Δ1 and Δ2 are now provisionally resolved:

```text
Δ1 personal/general Operating transfer
→ RETAIN Operating Architecture responsibility class
→ GENERALIZE role/actor language
→ institutional mechanisms conditional

Δ2 permanent dual/nested SoI taxonomy
→ DO NOT PROMOTE
→ use claim-relative boundary selection instead
```

The remaining decision-relevant architecture deltas are:

### Δ3 — Views vs control-plane compression
Can the eight accepted Views and five accepted Control Planes be simplified without losing ownership, observability or important cross-cutting semantics?

### Δ4 — Adaptive Work Control
Does the Semantic Compiler / adaptive Work-Control policy add measurable value beyond accepted Work Architecture plus simple PAOS-style routing and proportional activation?

### Δ5 — Architecture → runtime semantic compilation
How can material architecture semantics remain behaviorally salient in finite AI context/runtime without copying the full architecture or silently losing functions?

### Δ6 — Knowledge Capital ownership and promotion
Which reusable outputs remain knowledge, which become validated capability/skill, which become persistent Operating patterns/state, and how are promotion, ownership, freshness and retirement governed?

---

# 12. Current non-decisions

Still not established:

- whether the accepted five-layer architecture is the final parent representation;
- how the eight Views and five Control Planes should be reconciled/compressed;
- whether `Work Engine` survives as a distinct Work-Control mechanism;
- exact runtime realization;
- final capability/Knowledge Capital lifecycle representation;
- final evaluation model sufficient to prove incremental behavioral value.

---

# 13. Current gate

Do **not** return to blank-slate Human–AI architecture derivation.

Proceed only through the remaining deltas:

```text
Δ3 view/control-plane reconciliation
→ Δ4 adaptive Work-Control discrimination
→ Δ5 architecture/runtime semantic compilation
→ Δ6 Knowledge Capital lifecycle
→ integrated architecture selection/delta
→ behavioral + implementation evaluation
```

External reference research is opened only where it can discriminate these remaining decisions or a new qualified reopen trigger appears.
