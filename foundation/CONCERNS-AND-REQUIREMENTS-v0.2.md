# Concerns & Requirements Baseline v0.2

**Status:** CONTROLLING — promoted via authorized PR #18 merge `b355ed63ad94d6456a6913cac079458238067921` and post-merge readback  
**Date:** 2026-08-24  
**Scope:** solution-neutral requirements for a general Human–AI Work System and its materially relevant operating/runtime context  
**Supersession:** supersedes `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` as the controlling Requirements baseline; v0.1 remains immutable historical Qualified Prior evidence  
**Derivation basis:** Requirements v0.1 + accepted System of Interest and Target Architecture + qualified predecessor lineage + real-use/runtime evidence + bounded normalization and adversarial de-bias review

## 1. Purpose and boundary

This document defines what the Human–AI Work System must preserve or achieve. It does not prescribe a specific architecture, lifecycle, controller, agent topology, Skill, Project, state store, provider, product surface, artifact set or Runtime implementation.

The governing distinctions are:

```text
concern / requirement
≠ architecture mechanism
≠ Runtime implementation
≠ visible workflow
```

The baseline is semantically rich and operationally sparse.

---

# 2. Interpretation rules

## IR-01 — Semantically rich, operationally sparse

All Requirements apply semantically. A Requirement shall become explicit only when its activation can materially change the current work.

```text
requirement exists
≠ explicit Runtime step required
≠ artifact required
≠ Human interaction required
≠ agent required
```

## IR-02 — Materiality is claim-relative

A concern is material when neglecting it could plausibly change the next relevant:

- claim;
- route;
- professional Performance Floor;
- Authority/Risk state;
- Continuity state;
- transition;
- outcome; or
- Whole-System Economics.

Where no such plausible dependency exists, the concern may remain implicit. The system is not required to prove the irrelevance of every other Requirement.

## IR-03 — Sufficiency means next-claim sufficiency

`Sufficient` means enough to support the next intended claim, decision, action or transition. It does not mean exhaustive, perfect or final.

Where sufficiency for a material claim is not adequately supported, it shall not be assumed. The claim remains weaker, pending or `UNVERIFIED`.

## IR-04 — Non-compensatory floors before economy

Professional Performance, Reality Integrity, materially necessary Authority/Risk, Continuity and claim-matched Assurance floors shall not be compensated for by lower time, Human-attention, coordination or compute cost.

Economy is optimized only among routes that meet the relevant eligibility floors.

## IR-05 — Local contribution does not redefine wider state

Completion of local work, a Child Result, Tool Output, Agent Result or artifact shall not by itself redefine or strengthen the wider controlling:

- scope;
- outcome;
- state;
- Authority;
- Acceptance;
- Completion claim; or
- Promotion status.

A local contribution may support a wider claim only after legitimate integration and qualification at the wider scope. This Requirement does not prescribe a specific Parent/Rebind/Control-Return mechanism.

---

# 3. Core Requirements

## CR-01 — Outcome before means

For material work, the system shall distinguish sufficiently among:

```text
input / proposed means
≠ underlying need / purpose
≠ intended outcome
≠ constraints
≠ success condition
```

A request or initially proposed solution shall not be treated automatically as a complete specification.

## CR-02 — Claim-relative scope and contribution integrity

For material claims, decisions and actions, the system shall determine the relevant scope sufficiently to prevent invalid transfer of state, evidence, capability, Authority or outcomes across materially different boundaries.

The currently visible Chat, Skill, Agent, folder, Tool Output or Work Product shall not become the controlling system merely because it is the current focus.

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

Before materially repairing, redesigning, migrating, extending or replacing an existing system, process or artifact, the system shall reconstruct enough actual state to avoid changing an imagined system.

Where relevant this includes:

- authoritative Requirements;
- decisions;
- actual artifacts and workflows;
- interfaces;
- observed failures; and
- relevant outcomes.

This Requirement is proportional and does not mandate exhaustive archaeology that cannot change the next claim or route.

## CR-05 — Intended-use professional sufficiency and qualified reuse

Material professional work shall meet the applicable Performance Floor for its concrete Intended Use.

Where material, this includes:

- Domain or Professional Method;
- standards and practices;
- References and Exemplars;
- Anti-Patterns;
- Craft;
- evidence Requirements;
- Recipient/Use Context; and
- relevant Failure Modes.

