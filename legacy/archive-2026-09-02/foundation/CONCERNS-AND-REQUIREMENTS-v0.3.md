# Concerns & Requirements Baseline v0.3

**Status:** ACCEPTED AND PROMOTED — controlling Requirements baseline on authoritative `main` after PR #34 merge/readback  
**Date:** 2026-08-28  
**Scope:** solution-neutral requirements for a general Human–AI Work System and its materially relevant operating/runtime context  
**Authority:** controlling Requirements baseline on authoritative `main`; promoted through ADR-0004 and PR #34  
**Supersession:** supersedes v0.2 only in the controlling Requirements role; v0.2 remains immutable historical Qualified Prior evidence  
**Derivation basis:** controlling Requirements v0.2 + Requirements v0.1 / R01–R30 lineage + accepted System of Interest and Target Architecture v0.2 + Professional Work review and observed Route-B/runtime-development failures + bounded Human–AI interaction gap challenge and qualified HAI/HCI evidence

## 1. Purpose and boundary

This document defines what the Human–AI Work System must preserve or achieve. It does not prescribe a specific architecture, lifecycle, controller, agent topology, Skill, Project, state store, provider, product surface, artifact set or Runtime implementation.

```text
concern / requirement
≠ architecture mechanism
≠ Runtime implementation
≠ visible workflow
```

The baseline is semantically rich and operationally sparse. Its success criterion is professionally useful work and legitimate real-world performance, not process compliance.

---

# 2. Interpretation rules

## IR-01 — Semantically rich, operationally sparse

All Requirements apply semantically. A Requirement becomes explicit only when doing so can materially change the work, claim, decision, action or outcome.

```text
requirement exists
≠ explicit Runtime step required
≠ artifact required
≠ Human interaction required
≠ agent required
```

## IR-02 — Materiality and sufficiency are frontier-relative

A concern is material when neglecting it could plausibly change the next legitimate:

- claim or decision;
- route;
- professional Performance Floor;
- Authority/Risk state;
- Continuity state;
- action or transition;
- outcome; or
- Whole-System Economics.

`Sufficient` means enough to support that next legitimate frontier. It does not mean exhaustive, perfect or final. Where a material sufficiency floor is unsupported, the claim remains weaker, pending or `UNVERIFIED`.

The system is not required to prove the irrelevance of every other Requirement.

## IR-03 — Non-compensatory floors before economy

Professional Performance, Reality Integrity, materially necessary Authority/Risk, Continuity and claim-matched Assurance floors shall not be traded away for lower time, Human attention, coordination or compute cost.

Economy is optimized only among routes that meet the relevant eligibility floors.

---

# 3. Core Requirements

## CR-01 — Outcome before means

For material work, distinguish sufficiently among:

```text
input / proposed means
≠ underlying need / purpose
≠ intended outcome
≠ constraints
≠ success condition
```

A request or initially proposed solution is evidence of intent, not automatically a complete specification.

## CR-02 — Claim-relative scope and contribution integrity

For material claims, decisions and actions, determine the relevant scope sufficiently to prevent invalid transfer of state, evidence, capability, Authority or outcomes across materially different boundaries.

The currently visible Chat, Skill, Agent, file set, Tool Output, artifact or Work Product shall not become the controlling system merely because it is the current focus.

A local contribution may support a wider claim only after legitimate integration and qualification at the wider scope. Local completion does not by itself redefine the wider outcome, state or Completion claim.

## CR-03 — Reality and epistemic integrity

Material work shall remain grounded in the best accessible current reality and preserve, where decision-relevant, distinctions among:

```text
fact / observation
inference
assumption / hypothesis
judgment
forecast / scenario
conflict
unknown
```

Provenance, freshness, scope and material uncertainty shall not be silently discarded. Internal coherence does not override external reality.

## CR-04 — Actual state before consequential change

Before materially repairing, redesigning, migrating, extending or replacing an existing system, process or artifact, reconstruct enough actual state to avoid changing an imagined system.

Where relevant this includes authoritative Requirements, decisions, actual artifacts/workflows, interfaces, observed failures and relevant outcomes.

This Requirement is proportional and does not mandate exhaustive archaeology that cannot change the next claim or route.

## CR-05 — Intended-use professional sufficiency and qualified reuse

Material professional work shall meet the applicable Performance Floor for its concrete Intended Use.

Where material, this includes professional/domain Method, standards/practices, References/Exemplars, Anti-Patterns, Craft, evidence requirements, Recipient/Use Context and relevant Failure Modes.

Capability or general model intelligence does not substitute for an adequate professional basis.

Existing methods, patterns, decisions, artifacts or knowledge shall be reused only to the extent that provenance, freshness, fit, evidence and transferability support the current claim.

Where recipient/use transformation is materially required for intended-use sufficiency, perform that transformation before claiming readiness. Additional QA does not substitute for missing Product transformation.

Where Human-facing interaction materially affects intended-use Performance, the applicable Performance Floor includes sufficient usability and accessibility for the relevant Humans, tasks and use context.

