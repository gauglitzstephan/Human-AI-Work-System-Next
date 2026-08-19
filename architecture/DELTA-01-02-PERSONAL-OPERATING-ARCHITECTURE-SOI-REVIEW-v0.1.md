# Δ1 + Δ2 Differential Review v0.1

**Status:** PROVISIONAL DISCRIMINATION / PRE-ARCHITECTURE  
**Scope:** Δ1 personal/general transfer of Operating Architecture · Δ2 System-of-Interest boundary value  
**Parent priors:** `AI-native-Operating-Model` v0.2; `human-ai-work-architecture` v1.3.1; `Human-AI-Work-System`; `PAOS`.

---

# 1. Executive result

## Δ1 — Personal/general transfer of Operating Architecture

**Disposition:** RETAIN THE OPERATING-ARCHITECTURE RESPONSIBILITY CLASS, GENERALIZE ITS ACTOR/ORGANIZATION LANGUAGE, MAKE INSTITUTIONAL MECHANISMS CONDITIONAL.

The accepted enterprise-oriented Operating Architecture is not enterprise-only at the mechanism level. Its core responsibilities already arise in a one-Human-plus-AI system whenever capabilities, state, roles/authority, reusable patterns, platforms, economics or learning persist across Work Episodes.

The transferable abstraction is:

> **Operating Architecture = the persistent arrangement of capabilities, role/authority bindings, state/knowledge, reusable work patterns, technology interfaces, economics, controls and lifecycle ownership that makes repeated Human–AI work possible.**

What changes with scale is primarily **mechanism and cardinality**, not the core responsibility set.

```text
personal scale
role owner may equal one Human
capability portfolio may be Human + several AI/tool capabilities
coordination may be mostly internal/AI-mediated
formal governance may be unnecessary

organizational scale
roles bind to multiple Humans/teams/AI actors
coordination and interfaces become explicit
resource allocation/portfolio control becomes material
segregation, incentives and institutional governance may become necessary
```

Therefore:

```text
Operating Architecture — RETAIN
enterprise-specific ceremony — CONDITIONAL
```

## Δ2 — System-of-Interest boundary

**Disposition:** RETAIN THE HUMAN–AI WORK SYSTEM AS THE DEFAULT PERFORMANCE SoI; REPLACE PERMANENT SoI-P/SoI-E TAXONOMY WITH A CLAIM-RELATIVE BOUNDARY PRINCIPLE.

The explicit nested-SoI idea is useful as a diagnostic but does not yet justify permanent visible architecture objects.

Default:

- For claims about work quality, economics, Human agency, transition or outcomes, the focal SoI is the **Human–AI Work System**.
- For a technical/security/runtime/lifecycle claim, temporarily focus the relevant engineered subsystem/system element while preserving its interfaces to the parent Work System.
- For organizational strategy/Operating claims, widen the focal system only when those persistent responsibilities materially determine the claim.

Use the **smallest boundary that preserves the mechanism relevant to the claim**, while maintaining parent/environment relationships.

This is simpler than making `SoI-P` and `SoI-E` mandatory named objects.

---

# 2. Δ1 — Why personal Human–AI work already has operating-model properties

A single Human using AI is not identical to a legal or social organization. But once heterogeneous actors/capabilities are coordinated over time, several organization-like design problems already exist:

- purpose/value and prioritization;
- division/allocation of cognitive and production functions;
- capability selection and substitution;
- role, responsibility and authority boundaries;
- shared/authoritative state and memory;
- reusable work patterns and interfaces;
- execution environments and permissions;
- scarce resources and opportunity cost;
- quality/risk controls;
- learning, promotion and retirement.

These functions exist even when one Human holds every legitimate ownership role.

The key abstraction is therefore not `organization chart`, but:

```text
persistent coordination system
```

A personal Human–AI setup can be its smallest non-trivial case.

---

# 3. Transfer test of accepted Operating Architecture responsibilities

