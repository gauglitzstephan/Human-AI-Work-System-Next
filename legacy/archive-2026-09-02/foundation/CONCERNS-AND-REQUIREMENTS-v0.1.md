# Concerns & Requirements Baseline v0.1

**Status:** PROPOSED CONCEPTUAL BASELINE — becomes controlling only if the containing PR is accepted and merged  
**Date:** 2026-08-19  
**Scope:** solution-neutral architecture drivers for a general Human–AI Work System and its materially relevant operating/runtime context  
**Derivation basis:** Reference Map v0.3 + Q1–Q8 synthesis/tie-out + Qualified Prior / real-use evidence + Requirements Quality Audit

## 1. Purpose and boundary

This document is the normative problem/requirement baseline for subsequent architecture evaluation and realization work.

It deliberately does **not** prescribe:

- architecture layers or views;
- a Work Object, Dynamic Work Model, Work Graph, lifecycle or Semantic Compiler object;
- a PAOS surface topology;
- a fixed Human-in-the-loop pattern;
- a runtime, agent, Skill, Project, store or deployment topology.

The governing distinction is:

```text
reference construct ≠ requirement
requirement ≠ architecture mechanism
architecture mechanism ≠ runtime implementation
```

Requirements below are solution-neutral. A concrete architecture may satisfy them through different mechanisms if semantics, evidence, authority, quality and proportionality are preserved.

---

# 2. Concerns

## C1 — Purpose, Outcome & Legitimacy
What should improve, for whom, who is affected, which values/rights/constraints matter, and what actually counts as success?

## C2 — Scope, Boundary & Scale
For the current claim, decision or action, what is the relevant system boundary and scale? Which semantics transfer across scales and which do not?

## C3 — Reality, Evidence & Uncertainty
What is observed, inferred, assumed, contested, forecast, unknown or stale? What evidence supports the current model and what could change it?

## C4 — Professional Performance & Judgment
What does professionally sufficient work look like in this task/context? Which method, expertise, reference, craft, tacit judgment, exemplar or recipient/use criterion matters?

## C5 — Human–AI Joint Performance, Capability & Agency
Which functions are best performed by Humans, AI, combinations, tools, experts, validated workflows or existing processes? What legitimate Human judgment/agency must remain effective?

## C6 — State, Knowledge & Continuity
What is working context, authoritative operational state and reusable knowledge? How are provenance, freshness, identity, ownership, conflict, persistence and continuity preserved?

## C7 — Authority, Rights, Risk & Recoverability
Who may decide, accept, authorize, write, execute, override, stop or bear residual risk? What safety, security, privacy, rights or recoverability constraints apply?

## C8 — Work Admission, Coordination & Economy
Which work deserves attention now? How much search, decomposition, coordination, Human attention, tooling, assurance, persistence, delay and maintenance cost is justified?

## C9 — Quality, Assurance & Readiness
What exact quality/readiness claim is being made, what properties are non-compensatory for that claim, and what evidence/test/review can actually detect material failure?

## C10 — Transition, Use, Outcome, Value & Learning
What must happen after production for use, adoption, mechanism, outcome and value to occur? What can be learned from real use and how may that learning legitimately change the system?

## C11 — Runtime & Implementation Fidelity
Which properties depend on the actual model, instructions, state/context access, permissions, tools, versions, surfaces or technical realization? How is architecture semantics preserved through implementation?

---

# 3. Core Requirements

Core Requirements are universal **semantic obligations**. Their visible/process realization may collapse almost entirely for simple bounded work.

## CR-01 — Outcome before means
The system shall distinguish, as far as materially necessary, raw input or proposed means from the underlying need/purpose, intended outcome, relevant constraints and success condition before consequential commitment.

It shall not treat wording of a request or an initially proposed solution as an automatically complete specification.

## CR-02 — Claim-relative scope
For a material claim, decision, action or evaluation, the system shall determine the relevant scope/boundary/scale sufficiently to avoid invalid transfer of state, evidence, capability, authority or outcomes across materially different contexts.

No fixed universal SoI or scale taxonomy is required.

## CR-03 — Reality and epistemic integrity
Material work shall remain grounded in the best available current reality and preserve distinctions, where decision-relevant, among observation/fact, inference, assumption/hypothesis, judgment, forecast/scenario, conflict and unknown.

Provenance, scope, freshness and material uncertainty shall not be silently discarded. Internal coherence does not override external reality.

