# System of Interest — Foundation v0.4

**Status:** QUALIFIED FOUNDATION / POST-ARCHITECTURE CLOSURE-SYNCED  
**Purpose:** Define the parent problem and claim-relative System-of-Interest boundary for the Human–AI Work System across architecture, realization and evaluation.  
**Current basis:** predecessor lineage/reconciliation + external reference program + Concerns & Requirements v0.1 + accepted Target Architecture v0.2 / ADR-0002.  
**Acceptance note:** the core SoI/boundary semantics in this file are incorporated into the accepted Target Architecture v0.2. This file is a foundation/navigation artifact; it does not create a separate architecture acceptance event.

Current repository program state and next-work authority are controlled by `CURRENT.md`.

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

### Parent-continuity implication

A narrower realization, evaluation or implementation question remains a child of the Human–AI Work System unless a changed claim explicitly changes the SoI.

Examples:

```text
Custom Instructions / Project Instructions / Skill / agent / state-control mechanism
→ possible realization element
→ not a new parent SoI by recency

runtime conformance question
→ narrower technical focal boundary
→ interfaces and contribution to parent Work System remain explicit
```

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

---

# 4. Mission

Develop, realize and evaluate a general Human–AI Work System that:

1. supports high-quality professional work across heterogeneous tasks;
2. scales from one Human + AI to larger Human–AI organizations without architecture rewrite;
3. keeps persistent Operating responsibilities distinct from episodic Work and concrete Execution;
4. composes actors by capability, authority and economics rather than title or technology;
5. allows simple work to collapse to direct execution;
6. preserves material semantics through runtime realization;
7. learns and changes without discarding qualified prior knowledge or silently mutating authoritative state;
8. improves through evidence from real use without turning every local failure into new global architecture.

The mission is system-level. Producing architecture, a runtime carrier or an artifact is not itself the outcome.

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

These are performance concerns, not a final metric suite. `evaluation/EVALUATION-STRATEGY.md` governs claim-matched evaluation.

---

# 6. Scale-invariant role model

Architecture defines responsibility before actor binding.

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

This is an architectural abstraction, not a mandatory runtime object.

---

# 7. Persistent Operating vs episodic Work

Persistent Operating responsibilities and episodic Work remain distinct.

## Persistent Operating responsibilities

Only things that must remain coherent across Work Episodes belong to persistent Operating responsibility, such as:

- capability portfolio and performance expectations;
- role/authority bindings;
- authoritative state / Knowledge Capital;
- accepted recurring patterns/processes;
- platform/interfaces and permissions;
- economics/capacity;
- risk/control mechanisms;
- lifecycle/change ownership.

## Episodic Work responsibilities

A concrete Work Episode uses current reality and persistent operating context to:

- form/confirm the intended outcome / Work Object where explicit representation adds value;
- choose professional method/evidence;
- create Work Products;
- decompose conditionally into Work Units/Work Graph where dependency structure warrants it;
- allocate Human/AI/tool functions;
- execute/integrate;
- assure the claimed readiness;
- transition toward use/outcome where required.

One-off work does not become Operating state merely because it was useful. Institutionalization is a separate legitimate transition.

---

# 8. Work scales — recovered semantics, not a mandatory taxonomy

Prior architectures distinguish local operations, Work Episodes, persistent initiatives/projects, portfolios and the configured Work System.

These scales remain semantically distinct where they change purpose/owner, persistence, state/completion, authority/acceptance, dependencies, resource allocation/opportunity cost, outcome horizon or monitoring/reopen conditions.

Do not promote provisional labels such as `F0–F4` into a new canonical ontology unless they add decision value beyond existing concepts.

The complete **Work Episode** remains a strong default evaluation/control scope for bounded professional work, while simple direct work may collapse operationally to one response/action.

---

# 9. Qualified prior architecture status

High-priority closed-but-reopenable priors remain:

1. `AI-native-Operating-Model` v0.2 — responsibility architecture plus cross-cutting control semantics;
2. `human-ai-work-architecture` v1.3.1 — architecture views and accepted Work/State/Authority/Execution-context semantics;
3. `Human-AI-Work-System` — later Work/Core/B.6/Semantic Compiler/runtime line plus real-use/failure evidence;
4. `PAOS` — minimum-kernel/native-surface counter-design.