Capability or general model intelligence does not substitute for this basis.

Existing methods, patterns, decisions, artifacts or knowledge shall be reused only to the extent that provenance, freshness, fit, evidence and transferability support the current claim.

Professional quality shall not be reduced to a universal checklist where expertise, craft, tacit judgment or representative use is material.

## CR-06 — Comparative work composition

Required work shall first be understood by function, method and Performance need and then allocated according to actual capability, Authority, Whole-System Economics and context.

Serious alternatives may include:

```text
Human
AI
Human + AI
existing native capability
deterministic tool
workflow / Skill
specialist
one or several agents
existing process
no action
```

No form is inherently optimal. Decomposition, parallelization, additional Agents or additional coordination shall be used only where they provide relevant expected Performance, assurance, isolation or Economics benefit.

## CR-07 — Human agency, attention and legitimate contribution

The system shall preserve effective Human contribution where Human-specific:

- values or judgment;
- inaccessible or lived context;
- expertise;
- authorship;
- learning;
- Acceptance;
- responsibility;
- Authority; or
- Commitment

materially determine the work.

Human Attention, interruption, review, correction, re-grounding and coordination are scarce Work-System resources.

AI- or Tool-resolvable work shall not be transferred unnecessarily to the Human. `AI-resolvable first` is not a rule to maximize autonomy: Human involvement is legitimate where its comparative value is higher.

The system shall remain sufficiently correctable, stoppable and legible for responsible Human reliance and action.

## CR-08 — Capability, status and authority integrity

Where material, the system shall preserve distinctions among:

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

Technical ability does not create legitimate Authority.

## CR-09 — State, knowledge and continuity integrity

Where material, the system shall preserve distinctions among:

```text
working / transient context
≠ authoritative operational state
≠ accepted reusable knowledge
```

Retrieval, Memory, repetition, storage or model confidence shall not promote one state class into another.

Persistent Authority and ownership remain with the legitimate domain owner or store. Working representations are composed or derived as needed.

## CR-10 — Minimum sufficient work and Whole-System Economics

The system shall perform the smallest work that reaches the relevant sufficiency floors.

Additional:

- research;
- context;
- decomposition;
- Human interaction;
- Agents;
- Tools;
- Assurance;
- persistence; or
- monitoring

shall justify their marginal burden for the relevant outcome, claim or risk.

Where decision-relevant, Whole-System Economics includes:

```text
Human attention / energy
interruptions / context switching
correction / rework
review / escalation
AI inference / reasoning
tools / agents
latency / critical path
coordination
persistence / maintenance
evaluation / observability
failure cost
opportunity cost
Human capability effects
realized usefulness / value
```

`Minimum sufficient work` shall not permit omission of a materially required upstream prerequisite.

## CR-11 — Claim-matched professional assurance and evaluation

A claim shall not exceed evidence capable of establishing that exact claim in its relevant:

- scope;
- state or object;
- version;
- Runtime Environment; and
- Intended Use.

Assurance shall be capable of detecting the material Failure Modes of the claim.

```text
self-review
≠ verification
≠ independent challenge
≠ Domain/Professional Validation
≠ Recipient/Use Validation
≠ outcome evidence
```

Additional independence is required only where correlated or self-confirming error is material for the claim.

Generic quality scores, token counts, Agent counts or process conformity do not substitute for Domain-, claim- and use-relative Professional Evaluation.

## CR-12 — Transition, use and outcome integrity

Where success depends on more than production, the system shall preserve enough of the chain:

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

Where actual Performance depends materially on:

- model or version;
- reasoning mode;
- Instructions;
- context;
- Tool or connector access;
- permissions;
- surface;
- provider; or
- Runtime composition,

the system shall establish enough of those conditions for the current claim.

```text
architecture says it
≠ Runtime actually does it
```

Provider- or surface-specific facts shall not silently become general Work-System semantics.

Where Continuity, Recovery, substitutability or lock-in are material, relevant state, methods and semantics shall remain sufficiently portable or reconstructable.

Runtime evidence shall be sufficiently diagnosable where a material Performance or failure claim cannot otherwise be resolved. Diagnosability does not mandate universal full-trace logging.

## CR-14 — Evidence-bound learning and controlled change

New evidence shall first change the appropriately scoped qualified Working or Knowledge state.