## CR-04 — Current state before consequential change
When repairing, redesigning, extending, migrating or replacing an existing material system/process/artifact, the system shall inspect and reconcile enough current authoritative state, existing requirements/decisions and observed failure evidence to avoid redesigning an imagined system, duplicating valid structures or overwriting legitimate constraints.

This requirement is proportional and does not require exhaustive archaeology.

## CR-05 — Intended-use professional sufficiency and evidence-qualified reuse
For material professional work, the system shall establish enough of the applicable professional performance bar for the intended use, including relevant requirements, methods/practices, references/exemplars/anti-patterns, recipient/use context and failure modes.

Existing work, precedent, methods, patterns or knowledge shall be reused only to the extent that provenance, scope, freshness, applicability, evidence and transferability support the current claim. Prior acceptance or superficial similarity alone is insufficient.

Professional quality shall not be reduced to a universal checklist when tacit judgment, craft, expertise or representative use is material.

## CR-06 — Comparative Human–AI composition
Material functions shall be allocated according to the relative effective capability of available Humans, AI, tools, experts, workflows or existing processes in the actual context, subject to legitimate authority and intended-use quality.

The architecture shall not assume Human+AI collaboration, maximum autonomy or maximum Human involvement is inherently optimal. Serious alternative execution forms shall not be excluded solely by default ideology.

## CR-07 — Human agency, legitimate contribution and shared-state legibility
The system shall preserve effective Human involvement where Human values/judgment, non-substitutable information/expertise, acceptance or legitimate authority materially determine the work.

Human involvement shall not be added ceremonially when it does not improve quality, legitimacy, learning or risk.

Material changes to purpose, requirements, decisions, authority, capability limits, readiness or required next action shall become sufficiently legible to the responsible Human/actor when their judgment, reliance, acceptance, coordination or action depends on them.

## CR-08 — Capability, access and authority integrity
The system shall preserve distinctions among capability existence, actual access/binding, effective capability in the current context, legitimate authority, acceptance/accountability and verified performance where material.

Likewise, proposal/recommendation, decision, acceptance, authorization, execution, completion and outcome shall not be silently conflated.

## CR-09 — State and knowledge integrity
The system shall distinguish, where material:

```text
working/context state
≠ authoritative operational state
≠ reusable knowledge
```

Persistence, repetition, retrieval or model confidence shall not automatically promote one class into another.

For persistent state, authority and ownership remain with the legitimate domain/store; working representations are derived/composed as needed.

## CR-10 — Minimum sufficient work, preservation and transition integrity
The system shall activate additional research, decomposition, Human interaction, tooling, assurance, persistence, coordination or monitoring only when expected incremental value for the relevant outcome/claim/risk justifies its burden subject to binding requirements and quality floors.

New evidence or a local defect shall not unnecessarily invalidate unaffected qualified work; rework/reopening shall be bounded to the materially affected scope where safe.

`Minimum sufficient work` shall not permit material stage/dependency collapse: when a downstream transformation depends on a materially required upstream state or Work Product, that prerequisite must be sufficiently ready for that transition. An internal readiness condition is not automatically a Human Gate.

## CR-11 — Claim-matched, detection-capable assurance
A quality/correctness/readiness claim shall not exceed evidence capable of establishing that exact claim in its relevant scope, object/state/version/environment.

Assurance shall be capable of detecting material failure modes of the claim, not merely demonstrate that a procedure/checklist was executed. Where correlated or self-confirming error is material, sufficient methodological, evidential, perspective or real-world independence shall be introduced to improve detection capability.

If suitable evidence is unavailable, the claim shall remain weaker, FAIL or UNVERIFIED rather than being inferred from narrower upstream checks.

## CR-12 — Realization and outcome integrity
Where success depends on real-world transition/use beyond production, the system shall preserve enough of the chain:

```text
Work Product
→ receiving context
→ transition
→ use / adoption / action
→ mechanism
→ outcome
→ benefit / value
```

Production, technical completion, transition, use, observed outcome, causal effect and realized value shall remain distinct. Causal or value claims require evidence appropriate to those claims.

## CR-13 — Runtime and implementation fidelity / semantic preservation
Where actual runtime configuration can materially change behavior, state, capability, authority or evaluation, the system shall establish enough of the real execution conditions for the current claim/action/evaluation and shall not infer transfer across contexts without evidence.

Concrete implementation, compression, delegation or runtime composition shall preserve all material requirements/architecture semantics relevant to its claim. Simplification is permitted; **unowned material semantic loss is not**.

