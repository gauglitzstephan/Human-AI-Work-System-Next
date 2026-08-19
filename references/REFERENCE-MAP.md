# Reference Map v0.1

**Status:** WORKING MAP  
**Purpose:** Define the external knowledge coverage required before architecture decisions are promoted.

## 1. Reference-first principle

This program does not derive architecture from intuition or from the predecessor system alone.

External references are used to answer four questions:

1. **What is already known?**
2. **Which constructs or distinctions are established and why?**
3. **What failure modes and trade-offs are documented?**
4. **Under what conditions is a mechanism transferable to our System of Interest?**

A reference is evidence, not an instruction. Adoption requires fit to the problem, scope, and evidence from our own work domain.

---

## 2. Reference families

### R1 — Systems engineering and architecture description

**Questions**
- How should the System of Interest, operational environment, stakeholders, concerns, viewpoints, views, requirements, and lifecycle be distinguished?
- How should architecture descriptions avoid confusing one decomposition with the architecture itself?
- How should competing architectural alternatives be evaluated?

**Seed references**
- ISO/IEC/IEEE 42010:2022 — Architecture description.
- ISO/IEC/IEEE 15288 family / SEBoK concept-definition material — mission analysis, stakeholder needs, System of Interest, lifecycle.
- ISO/IEC/IEEE 42030:2019 — architecture evaluation framework.

**Transfer test**
Use the architectural discipline and distinctions where they reduce ambiguity; do not import heavyweight documentation or process obligations without demonstrated value.

---

### R2 — Human factors, cognitive systems engineering, and joint cognitive systems

**Questions**
- Is the correct object a tool used by a person, an AI subsystem, or a joint cognitive/work system?
- How should work allocation reflect cognitive strengths, workload, expertise, learning, coordination, and resilience?
- What creates automation bias, skill degradation, brittle handoffs, or loss of situation awareness?

**Seed search targets**
- joint cognitive systems / cognitive systems engineering;
- human supervisory control and adaptive automation;
- human factors literature on automation reliance, workload, situation awareness, and function allocation.

**Transfer test**
Prioritize mechanisms with demonstrated relevance to knowledge work and AI-mediated professional work rather than transferring safety-critical control-room practice wholesale.

---

### R3 — Human–AI collaboration and HCI

**Questions**
- When does Human+AI outperform the better standalone actor, and when does collaboration add coordination cost?
- Which forms of scaffolding improve or impair performance?
- How should human judgment, agency, authorship, reliance, and learning be represented?

**Seed references**
- Microsoft Research, *Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing* (2026).
- Recent meta-analytic and experimental Human–AI complementarity literature.

**Transfer test**
Separate augmentation, synergy, preference, trust, and actual performance. Do not equate more structured interaction with better collaboration.

---

### R4 — AI agents, workflows, and orchestration

**Questions**
- Which control patterns are effective for model-driven workflow execution?
- When should work remain deterministic, single-agent, multi-agent, or human-controlled?
- How should tools, handoffs, stopping conditions, context, and guardrails be represented?

**Seed references**
- Anthropic, *Building Effective Agents* (2024): workflows vs agents; simple composable patterns; complexity only when justified.
- OpenAI, *A Practical Guide to Building AI Agents*: model/tools/instructions, orchestration, exit conditions, human intervention, risk-sensitive tool use.
- OpenAI Agents SDK and current production guidance as implementation references, not architectural authority.

**Transfer test**
Our System of Interest may be broader than an agent. Agent architecture is therefore a candidate realization/control reference, not the default ontology of professional work.

---

### R5 — Decision science, metareasoning, and robust decision making

**Questions**
- When is additional information worth acquiring?
- How should the system decide whether to deliberate, test, stage, commit, or stop?
- How should deep uncertainty, robustness, reversibility, and optionality affect work selection?
- How should cognitive/computational effort be traded against expected improvement?

**Seed search targets**
- value of information / value of computation;
- rational metareasoning;
- robust decision making / decision making under deep uncertainty;
- real options / reversible vs irreversible commitment.

**Transfer test**
Prefer compact decision mechanisms that change actual work selection over importing full analytical methodologies into every task.

---

### R6 — Knowledge, information, memory, and state architecture

**Questions**
- What distinctions are needed among working context, authoritative records, derived views, persistent memory, references, and reusable knowledge?
- How should provenance, freshness, conflict, retrieval, and update authority be handled?
- When should knowledge be in runtime context versus retrieved just in time?

**Seed search targets**
- information architecture and provenance;
- knowledge management / organizational memory;
- data lineage and authoritative-source patterns;
- retrieval and context engineering for AI systems.

**Transfer test**
Avoid treating all information as one persistent memory layer. State ownership and authority must remain domain-specific where reality requires it.

---

### R7 — Assurance, verification, validation, and AI risk management

**Questions**
- How should claims relate to evidence and verification methods?
- What is the difference between verification, validation, evaluation, monitoring, and independent assessment?
- How should risk, human oversight, and deployment-like test conditions influence assurance?

**Seed references**
- NIST AI Risk Management Framework and AIRC material on roles, human oversight, TEVV, representative conditions, and monitoring.
- assurance-case / claims-evidence literature where applicable.
- systems/software V&V references.

**Transfer test**
Use risk-proportionate assurance. Do not impose safety-case formality on low-consequence work, but preserve the semantic distinction between a claim and the evidence that licenses it.

---

### R8 — Professional work, organization design, coordination, and socio-technical systems

**Questions**
- What makes professional work different from isolated task completion?
- How do specialization, coordination, handoffs, incentives, acceptance, and organizational authority affect performance?
- When is an existing process superior to AI mediation?

**Seed search targets**
- socio-technical systems;
- organization design / coordination theory;
- knowledge work and expertise;
- workflow and operations management.

**Transfer test**
Retain organizational mechanisms only when they explain real work performance rather than adding managerial vocabulary.

---

### R9 — Software/system runtime architecture and observability

**Questions**
- How should abstract work-control mechanisms be realized across prompts, code, tools, agents, event systems, and persistent state?
- Which responsibilities require deterministic enforcement?
- How should observability, recovery, rollback, versioning, and failure containment work?

**Seed search targets**
- workflow engines and durable execution;
- distributed systems reliability;
- policy enforcement / authorization;
- observability and event/state-machine design.

**Transfer test**
Keep implementation concerns separate from conceptual work semantics until a concrete realization claim requires them.

---

## 3. Reference record schema

Every reference promoted into the knowledge base should record:

```text
Reference ID
Source / authors / organization
Date / version / freshness
Reference family
Question it informs
Relevant claim(s)
Mechanism / construct
Evidence type and scope
Boundary conditions
Known limitations / conflicts
Transferability to our System of Interest
Implication, if any
Status: DISCOVERED | REVIEWED | SYNTHESIZED | USED
```

## 4. Coverage rule

Architecture work should not proceed merely because one relevant discipline has a plausible answer. Before a major architectural commitment, check whether another reference family contains a materially different perspective on the same concern.

Examples:
- agent orchestration must be checked against human factors and decision science;
- state/memory proposals must be checked against information architecture and authoritative-domain ownership;
- human review proposals must be checked against actual human detection capability and Human–AI performance evidence.

## 5. Current gap

This map is intentionally incomplete. The next reference work should identify the strongest current sources inside each family, extract constructs and conflicts, and produce a **cross-reference synthesis by architectural concern**, not nine isolated literature summaries.