Their accepted semantics remain qualified priors within scope rather than being re-derived absent a named trigger.

---

# 10. Architecture principles

The system remains constrained by `architecture/ARCHITECTURE-PRINCIPLES-v0.1.md`, especially:

- optimize the whole Human–AI Work System;
- responsibility/role before actor;
- scale-invariant semantics, scale-conditional structures;
- persistent Operating vs episodic Work;
- economics as architecture input;
- type-correct separation of architecture description, work-control and runtime realization;
- capability/access/authority separation;
- proportionality and latent complexity;
- actor substitution/extensibility/portability;
- preserve material semantics through realization;
- accepted prior architecture is closed-but-reopenable.

---

# 11. Bootstrap differential history

The bootstrap pass resolved several questions provisionally before the independent requirements-derived Target Architecture was accepted.

### Δ1 — Personal/general Operating Architecture

Result retained in the accepted baseline: Operating responsibility is scale-invariant; institutional mechanisms are conditional.

### Δ2 — System-of-Interest boundary

Result retained in the accepted baseline: no permanent dual/nested `SoI-P / SoI-E` taxonomy; use claim-relative boundary selection.

### Δ3 — Views vs Control Planes

The bootstrap reconciliation remains lineage evidence. Target Architecture v0.2 subsequently selected a smaller requirements-derived conceptual baseline and does not require predecessor Views or Control-Plane groupings as mandatory architecture objects.

The bootstrap differential records remain useful evidence; they do not independently control current development.

---

# 12. Architecture status after PR #3

PR #3 merged `Concerns & Requirements v0.1`, `Target Architecture v0.2` and ADR-0002. Under ADR-0002, the merge accepts the conceptual baseline within its explicit scope/non-claims.

The previously controlling bootstrap sequence:

```text
Δ4 Adaptive Work-Control
→ Δ5 Architecture → runtime semantic compilation
→ Δ6 Knowledge Capital ownership/promotion
```

is therefore **SUPERSEDED AS THE ARCHITECTURE-DEVELOPMENT PROGRAM**.

This does not erase its findings. Relevant issues may reappear as:

- realization questions;
- implementation constraints;
- evaluation hypotheses;
- Knowledge-Capital / operating-design questions;
- architecture reopen triggers if evidence eventually warrants reopening.

They are no longer mandatory sequential architecture gates.

Foundational architecture is closed by default under ADR-0002.

---

# 13. Current open claims / non-claims

Still not established by conceptual architecture acceptance:

- behavioral superiority / Human–AI synergy;
- runtime installation or conformance;
- cross-domain empirical generality;
- the best concrete allocation across Human, AI, tools, instructions, Skills/workflows, Projects/contexts and state stores;
- which reusable mechanisms deserve promotion into persistent capability / Operating state;
- in-use outcome/value performance;
- whether any particular runtime/controller/agent/topology improves total-system performance against the best realistic incumbent.

These are realization/evaluation questions unless a named ADR-0002 reopen trigger is established.

---

# 14. Current parent program

The repository is now in:

> **Architecture → Runtime / Operating Realization**

Parent continuity is:

```text
Human–AI Work System                         PARENT SoI
↓
problem / mission / performance concerns     FOUNDATION
↓
Concerns & Requirements v0.1                 ACCEPTED BASELINE
↓
Target Architecture v0.2                     ACCEPTED CONCEPTUAL BASELINE
↓
Runtime / Operating Realization              CURRENT PROGRAM
↓
behavioral + implementation evaluation       REQUIRED BEFORE EFFECTIVENESS CLAIM
↓
evidence-driven improvement                  LOCAL BY DEFAULT; ARCHITECTURE REOPEN ONLY BY TRIGGER
```

The realization phase must recover the actual current Human–AI operating/runtime configuration and qualified predecessor behavior before redesign. It then identifies only material coverage gaps or failures against the accepted system semantics and tests the smallest adequate changes.

A child mechanism is justified by its contribution to this parent system, not by architectural elegance or availability of a product feature.