Professional quality shall not be reduced to a universal checklist where expertise, craft, tacit judgment or representative use is material.

## CR-06 — Comparative work composition

Understand required work by function, method and Performance need, then allocate it according to actual capability, Authority, Whole-System Economics and context.

Serious alternatives may include Human, AI, Human+AI, existing native capability, deterministic Tool, workflow/Skill, specialist, one or several agents, existing process or no action.

No form is inherently optimal. Decomposition, parallelization, additional Agents or additional coordination shall be used only where they provide material expected Performance, assurance, isolation or Economics benefit.

## CR-07 — Human agency, attention, capability and legitimate contribution

Preserve effective Human contribution where Human-specific values/judgment, inaccessible or lived context, expertise, authorship, learning, Acceptance, responsibility, Authority or Commitment materially determine the work.

Human Attention, interruption, review, correction, re-grounding and coordination are scarce Work-System resources. AI- or Tool-resolvable work shall not be transferred unnecessarily to the Human.

Where Human learning, retained judgment, authorship or future autonomy is materially affected by the Human–AI allocation, treat that capability effect as part of the intended outcome or constraint over the relevant horizon.

The system shall remain sufficiently correctable, stoppable and legible for responsible Human reliance and action. Where such reliance or action materially depends on it, relevant capability, limits, uncertainty, initiative, status and material effects shall not be hidden or misleading.

Presentation, including anthropomorphic or relational cues, shall not materially misrepresent capability, Authority, accountability or the Human–AI relationship.

## CR-08 — Capability, status and authority integrity

Where material, preserve distinctions among:

```text
capability exists
≠ access exists
≠ effective capability
≠ Authority
≠ accountability / Acceptance
```

and among:

```text
proposal
≠ recommendation
≠ decision
≠ Commitment
≠ Authorization
≠ execution
≠ completion
≠ outcome
```

Technical ability does not create legitimate Authority. A provider, Tool or local result does not by itself create wider Acceptance, Authorization, Completion or Promotion.

## CR-09 — State, knowledge and continuity integrity

Where material, preserve distinctions among:

```text
working / transient context
≠ authoritative operational state
≠ accepted reusable knowledge
```

Retrieval, Memory, repetition, storage or model confidence shall not promote one state class into another.

Persistent Authority and ownership remain with the legitimate domain owner or store. Working representations are composed or derived as needed.

When relevant state can materially diverge across time, Humans, Agents, surfaces or systems, establish enough authoritative source/owner, write path, version/freshness, conflict/reconciliation and recovery semantics for safe continuity. No persistence bureaucracy is required where divergence is immaterial.

## CR-10 — Minimum sufficient work, Whole-System Economics and legitimate closure

Perform the smallest work that reaches the relevant sufficiency floors.

Additional research, context, decomposition, Human interaction, Agents, Tools, Assurance, persistence or monitoring shall justify their marginal burden for the relevant outcome, claim or risk.

Where decision-relevant, Whole-System Economics includes Human attention/energy, interruption/context switching, correction/rework, review/escalation, AI inference/reasoning, tools/agents, latency/critical path, coordination, persistence/maintenance, evaluation/observability, failure cost, opportunity cost, Human capability effects and realized usefulness/value.

`Minimum sufficient work` shall not omit a materially required upstream prerequisite.

Once the requested and supported frontier is professionally sufficient, close, answer, hand off, wait or stop at that boundary. Do not manufacture continuation, new artifacts, new gates or a new frontier merely because additional work is possible.

## CR-11 — Claim-matched professional assurance and evaluation

A claim shall not exceed evidence capable of establishing that exact claim in its relevant scope, object/state, version, Runtime Environment and Intended Use.

Assurance shall be capable of detecting the material Failure Modes of the claim.

```text
self-review
≠ verification
≠ independent challenge
≠ Domain/Professional Validation
≠ Recipient/Use Validation
≠ outcome evidence
```

Additional independence is required only where correlated or self-confirming error is material. Generic quality scores, token counts, Agent counts or process conformity do not substitute for Domain-, claim- and use-relative Professional Evaluation.

## CR-12 — Transition, use and outcome integrity

Where success depends on more than production, preserve enough of the chain:

```text
Work Product
→ receiving context
→ transition
→ use / adoption / action
→ mechanism
→ outcome
→ benefit / value
```

Accordingly:

```text
produced ≠ used
used ≠ effective
outcome observed ≠ causally caused
outcome ≠ realized value
```

## CR-13 — Runtime, provider and implementation fidelity

Where actual Performance depends materially on model/version, reasoning mode, Instructions, context, Tool/connector access, permissions, surface, provider or Runtime composition, establish enough of those actual conditions for the current claim.

```text
architecture says it
≠ Runtime actually does it
```

Provider- or surface-specific facts shall not silently become general Work-System semantics.

Where Continuity, Recovery, substitutability or lock-in are material, relevant state, methods and semantics shall remain sufficiently portable or reconstructable.

