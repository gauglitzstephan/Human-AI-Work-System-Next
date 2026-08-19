# Layer × View × Work-Control × Runtime Correspondence Test v0.1

**Status:** DIFFERENTIAL INTEGRATION TEST / PRE-ARCHITECTURE  
**Date:** 2026-08-19  
**Purpose:** Test whether the strongest qualified predecessor models are competing architectures or different architectural types that can compose without duplication, missing ownership, or forced runtime ceremony.

## Inputs

### Qualified Prior A — Whole-system responsibility architecture
`AI-native-Operating-Model` Foundation v0.2, accepted 2026-08-17:

```text
L1 Strategic Architecture
L2 Operating Architecture
L3 Work Architecture
L4 Execution Architecture
L5 Learning Architecture
```

with cross-cutting control planes:

```text
CP1 Reality & Provenance
CP2 Authority / Governance / Security
CP3 Assurance & Risk
CP4 Performance / Economics / Value
CP5 Knowledge / Configuration / Change
```

### Qualified Prior B — Architecture-description views
`human-ai-work-architecture` v1.3.1 / inherited v1.0–v1.3:

```text
V1 Mission & Outcome
V2 Work Process
V3 Information & State
V4 Capability & Resource
V5 Interaction & Authority
V6 Quality & Assurance
V7 Governance & Learning
V8 Execution Context & Integration
```

### Prior C — Work-control candidate
`Human-AI-Work-System` Core/B.6:

```text
Work Object / Work Product / Working State
Work Graph / Work Units
Semantic Compiler / Minimum Sufficient Work
Qualification / Realization
Information Value / Prospective Robustness / Commitment Design
```

### Counter-design / realization prior D
`PAOS`:

```text
Minimum Kernel K1–K8
Entry Surface
Context Home
Execution Surface
Return Surface
simple Operating Loop
conditional Projects / selective handover
no universal explicit Work Object requirement
```

---

# 1. Type hypothesis under test

```text
Layer
  = persistent responsibility / ownership domain in the whole system

View
  = concern-specific representation that can cut across multiple layers

Control Plane
  = cross-layer normative semantics / control contract that must remain coherent

Work-Control Policy
  = decision/control mechanism operating primarily inside Work Architecture

Runtime / Operating Profile
  = concrete configuration of surfaces, instructions, tools, state, skills,
    permissions, execution mechanisms and interaction rules
```

If this type system holds, the predecessor models are partly **orthogonal**, not mutually exclusive.

---

# 2. Layer × View correspondence

Legend:

- **P** — primary / load-bearing view for the layer;
- **M** — materially applicable;
- **C** — conditional / context-specific;
- **I** — mainly inherited/interface constraint; the layer should not redefine it.

| Responsibility Layer | V1 Mission & Outcome | V2 Work Process | V3 Info & State | V4 Capability & Resource | V5 Interaction & Authority | V6 Quality & Assurance | V7 Governance & Learning | V8 Execution Context & Integration |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **L1 Strategic** | **P** | C | M | M | **P** | M | M | C |
| **L2 Operating** | M | **P** | **P** | **P** | **P** | **P** | **P** | M |
| **L3 Work** | **P** | **P** | **P** | **P** | **P** | **P** | M | M |
| **L4 Execution** | I | **P** | **P** | **P** | **P** | **P** | M | **P** |
| **L5 Learning** | M | **P** | **P** | M | **P** | **P** | **P** | M |

## Interpretation

### Finding 2.1 — The five layers and eight views are not the same decomposition

No view maps one-to-one to one layer.

Examples:

- **V3 Information & State** is relevant to strategic assumptions, canonical Operating data/knowledge, episode Working State, actual runtime state, and Learning evidence.
- **V5 Interaction & Authority** spans strategic decision ownership, persistent organizational decision rights, Work Unit gates, runtime credentials and change/promotion authority.
- **V6 Quality & Assurance** changes form by layer but remains material across all of them.
- **V8 Execution Context** is primary in Execution Architecture but also determines which capabilities/state are actually available to Work and which evidence Learning can interpret.

