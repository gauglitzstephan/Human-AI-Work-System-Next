# Prior Architecture Differential Review v0.1

**Status:** DIFFERENTIAL SYNTHESIS / PRE-ARCHITECTURE  
**Date:** 2026-08-19  
**Question:** Are the main predecessor repositories competing architectures, complementary views, subordinate mechanisms, or implementation profiles — and what architecture question is actually still unresolved?

---

# 1. Executive judgment

The four strongest predecessor lines are **not four equivalent competing architectures**.

They operate at materially different abstraction / responsibility levels:

```text
WHOLE-SYSTEM RESPONSIBILITY ARCHITECTURE
    AI-native-Operating-Model

ARCHITECTURE DESCRIPTION / CROSS-CUTTING VIEW SYSTEM
    human-ai-work-architecture

WORK-ARCHITECTURE / ADAPTIVE WORK-CONTROL SEMANTICS
    Human-AI-Work-System Core/B.6 + Semantic Compiler

CONCRETE NATIVE-SURFACE OPERATING PROFILE / MINIMUM RUNTIME RIVAL
    PAOS
```

This is the most important differential finding so far.

A large portion of prior architectural churn can be explained by **type confusion**:

- a whole-system responsibility decomposition was compared with a view system;
- a work-control mechanism was allowed to look like a whole-system architecture;
- a runtime/native-surface profile was treated as if it answered the same questions as a reference architecture;
- repeated concepts were reintroduced because their original architectural type/owner was lost during migration.

The Next program should therefore first recover **architecture type and relationship**, not invent another universal hierarchy.

---

# 2. Prior A — AI-native Operating Model

## Declared object

A grounded architecture for how strategy, organization, Humans, AI, tools, workflows, controls and learning combine to produce outcomes.

## Type

**Whole-system responsibility / operating architecture candidate — ACCEPTED foundation v0.2.**

## Five accepted responsibility layers

```text
Strategic Architecture
Operating Architecture
Work Architecture
Execution Architecture
Learning Architecture
```

Cross-cutting control planes:

```text
Reality & Provenance
Authority / Governance / Security
Assurance & Risk
Performance / Economics / Value
Knowledge / Configuration / Change
```

## What it uniquely answers

- what persistent responsibility class owns strategy vs organization vs concrete work vs runtime execution vs adaptation;
- where persistent organizational processes/capabilities live;
- where concrete Work patterns are instantiated;
- where authoritative mutation after learning belongs;
- how whole-system value and operationalization remain connected.

## Evidence status

Externally grounded and accepted after seven scenario classes plus bounded repairs.

## Differential disposition

**LEADING PRIOR FOR WHOLE-SYSTEM RESPONSIBILITY ARCHITECTURE.**

Do not replace unless a material defect or stronger rival is shown.

---

# 3. Prior B — human-ai-work-architecture

## Declared object

Personal Human–AI Work Architecture with canonical architecture, implementation candidates, evidence/evaluation and change control.

## Type

The accepted v1.3.1 baseline is best interpreted primarily as an **architecture-description / semantic-view system for Human–AI work**, not simply a rival layer taxonomy.

Its eight views:

```text
1 Mission & Outcome
2 Work Process
3 Information & State
4 Capability & Resource
5 Interaction & Authority
6 Quality & Assurance
7 Governance & Learning
8 Execution Context & Integration
```

## What it uniquely answers

- how the same Human–AI Work System must be represented across orthogonal concerns;
- semantic distinctions that must survive all implementations;
- Work Object / Work Product / Working State;
- transition integrity and Internal Gate vs Human Gate;
- capability-provider/access/authority;
- execution-context binding and adapters;
- subject/evaluator context separation.

## Relationship to Prior A

The eight views do **not obviously compete** with the five responsibility layers.

Plausible relation:

> The five layers say **which responsibility domain owns what**.  
> The eight views say **from which concern perspective the system/layers must be described and checked**.

Example:

- `Information & State View` applies across Strategic, Operating, Work, Execution and Learning layers;
- `Interaction & Authority View` cuts across them;
- `Execution Context View` is concentrated in Execution but binds Work/Operating semantics to realization.

## Differential disposition

**RETAIN AS CROSS-CUTTING VIEW / SEMANTIC ARCHITECTURE PRIOR.**