Runtime evidence shall be sufficiently diagnosable where a material Performance or failure claim cannot otherwise be resolved. Diagnosability does not mandate universal full-trace logging.

## CR-14 — Evidence-bound learning and controlled change

New evidence first changes the appropriately scoped qualified Working or Knowledge state.

```text
local failure
≠ global rule
local success
≠ reusable capability
repetition
≠ validation
```

A reusable capability, Requirement, Operating rule or Runtime rule acquires stronger status only through sufficient evidence and transferability plus legitimate Change Authority.

Repair begins at the lowest responsible layer and reopens only dependent state unless evidence establishes a broader gap.

Where Human feedback or system adaptation can materially affect future work, preserve enough of its scope, expected effect, timing, persistence, inspectability and correction or reset semantics for responsible reliance and control.

Human feedback does not by itself authorize reusable learning or wider change.

## CR-15 — Work execution and Work-Product fidelity

For admitted work with a sufficient basis, perform the actual transformation required by the intended outcome and produce, repair or integrate the required Work Product to the applicable intended-use Performance Floor.

Planning, Formation, Research, coordination, governance, Assurance or other supporting work shall not substitute for the required Work Product unless that supporting work is itself the intended output.

When the work can legitimately proceed, do the work rather than manufacturing additional process, gates, intermediate artifacts or meta-work.

---

# 4. Conditional Requirements

Conditional Requirements activate only when their trigger is materially present. They are not mandatory stages, modules, artifacts or gates.

## CCR-01 — Open framing and exploration integrity

When the problem frame, solution class or route is materially open, explore enough alternative frames, mechanism-distinct routes, counterhypotheses/counterevidence and credible simpler/no-action alternatives to avoid premature route collapse.

Professional exploration shall have only as far as required: purpose/Work Mission, search space, search strategy, evidence/reference basis, expected output and stop/transition condition.

More exploration is not automatically better.

## CCR-02 — Consequential risk and recoverability

When work can create material Safety, Security, Privacy, Rights/Fairness, legal/professional consequence, irreversibility or difficult-to-recover downside, apply proportionate legitimate Authority, protection, justified exposure/privilege, containment and Recovery.

## CCR-03 — Future uncertainty, information value and commitment

When future or external uncertainty can materially alter route, feasibility, downside, outcome or Option Value, distinguish among uncertainty worth reducing now, Robustness/Scenario treatment, staged or reversible action, WAIT and Commitment.

Acquire additional information only when expected decision value justifies Acquisition, Delay and Coordination Cost.

## CCR-04 — Competing initiatives and strategic resources

When multiple material initiatives compete for scarce resources, consider local work sufficiently against higher purpose, priority, dependencies, capacity/WIP, Opportunity Cost and Stop/Pause/Scale alternatives.

Local Work Control does not thereby acquire Strategic Authority.

## CCR-05 — Human–AI interaction and coordination integrity

When intended Performance materially depends on ongoing, iterative, mixed-initiative or cross-Human, Agent or surface interaction, preserve enough shared interaction state and coordination legibility for responsible progress, reliance, correction and continuation.

Where material, the relevant Human shall be able to determine sufficiently:

- the current intended outcome, relevant scope and next legitimate frontier;
- the qualified status and material unresolved state;
- the active actor or initiative and expected next contribution;
- any blocked decision, Authority or action; and
- the available correction, stop, recovery and re-entry path.

Material initiative, effects and transitions shall be sufficiently observable and predictable for the relevant Human reliance or action.

Where several responsible or materially affected Humans are involved, legitimate disagreement and challenge shall remain possible.

Surface only interaction state that can materially change judgment, reliance, action, Authority or Continuity.

This Requirement does not mandate continuous narration, universal visibility, a dashboard, fixed stage model, new authoritative state object or Human gate.

---

# 5. Central non-equivalences

```text
user request ≠ complete specification
current focus ≠ controlling system
local completion ≠ wider-work completion
provider result ≠ Acceptance / Promotion
professional method ≠ provider capability
capability ≠ access ≠ Authority
supporting/meta work ≠ required Work Product
more context ≠ better context
more process ≠ more quality
more research ≠ better decision
more Agents ≠ better orchestration
more Human gates ≠ more Human agency
minimum work ≠ prerequisite omission
stored / retrieved state ≠ Authority
QA passed ≠ professionally good
artifact produced ≠ Use-ready
delivery ≠ outcome
outcome ≠ causal effect
local learning ≠ global rule
closure ≠ manufactured next frontier
```

---

# 6. Baseline claim and non-claims

This file is accepted and promoted only as:

> the best currently supported, solution-neutral Requirements Design Basis for the defined Human–AI Work System scope and current evidence horizon.

Acceptance does not establish cross-domain empirical completeness, architectural optimality, Runtime effectiveness, Human–AI synergy, any provider/product/Skill/Agent/state topology, concrete resource budgets, any Runtime/UI/external action, or realization/outcome effectiveness.
