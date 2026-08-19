# Seed Reference Register v0.3

**Status:** VERIFIED BOOTSTRAP ANCHORS / NOT COMPLETE LITERATURE BASE  
**Checked:** 2026-08-19  
**Reference Map:** `REFERENCE-MAP.md` v0.3

This register contains sources already checked closely enough to support bootstrap/reference-map decisions. It is not intended to give equal numerical coverage to every family.

---

## R1 — Systems / Architecture

### REF-001 — ISO/IEC/IEEE 42010:2022
- Source: ISO
- URL: https://www.iso.org/standard/74393.html
- Scope: architecture descriptions, entity of interest, stakeholders/concerns, viewpoints/views/model kinds.
- Use here: prevents one decomposition from being mistaken for the architecture itself.
- Status: REVIEWED FOR BOOTSTRAP

### REF-002 — SEBoK: System Concept Definition
- Source: SEBoK
- URL: https://sebokwiki.org/wiki/System_Concept_Definition
- Scope: problem space, mission analysis, stakeholder needs, measures of success, System of Interest before detailed solution definition.
- Use here: supports pre-architecture SoI and need qualification.
- Status: REVIEWED FOR BOOTSTRAP

---

## R4 — Human–AI Interaction / Joint Performance

### REF-003 — Microsoft Research: Scaffolding Human-AI Collaboration
- Source: Microsoft Research
- URL: https://www.microsoft.com/en-us/research/publication/human-ai-collaboration-field-experiment/
- Published: 2026
- Evidence: field experiment / preprint, 388 employees in one Fortune 500 retailer setting.
- Use here: explicit collaboration structure is not automatically beneficial; interaction/process overhead must earn its cost behaviorally.
- Boundary: do not generalize effect sizes beyond the setting.
- Status: REVIEWED FOR BOOTSTRAP

---

## R7 — Intelligence / Decision / Foresight

### REF-004 — ISO 56006:2021
- Title: Innovation management — Tools and methods for strategic intelligence management — Guidance
- URL: https://www.iso.org/standard/72621.html
- Scope: strategic intelligence management in an innovation-management setting.
- Use here: evidence that strategic intelligence is an established organizational practice linked to decision support.
- Boundary: innovation-management scope does not define a universal Human–AI intelligence subsystem.
- Status: REVIEWED FOR R7 PLACEMENT

### REF-005 — ODNI / ICD 203 Analytic Standards
- Official overview: https://www.dni.gov/index.php/ic-legal-reference-book/123-about
- Scope: analytic objectivity, source credibility, uncertainty, distinction between information/assumptions/judgments, alternatives, customer relevance, argumentation, changed judgments and evaluation.
- Use here: establishes intelligence-analysis tradecraft as a mature decision-support reference.
- Boundary: intelligence analysis informs decisions; the Intelligence Community explicitly distinguishes analysis from policy recommendation.
- Status: REVIEWED FOR R7 PLACEMENT

---

## R12 / R13 — Assurance / Governance / Risk

### REF-006 — NIST AI Risk Management Framework Core
- Source: NIST AI Resource Center
- URL: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- Scope: lifecycle risk management, roles/responsibilities, human oversight, TEVV, representative conditions, monitoring.
- Use here: keeps assurance claim-bound and use-context-sensitive.
- Boundary: do not import high-risk governance ceremony into low-consequence work by default.
- Status: REVIEWED FOR BOOTSTRAP

---

## R14 — Agents / Workflows / AI Capability Engineering

### REF-007 — Anthropic: Building Effective Agents
- URL: https://www.anthropic.com/engineering/building-effective-agents
- Published: 2024-12-19
- Scope: workflows vs agents, composable orchestration patterns, complexity management.
- Use here: simplest sufficient architecture; agentic complexity must improve the use case.
- Boundary: implementation/control reference, not a professional-work ontology.
- Status: REVIEWED FOR BOOTSTRAP

### REF-008 — OpenAI: A Practical Guide to Building AI Agents
- URL: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- Scope: model/tools/instructions, orchestration, exit conditions, guardrails, human intervention, evals.
- Use here: current agent-runtime design evidence.
- Boundary: vendor/product guidance is not neutral architecture authority.
- Status: REVIEWED FOR BOOTSTRAP

---

## R16 — Strategic Management / Strategy Formation / Renewal

### REF-009 — Mintzberg & Waters (1985), Of strategies, deliberate and emergent
- Source: Strategic Management Journal
- DOI: https://doi.org/10.1002/smj.4250060306
- Evidence type: foundational conceptual/empirical strategy-process work.
- Relevant claim: deliberate and emergent strategies are ends of a continuum; realized strategy is not reducible to prior explicit plan.
- Use here: separates strategy over time from a single local decision.
- Status: REVIEWED FOR R16 PROMOTION

### REF-010 — Noda & Bower (1996), Strategy making as iterated processes of resource allocation
- Source: Strategic Management Journal
- DOI: https://doi.org/10.1002/smj.4250171011
- Evidence type: field-based study.
- Relevant claim: strategic commitment can emerge through iterations of resource allocation influenced by strategic context and early business-development results.
- Use here: connects strategy formation, initiatives, feedback and resource commitment while preserving their distinct roles.
- Status: REVIEWED FOR R16/R17 BOUNDARY

