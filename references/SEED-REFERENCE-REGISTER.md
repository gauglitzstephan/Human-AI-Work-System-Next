# Seed Reference Register v0.2

**Status:** VERIFIED BOOTSTRAP SEED SET / MATERIAL COVERAGE STILL OPEN  
**Checked:** 2026-08-19  
**Reference Map:** `REFERENCE-MAP.md` v0.2

This is a starting register, not a completed literature review. Each source is included because it informs a bootstrap concern; none is architectural authority for this project.

The Reference Map coverage audit substantially widened the research surface. This register therefore distinguishes **already verified bootstrap anchors** from the **next external-verification frontier** instead of pretending the current six sources cover v0.2.

---

## REF-001 — ISO/IEC/IEEE 42010:2022

- **Family:** R1 — Systems Engineering, Architecture, Requirements & Lifecycle
- **Source:** ISO
- **URL:** https://www.iso.org/standard/74393.html
- **Current status:** Published, Edition 2 (2022)
- **Relevant scope:** architecture descriptions, entities of interest, viewpoints, views, model kinds, architecture-description frameworks.
- **Bootstrap implication:** distinguish the architecture of the entity from its description; use concerns/viewpoints rather than assuming one decomposition is the architecture.
- **Transfer caveat:** the standard does not prescribe our architecting method, runtime design, or System of Interest.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-002 — SEBoK: System Concept Definition

- **Family:** R1 — Systems Engineering, Architecture, Requirements & Lifecycle
- **Source:** Systems Engineering Body of Knowledge (SEBoK)
- **URL:** https://sebokwiki.org/wiki/System_Concept_Definition
- **Current status:** SEBoK material current in 2026
- **Relevant scope:** problem space, business/mission analysis, stakeholder needs, measures of success, lifecycle concepts, System of Interest before detailed solution definition.
- **Bootstrap implication:** clarify why/what and stakeholder needs before freezing how; problem and solution exploration may iterate but should remain distinguishable.
- **Transfer caveat:** SEBoK is broad systems-engineering guidance; documentation/process weight must remain proportional to this project's needs.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-003 — NIST AI Risk Management Framework Core

- **Families:** R12 / R13 — Evaluation & Assurance / Governance, Risk & Control
- **Source:** NIST AI Resource Center
- **URL:** https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- **Relevant scope:** lifecycle risk management, human-AI roles/responsibilities, targeted scope, human oversight, TEVV, representative deployment conditions, monitoring.
- **Bootstrap implication:** keep role/authority/oversight and evaluation claims explicit; evaluate systems under conditions sufficiently similar to intended use for the claim being made.
- **Transfer caveat:** this project is not automatically a regulated or high-risk AI deployment; controls must be risk-proportionate.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-004 — Anthropic: Building Effective Agents

- **Family:** R14 — AI/ML, Agents, Workflows, Context & Reusable Capability Engineering
- **Source:** Anthropic Engineering
- **URL:** https://www.anthropic.com/engineering/building-effective-agents
- **Published:** 2024-12-19
- **Relevant scope:** workflows vs agents, orchestration patterns, tool-using systems, complexity management.
- **Bootstrap implication:** prefer simple composable patterns; add agentic complexity when it measurably improves the use case rather than because a framework makes it available.
- **Transfer caveat:** our System of Interest may be broader than an AI agent; this is primarily a realization/control reference.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-005 — OpenAI: A Practical Guide to Building AI Agents

- **Family:** R14 — AI/ML, Agents, Workflows, Context & Reusable Capability Engineering
- **Source:** OpenAI
- **URL:** https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- **Relevant scope:** model/tools/instructions, workflow execution, single vs multi-agent orchestration, exit conditions, tool risk, guardrails, human intervention, baselines and evals.
- **Bootstrap implication:** distinguish model-driven workflow control from simpler LLM use; keep orchestration incremental; treat stopping, tool access, and handoff as explicit runtime concerns.
- **Transfer caveat:** vendor guidance and product architecture are not a neutral ontology of professional work.
- **Register status:** REVIEWED FOR BOOTSTRAP

## REF-006 — Microsoft Research: Scaffolding Human-AI Collaboration

