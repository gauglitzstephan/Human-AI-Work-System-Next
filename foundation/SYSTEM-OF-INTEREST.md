# System of Interest — Foundation v0.1

**Status:** PROVISIONAL / PRE-ARCHITECTURE  
**Purpose:** Establish the problem space and decision boundaries before committing to an architecture.

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

The boundary is **not yet decided**. At least two serious alternatives must be evaluated.

### Boundary hypothesis A — socio-technical joint work system

The System of Interest includes the relevant human actor(s), AI work-control mechanisms, AI models/agents as configured for the work, capability access, state/knowledge interfaces, and tool/process interfaces required to perform the work.

**Implication:** human cognition, agency, authority, and learning are first-class system properties rather than external usage concerns.

### Boundary hypothesis B — AI work-support system

The System of Interest is the designed AI-mediated work-support system. Human actors, organizations, and many external processes sit in the operational environment and interact with it through defined interfaces and authority boundaries.

**Implication:** human outcomes and agency remain critical stakeholder concerns, but the architecture can distinguish the engineered support system from the wider joint cognitive system.

### Boundary decision test

The selected boundary should make responsibility, state ownership, authority, performance attribution, lifecycle management, and evaluation clearer rather than merely producing a more elegant diagram.

Other boundary hypotheses may emerge from reference work.

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

## 8. Candidate units of concern

A major unresolved question is the unit at which the system controls work. Possible units include:

- interaction / turn;
- task;
- work item;
- work product;
- decision;
- workflow / case;
- project;
- persistent operational process.

The system may require **multiple nested units** rather than a single universal unit. A core architecture must not silently transfer state or completion semantics from one level to another.

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
- in-lab task performance from in-use performance.

Potential measures may include outcome quality, critical error rate, rework, human correction burden, elapsed work, turns/tokens/tool calls, state-recovery success, false-completion rate, transition success, human learning/agency measures, and robustness under changed conditions.

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

---

## 11. Explicit non-decisions

At Foundation v0.1 we do **not** assume:

- that a `Work Engine` is a subsystem rather than a control viewpoint or policy;
- that `Capabilities` form a peer subsystem to any engine;
- that `Environment` is an architectural component rather than operational context;
- that DWM, Semantic Compiler, Work Graph, Realization, Prospective Robustness, or predecessor lifecycle stages retain their prior form;
- that the best implementation is a prompt, Custom Instructions, skills, an agent graph, a multi-agent system, deterministic orchestration, or any particular platform;
- that one architecture can be represented adequately by one hierarchy.

---

## 12. Next qualification gates

Before freezing a conceptual architecture:

1. complete a bounded but serious reference sweep across the relevant disciplines;
2. harvest the predecessor architecture and high-information real work evidence with provenance;
3. derive and reconcile stakeholder concerns and candidate requirements;
4. compare alternative SoI boundaries and units of concern;
5. define an initial performance model sufficient to discriminate architectural alternatives;
6. only then define architecture viewpoints and candidate conceptual structures.
