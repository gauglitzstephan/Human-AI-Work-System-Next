# Joint Cognitive Work Architecture — Reconciliation Note

**Status:** CANDIDATE architecture reconciliation on `candidate/joint-cognitive-work-architecture-2026-09-06`; not an accepted new Target Architecture, not a runtime change, and not a modification of PR #60 or installed Custom Instructions.  
**Bound repository base:** `main@78ab1b13c8a2bc15802a1d1e2dc5ecf4627113ed`.  
**Purpose:** preserve and sharpen the deeper Human–AI work architecture that became decision-relevant during genuine use, while reconciling it with qualified prior architecture rather than rediscovering or replacing that prior.

## 1. Executive finding

The current work exposed a recurring failure pattern:

> a locally plausible problem or solution object can be optimized before its relation to the higher purpose, relevant problem boundary, dependencies, constraints and critical assumptions is sufficiently qualified.

This is not adequately described as `proposed means ≠ requirement` alone, nor as ordinary reframing. The missing emphasis is **upward and downward traceability of work before substantial local optimization**.

At the same time, the underlying architectural idea is **not new**. Qualified prior architecture in this repository already established that:

- the Human–AI **work system**, not an isolated AI component, is the relevant unit for work-performance claims;
- responsibilities should be distinguished before actor bindings;
- persistent Operating architecture differs from episodic Work architecture;
- work selection must preserve upstream prerequisites, qualified state, dependencies, authority, uncertainty and economics;
- the current focus is not automatically the controlling system;
- local completion does not establish wider-work completion;
- minimum work does not justify prerequisite omission;
- architecture semantics and runtime realization are different objects.

The new contribution of this reconciliation is therefore a **sharper formative description of the work domain and a missing active relation for ordinary Joint Work**:

> **Purpose–Problem–Solution Traceability**, with **Problem-Space Sufficiency before substantial local solution optimization**.

No new runtime component follows from this finding.

---

## 2. Recovered qualified prior architecture

The historical qualified architecture remains reference evidence, not automatically current operating authority. It changes the burden of proof for rediscovery.

### 2.1 System of Interest

`legacy/archive-2026-09-02/foundation/SYSTEM-OF-INTEREST.md` defines the parent problem as a coupled socio-technical Human–AI Work System rather than isolated model performance:

```text
Human judgment and agency
+ AI capabilities
+ tools / workflows
+ methods
+ state / knowledge
+ authority / control
+ interfaces
+ receiving context / downstream use
→ joint work-system performance
```

A Skill, prompt, model, Project, file set or runtime carrier does not become the parent System of Interest merely because it is the current topic.

### 2.2 Accepted historical Target Architecture

`legacy/archive-2026-09-02/architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md` accepted three orthogonal conceptual commitments:

1. **Distinct Responsibilities** — Strategic / Operating / Work / Execution / Learning-Change;
2. **Distributed Typed State** — authoritative state remains with legitimate owners while working context is composed as needed;
3. **Adaptive Work-Selection Contract** — admitted work selects the minimum justified next work from current reality, intended outcome/claim, requirements, preserved state, dependencies, capability/authority/runtime reality, consequence, uncertainty and economics.

The same baseline explicitly protects against downstream work beginning before materially required upstream state is sufficiently ready.

### 2.3 Prior architecture principles

`legacy/archive-2026-09-02/architecture/ARCHITECTURE-PRINCIPLES-v0.1.md` already states several principles directly relevant here:

- optimize the Human–AI work system, not an isolated AI component;
- model responsibilities before assigning actors;
- distinguish persistent operating architecture from episodic work architecture;
- include Human attention, time, coordination, rework and learning in work-system economics;
- preserve type integrity;
- use proportional / latent complexity rather than visible ceremony;
- preserve material semantics through compression and realization;
- treat qualified prior architecture as closed-but-reopenable Knowledge Capital.

### 2.4 Prior Requirements already covering adjacent semantics

`legacy/archive-2026-09-02/foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md` already includes:

```text
user request ≠ complete specification
input / proposed means ≠ underlying need / purpose ≠ intended outcome
current focus ≠ controlling system
local completion ≠ wider-work completion
minimum work ≠ prerequisite omission
more research ≠ better decision
```

It also requires claim-relative scope, outcome-before-means, open framing when the problem/solution class is materially open, and higher-purpose consideration when local initiatives compete for resources.

Therefore this Candidate must **refine and reactivate** the prior architecture, not create a parallel architecture lineage.

---

## 3. Deeper architecture description

The following is a **descriptive abstraction of the work system**, not a lifecycle, pipeline or mandatory runtime sequence.

```text
WORK DOMAIN
Purpose / values / success conditions / constraints / environment

        ↓

JOINT COGNITIVE WORK
Sensemaking / problem formation / reality grounding
Research / learning / hypothesis development
Decision / strategy / creation
Execution / integration
Evaluation / assurance
Adaptation / learning

        ↓

WORK ORGANIZATION
Human ↔ AI ↔ tools ↔ providers
allocation / coordination / authority / interdependence

        ↓

REALIZATION
Chat / Projects / Work / Skills / Research / Apps / artifacts / external systems
```

### Interpretation

- **Work Domain** describes what constrains and gives purpose to the work.
- **Joint Cognitive Work** describes the invariant kinds of transformation that may be needed, without assigning them to a particular actor or surface.
- **Work Organization** concerns allocation and coordination among Human, AI, tools and specialist providers.
- **Realization** is the product- and technology-specific carrier layer.

Accordingly:

```text
CI / Chat / Work / Projects / Skills / Apps
≠ architecture of thinking/work

They are realizations / carriers of work-system functions.
```

This interpretation is consistent with the current reduced operating baseline, where native ChatGPT owns ordinary conversation/reasoning/planning, Global CI carries cross-context cooperation defaults, Projects carry scoped continuity, Work owns sustained execution, Skills provide differentiated methods, and the Native Work Transition carries the conditional bridge.

---

## 4. Means–ends abstraction space for work

For material work, the relevant work object may be understood in a **means–ends abstraction space**:

```text
Fundamental purpose / Human values
            ↕ why / how
Situation / environment / stakeholders
            ↕
Parent Outcome of current work
            ↕
Success criteria / priorities / constraints
            ↕
Problem boundary / frame
            ↕
Causal structure / dependencies / assumptions / uncertainty
            ↕
Required work functions / capabilities
            ↕
Activities / decisions
            ↕
Human–AI allocation / coordination
            ↕
Strategies / methods / providers
            ↕
Concrete solutions / artifacts / actions
```

These are **not mandatory explicit levels** and need not be represented for bounded ordinary work.

### Parent Outcome is relative

`Parent Outcome` means the relevant higher outcome for the current Work Object. It may itself be a means toward a more fundamental purpose.

Do not climb indefinitely toward an ultimate purpose. Move upward only while uncertainty at the higher level could materially change the current problem boundary, decision level, route or relevant solution space.

---

## 5. Purpose–Problem–Solution Traceability

The core relational refinement is:

### Upward traceability — WHY

A substantial local problem or optimization should be sufficiently traceable to the relevant higher purpose/outcome:

> Why is this local problem worth solving, and how could solving it materially improve the higher outcome?

### Downward traceability — HOW

A required function or outcome can normally admit several possible realizations:

> What different interventions, strategies, methods or solutions could realize the needed function without prematurely equating one means with the requirement?

### Cross-cutting sensitivity

Dependencies, constraints, assumptions, evidence gaps, stakeholder/value conflicts and uncertainty may shift either:

- the **problem boundary**;
- the **causal relevance** of the local problem;
- the **decision level**;
- or the **relevant solution space**.

A locally coherent optimization is therefore not sufficient evidence that the correct work object has been chosen.

---

## 6. Canonical cooperation semantic Candidate — Problem-Space Sufficiency

The following is a **canonical cooperation semantic Candidate**, not yet a Global-CI wording or separate runtime mechanism:

> **Problem-Space Sufficiency before substantial local solution optimization.** Before substantial local solution work, ensure the current problem level is sufficiently grounded in the relevant higher purpose/outcome. If unresolved dependencies, constraints, assumptions, stakeholder/value conflicts, evidence gaps or uncertainties could materially change the problem boundary, decision level or relevant solution space, resolve them proportionately through accessible-context recovery, research, Human interaction, comparison or probes before optimizing locally. Do not broaden or reopen a sufficiently grounded problem merely because a deeper frame is imaginable.

### Sufficiency does not mean exhaustive understanding

Problem-space formation is sufficient when enough is known, for the next legitimate frontier, about the materially relevant subset of:

1. **higher purpose / Parent Outcome** — what improvement ultimately matters for this Work Object;
2. **problem boundary / scope** — what is and is not currently being treated as the problem;
3. **causal or means–ends relevance** — why the local problem is expected to affect the higher outcome;
4. **material dependencies and constraints** — what adjacent conditions can enable, block or dominate the local intervention;
5. **critical assumptions and uncertainty** — what the current frame relies on;
6. **solution sensitivity** — which unknowns could materially change the problem boundary, decision level or solution class;
7. **stakeholder / value / authority distinctions** — where differing legitimate perspectives or authority can materially change the frame;
8. **actual current state / evidence** — enough reality contact to avoid optimizing a proxy, obsolete state or imagined system.

Not every item must be explicit. The system is not required to prove that every deeper question is irrelevant.

### Legitimate next moves when sufficiency is missing

Depending on the unresolved dependency, the next work may be:

- recover accessible prior context/state;
- retrieve or research relevant external evidence;
- ask a discriminating Human question where judgment, inaccessible context or authority is required;
- compare competing problem representations;
- test a critical assumption;
- run a bounded probe/experiment;
- defer or stage commitment when information value justifies it.

The principle does **not** imply that more research, more questions or more exploration are inherently better.

---

## 7. Anti-failure boundary: do not create a universal discovery process

This reconciliation does **not** justify:

- a CWA workflow;
- a NASA-style requirements hierarchy for every chat;
- CATWOE or another problem-structuring ritual by default;
- a persistent `Problem Space` state object;
- a new `problem-formation` Skill;
- a root-cause interrogation before bounded tasks;
- a universal Work Graph or stage machine;
- a global router/controller;
- mandatory research before solution work;
- reopening a sufficiently grounded frame merely because a more abstract framing is possible.

For bounded work where higher-level uncertainty cannot materially change the requested contribution, answer or execute directly.

---

## 8. Reference-family interpretation

The following external reference families informed the reconciliation. They are **lenses**, not imported operating frameworks.

| Reference family | Parent concern / useful contribution | Transfer boundary |
|---|---|---|
| Value-Focused Thinking | distinguish fundamental objectives from means; alternatives serve values | Human/social objectives may remain plural and contested |
| Soft Systems Methodology / Problem Structuring | treat messy situations as requiring problem construction/learning, not only optimization | do not turn SSM into a universal chat workflow |
| Cognitive Work Analysis / Work Domain Analysis | purpose, values, functions and objects connected through means–ends relations; formative constraint-based design | use as abstraction lens, not mandatory five-level artifact |
| NASA / Systems Engineering | derive and validate lower-level requirements against higher-level mission/stakeholder needs; preserve traceability | strongest once mission/stakeholder expectations are sufficiently formed |
| Decision Analysis | analyze a bounded decision at the right decision level under objectives, uncertainty and trade-offs | does not own open problem formation |
| Joint Cognitive Systems / Coactive Design | treat coordinated Human–technology activity as the unit; observability, predictability and directability matter | no requirement for visible role/process theater |
| Resilience / adaptive systems | frames and capabilities must remain requalifiable when assumptions/environment change | does not imply constant reopening |
| Human–AI complementarity research | Human+AI is not automatically synergistic; evaluate joint performance and coordination | no general claim that one allocation is optimal |

### Selected external anchors

