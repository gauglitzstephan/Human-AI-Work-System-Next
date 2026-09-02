# Cross-Reference Synthesis & Discrimination v0.1

**Status:** STAGE-1 SYNTHESIS / PRE-ARCHITECTURE  
**Date:** 2026-08-19  
**Scope:** Q1 SoI Boundary · Q2 Focal Units / Scale · Q3 Work Control vs Strategy vs Portfolio Control  
**Method:** `REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md` E1–E4 + D0–D4.  
**Claim boundary:** This is a decision-relevant synthesis of external references and internal hypotheses. It does not define the final architecture or runtime.

---

# 0. Executive discrimination

The first three questions produce a coherent candidate structure:

```text
PRIMARY PERFORMANCE SoI
Human–AI Work System
(sociotechnical system whose joint work/outcomes are evaluated)

    contains / uses
        ↓
ENGINEERED SUPPORT SoI
AI Work-Support / Control Subsystem
(models, runtime control, tools, context/state interfaces, technical guards)

    operates through
        ↓
DEFAULT CONTROL UNIT
Work Episode / Case

    may be nested in
        ↓
Initiative / Project / Programme

    competes within
        ↓
Portfolio / Resource-Attention System

    is oriented and revised by
        ↕
Strategy / Strategic Renewal
```

This is a **nested-control hypothesis**, not an accepted component diagram.

Key discrimination:

```text
one fixed SoI boundary        → REJECT AS DEFAULT
one universal focal unit      → REJECT
Work Engine owns strategy     → REJECT
Work Engine owns portfolio    → REJECT
linear Strategy→Execute only  → REJECT
nested SoIs + nested units    → PROMISING
coupled control levels        → PROMISING
```

---

# 1. Q1 — What is the right System-of-Interest boundary?

## 1.1 Competing hypotheses

### H-A — Sociotechnical Human–AI Work System

Relevant humans, AI, tools, work objects, information/state, roles and surrounding work arrangements are inside the performance SoI.

**Strength:** joint work and outcome performance can be attributed to the actual human–technology configuration rather than to the AI component alone.

**Risk:** engineered responsibilities, technical ownership and security/lifecycle boundaries can become diffuse.

### H-B — Engineered AI Work-Support System

The designed AI-mediated support/control system is the SoI; humans and organizations are external actors/interfaces.

**Strength:** clearer technical ownership, V&V, lifecycle, runtime and security scope.

**Risk:** the object being optimized can collapse from real work to software/component performance.

### H-C — Nested / dual SoI model

Use different but explicitly related SoIs for different claims:

1. **Primary performance SoI:** sociotechnical Human–AI Work System;
2. **Nested engineered SoI:** AI Work-Support / Control Subsystem;
3. enabling systems and operational environment remain separately identified.

This avoids making one boundary serve incompatible analytical purposes.

---

## 1.2 Reference synthesis

### Systems Engineering / Architecture — R1

ISO/IEC/IEEE 42010 does not prescribe one kind of entity of interest; architecture-description concepts can apply to software, systems, enterprises, systems-of-systems, products and other entities. ISO/IEC/IEEE 15288 likewise applies lifecycle processes to systems of interest, system elements and systems-of-systems.

**Implication:** systems-engineering references require explicit boundary/relationship semantics but do not force one metaphysical root boundary.

### Work System Theory — R2

Alter’s Work System Theory/Method uses the work system—not the IT artifact—as the focal object for understanding and improving organizational work. The method explicitly treats the information system as part of the work system until a later analytical distinction between changes that do and do not involve the information system.

**Implication:** if the claim is about work performance, the technical AI system alone is an under-bounded object.

### Cognitive Systems Engineering / Joint Cognitive Systems — R3

Cognitive Systems Engineering rejects purely mechanistic decomposition for complex human–machine systems and analyzes cognitive functions across the coupled system. The design object is the adaptive human–machine cognitive system, including mutual representations and coordination.

**Implication:** cognitive/work performance can be an emergent property of the joint configuration rather than a sum of component performances.

### Human–AI Teaming / HSI — R4