### REF-011 — Teece, Pisano & Shuen (1997), Dynamic capabilities and strategic management
- Source: Strategic Management Journal
- DOI: https://doi.org/10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z
- Relevant claim: under rapid change, competitive advantage depends on coordination/reconfiguration processes, asset positions and path dependencies.
- Use here: strategy includes capability configuration/renewal and path dependence, not only choice among current alternatives.
- Status: REVIEWED FOR R16 PROMOTION

---

## R17 — Project / Programme / Portfolio / Initiative / Management Control

### REF-012 — ISO 21500:2021
- Title: Project, programme and portfolio management — Context and concepts
- URL: https://www.iso.org/standard/75704.html
- Use here: formal evidence that project, programme and portfolio are distinct management concepts within a shared organizational context.
- Status: REVIEWED FOR R17 PROMOTION

### REF-013 — ISO 21503:2022
- Title: Guidance on programme management
- URL: https://www.iso.org/standard/82868.html
- Use here: programme management has its own concepts, prerequisites, practices, roles and responsibilities.
- Status: REVIEWED FOR R17 PROMOTION

### REF-014 — ISO 21504:2022
- Title: Guidance on portfolio management
- URL: https://www.iso.org/standard/82867.html
- Use here: project/programme portfolio management is a distinct management object and is not identical to project/programme management.
- Status: REVIEWED FOR R17 PROMOTION

### REF-015 — ISO 21505:2017
- Title: Guidance on governance
- URL: https://www.iso.org/standard/63578.html
- Use here: distinguishes governance of projects/programmes/portfolios as an executive concern.
- Status: REVIEWED FOR R17 PROMOTION

### REF-016 — ISO 21513:2026
- Title: Guidance on post-project and post-programme evaluation
- URL: https://www.iso.org/standard/63585.html
- Use here: post-completion evaluation includes objectives, actual outcomes, benefit realization and governance/management effectiveness.
- Status: REVIEWED FOR R17 / R11 BOUNDARY

### REF-017 — Malmi & Brown (2008), Management control systems as a package
- Source: Management Accounting Research
- DOI: https://doi.org/10.1016/j.mar.2008.09.003
- Relevant claim: management control includes planning, cybernetic, reward/compensation, administrative and cultural controls, and is distinguishable from decision making.
- Use here: multi-work operating control is not exhausted by local decision analysis.
- Status: REVIEWED FOR R17 PROMOTION

---

## L16 — Organizational Persistence / Institutionalization anchors

### REF-018 — Crossan, Lane & White (1999), An Organizational Learning Framework: From Intuition to Institution
- Source: Academy of Management Review
- DOI: https://doi.org/10.5465/amr.1999.2202135
- Relevant claim: organizational learning links individual, group and organizational levels through intuiting, interpreting, integrating and institutionalizing.
- Use here: institutionalization is distinct from individual learning or information storage.
- Status: REVIEWED FOR L16 PROMOTION

### REF-019 — Argote, Lee & Park (2020), Organizational Learning Processes and Outcomes
- Source: Management Science
- DOI: https://doi.org/10.1287/mnsc.2020.3693
- Relevant claim: organizational learning can be separated into search, knowledge creation, knowledge retention and knowledge transfer.
- Use here: retention and transfer need separate mechanisms from creation.
- Status: REVIEWED FOR L16 PROMOTION

### REF-020 — Cohen & Bacdayan (1994), Organizational Routines Are Stored as Procedural Memory
- Source: Organization Science
- DOI: https://doi.org/10.1287/orsc.5.4.554
- Evidence: laboratory study.
- Use here: organizational routines can embody procedural memory distributed in action, not merely explicit documents.
- Status: REVIEWED FOR L16 PROMOTION

### REF-021 — Pentland, Hærem & Hillison (2011), The (N)Ever-Changing World
- Source: Organization Science
- DOI: https://doi.org/10.1287/orsc.1110.0624
- Evidence: empirical multi-organization study of routine stability/change.
- Use here: persistence must preserve adaptability; routine does not mean static frozen procedure.
- Status: REVIEWED FOR L16 PROMOTION

### REF-022 — ISO 30401:2018 Knowledge management systems — Requirements
- URL: https://www.iso.org/standard/68683.html
- Use here: organizational knowledge can be governed through a management-system concern.
- Freshness caveat: a DIS revision is in progress to replace the 2018 edition; do not treat the current text as a permanent design recipe.
- Status: REVIEWED AS SUPPORTING L16/R9 REFERENCE

---

# Next verification frontier

The register is now strong enough for Reference Map v0.3 coverage decisions, but not for architecture derivation.

Highest-priority remaining external synthesis:

1. R2 — Work System / Activity / Socio-technical / Adaptive Case conflicts;
2. R3 — Cognitive Work / Human Factors transfer into professional knowledge work;
3. R4 — comparative Human-only / AI-only / Human–AI performance and mixed initiative;
4. R6 — expertise formation, deskilling and Human review competence;
5. R7 — metareasoning / value-of-information / robustness beyond intelligence anchors;
6. R9 — provenance, authoritative state, memory and context architecture;
7. R10 — economics, power, ownership, adoption;
8. R11 — implementation, adoption, benefits and outcome realization;
9. R12/R13 — assurance independence, security/privacy/resilience proportionality;
10. R15 — durable execution, cross-surface state and runtime reliability.

Do not write ten independent literature reviews. Synthesize by decision-relevant concern and conflict.
