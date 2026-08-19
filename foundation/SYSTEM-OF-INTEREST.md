# System of Interest — Foundation v0.2

**Status:** PROVISIONAL / PRE-ARCHITECTURE / PARTIALLY SYNTHESIZED  
**Purpose:** Establish the problem space and decision boundaries before committing to an architecture.  
**Synthesis basis:** `REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md` + `CROSS-REFERENCE-SYNTHESIS-DISCRIMINATION-v0.1.md` Stage 1.

## 1. Why this document exists

The predecessor work contains substantial architecture, terminology, and runtime experience. The reconstruction must preserve that knowledge without allowing it to silently define the new solution.

This document therefore describes the **problem, mission, stakeholders, operational context, candidate boundaries, performance concerns, and unresolved decisions** of the entity we may ultimately call the Human–AI Work System.

It is not an architecture specification.

---

## 2. Problem statement — working hypothesis

Current general-purpose AI systems can perform many isolated cognitive and production tasks well, yet reliable professional work requires more than task competence. It requires appropriate interpretation of intent, use of current reality and authoritative state, selection and sequencing of work, composition of human and machine capabilities, evidence-sensitive qualification, controlled action, and adaptation to the receiving context and downstream use.

The problem is not simply to make an AI agent more autonomous. The broader problem is:

> **How can humans and AI systems be composed so that real professional work is performed better across heterogeneous tasks and scales, while preserving justified human agency, trustworthy state, appropriate authority, proportional complexity, and evidence-bounded claims?**

This is a hypothesis about the problem space and must be tested against references and real work evidence.

---

## 3. Mission — provisional

Develop and validate a general Human–AI Work System that can improve the quality and economics of professional work by selecting and composing the right cognitive, production, verification, coordination, and action mechanisms for the current situation.

The system should degrade gracefully from trivial work to complex, persistent, multi-actor work rather than requiring a heavyweight process everywhere.

---

## 4. Intended outcomes — candidate set

The system is intended to improve, where relevant:

1. **Outcome effectiveness** — the work contributes to the actual intended outcome rather than merely producing plausible output.
2. **Professional quality** — work products and decisions meet the requirements of their real receiving context.
3. **Reality contact** — claims, actions, and state reflect qualified evidence and authoritative sources.
4. **Work efficiency** — unnecessary cognition, coordination, tool use, rework, latency, and complexity are avoided.
5. **Human agency and authorship** — human judgment, values, learning, authority, and acceptance remain where they materially belong.
6. **Robustness and adaptability** — the system handles uncertainty, changed state, failure, and heterogeneity without brittle process inflation.
7. **Transition and use** — when real use matters, successful work extends beyond artifact production into appropriate handoff, implementation, adoption, or operation.

These are performance concerns, not yet an accepted metric model.

---

## 5. Operational context

The target domain is **professional work broadly construed**, including but not limited to:

- small bounded corrections and calculations;
- analysis and research;
- open decisions under uncertainty;
- creation or repair of professional artifacts;
- work requiring external state, files, tools, or applications;
- work distributed across humans, AI, deterministic tools, and existing processes;
- persistent operational processes;
- high-consequence or authority-sensitive actions;
- work where learning, authorship, or acceptance matters as much as immediate output.

A valid architecture must therefore explain how it handles differences in task scale, persistence, consequence, reversibility, epistemic uncertainty, authority, and receiving context without treating every task as a large project.

---

## 6. Candidate System-of-Interest boundaries

The final boundary is **not yet decided**. Stage-1 cross-reference synthesis materially changes the candidate set: a nested/claim-relative boundary is now the leading hypothesis rather than forcing one boundary to answer incompatible performance and engineering questions.

### Boundary hypothesis A — socio-technical joint work system

The System of Interest includes the relevant human actor(s), AI work-control mechanisms, AI models/agents as configured for the work, capability access, state/knowledge interfaces, and tool/process interfaces required to perform the work.

**Implication:** human cognition, agency, authority, and learning are first-class system properties rather than external usage concerns.

### Boundary hypothesis B — AI work-support system