Next must test whether all eight views remain necessary at the new SoI, but should not collapse them into the five-layer hierarchy.

---

# 4. Prior C — Human–AI Work System Core / B.6 / Semantic Compiler

## Declared object

Versioned system for designing, grounding, executing, transitioning and evaluating high-quality Human–AI professional work with ChatGPT.

## Type

**Work-Architecture semantics + adaptive work-control policy + thin runtime projection.**

It is not best treated as a complete whole-system responsibility architecture.

## Strongest distinct mechanism candidate

The `Semantic Compiler`:

```text
current authoritative state
+ next claim/state transition
+ already qualified state
+ requirements/performance model
+ blockers/dependencies
+ authority
+ effective capabilities
+ consequence/reversibility
+ uncertainty
→ minimum sufficient admissible work frontier
```

This is a candidate **adaptive controller inside / for Work Architecture**.

## Relationship to Prior A

Most Core semantics map naturally into Prior A's **Work Architecture**, with interfaces to:

- Strategic Architecture for parent purpose/priority;
- Operating Architecture for persistent capabilities/processes/state/authority context;
- Execution Architecture for concrete mechanism/runtime;
- Learning Architecture for evidence-qualified adaptation.

## Relationship to Prior B

The Semantic Compiler consumes/uses concerns represented by several views:

- Work Process;
- Information & State;
- Capability & Resource;
- Interaction & Authority;
- Quality & Assurance;
- Execution Context.

Thus it is more plausibly a **control function/policy** than another complete architecture description.

## Differential disposition

**OPEN DECISION: retain Semantic Compiler as Work-Control kernel/policy only if it demonstrates incremental behavioral value or compression beyond the accepted Work Architecture.**

The term `Work Engine` should not be introduced unless it names a materially different responsibility/mechanism from Semantic Compiler + Work Architecture.

---

# 5. Prior D — PAOS

## Declared object

Personal AI Minimum Kernel / native-surface architecture for human-governed AI work.

## Type

**Concrete operating/runtime profile + deliberate minimum-complexity counter-design.**

## Strongest distinctions

```text
Entry Surface
Context Home
Execution Surface
Return Surface
```

plus:

- simple/global work stays simple;
- Projects are conditional Context Homes;
- selective handover;
- formal Work Objects only when governance benefit justifies them;
- no universal WOLC / Work Object lifecycle.

## Relationship to A/B/C

PAOS can be understood as one possible **realization / operating profile** constrained by higher-level semantics, not a replacement for all architecture.

Its critical role in Next is as an adversarial check:

> Can the architecture remain mostly latent while ordinary work stays direct?

## Differential disposition

**RETAIN AS REQUIRED MINIMUM-RUNTIME / PROPORTIONALITY RIVAL.**

Any new globally visible architecture concept must show value over PAOS-like conditional activation.

---

# 6. Type map

Provisional relationship model:

```text
┌─────────────────────────────────────────────────────┐
│ WHOLE HUMAN–AI WORK SYSTEM                          │
│                                                     │
│ Responsibility architecture                         │
│ → Strategic / Operating / Work / Execution / Learn │
│   [AI-native Operating Model prior]                 │
│                                                     │
│ Cross-cutting architecture views                    │
│ → Mission / Work / State / Capability / Authority  │
│   / Assurance / Governance / Execution Context     │
│   [human-ai-work-architecture prior]                │
│                                                     │
│ Within Work Architecture:                           │
│ → Work Graph / Work Units / Work Products           │
│ → adaptive next-work selection                      │
│   [Semantic Compiler / possible Work-Control kernel]│
│                                                     │
│ Concrete Operating / Runtime Profiles:              │
│ → PAOS-like native-surface configuration            │
│ → CI / Skills / Projects / Codex / tools / state    │
└─────────────────────────────────────────────────────┘
```

This is **not yet an accepted architecture**. It is a type-correct reconciliation hypothesis.

---

# 7. What is genuinely still unresolved?

The unresolved frontier is materially narrower than the Next program previously assumed.

## D1 — Whole-system SoI scope

Does the accepted AI-native Operating Model's whole-system architecture transfer cleanly from organization-oriented operating model to the intended **general/personal Human–AI Work System**, or does it over-assume an organizational/enterprise setting?