The National Academies identifies gaps when AI research focuses on independent AI performance rather than functionality in dynamic, distributed, adaptive collaborative tasks. It recommends context-of-use analysis and system/team-level performance measures, including role flexibility, coordination and resilience.

**Implication:** for Human–AI joint-performance claims, humans cannot be modeled merely as an external acceptance oracle.

### Security / Runtime / Management-System references — R13/R15 + BRC-02

Engineering and management references still require bounded technical responsibility, permissions, operational controls, lifecycle ownership and auditable managed processes.

**Implication:** a broad sociotechnical performance SoI does not eliminate the need for a separately bounded engineered subsystem.

---

## 1.3 Conflict

The apparent A-vs-B conflict is largely a **claim-relative boundary conflict**:

- Human Factors / Work Systems ask: *what configuration explains work performance?*
- Systems/Software Engineering asks: *what engineered entity are we designing, verifying, operating and changing?*
- Governance asks: *who owns which decision, risk and lifecycle obligation?*

Forcing all three questions into one boundary creates category errors.

---

## 1.4 Provisional decision

### Q1 DISPOSITION: **PROMOTE H-C AS LEADING BOUNDARY HYPOTHESIS**

Use nested claim-relative SoIs unless later evidence shows a simpler single boundary can preserve the same semantics.

Provisional naming:

```text
SoI-P — Human–AI Work System
  purpose: joint professional-work / outcome performance

SoI-E — AI Work-Support / Control Subsystem
  purpose: engineered behavior, technical lifecycle, V&V, runtime/security
```

Do not assume `SoI-E` is one software process or one “Work Engine.” Its internal structure remains open.

### Falsifier

Reject H-C if:
- nested boundaries add terminology without changing responsibility, evaluation or design decisions; or
- one simpler SoI boundary can express joint performance and engineered accountability without loss.

---

# 2. Q2 — What focal units / scales are required?

## 2.1 Candidate alternatives

### U-A — One universal work item

Use one generalized Work Object / task unit at every scale.

**Benefit:** semantic simplicity.

**Risk:** state, completion, authority and resource semantics leak across radically different scales.

### U-B — One default episode plus arbitrary containers

Use Work Episode/Case as the only meaningful control unit; projects/portfolios are metadata containers.

**Benefit:** runtime simplicity.

**Risk:** multi-session persistence, dependencies, shared outcomes, strategic resource allocation and portfolio effects become under-modeled.

### U-C — Typed nested focal units

Different units exist because they have different semantics; the system activates only the smallest unit that preserves material mechanisms.

---

## 2.2 Reference synthesis

### Work System Theory — R2

WST distinguishes a standing work system from its evolution over time. The focal object is not merely a single conversational turn or technical invocation.

### Adaptive Case Management / CMMN — R2/BRC-04

CMMN represents cases in which activities may occur in unpredictable order in response to evolving situations and uses living case information/milestones rather than assuming an a-priori process sequence.

**Implication:** `case/episode` is a strong candidate default control unit for open professional work.

### Human–AI Teaming — R3/R4

The National Academies explicitly notes performance evolution across work sessions, shifts, task episodes, software updates and longer horizons.

**Implication:** time/coordination effects cannot be collapsed into a single-turn model.

### Project / Programme / Portfolio — R17

ISO 21500 treats project, programme and portfolio as distinct management concepts and points to separate standards for each. ISO 21503 and 21504 maintain distinct programme and portfolio scopes.

**Implication:** persistent multi-work coordination and resource allocation are not just larger tasks.

### Enterprise / Operating Model — BRC-01/BRC-03

Operating-model and enterprise-architecture references work at the standing organizational capability/process/platform level rather than at individual episodes.

**Implication:** the configured Work System itself is a persistent object distinct from work occurring within it.

---

## 2.3 Discriminating semantics

A focal-unit type earns separation when at least one of these changes materially:

- purpose/owner;
- state/completion semantics;
- authority/acceptance;
- persistence horizon;
- dependencies;
- resource allocation;
- outcome/benefit horizon;
- monitoring/reopen conditions;
- competing-work opportunity cost.

---

## 2.4 Provisional unit model