### Finding 2.2 — The layer model supplies ownership that the view model deliberately does not

The eight-view architecture tells us **what must be represented and kept semantically distinct**.

It does not by itself give persistent ownership for questions such as:

- who owns strategy formation/change;
- who owns canonical organizational capability/process state;
- who owns a concrete Work design;
- who owns runtime implementation;
- who owns the learning/adaptation loop.

The five-layer model supplies this responsibility partition.

### Finding 2.3 — The view model supplies cross-cutting integrity that the layer model alone would otherwise duplicate

Without views, every layer could invent its own meanings for:

- state;
- capability;
- authority;
- readiness;
- assurance;
- execution context.

The view system therefore functions as an architecture-description / semantic-consistency system across responsibility layers.

### Disposition

**Five layers × eight views: COMPLEMENTARY / ORTHOGONAL ENOUGH TO RETAIN AS LEADING INTEGRATION HYPOTHESIS.**

Do not merge them into one list.

---

# 3. Naming collision audit

Several names look duplicative because a layer and a view share domain language.

## Collision A

```text
Work Architecture
vs
Work Process View
```

**Resolution:**

- Work Architecture = responsibility domain for designing/composing/assuring concrete professional work;
- Work Process View = representation of temporal/workflow/state-transition behavior across any relevant layer.

A strategic review process or Learning change loop can appear in V2 without becoming Work Architecture.

## Collision B

```text
Learning Architecture
vs
Governance & Learning View
```

**Resolution:**

- Learning Architecture = responsibility owner for observation → interpretation → diagnosis → change implication/routing → follow-up evidence;
- V7 = representation of governance, lifecycle, promotion, learning and change semantics across the whole system.

Learning Architecture does not acquire authority to mutate another layer merely because V7 includes change.

## Collision C

```text
Execution Architecture
vs
Execution Context & Integration View
```

**Resolution:**

- Execution Architecture = responsibility for translating approved Work/Operating design into concrete processes/actors/agents/tools/permissions/controls;
- V8 = representation of the actual runtime context, bindings, stacks and integration conditions relevant to a claim.

An Execution Context is not the whole Execution Architecture.

## Collision D

```text
Operating Architecture
vs
Runtime / Operating Profile
```

**Resolution:**

- Operating Architecture = persistent system of capabilities, roles, processes, data/knowledge, governance, platforms, performance and lifecycle that makes outcomes repeatably achievable;
- Runtime/Operating Profile = one concrete configuration on current surfaces/platforms.

PAOS is closer to the second than the first.

---

# 4. Five Control Planes × Eight Views

The five control planes overlap strongly with some views. Test whether they are redundant.

| Control Plane | Primary View carriers | Why not identical to the View |
|---|---|---|
| **CP1 Reality & Provenance** | V3 Info & State, V6 Assurance, V1 Mission | Plane contains normative rules (`authoritative source`, provenance, observation≠inference); views show how those semantics appear in different concerns/layers. |
| **CP2 Authority / Governance / Security** | V5 Authority, V7 Governance, V8 Execution Context | Plane is a cross-layer control contract; V5 describes decision/interaction rights, V8 concrete identity/access, V7 durable governance/change. |
| **CP3 Assurance & Risk** | V6 Quality & Assurance, V8 Execution Context | Plane specifies cross-layer assurance/risk semantics; view represents claim-specific quality/assurance and runtime evidence. |
| **CP4 Performance / Economics / Value** | V1 Mission & Outcome, V4 Capability & Resource, V6 Assurance | Plane forces end-to-end value/cost semantics across layers; no single view owns strategy-to-outcome economics. |
| **CP5 Knowledge / Configuration / Change** | V3 Info & State, V7 Governance & Learning, V8 Execution Context | Plane preserves canonicality/version/change semantics across knowledge, architecture and deployed runtime; views expose each projection. |