The System of Interest is the designed AI-mediated work-support system. Human actors, organizations, and many external processes sit in the operational environment and interact with it through defined interfaces and authority boundaries.

**Implication:** human outcomes and agency remain critical stakeholder concerns, but the architecture can distinguish the engineered support system from the wider joint cognitive system.

### Boundary hypothesis C — nested / claim-relative Systems of Interest — LEADING CANDIDATE

Use explicitly related SoIs for different classes of claims:

```text
SoI-P — Human–AI Work System
        primary performance / professional-work / outcome SoI
        includes the sociotechnical configuration material to joint work

        contains / uses
             ↓

SoI-E — AI Work-Support / Control Subsystem
        nested engineered SoI for technical behavior, lifecycle,
        verification, runtime, security and implementation responsibility
```

**Rationale:** work-system and joint-cognitive references indicate that joint work performance may not be attributable to the AI component alone, while systems/software engineering, assurance and security still require a clearly bounded engineered entity.

**Non-decision:** Hypothesis C does not imply that `SoI-E` is a single Work Engine, agent, service or software component.

### Boundary decision test

The selected boundary model should make responsibility, state ownership, authority, performance attribution, lifecycle management and evaluation clearer rather than merely producing a more elegant diagram.

**Falsifier for C:** reject the nested model if it adds semantic complexity without changing any material evaluation, responsibility, architecture or lifecycle decision, or if one simpler boundary preserves the same distinctions.

---

## 7. Stakeholders and affected actors — provisional

Candidate stakeholder classes include:

- the person whose work or decision is being supported;
- collaborators and professional recipients of work products;
- people with decision, approval, or action authority;
- operators or maintainers of persistent Human–AI workflows;
- organizations whose systems, policies, or records provide authoritative state;
- people affected by downstream actions or decisions;
- developers and evaluators of the Human–AI Work System.

Stakeholders are not assumed to have aligned objectives. Conflicts among outcome quality, speed, autonomy, assurance, cost, learning, and organizational control must be representable.

---

## 8. Candidate focal units and scale

Stage-1 synthesis rejects a single universal work unit as the default. Different scales earn distinct types only when purpose, state, authority, persistence, dependencies, resource allocation, outcome horizon or opportunity cost materially change.

Leading candidate set:

```text
F0 — Interaction / Operation
     local exchange, tool invocation or concrete execution operation

F1 — Work Episode / Case
     bounded purpose-directed work with local state and exit conditions
     LEADING DEFAULT work-control focal unit

F2 — Initiative / Project / Programme
     persistent multi-episode coordinated work/change with dependencies,
     shared outcome horizon and continuation/closure semantics

F3 — Portfolio
     competing initiatives/bets sharing scarce resources and attention;
     selection, balancing, scale/pause/kill and opportunity-cost semantics

F4 — Configured Human–AI Work System
     standing arrangement through which episodes and initiatives occur
```

Compression rule:

- simple direct work must not require explicit F2/F3 machinery;
- F2 activates only when persistence/dependency/shared-outcome semantics matter;
- F3 activates only when material initiatives compete for scarce resources/attention;
- organization, market, institution and ecosystem remain environment or higher-scope SoI candidates rather than mandatory runtime units.

**Open issue:** whether `Programme` requires a distinct type or can remain a subtype/configuration of F2.

---

## 9. Performance model — open design problem

A future performance model must distinguish at least:

- output quality from outcome effectiveness;
- quality from efficiency;
- immediate task success from downstream transition/use;
- human effort from AI/tool cost;
- factual/epistemic integrity from persuasive plausibility;
- behavioral reliability from architecture elegance;
- capability from authority;
- in-lab task performance from in-use performance;
- episode-level success from initiative/portfolio contribution;
- local optimization from system/strategic coherence.

Potential measures may include outcome quality, critical error rate, rework, human correction burden, elapsed work, turns/tokens/tool calls, state-recovery success, false-completion rate, transition success, human learning/agency measures, robustness under changed conditions, WIP/resource burden and contribution to higher-level outcomes.

No metric is accepted merely because it is easy to measure.

---

## 10. Candidate architectural concerns