The accepted `AI-native-Operating-Model` defines ten Operating Architecture responsibilities. Each is tested below for personal/general transfer.

| Prior responsibility | Personal/general disposition | Transfer interpretation |
|---|---|---|
| Value streams / stakeholder model | **RETAIN, COMPRESS** | beneficiary, receiving context, value mechanism; formal value-stream mapping only when needed |
| Capabilities | **RETAIN** | Human/AI/tool/workflow capability portfolio and performance envelopes already matter personally |
| Organization and roles | **RETAIN ABSTRACTION, GENERALIZE** | role/responsibility before actor; one Human may bind many roles; teams/org units conditional |
| Governance and decision rights | **RETAIN CORE, COMPRESS** | purpose, commitments, acceptance and external-action authority already need ownership; boards/committees conditional |
| Processes / ways of working | **RETAIN CONDITIONALLY** | recurring accepted patterns may persist; one-off work remains Work Architecture only |
| Data and knowledge | **RETAIN** | authoritative state, provenance, context, Knowledge Capital and persistence are already material personally |
| Technology / AI platforms | **RETAIN INTERFACE ROLE** | model/tool/surface capability, state and portability affect real work even for one user |
| Performance and economics | **RETAIN** | attention, time, AI/tool cost, coordination, rework, opportunity cost and value are first-class at personal scale |
| Risk, controls and assurance | **RETAIN PROPORTIONALLY** | consequence/authority/security/recovery matter; formal control environment conditional |
| Change and lifecycle | **RETAIN FOR PERSISTENT OBJECTS** | capabilities, skills, instructions, patterns and state need promotion/version/retirement only when persisted |

**Finding:** No prior Operating responsibility is purely enterprise-specific at the abstract level. What is enterprise-specific is the **realization mechanism and required rigor**.

---

# 4. Minimum Personal Operating Architecture — profile, not new layer model

Do not create a new architecture hierarchy. For a one-Human-plus-AI context, the retained Operating Architecture can project to a minimal profile:

```text
Persistent Purpose / Value Constraints

Capability & Role Bindings
  Human / AI / tools / workflows
  who can do what; who owns what

Authoritative State & Knowledge
  what persists; where truth lives; what is reusable

Reusable Patterns & Context Routing
  only accepted recurring mechanisms

Authority / Risk / Recovery
  decision/action rights; sensitive state; rollback

Performance / Economics / Learning
  quality + attention/time/cost + observed outcomes
  retain / change / retire
```

This is a **profile/projection** of Operating Architecture, not a sixth architecture or a mandatory user-visible dashboard.

At organizational scale the same responsibilities may expand into teams, governance structures, portfolios, service management, capability owners, platform teams, enterprise state domains and formal control systems.

---

# 5. Role model for scale invariance

The strongest transfer mechanism is to separate `role/responsibility` from `actor`.

Candidate abstract contract:

```yaml
role:
  purpose:
  responsibilities:
  required_capability:
  decision_rights:
  action_authority:
  accountability_or_acceptance:
  interfaces:
  lifecycle_owner:

actor_binding:
  actor_type: human | ai | tool | workflow | team | external
  actor_identity:
  verified_capability:
  access:
  granted_authority:
  current_constraints:
```

Examples:

```text
Decision Owner = Human
Research Producer = AI
Evidence Retriever = app/tool
Artifact Producer = AI or Human+AI
Technical Verifier = deterministic tool
Recipient Acceptance = Human/external stakeholder
System Maintainer = same Human at personal scale / dedicated owner at larger scale
```

A person may bind multiple roles; scaling changes bindings, not the conceptual ownership questions.

---

# 6. Economic architecture at personal scale

Personal Human–AI work is economic action even without market exchange inside the system.

Scarce resources include:

- Human time;
- attention;
- energy;
- model/tool cost;
- latency;
- context-reconstruction cost;
- maintenance;
- switching cost;
- opportunity cost across initiatives;
- risk/downside;
- future capability/learning.