This is where the `nested claim-relative SoI` hypothesis may add real value.

## D2 — Five layers vs eight views

Are these orthogonal dimensions as hypothesized, or do they duplicate/contradict each other?

Need an explicit `Layer × View` correspondence test — not another new taxonomy.

## D3 — Work-control kernel

Does the accepted Work Architecture need a distinct adaptive controller?

Compare:

```text
Work Architecture alone
vs
Work Architecture + Semantic Compiler
vs
PAOS-like implicit/simple routing
vs
new Work Engine abstraction
```

The last option has no right to exist unless it beats/clarifies the first three.

## D4 — Persistent personal vs organizational operating semantics

Which Operating Architecture responsibilities are always relevant to one-person/personal AI work, and which are conditional only when persistent organizational/institutional structure exists?

This is likely the true transfer problem behind `Operating Model` confusion.

## D5 — Architecture-to-runtime projection

How do accepted semantics remain behaviorally salient when only a small subset can live in the active runtime/context?

This is supported by HAWS salience regressions and may be more important than another architecture layer.

## D6 — Knowledge Capital placement

Prior lines consistently distinguish reusable Knowledge Capital from authoritative current state, but differ in where it is owned:

- cross-cutting Knowledge/Change plane;
- separate repository layer;
- Work/Operating/Learning outputs.

Need to resolve **ownership and promotion**, not re-prove that knowledge matters.

---

# 8. What can be provisionally frozen now?

Subject to a focused lineage audit, the following appear sufficiently convergent to stop first-principles re-derivation:

1. input/request is not automatically the complete requirement;
2. current/authoritative reality precedes redesign when material;
3. Work Object / Work Product / Working State are distinct roles where material;
4. Work may decompose into bounded units/dependencies when materially different methods/capabilities/interfaces/authority/assurance exist;
5. Human/AI/tool/workflow allocation is capability- and authority-relative, not ideology-driven;
6. capability/access/authority are distinct;
7. internal readiness gates are not automatically Human interaction gates;
8. output/artifact/delivery/acceptance/use/outcome/value are distinct;
9. persistent organizational process/state requires explicit ownership/promotion and is not created by reuse alone;
10. runtime/platform context can materially change effective capability and must not be inferred across contexts;
11. more architecture/process is not automatically better; simple work must collapse aggressively;
12. accepted design and runtime installation/performance are different claims.

These are **provisional common-core semantics**, not yet a new Core file.

---

# 9. Immediate implication for Q4–Q8

The previously planned Q4–Q8 sequence is replaced by **differential questions**:

### Q4D — Human capability delta
What external evidence since the strongest prior grounding changes the already accepted Human/AI allocation, stewardship, learning or recovery semantics?

### Q5D — State/knowledge delta
Where do qualified priors materially disagree on authoritative state, working context, Knowledge Capital ownership/promotion or cross-surface continuity?

### Q6D — Authority delta
What new agentic/tool reality is not already covered by capability/access/authority, action-specific authorization, Human Gates and execution-context semantics?

### Q7D — Realization delta
What is missing beyond the already accepted Work Product → transition → use/mechanism → outcome/value chain?

### Q8D — Economics/proportionality delta
Can total-system cost/attention/maintenance be made operational enough to choose between full architecture, Semantic Compiler and PAOS-like minimal runtime?

Research should now answer these **deltas**, not reconstruct the base concepts.

---

# 10. Gate result

**FOUR PRIORS AS EQUIVALENT COMPETING ARCHITECTURES:** REJECT  
**TYPE-CORRECT COMPLEMENTARY MODEL:** PROMISING  
**AI-native Operating Model as leading whole-system prior:** RETAIN  
**Eight-view architecture as cross-cutting description prior:** RETAIN  
**Semantic Compiler as potential Work-control kernel:** OPEN / TEST  
**PAOS as minimum-runtime rival:** RETAIN  
**new universal Work Engine from scratch:** NO BASIS YET

Next decision-relevant work:

> **Layer × View × Runtime Correspondence Test v0.1**

Test whether the five responsibility layers, eight accepted views, Work-control/Semantic Compiler functions and PAOS runtime profile compose coherently without duplication or missing ownership.

If they do, the new architecture may be largely a **typed integration and compression of existing qualified priors**, not a new theory.