### Q2 DISPOSITION: **PROMOTE U-C — TYPED NESTED FOCAL UNITS**

Minimum candidate set:

```text
F0 — Interaction / Operation
     one local exchange, tool invocation or execution operation
     mainly trace/execution semantics

F1 — Work Episode / Case
     bounded purpose-directed work object with local state and exit conditions
     DEFAULT work-control focal unit

F2 — Initiative / Project / Programme
     persistent multi-episode coordinated change/work with dependencies,
     shared outcomes and explicit continuation/closure semantics

F3 — Portfolio
     competing initiatives/bets sharing scarce resources/attention;
     selection, balancing, scale/pause/kill and opportunity-cost semantics

F4 — Configured Human–AI Work System
     standing arrangement of actors/capabilities/state/controls/interfaces
     through which episodes and initiatives occur
```

Organization / market / institution / ecosystem remain candidate environment or higher SoI scopes rather than mandatory runtime units.

### Compression rule

```text
simple direct work → F1 may collapse operationally to immediate action
no persistent initiative → do not create F2
no competing material bets → do not activate F3
```

### Open question

Whether `Programme` requires a distinct type between F2 and F3 or can remain a subtype/configuration of F2 should be decided only if its benefit-coordination semantics materially affect our use cases.

---

# 3. Q3 — How should Work Control, Strategy and Portfolio Control relate?

## 3.1 Competing architectures

### C-A — Unified universal controller

One Work Engine chooses everything from next tool call through strategy and portfolio allocation.

**Benefit:** elegant single-control concept.

**Risk:** conflates local task progress, strategic direction, commitment authority and cross-initiative resource allocation.

### C-B — Strict top-down hierarchy

```text
Strategy
→ Portfolio
→ Initiative
→ Work Episode
→ Operation
```

**Benefit:** clear decomposition and authority chain.

**Risk:** assumes strategy is fully formed upstream and ignores emergent strategy, learning and bottom-up strategic effects.

### C-C — Coupled multi-level control

Separate control domains with typed interfaces and upward/downward feedback.

---

## 3.2 Reference synthesis

### Local decision / metareasoning — R7

Decision and metareasoning fields address which question, information, computation, test or action is worth performing under local uncertainty/cost.

**Relevant object:** current decision/work state.

### Strategy formation — R16

Mintzberg & Waters distinguish deliberate and emergent strategy. Real strategy can form as a pattern rather than merely execute a prior plan.

Noda & Bower model strategy making in large firms as iterated resource-allocation processes in which local initiative results affect later managerial commitment.

Teece/Pisano/Shuen emphasize reconfiguration of capabilities in changing environments.

**Relevant object:** direction, position, capability path and coherent pattern across decisions/actions over time.

### Portfolio / programme management — R17

ISO distinguishes portfolio from project/programme management; portfolio management concerns a portfolio of projects/programmes and must be adapted to its environment.

**Relevant object:** selection/balancing of multiple initiatives competing for scarce resources and strategic contribution.

### Operating Model / Management Control — BRC-01 + R17

Operating-model research connects accountabilities, processes, platforms, metrics and behaviors with value creation. Management/control systems address how persistent organizational activity is directed, monitored and adapted.

**Relevant object:** standing configuration and control regime rather than one episode.

---

## 3.3 Conflict

Strategy and portfolio cannot be separated by a naive one-way sequence because:

```text
strategy constrains resource allocation
AND
resource-allocation outcomes help form/revise strategy
```

Likewise, work evidence can trigger strategic change, but a local Work Episode must not silently redefine strategic purpose or reallocate a whole portfolio.

---

## 3.4 Provisional control model

### Q3 DISPOSITION: **PROMOTE C-C — COUPLED MULTI-LEVEL CONTROL**

Candidate control domains:

```text
SC — Strategic Control
     What directions/positions/capabilities/bets should be pursued or revised?

PC — Portfolio / Initiative Control
     Which initiatives receive resources/attention; which scale, pause, combine or stop?

WC — Work / Episode Control
     Given an admitted Work Episode, what is the minimum sufficient next work,
     method, capability, evidence or stop/continue decision?

OC — Operational / Execution Control
     How is an authorized concrete operation executed, observed, retried,
     contained, rolled back or failed safely?
```