The following are **questions to cover**, not a declaration of final views or components:

- How is intent and the relevant work outcome reconstructed?
- How is current and authoritative state obtained, represented, and updated?
- How is the next work selected, decomposed, sequenced, stopped, or resumed?
- How are Human / AI / deterministic tool / workflow / existing process alternatives compared and allocated?
- How are domain or task capabilities discovered and applied?
- How are evidence, claims, verification, and qualification related?
- How are authority, reversibility, and consequential actions controlled?
- How are work products transitioned into real use where necessary?
- How are uncertainty, change, robustness, and optionality handled?
- How are context, knowledge, references, and persistent memory managed?
- How is system complexity kept proportional to the work?
- How is the system evaluated, learned from, versioned, rolled back, and retired?
- How is episode-level work control kept distinct from strategic direction and portfolio/initiative control?
- How can local work evidence challenge higher-level strategy/portfolio state without silently acquiring authority to change it?
- How are multiple nested focal units linked without importing project/portfolio ceremony into ordinary work?

---

## 11. Stage-1 control-level discrimination

Cross-reference synthesis currently supports a **coupled multi-level control hypothesis**:

```text
SC — Strategic Control
     directions, positions, capabilities, strategic bets and renewal

PC — Portfolio / Initiative Control
     admission, resource/attention allocation, dependencies,
     scale/pause/combine/kill

WC — Work / Episode Control
     minimum sufficient next work for an admitted episode

OC — Operational / Execution Control
     execution, observation, retry, containment, rollback, safe failure
```

This is **not a component diagram**. The domains may later be realized through human decisions, policies, views, capabilities, runtime functions or combinations.

Leading implication for the `Work Engine` hypothesis:

> if the concept survives, its defensible scope is currently closest to **WC — Work / Episode Control**, not universal strategy/portfolio ownership.

Strategy and portfolio state may constrain WC; work evidence may challenge them upward; neither direction automatically transfers authority.

---

## 12. Explicit non-decisions

At Foundation v0.2 we do **not** assume:

- that a `Work Engine` is a subsystem rather than a control viewpoint or policy;
- that `Capabilities` form a peer subsystem to any engine;
- that `Environment` is an architectural component rather than operational context;
- that SC/PC/WC/OC are software modules;
- that DWM, Semantic Compiler, Work Graph, Realization, Prospective Robustness, or predecessor lifecycle stages retain their prior form;
- that the best implementation is a prompt, Custom Instructions, skills, an agent graph, a multi-agent system, deterministic orchestration, or any particular platform;
- that one architecture can be represented adequately by one hierarchy;
- that an Operating Model, Management System, Enterprise Architecture or AI “Operating System” is identical with the Human–AI Work System.

---

## 13. Reference-envelope constraint

The external reference program is bounded by `REFERENCE-ENVELOPE-DEPTH-CALIBRATION-v0.1.md`.

Key rule:

> Research knowledge necessary to understand/architect the Human–AI Work System deeply; treat Operating Models, Management Systems, Enterprise/Business Architecture, Process/Case Management, Service Management and Personal-AI-OS practice as bridge references unless a distinct missing mechanism family is demonstrated.

Reference depth is decision-relative (D0 Map → D4 Domain Deep Dive), not equal across all families.

---

## 14. Next qualification gates

Completed/advanced:

1. bounded Reference Map coverage and Red Team;
2. first Anchor & Conflict Sweep;
3. Reference Envelope & Depth Calibration;
4. Stage-1 Cross-Reference Synthesis on Q1 SoI boundary, Q2 focal units and Q3 control levels.

Next:

5. synthesize Q4 Human/joint cognition & capability formation;
6. synthesize Q5 state / knowledge / persistence;
7. synthesize Q6 authority / action / control;
8. synthesize Q7 Work Product → use → outcome/value performance;
9. synthesize Q8 local/global economics & proportionality;
10. reconcile those results with the predecessor evidence matrix and real-work evidence;
11. derive `CONCERNS-AND-REQUIREMENTS v0.1`;
12. only then define architecture viewpoints and compare conceptual architecture alternatives.
