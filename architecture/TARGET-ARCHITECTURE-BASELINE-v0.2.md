# Target Architecture Baseline v0.2

**Status:** PROPOSED CONCEPTUAL BASELINE — becomes controlling only if the containing PR is accepted and merged  
**Date:** 2026-08-19  
**Requirements baseline:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`  
**Claim boundary:** conceptual Human–AI Work System architecture only; runtime/operating realization and behavioral effectiveness remain separate.

## 1. Baseline claim

The smallest currently supported conceptual architecture consists of three structural commitments:

```text
A. DISTINCT RESPONSIBILITIES
   Strategic / Operating / Work / Execution / Learning-Change

B. DISTRIBUTED TYPED STATE
   authoritative state remains with legitimate owners/stores;
   working context is composed as needed

C. ADAPTIVE WORK-SELECTION CONTRACT
   for admitted/triggered work, select the minimum justified next work
   from current reality, intended outcome/claim, requirements, preserved state,
   dependencies, capability/authority/runtime reality, consequence, uncertainty
   and economics
```

These commitments are orthogonal:
- Responsibilities define durable ownership/decision domains.
- Typed State preserves semantic/authority continuity.
- Adaptive Work Selection controls what justified work happens next.

They do not imply a runtime pipeline, a fixed lifecycle, a central state store or a Semantic Compiler subsystem.

---

# 2. Scope and boundary

This baseline is intended for a general Human–AI Work System whose responsibilities may be co-located in one Human or distributed across Humans, AI, tools, teams and external actors.

Use claim-relative boundary selection. The architecture does not require a permanent `SoI-P / SoI-E` taxonomy or a fixed scale ontology.

The baseline covers:
- purpose-directed professional and general work;
- materially relevant persistent operating context;
- actual runtime/implementation conditions where they change a claim;
- transition/use/outcome boundaries where production and real-world success can diverge.

It is not a universal enterprise architecture, organization chart, product architecture or platform specification.

---

# 3. Responsibility distinctions

## 3.1 Strategic Responsibility
Owns legitimate purpose/outcome direction, priorities, major trade-offs, strategic constraints and material commitments across competing possibilities.

Local work may provide evidence that challenges strategy; it does not silently acquire strategic authority.

## 3.2 Operating Responsibility
Owns persistent capability and coordination arrangements that must remain usable across work episodes, including persistent roles/ownership, processes/patterns, authoritative operational state, shared infrastructure, capacity/economics, governance and lifecycle of persistent mechanisms.

Repeated work does not automatically become authoritative Operating state; institutionalization requires legitimate ownership/acceptance.

## 3.3 Work Responsibility
Owns transformation of a real need/problem/outcome into intended-use-sufficient work, including qualification, professional method/reference, composition, execution/integration coordination, refinement, assurance and transition/use work where material.

## 3.4 Execution Responsibility
Owns the concrete act of running tools/models/workflows/actions, actual state reads/writes, permissions, returned runtime state, retries/recovery and technical observability.

Conceptual capability does not establish actual execution capability.

## 3.5 Learning / Change Responsibility
Owns observing evidence/outcomes, diagnosing deviations, identifying change implications, routing change proposals and evaluating effects.

It does **not** automatically own mutation authority over Strategy, Operating state, Work methods or Runtime; the affected legitimate owner retains the decision/write authority.

### Responsibility ≠ Actor
A single Human may occupy all five responsibilities; larger systems may distribute them. The architecture requires responsibility clarity, not organizational ceremony.

---

# 4. Distributed Typed State

There is no required universal DWM store or mandatory central state object.

Material state remains authoritative where legitimate domain ownership and reality place it. Current work composes only the working context required for safe progress.

Where material, state must preserve enough of:

```text
semantic type
scope
provenance
freshness / version
authority / owner
write path
status
conflict / supersession
```

Relevant semantic distinctions include, as needed:

```text
fact / observation
inference / assumption / forecast / scenario
requirement
proposal / recommendation / decision
acceptance / authorization
execution result
readiness claim
outcome observation
reusable knowledge
```

Core non-equivalence:

```text
working/context state
≠ authoritative operational state
≠ reusable knowledge
```

A coherent Dynamic Work Model may be used as a conditional derived work-state projection when complexity makes integration valuable. It is not required for ordinary bounded work and is not automatically authoritative.

Shared-state legibility is required when Human/actor judgment, reliance, acceptance, coordination, authority or next action depends on a material state change.

---

# 5. Adaptive Work-Selection Contract

The Work-Selection Contract applies to **admitted or triggered work**. It does not own Strategy, persistent Operating management or legitimate Change authority.

## 5.1 Inputs
Use only as far as material:

- intended outcome / next legitimate claim or transition;
- relevant scope;
- current authoritative/observed reality;
- already-qualified/preserved state;
- requirements / professional performance needs;
- blockers / dependencies;
- available/effective capability;
- access / authority / Human contribution;
- actual runtime conditions;
- consequence / reversibility / risk;
- uncertainty / relevant horizon;
- resource, coordination, delay and opportunity cost.

## 5.2 Decision
Select the **minimum justified next work** capable of materially improving the next legitimate state/claim without unnecessary reopening or ceremony.

Possible outputs include:
- direct answer/work;
- retrieval/research/measurement;
- professional/reference resolution;
- decomposition or dependency representation;
- Human contribution/Gate;
- tool/action execution;
- product refinement;
- assurance/validation;
- transition/use work;
- wait/stage/reversible action;
- stop/no-action/external handoff.

## 5.3 Preservation and transition integrity
Already-qualified work is preserved unless new evidence or dependency impact materially reopens it.

`Minimum work` must not become `stage/dependency collapse`: downstream transformation may begin only when materially required upstream state/Work Products are sufficiently ready for that transition.

An internal readiness condition is not automatically a Human Gate.

## 5.4 Evidence-qualified reuse
Before reusing prior work, patterns, decisions, methods or knowledge, appraise enough provenance, scope, freshness, evidence, applicability and transferability for the current claim. Prior acceptance or similarity alone is insufficient.

## 5.5 Uncertainty and commitment
Future/uncertainty work activates only when it can materially change route, feasibility, downside, realization or option value. Learn what is worth learning, preserve robustness/flexibility only when valuable, and commit when additional information/delay/optionality no longer justifies its cost.

---

# 6. Cross-cutting invariants

The following are **invariant groupings, not additional architecture objects or runtime modules**.

## 6.1 Reality & State Integrity
Do not silently promote inference to fact, stale state to current, working copies to authority, retrieved content to legitimate rule, assumptions to forecasts, attempts to completion, or local observations to shared truth.

## 6.2 Capability, Authority & Agency Integrity
Keep capability, access, effective performance, legitimate authority, acceptance and accountability distinct. Human Gates arise from real non-substitutable contribution/authority, not ceremony.

## 6.3 Professional Quality & Claim Integrity
Making work professionally good is distinct from proving a claim about its quality/readiness. Assurance must match the exact claim and possess credible detection capability for its material failure modes. Where correlated/self-confirming error is material, increase genuine independence enough to improve detection.

## 6.4 Value, Realization & Change Integrity
Production, transition, use, outcome, causal effect and value remain distinct. New evidence triggers bounded repair/change through legitimate owners, not automatic global mutation. Additional structure/process must earn net value.

These groupings may be described differently in future architecture descriptions if the same semantics remain intact.

---

# 7. Conditional mechanisms

Conditional Requirements in the requirements baseline activate behavior only when their trigger is material:

- open framing/search integrity;
- persistent/divergent state handling;
- consequential risk/control;
- recipient/use-dependent maturity/refinement;
- material future uncertainty/commitment design;
- competing initiatives/resource coherence;
- Human capability formation/preservation.

They are not mandatory lifecycle stages, modules, stores or artifacts.

A Work Graph is one valid conditional representation for dependency-rich work, not a universal Work structure.

B.6 (`QUALIFY → DESIGN/COMPOSE → EXECUTE+INTEGRATE → TRANSITION* → CLOSE`) may be used as a human-readable Professional Work projection. It is not the authoritative state model or mandatory stage machine.

PAOS-like surface routing may be used as a concrete minimal Personal-AI operating profile. It is not universal system architecture.

The existing eight-view architecture may be used as an architecture-description scheme where useful. Views are not system components.

---

# 8. Runtime / implementation boundary

Architecture acceptance does not imply runtime installation or behavior.

For every material runtime claim, establish enough actual execution context such as:
- effective instructions/policies and precedence where knowable;
- accessible state/context;
- actual model/runtime;
- available tools/capability providers and bindings;
- permissions/identity/action path;
- material versions/configuration;
- evaluator evidence-access context where different from subject execution.

Concrete runtime realization may be simpler than this architecture, but it must preserve every material requirement/semantic relevant to its claim. **Unowned material semantic loss is prohibited.**

The baseline does not require a Runtime Adapter object, V8 view, instruction format, Skill topology, agent topology or state technology.

---

# 9. Requirements trace

| Requirement | Primary owner/mechanism |
|---|---|
| CR-01 Outcome before means | Strategic/Work Responsibility + Work Selection |
| CR-02 Claim-relative scope | Responsibility boundary + Typed State |
| CR-03 Reality integrity | Typed State + Reality invariant |
| CR-04 Current state before change | Work Selection + Typed State |
| CR-05 Professional sufficiency / reuse | Work Responsibility + local professional method + qualified reuse |
| CR-06 Comparative composition | Work Selection + capability semantics |
| CR-07 Human agency / legibility | Authority/Agency invariant + shared-state legibility |
| CR-08 Capability/access/authority | Capability/Authority invariant + runtime reality |
| CR-09 State/knowledge integrity | Distributed Typed State |
| CR-10 Minimum sufficient work | Adaptive Work Selection + transition integrity |
| CR-11 Claim-matched assurance | Professional Quality & Claim Integrity |
| CR-12 Realization/outcome integrity | Work/Operating/Learning boundaries + Realization invariant |
| CR-13 Runtime/implementation fidelity | Runtime boundary + semantic-preservation rule |

All seven Conditional Requirements are owned by their corresponding conditional behaviors; none requires a permanent architecture object.

---

# 10. Explicit non-claims

Acceptance of this conceptual baseline does **not** claim:

- behavioral superiority or Human–AI synergy;
- runtime installation, conformance or deployment;
- that five Responsibilities must be implemented as five layers/subsystems;
- that one DWM, Work Graph, lifecycle, B.6 projection or Semantic Compiler object is universally required;
- that the four invariant groupings are four architecture modules;
- that the seven Conditional Requirements are seven components;
- that the eight predecessor Views are final/mandatory;
- that PAOS surfaces are universal;
- that any particular model/tool/agent/workflow is effective;
- that architecture acceptance establishes outcome/value;
- that this is a universal enterprise/organization architecture.

---

# 11. Reopen conditions

Reopen this baseline only for a named material trigger:

1. changed intended claim / System-of-Interest scope;
2. new external evidence materially contradicts a baseline assumption or requirement;
3. repeated or consequential real-use failure cannot be represented/prevented/repaired cleanly by the current semantics;
4. a materially simpler rival satisfies the same requirements with lower conceptual/runtime/coordination/maintenance/evaluation burden;
5. implementation/runtime reality shows a required semantic cannot be realized or preserved within intended contexts;
6. audit reveals an unowned requirement, semantic regression or hidden mandatory structure;
7. two accepted responsibilities/contracts create a material ownership or authority contradiction;
8. new legitimate concern/requirement is established by reference + real-use evidence.

Without a trigger, prefer local method/runtime repair over foundational architecture expansion.

---

# 12. Architecture-description and realization boundary

This file is the proposed **conceptual architecture baseline**, not the complete architecture description for every stakeholder and not an implementation specification.

After acceptance, the next program is a separate `Architecture → Runtime / Operating Realization` problem: determine how the baseline's material semantics are allocated to actual Humans, AI, tools, state stores, instructions, Skills/workflows, projects/contexts and operating mechanisms without copying the whole architecture or losing required semantics.

That realization work is not authorized or decided by this baseline file.