This does **not** assert four software components.

They may be views, policies, capabilities, human decisions, runtime functions or combinations.

---

## 3.5 Direction of information and authority

### Downward

```text
Purpose / values / rights
→ Strategy constraints and priorities
→ Portfolio allocations / initiative mandate
→ Episode purpose / scope / resource envelope
→ Authorized operations
```

### Upward

```text
Execution evidence / failure
→ Episode learning
→ Initiative outcome / capability evidence
→ Portfolio reallocation signal
→ Strategic belief / position / capability update
```

### Cross-level authority invariant

Evidence may travel upward without automatically carrying authority.

```text
local result may challenge strategy
≠ local result changes strategy

Work Engine may propose portfolio reallocation
≠ Work Engine reallocates portfolio

portfolio result may reveal emergent strategy
≠ resource drift is automatically legitimate strategy
```

---

# 4. Implication for the “Work Engine” hypothesis

The Work Engine concept becomes **narrower and more defensible** after Q1–Q3.

If the term survives, its likely scope is closest to **WC — Work / Episode Control**:

> select and coordinate the minimum sufficient next work for the current admitted episode, given current state, purpose, constraints, capability, evidence, authority and resource envelope.

It should probably **consult but not own**:

- strategic state;
- portfolio/initiative state;
- durable organizational governance;
- authoritative domain state;
- ultimate human/institutional purpose or commitment authority.

This is a hypothesis for later architecture comparison, not yet a component decision.

---

# 5. Implication for Operating Model references

Operating Models are now easier to place.

They do not need to become the root SoI or another control level.

Likely role:

> describe/configure how SC, PC, WC, OC, capabilities, roles, platforms, information and governance are arranged for a particular persistent personal/organizational context.

Thus:

```text
Reference Architecture
    constrains permissible system designs

Operating Model
    configures how one context operates

Work Engine / WC candidate
    controls bounded episode-level work

Runtime
    realizes selected functions on technical surfaces
```

These are different artifact/system roles.

---

# 6. Remaining counterarguments

## CA-1 — Nested semantics may become too complex

A single flexible Work Object could theoretically carry scale metadata rather than typed F0–F4 units.

**Test later:** can one object preserve distinct state/authority/resource/outcome semantics without conditional-field explosion or category error?

## CA-2 — Strategy may be irrelevant to general professional work

Many tasks have no strategy content.

**Response:** R16/SC is not globally activated; it matters only where current work is a bet/initiative/position/resource commitment or where portfolio/strategic coherence changes whether work should proceed.

## CA-3 — Portfolio may be personal productivity dressed as management science

Portfolio semantics may overfit organizational PM practice.

**Test later:** compare personal multi-project/initiative cases against ISO/portfolio constructs and simpler attention/WIP control; retain only mechanisms that survive transfer.

## CA-4 — Sociotechnical SoI may dilute product engineering

A large SoI can make every defect appear “systemic.”

**Response:** nested SoI-E preserves concrete technical ownership and V&V; the broader SoI-P is only used for claims that genuinely depend on human/work context.

---

# 7. Stage-1 synthesis decisions

| Question | Decision | Confidence | Remaining test |
|---|---|---:|---|
| Q1 SoI boundary | **Nested claim-relative SoIs (H-C)** | Medium-high | test on real cases + authority/security trace |
| Q2 Focal units | **Typed nested units (U-C)** | Medium-high | test minimum unit set / Programme subtype |
| Q3 Control levels | **Coupled multi-level control (C-C)** | High | test whether WC can remain small and strategy/portfolio stay latent |

These are **pre-architecture synthesis candidates**, not frozen architecture decisions.

---

# 8. Next synthesis stage

Proceed to:

```text
Q4 Human/joint cognition & capability formation
Q5 State / knowledge / persistence
Q6 Authority / action / control
```

Then:

```text
Q7 Work Product → use → outcome/value performance
Q8 Local/global economics & proportionality
```

Only after Q1–Q8 are reconciled should the project derive `CONCERNS-AND-REQUIREMENTS v0.1`.