## Finding 4.1

Control planes are **not obviously additional architecture layers**.

They are best interpreted as:

> cross-layer normative contracts / invariant semantics whose state and implementation are inspected through one or more architecture views.

## Finding 4.2 — potential redundancy risk

The control-plane labels do add vocabulary and substantially overlap view concerns.

Therefore their right to remain explicit depends on whether they provide unique value as:

- named invariant owner;
- cross-layer conformance contract;
- traceability object from strategy through runtime;
- mechanism preventing semantic drift during architecture-to-runtime compression.

If views + explicit invariants can provide this with less vocabulary, control planes may be **compressible as contracts rather than first-class diagram boxes**.

### Disposition

**CONTROL PLANES: RETAIN FUNCTION, EXPLICIT REPRESENTATION OPEN.**

This is a genuine future compression question.

---

# 5. Work Architecture × Semantic Compiler

## Accepted Work Architecture already owns

- form the actual outcome/work object;
- use current authoritative reality and professional reference;
- define Work Product / receiving context / quality;
- decompose into Work Units when material differences require it;
- allocate Human/AI/tool/workflow/process capabilities;
- maintain state/authority/assurance;
- execute/integrate/refine;
- connect to realization and Learning.

## Semantic Compiler candidate adds

An explicit adaptive selection policy:

```text
current authoritative state
+ intended next legitimate claim/state
+ already qualified state
+ requirements / performance model
+ blockers / dependencies
+ authority
+ effective capabilities
+ consequence / reversibility
+ decision-relevant uncertainty
        ↓
minimum sufficient admissible work frontier
```

## Discrimination

These are **not independent complete architectures**.

The Semantic Compiler is best typed as a candidate **Work-Control policy / controller** that selects which Work Architecture functions/units need activation now.

Potential incremental value:

1. prevents Work Architecture from becoming a latent checklist activated wholesale;
2. provides explicit stopping / minimum-sufficient-work semantics;
3. creates a compilation boundary from rich architecture/method/reference knowledge to a small next work frontier;
4. may reduce active-context/salience burden;
5. creates a testable decision policy for next-work selection.

Potential non-value / duplication:

1. Work Architecture already says use smallest sufficient method/work and collapse simple work;
2. PAOS already routes direct vs discovery vs bounded work implicitly;
3. a named Compiler may be metaphor/vocabulary without incremental behavior;
4. implementation may be distributed policies rather than one controller.

### Disposition

**SEMANTIC COMPILER: OPEN AS OPTIONAL WORK-CONTROL MECHANISM, NOT NEW ARCHITECTURE LAYER.**

Promotion requires behavioral evidence of incremental value over:

- Work Architecture alone;
- PAOS-like simple/conditional routing.

`Work Engine` should not be introduced as an additional abstraction unless it is shown to own more/different responsibility than this candidate controller.

---

# 6. PAOS correspondence

## PAOS Minimum Kernel K1–K8 maps largely to higher-level semantics

| PAOS Kernel | Higher-level correspondence |
|---|---|
| K1 Human purpose & authority | L1/L2/L3 + CP2 + V1/V5 |
| K2 Reality & epistemic status | CP1 + V3/V6 |
| K3 Proportional disposition | L3 Work + Work-Control candidate + CP4 |
| K4 Work & capability fit | L3 + V2/V4/V6 |
| K5 Evaluation & acceptance | V6 + realization semantics |
| K6 Persistence & external action | V3/V5/V8 + CP2/CP5 |
| K7 Local learning/shared promotion | L5 + CP5 + V7 |
| K8 Portability & exit | L2/L4/L5 + CP5 + V8 |

### Finding

PAOS does not expose most higher-level architecture as visible runtime structure, yet preserves many of its boundaries in eight compact rules.

This is important evidence for **architecture/runtime separation**:

> rich architecture semantics may compile into a much smaller runtime contract.

## PAOS surfaces map primarily to V8 / Execution realization

