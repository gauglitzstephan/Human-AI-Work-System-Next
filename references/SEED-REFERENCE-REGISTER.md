# Seed Reference Register v0.1

**Status:** VERIFIED SEED SET  
**Checked:** 2026-08-19

This is a starting register, not a completed literature review. Each source is included because it informs a bootstrap concern; none is architectural authority for this project.

## REF-001 — ISO/IEC/IEEE 42010:2022

- **Family:** Systems engineering / architecture description
- **Source:** ISO
- **URL:** https://www.iso.org/standard/74393.html
- **Current status:** Published, Edition 2 (2022)
- **Relevant scope:** architecture descriptions, entities of interest, viewpoints, views, model kinds, architecture-description frameworks.
- **Bootstrap implication:** distinguish the architecture of the entity from its description; use concerns/viewpoints rather than assuming one decomposition is the architecture.
- **Transfer caveat:** the standard does not prescribe our architecting method, runtime design, or System of Interest.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-002 — SEBoK: System Concept Definition

- **Family:** Systems engineering / concept definition
- **Source:** Systems Engineering Body of Knowledge (SEBoK)
- **URL:** https://sebokwiki.org/wiki/System_Concept_Definition
- **Current status:** SEBoK v2.14 material available in 2026
- **Relevant scope:** problem space, business/mission analysis, stakeholder needs, measures of success, lifecycle concepts, System of Interest before detailed solution definition.
- **Bootstrap implication:** clarify why/what and stakeholder needs before freezing how; problem and solution exploration may iterate but should remain distinguishable.
- **Transfer caveat:** SEBoK is broad systems-engineering guidance; documentation/process weight must remain proportional to this project's needs.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-003 — NIST AI Risk Management Framework Core

- **Family:** Assurance / AI risk / Human–AI roles
- **Source:** NIST AI Resource Center
- **URL:** https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- **Relevant scope:** lifecycle risk management, human-AI roles/responsibilities, targeted scope, human oversight, TEVV, representative deployment conditions, monitoring.
- **Bootstrap implication:** keep role/authority/oversight and evaluation claims explicit; evaluate systems under conditions sufficiently similar to intended use for the claim being made.
- **Transfer caveat:** this project is not automatically a regulated or high-risk AI deployment; controls must be risk-proportionate.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-004 — Anthropic: Building Effective Agents

- **Family:** AI agents / orchestration
- **Source:** Anthropic Engineering
- **URL:** https://www.anthropic.com/engineering/building-effective-agents
- **Published:** 2024-12-19
- **Relevant scope:** workflows vs agents, orchestration patterns, tool-using systems, complexity management.
- **Bootstrap implication:** prefer simple composable patterns; add agentic complexity when it measurably improves the use case rather than because a framework makes it available.
- **Transfer caveat:** our System of Interest may be broader than an AI agent; this is primarily a realization/control reference.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-005 — OpenAI: A Practical Guide to Building AI Agents

- **Family:** AI agents / runtime realization
- **Source:** OpenAI
- **URL:** https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- **Relevant scope:** model/tools/instructions, workflow execution, single vs multi-agent orchestration, exit conditions, tool risk, guardrails, human intervention, baselines and evals.
- **Bootstrap implication:** distinguish model-driven workflow control from simpler LLM use; keep orchestration incremental; treat stopping, tool access, and handoff as explicit runtime concerns.
- **Transfer caveat:** vendor guidance and product architecture are not a neutral ontology of professional work.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-006 — Microsoft Research: Scaffolding Human-AI Collaboration

- **Family:** Human–AI collaboration / HCI
- **Source:** Microsoft Research
- **URL:** https://www.microsoft.com/en-us/research/publication/human-ai-collaboration-field-experiment/
- **Published:** 2026-04
- **Evidence type:** field experiment / preprint, 388 employees at a Fortune 500 retailer
- **Relevant scope:** structured behavioral protocols and cognitive reframing around Human–AI collaboration.
- **Reported finding relevant here:** more explicit collaboration structure was not automatically better; one structured protocol was associated with lower document quality and substantially lower production relative to unstructured use, subject to stated design limitations.
- **Bootstrap implication:** do not equate visible process/scaffolding with effective Human–AI work; structure must earn its cost behaviorally.
- **Transfer caveat:** one field setting and task family; do not generalize effect sizes beyond scope.
- **Register status:** REVIEWED FOR BOOTSTRAP

---

## Next reference work

The seed set is intentionally architecture-heavy. The next sweep must strengthen undercovered reference families before conceptual architecture is frozen, especially:

1. cognitive systems engineering / joint cognitive systems;
2. human expertise, naturalistic decision making, and reflective professional practice;
3. Human–AI complementarity / comparative performance;
4. metareasoning, value of information/computation, robust decision making, and commitment under uncertainty;
5. knowledge/state/provenance architecture;
6. organization design, coordination, and socio-technical work systems;
7. runtime reliability, durable workflow, observability, recovery, and authorization.

The deliverable should be a **cross-reference synthesis by concern and mechanism**, not a collection of standalone summaries.