- NASA Systems Engineering Engine / system-design material: https://www.nasa.gov/reference/4-0-system-design-processes/
- NASA stakeholder expectations: https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
- NASA technical requirements: https://www.nasa.gov/reference/4-2-technical-requirements-definition/
- NASA logical decomposition: https://www.nasa.gov/reference/4-3-logical-decomposition/
- Cognitive Work Analysis / Work Domain Analysis overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC8250482/
- Value-Focused Thinking: https://www.sciencedirect.com/science/article/pii/0377221796000045
- Soft Systems Methodology overview: https://www.ifm.eng.cam.ac.uk/research/dstools/soft-systems-methodology/
- Human–AI combination meta-analysis: https://doi.org/10.1038/s41562-024-02024-1

---

## 9. Relationship to current active system

This Candidate **does not replace** the current reduced baseline.

Current active owners already cover much of the need:

- `baseline/OPERATING-BASELINE.md` — outcome before means, recovery, requalification, professional sufficiency, Human agency, relevant context, continuity, proportionality, claim integrity;
- `baseline/NATIVE-WORK-TRANSITION.md` — qualified Work Object and Work Formation Sufficiency before native execution;
- `decision-analysis` — refuses bounded decision analysis until decision object, owner, outcome and material decision level are sufficiently formed;
- `system-development` — claim/boundary qualification and need/solution separation for system changes;
- `REAL-USE-VALIDATION-METHOD.md` — already evaluates whether work solved the **actual need rather than a proxy/process artifact** and whether alternatives/trade-offs were handled at the **right level**.

The present gap is therefore not a missing total capability. It is a **weaker preventive activation relation in ordinary Joint Work before substantial local optimization**.

---

## 10. Real-use implication

A material failure signal is:

```text
plausible local problem accepted
→ substantial analysis/design/optimization invested
→ locally high-quality solution produced
→ later evidence shows higher-level purpose/dependency/assumption
   would have materially changed the problem boundary or solution space
```

A positive behavior signal is:

```text
local problem appears
→ higher-level relevance / boundary sufficiently grounded
→ if materially unstable: recover / research / interact / probe
→ if sufficiently grounded: optimize directly
```

One successful or failed episode remains bounded evidence. Do not automatically mutate CI or architecture from a single case; localize the responsible carrier/mechanism first.

---

## 11. Current Candidate disposition

**Recovered / preserved:**
- Human–AI Work System as the work-performance System of Interest;
- responsibility-before-actor logic;
- Strategic / Operating / Work / Execution / Learning distinctions;
- distributed typed state;
- adaptive minimum-justified work selection;
- proportionality / whole-system economics;
- outcome-before-means, claim-relative scope and current-focus boundaries;
- runtime realization distinct from conceptual architecture;
- current Chat / Project / Work / Skill ownership boundaries.

**Sharpened / candidate:**
- descriptive `Work Domain → Joint Cognitive Work → Work Organization → Realization` architecture view;
- means–ends abstraction space above concrete work;
- Parent Outcome as a relative rather than absolute top level;
- Purpose–Problem–Solution Traceability;
- Problem-Space Sufficiency before substantial local solution optimization;
- the preventive activation gap in ordinary Joint Work as distinct from post-hoc evaluation of proxy/wrong-level work.

**Not established:**
- that Global CI is the correct or sole carrier of the new semantic;
- exact runtime wording;
- behavioral reliability;
- need for any new Skill/component;
- superiority of this architecture description over every prior description;
- merge/promotion readiness.

---

## 12. Next legitimate frontier

1. **Preserve this reconciliation as Candidate Knowledge Capital.**
2. Use genuine work to test the failure class: premature local optimization under unstable higher-level problem space.
3. If the semantic survives review and real-use evidence, decide the smallest durable owner/carrier:
   - existing Operating Baseline refinement;
   - canonical cooperation semantic source;
   - compact Global-CI runtime cue;
   - method-local activation where appropriate;
   - or no change if native behavior already realizes it reliably.
4. Any CI compile remains a later target-specific semantic-regression task.

Do not modify PR #60 solely from this architecture reconciliation while its R2 candidate is still under genuine-use evaluation.