```text
Entry Surface
Context Home
Execution Surface
Return Surface
```

These are concrete operating-context / routing roles rather than new whole-system layers.

## PAOS direct path

```text
Input → useful output
```

for clear low-risk work demonstrates that preserving architecture semantics does not require visible Work Unit or lifecycle objects on every case.

### Disposition

**PAOS: RETAIN AS REQUIRED RUNTIME COMPRESSION / PROPORTIONALITY PROFILE AND BASELINE.**

---

# 7. Architecture-to-runtime projection

The correspondence test suggests the following type-correct chain:

```text
REFERENCE / WHOLE-SYSTEM RESPONSIBILITY ARCHITECTURE
Strategic | Operating | Work | Execution | Learning

             constrained by / checked through
                         ↓

CROSS-CUTTING SEMANTIC CONTRACTS + VIEWS
Reality | State | Capability | Authority | Assurance | Value | Change | Runtime

                         ↓
              inside Work when needed

OPTIONAL ADAPTIVE WORK-CONTROL POLICY
Semantic Compiler / minimum-sufficient-work selection

                         ↓

RUNTIME / OPERATING PROFILE
PAOS-like kernel + CI + Project Context + Skills + Apps + Codex + tools + state

                         ↓

REAL WORK / USE / OUTCOMES
```

Important:

```text
architecture richness
≠ runtime verbosity

view coverage
≠ every-view activation

Work Unit semantics
≠ formal Work Unit artifact on every task

control-plane semantics
≠ five runtime controllers
```

---

# 8. Missing-ownership test

With the typed integration hypothesis, test whether any major responsibility has no plausible owner.

| Responsibility | Candidate owner/type | Gap? |
|---|---|---|
| Purpose / strategic outcome / priorities | Strategic Architecture + V1/V5 | No obvious gap |
| Persistent capabilities / processes / data / governance / platforms | Operating Architecture + V3/V4/V5/V7/V8 | No obvious gap |
| Concrete professional work design/composition | Work Architecture + V1–V6 | No obvious gap |
| Next-work activation / stopping | Work Architecture; optional Semantic Compiler | **Open mechanism question**, not ownership gap |
| Concrete actor/tool/agent execution | Execution Architecture + V8 | No obvious gap |
| Evidence / outcomes / adaptation routing | Learning Architecture + V6/V7 | No obvious gap |
| Strategy↔portfolio/resource feedback | Strategic + Operating; portfolio mechanism conditional | Boundary requires more test, but no empty layer |
| Knowledge Capital lifecycle | Learning + Operating owners depending asset type; CP5/V3/V7 | Ownership details still need reconciliation |
| Cross-layer semantic consistency | Views + control-plane contracts | Representation/compression question remains |

### Result

**NO CLEAR MISSING TOP-LEVEL RESPONSIBILITY LAYER FOUND.**

This agrees with the 2026-08-17 seven-scenario validation of the AI-native Operating Model, which also found no missing foundational layer/control plane in its tested scope.

---

# 9. Duplication test

## Duplications to avoid

### Do not create both

```text
Work Architecture
AND
Work Engine as another peer whole-system layer
```

without a unique ownership difference.

### Do not model

```text
V3 Information & State
AND
Knowledge/State layer
```

as peer structural subsystems merely because both vocabulary sets exist.

### Do not make

```text
PAOS Project / Context Home
```

into a universal logical Work-unit taxonomy.

### Do not maintain both

```text
five responsibility layers
AND
SC/PC/WC/OC
```

as two competing master hierarchies unless the second is explicitly typed as a control view and demonstrates incremental discrimination.

### Do not promote

```text
control planes
```

into additional runtime components by default.

---

# 10. Genuine deltas after correspondence

The new program should concentrate on six unresolved deltas rather than reconstructing the base architecture.

## Δ1 — Personal/general transfer of Operating Architecture

The five-layer prior was written as an AI-native operating model with enterprise/organization language.

Question:

> Which Operating Architecture responsibilities remain constitutive for a one-person / personal Human–AI Work System, and which become conditional only when persistent organizational structure exists?

This is a real transfer question.

## Δ2 — SoI / boundary formalization

Does explicit nested claim-relative `SoI-P / SoI-E` materially improve the existing layer/view model, especially for:

- joint-performance attribution;
- engineered lifecycle/security scope;
- external/enabling systems;
- responsibility and evaluation?

If not, reject the new notation.

## Δ3 — View / control-plane compression

Can the five control-plane functions be represented as invariant contracts carried by the eight views without losing ownership or conformance?

Potential simplification opportunity.

## Δ4 — Adaptive Work-Control incremental value

Does Semantic Compiler / a Work-Control policy materially improve behavior over accepted Work Architecture + PAOS conditional routing?

This is the strongest current candidate for an empirically testable `Work Engine` nucleus.

## Δ5 — Architecture-to-runtime semantic compilation

How do we preserve load-bearing semantics under severe active-context/salience limits without embedding the full architecture in runtime instructions?

HAWS v0.6.1→v0.6.2 salience regressions and PAOS compression make this a genuine design/evaluation problem.

## Δ6 — Knowledge Capital ownership/promotion

Where should reusable professional knowledge, validated Work patterns, Skills/capabilities, Operating patterns and personal/organizational state live, and what transitions them between statuses?

The distinction exists; ownership/promotion across architecture types remains partially distributed.

---

# 11. Freeze candidates

The following should now be treated as **provisionally inherited common semantics** unless a specific reopen trigger appears:

1. request/input ≠ complete requirement;
2. current/authoritative reality before material redesign;
3. Work Object / Work Product / Working State are distinct roles when material;
4. bounded Work Units / Work Graph are conditional decomposition mechanisms, not mandatory visible bureaucracy;
5. allocate Human/AI/tool/workflow/process by effective capability, evidence, authority and context;
6. capability ≠ access ≠ authority ≠ verified performance;
7. internal readiness gate ≠ Human Gate;
8. technical completion ≠ professional fitness ≠ acceptance ≠ use ≠ outcome ≠ value;
9. authoritative persistent Operating state/pattern requires explicit ownership and promotion;
10. runtime execution context can change capability/state and must be observed rather than inferred;
11. Learning proposes/routes cross-domain change but does not silently seize mutation authority;
12. simple work must remain capable of direct collapse;
13. architecture acceptance ≠ runtime installation ≠ behavioral effectiveness.

They may be worded differently later; do not reopen their mechanism merely for vocabulary cleanup.

---

# 12. Gate result

| Test | Result |
|---|---|
| Five responsibility layers vs eight views | **COMPLEMENTARY — PASS** |
| Five control planes vs views | **FUNCTIONALLY USEFUL; REPRESENTATION OPEN / POSSIBLY COMPRESSIBLE** |
| Work Architecture vs Semantic Compiler | **LAYER + OPTIONAL CONTROL POLICY; behavioral delta OPEN** |
| Whole architecture vs PAOS | **ARCHITECTURE + MINIMAL RUNTIME PROFILE; complementary and useful rival** |
| Missing top-level responsibility | **NONE FOUND in current lineage** |
| Need for new peer `Work Engine` layer | **NO** |
| Need for blank-slate Q4–Q8 | **NO** |

## Next decision-relevant work

Do not resume generic Cross-Reference synthesis.

Proceed on the **six genuine deltas**, beginning with the most upstream pair:

> **Δ1 Personal/general transfer of Operating Architecture + Δ2 SoI/boundary formalization**

Use predecessor semantics as the baseline and external references only to discriminate the transfer/boundary question.

After Δ1–Δ2, address:

- Δ3 view/control-plane compression;
- Δ4 adaptive Work-Control behavioral value;
- Δ5 architecture→runtime semantic compilation;
- Δ6 Knowledge Capital ownership/promotion.

Only these unresolved deltas should be allowed to change the architecture.