```text
local failure
≠ global rule
local success
≠ reusable capability
repetition
≠ validation
```

A reusable capability, Requirement, Operating rule or Runtime rule shall acquire stronger status only through sufficient evidence and transferability plus legitimate Change Authority.

Repair shall begin at the lowest responsible layer and reopen only dependent state unless evidence establishes a broader gap.

---

# 4. Conditional Requirements

Conditional Requirements activate only when their trigger is materially present. They are not mandatory stages, modules, artifacts or gates.

## CCR-01 — Open framing and exploration integrity

When the problem frame, solution class or route is materially open, the system shall explore enough:

- alternative frames;
- mechanism-distinct routes;
- counterhypotheses or counterevidence; and
- credible simpler or no-action alternatives

to avoid premature route collapse.

Professional exploration shall have, only as far as required:

```text
purpose / Work Mission
search space
search strategy
evidence / Reference basis
expected output
stop / transition condition
```

More exploration is not automatically better.

## CCR-02 — Persistent or divergent state

When relevant state can diverge across time, Humans, Agents, surfaces or systems and that divergence can affect future work, the system shall establish enough:

- authoritative source and owner;
- write path;
- version or freshness;
- conflict and reconciliation semantics; and
- recovery.

Continuity sufficiency precedes carrier economy. After the Continuity Floor is met, use the shallowest adequate carrier.

No persistence bureaucracy is required for transient work without material divergence risk.

## CCR-03 — Consequential risk and recoverability

When work can create material:

- Safety;
- Security;
- Privacy;
- Rights/Fairness;
- legal or professional consequence;
- irreversibility; or
- difficult-to-recover downside,

the system shall apply proportionate legitimate Authority, protection, justified exposure or privilege, containment and Recovery.

## CCR-04 — Recipient/use-dependent maturity

When a plausible or technically complete Work Product may still differ materially from what its next Recipient or Use Context requires, the system shall perform the necessary Product transformation before claiming the corresponding readiness.

Additional QA does not substitute for missing Product transformation.

## CCR-05 — Future uncertainty, information value and commitment

When future or external uncertainty can materially alter route, feasibility, downside, outcome or Option Value, the system shall distinguish among:

- uncertainty worth reducing now;
- Robustness or Scenario treatment;
- staged or reversible action;
- WAIT; and
- Commitment.

Additional information shall be acquired only when its expected decision value justifies Acquisition, Delay and Coordination Cost.

## CCR-06 — Competing initiatives and strategic resources

When multiple material initiatives compete for scarce resources, local work shall be considered sufficiently against:

- higher purpose;
- priority;
- dependencies;
- capacity or WIP;
- Opportunity Cost; and
- Stop, Pause or Scale alternatives.

Local Work Control does not thereby acquire Strategic Authority.

## CCR-07 — Human capability formation or preservation

When Human learning, expertise, judgment, authorship or future autonomy is itself an intended outcome or a material delegation risk, the Human–AI allocation shall consider its effects over the relevant horizon.

This trigger does not justify ceremonial Human work by default.

---

# 5. Central non-equivalences

The baseline rejects these inference shortcuts:

```text
user request ≠ complete specification
current focus ≠ controlling system
local completion ≠ wider-work completion
provider result ≠ Acceptance / Promotion
professional method ≠ provider capability
capability ≠ access ≠ Authority
more context ≠ better context
more process ≠ more quality
more research ≠ better decision
more Agents ≠ better orchestration
fewer Agents ≠ automatically better Economics
more Human gates ≠ more Human agency
minimum work ≠ prerequisite omission
stored / retrieved state ≠ Authority
QA passed ≠ professionally good
artifact produced ≠ Use-ready
delivery ≠ outcome
outcome ≠ causal effect
local learning ≠ global rule
```

---

# 6. Baseline claim and non-claims

This file is accepted only as:

> the best currently supported, solution-neutral Requirements Design Basis for the defined Human–AI Work System scope and current evidence horizon.

Acceptance does not establish:

- cross-domain empirical completeness;
- architectural optimality;
- Runtime effectiveness;
- Human–AI synergy;
- a particular provider, product, Skill, Agent or state topology;
- concrete time, token or Agent budgets;
- any Runtime, Skill, Project, UI or external action;
- realization, transition or outcome effectiveness.

---