Therefore `economics` should remain a cross-cutting architecture concern, not an enterprise-only addition.

Key rule:

> A design is not superior because it automates more. It is superior only when the expected increase in whole-system value exceeds added coordination, verification, maintenance, lock-in, cognitive and failure costs.

---

# 7. Δ2 — Boundary comparison against qualified priors

## Prior A — human-ai-work-architecture v1.0

Already used a broad personal Human–AI Work System SoI including Human worker, behavioral kernel, context/state, memory, models, research/tools, orchestration, assurance, execution, closure and learning; external actors/sources/outcomes remained external reality.

**Strength:** clear work-system boundary and personal scope.

## Prior B — AI-native-Operating-Model

Uses a broader responsibility architecture covering Strategy, Operating, Work, Execution and Learning and optimizes the whole work system.

**Strength:** persistent organizational/operating responsibilities and explicit Work↔Operating separation.

## Current candidate — permanent nested SoI-P / SoI-E

Would separately name a performance SoI and an engineered support SoI.

**Possible benefit:** precise claim/engineering scope.

**Cost:** new permanent terminology and boundary objects which may duplicate normal systems-engineering decomposition into parent system + system elements/subsystems.

---

# 8. Δ2 decision

## Prefer claim-relative boundary selection over mandatory dual-SoI taxonomy

Architecture principle:

> **Select the focal System of Interest relative to the claim and decision. Default to the Human–AI Work System for work/outcome claims; focus a nested engineered system element only when technical ownership, security, V&V, runtime or lifecycle requires it. Widen to organization/portfolio/institution only when that scale changes the mechanism.**

This yields:

```text
Work/outcome claim
→ Human–AI Work System is focal SoI

runtime/security claim
→ relevant engineered subsystem is focal entity for that analysis
  + parent Work System interfaces preserved

organizational operating claim
→ persistent Operating Architecture / organization becomes focal scope where material
```

No global requirement to maintain identifiers `SoI-P` / `SoI-E`.

### Reopen trigger for explicit nested SoI objects

Promote explicit nested SoI types only if real architecture/evaluation work repeatedly shows that ordinary parent/subsystem notation cannot keep responsibility, evidence or lifecycle claims distinct.

---

# 9. Implications for the parent architecture

The strongest current parent candidate remains:

```text
Responsibility architecture
  Strategic
  Operating
  Work
  Execution
  Learning

Cross-cutting concerns/views
  describe state, authority, assurance, economics, etc.

Runtime profiles
  instantiate only the structures needed for the current personal/team/enterprise context
```

Δ1 does **not** justify removing Operating Architecture for personal use.

Instead, it suggests:

```text
Operating Architecture = scale-invariant responsibility class
Operating Model/Profile = context-specific realization of that class
```

Δ2 does **not** currently justify another structural layer or permanent dual-SoI model.

---

# 10. Architecture principles added by this review

This review directly supports:

- AP2 role/responsibility before actor;
- AP3 scale-invariant semantics / scale-conditional structures;
- AP4 persistent Operating vs episodic Work;
- AP5 economics as architecture input;
- AP6 architecture type correctness;
- AP10 actor substitution/extensibility/portability.

See `ARCHITECTURE-PRINCIPLES-v0.1.md`.

---

# 11. Current disposition

| Delta | Result | Confidence |
|---|---|---:|
| Δ1 Operating Architecture personal/general transfer | **RETAIN + GENERALIZE + PROFILE** | high |
| Δ2 permanent nested SoI-P/SoI-E taxonomy | **DO NOT PROMOTE** | medium-high |
| Claim-relative boundary selection | **PROMOTE AS ARCHITECTURE PRINCIPLE** | high |

Remaining architecture deltas now move to:

1. Δ3 — views vs control-plane compression;
2. Δ4 — incremental value of adaptive Work-Control / Semantic Compiler;
3. Δ5 — architecture→runtime semantic compilation under salience/context constraints;
4. Δ6 — Knowledge Capital ownership/promotion.