Implementation must make materially unsupported/inherited/delegated semantics sufficiently identifiable for conformance and debugging without requiring duplication of the full architecture in every runtime.

---

# 4. Conditional Requirements

Conditional Requirements activate only when their trigger is materially present. They are not mandatory lifecycle stages, modules or artifacts.

## CCR-01 — Open framing / search integrity
When problem framing, solution class or route is materially open, the system shall consider enough alternative frames, materially different mechanisms, counterhypotheses/counterevidence and credible simpler/no-action options to avoid premature route collapse.

More alternatives are not automatically better; stop when additional search no longer changes the decision frontier enough to justify its cost.

## CCR-02 — Persistent or divergent state
When material state can diverge across time, Humans, agents, surfaces, systems or reporting views, the system shall establish enough authoritative source/owner, write path, freshness/version and conflict/reconciliation semantics for safe operation.

No state architecture bureaucracy is required for bounded work where divergence is immaterial.

## CCR-03 — Consequential risk / control
When work can create material safety, security, privacy, rights, irreversible or otherwise hard-to-recover consequences, the system shall apply proportionate legitimate authority, necessary protection, minimal justified exposure/privilege and suitable containment/recovery/rollback capabilities.

## CCR-04 — Recipient/use-dependent maturity
When a plausible/technically complete Work Product can still differ materially from what the next recipient/use context needs, the system shall identify and perform the highest-value product refinement needed to reach the supported next-use maturity before claiming readiness.

Additional QA does not substitute for missing product transformation.

## CCR-05 — Material future uncertainty / commitment
When plausible future/external change can materially alter route, feasibility, downside, realization or option value, the system shall distinguish uncertainty worth reducing now from uncertainty better handled through robustness, staged/reversible action or explicit contingent adaptation.

It shall not convert scenario plausibility into forecast probability or preserve optionality regardless of its cost.

## CCR-06 — Competing initiatives / strategic resources
When multiple material initiatives compete for scarce resources, attention or capability, local work shall be evaluated sufficiently against higher-level purpose/priority, dependencies, capacity/WIP, opportunity cost and scale/pause/stop choices.

Local work-control logic shall not silently own strategic/portfolio authority.

## CCR-07 — Human capability formation / preservation
When Human learning, expertise, authorship, judgment or future recovery/autonomy is itself part of the intended outcome or a material delegation risk, the system shall consider the effect of Human–AI allocation on that capability over the relevant horizon.

This is conditional; it does not justify ceremonial Human work by default.

---

# 5. Negative requirements / non-equivalences

The baseline explicitly rejects these inference shortcuts:

```text
user request ≠ complete specification
Human + AI ≠ automatically optimal team
more process ≠ more quality
more research ≠ better decision
more Human gates ≠ more agency
stored information ≠ authoritative truth
tool/capability exists ≠ usable/authorized capability
QA passed ≠ professionally good
artifact completed ≠ recipient/use-ready
delivery ≠ outcome
outcome observed ≠ causal effect
repetition ≠ validated reusable capability
local correction ≠ global/shared rule
implementation simplicity ≠ permission for semantic loss
minimum work ≠ dependency/stage collapse
new room/agent ≠ independent assurance
```

---

# 6. Requirement activation principle

The system is semantically rich but should be operationally sparse.

A requirement becomes explicit only as far as needed to change route, quality, authority, risk, state continuity, assurance, transition, outcome, learning or net value.

For simple bounded work, the practical path may collapse to:

```text
input
→ understand sufficiently
→ do work
→ appropriate check
→ answer / close
```

The existence of a requirement in this baseline is not authorization to create a visible workflow, artifact, gate, room, agent, schema or persistent state.

---

# 7. Baseline quality status

The Requirements Quality Audit found the set acceptable after bounded repairs for:

- duplicate/persistence placement;
- runtime/implementation fidelity;
- conditional Human capability preservation;
- solution-neutral comparative allocation;
- open-search integrity;
- broader consequential-risk trigger.

The subsequent Target Architecture and adversarial regression audits found no remaining unowned requirement after adding explicit evidence-qualified reuse, semantic-preservation, detection-capable assurance, shared-state legibility and material transition-integrity semantics.

Acceptance of this file as a baseline means only that it is a sufficiently complete and solution-neutral architecture-driver set for the current scope. It does not prove architectural optimality, runtime effectiveness or behavioral alpha.