- **Family:** R4 — HCI, Human–AI Interaction, Mixed Initiative & Joint Performance
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

# Next external-verification frontier

Reference Map v0.2 contains fifteen families. The six sources above are intentionally insufficient to cover them.

The next sweep should prioritize **discriminating evidence**, not equal coverage by page count.

## Priority A — can change the System-of-Interest boundary or work-control model

1. **R2 Work / Activity / Sociotechnical Systems**
   - Work System Theory;
   - Activity Theory / practice traditions;
   - sociotechnical work design;
   - adaptive case work / OMG CMMN.

2. **R3 Cognitive Work / Human Factors**
   - Human Systems Integration;
   - Cognitive Systems Engineering / Cognitive Work Analysis;
   - Joint Cognitive Systems;
   - Distributed Cognition.

3. **R4 Human–AI Joint Performance**
   - systematic/meta-analytic Human–AI complementarity evidence;
   - mixed initiative / coactive design;
   - common ground / appropriate reliance.

4. **R6 Expertise / Learning / Capability Formation**
   - adaptive expertise;
   - professional/tacit knowledge;
   - workplace learning and reflective practice;
   - deskilling / cognitive offloading / AI-assisted learning.

5. **R7 Decision / Sensemaking / Metareasoning**
   - Naturalistic Decision Making / macrocognition;
   - value of information / value of computation;
   - robust decision making / deep uncertainty;
   - real options / staged commitment.

6. **R9 Knowledge / Provenance / State**
   - knowledge management and organizational memory;
   - provenance / data lineage / authoritative-record patterns;
   - information architecture / context engineering;
   - AI memory research with freshness and authority boundaries.

7. **R10 Organization / Economics / Power / Ownership**
   - coordination / transaction-cost / principal-agent theory;
   - decision rights and organizational design;
   - platform/institutional economics;
   - technical capability vs diffusion/adoption;
   - ownership / complementary assets / value capture.

8. **R11 Realization / Adoption / Outcomes**
   - implementation science / technology adoption;
   - behavior change / organizational change;
   - benefits realization / outcome chains / externalities.

## Priority B — can change qualification, risk and implementation boundaries

9. **R12 Evaluation / Assurance**
   - NIST TEVV;
   - OMG SACM / structured assurance;
   - representative-use evaluation;
   - causal inference / impact evaluation;
   - AI eval methodology and independence.

10. **R13 Security / Privacy / Resilience / Rights**
    - threat modeling / secure development;
    - prompt-injection and excessive-agency threats;
    - privacy engineering / data governance;
    - resilience / fallback / meaningful human control / contestability.

11. **R15 Runtime Reliability / Interoperability**
    - durable execution / distributed systems;
    - versioning / configuration management;
    - observability / SRE / recovery;
    - authorization and cross-surface state contracts.

## Priority C — important but less likely to set the initial boundary alone

12. **R5 Human Goals / Motivation / Wellbeing**
13. **R8 Design / Creativity / Collective Intelligence**
14. **R14 Current AI/Agent/Skill/Context Engineering** — maintain freshness continuously; do not over-weight vendors.

R1 already has a credible bootstrap anchor set but will require additional requirements/quality-attribute sources during architecture evaluation.

---

# Separate current-product register

Current ChatGPT/Codex product capabilities are tracked as a **frontier-use / realization stress test**, not as neutral scientific references. See:

- `FRONTIER-USER-CHALLENGE-v0.1.md`

This prevents fast-changing product surfaces from silently dominating the general Reference Map.

---

# Synthesis deliverable

Do **not** produce fifteen isolated literature summaries.

Build a concern-driven synthesis such as:

```text
Concern / decision
→ candidate mechanism(s)
→ relevant reference families
→ strongest evidence
→ incompatible assumptions / counterevidence
→ unit of analysis
→ transfer conditions to our SoI
→ internal evidence comparison
→ architecture implication or NO IMPLICATION YET
```

The first synthesis should focus on the concerns that can discriminate:

- SoI boundary;
- focal units / scale;
- human role and capability formation;
- work-control / initiative model;
- state/knowledge boundary;
- authority/action boundary;
- outcome/evaluation model;
- proportionality / operating economics.
