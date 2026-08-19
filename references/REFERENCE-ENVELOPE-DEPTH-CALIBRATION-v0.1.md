# Reference Envelope & Depth Calibration v0.1

**Status:** PRE-SYNTHESIS CALIBRATION / WORKING DECISION RECORD  
**Date:** 2026-08-19  
**Target:** Reference Map v0.3 and provisional System of Interest  
**Purpose:** Bound what the Reference Map is a map *of*, distinguish neighboring system classes, and prevent both reference sprawl and asymmetric over-depth before Cross-Reference Synthesis & Discrimination.

---

# 1. Problem

Reference Map v0.3 is intentionally broad. Broad coverage is useful only if the map remains tied to a clear object of inquiry.

Two failure modes are now material:

1. **reference sprawl** — every adjacent management, technology, organizational or personal-productivity field becomes a peer Reference Family because it contains something useful;
2. **depth distortion** — some families are researched to architecture-level depth while others are represented by labels, creating accidental weighting before synthesis.

The required calibration question is therefore:

> What external knowledge must be understood deeply enough to architect a general Human–AI Work System, what adjacent knowledge is conditionally useful for configuring or institutionalizing such a system, and what should remain environment/domain-specific until a concrete use case requires it?

This artifact does not decide the final System-of-Interest boundary.

---

# 2. Candidate object of inquiry

The current reference program is centered on a candidate **Human–AI Work System**:

> a system in which humans, AI capabilities, tools, information/state mechanisms and existing social/organizational processes are selectively composed to perform purpose-directed real work across heterogeneous tasks and scales.

The reference program must remain valid while the foundation still compares at least two SoI boundary hypotheses:

- **A — sociotechnical joint work system:** relevant humans are inside the SoI;
- **B — engineered AI work-support system:** the designed support system is the SoI and humans sit in the operational environment through explicit interfaces.

Reference work may introduce another serious boundary hypothesis, but should not silently decide A vs B through vocabulary imported from one discipline.

---

# 3. Critical non-equivalences

The following neighboring concepts are relevant but not interchangeable.

```text
Human–AI Work System
≠ Human–AI Operating Model
≠ Management System
≠ Enterprise / Business Architecture
≠ Workflow / Case / Process Model
≠ AI Agent System
≠ AI "Operating System" / Workspace Platform
```

## 3.1 Human–AI Work System

**Question:** What configuration actually performs the work and produces effects?

Possible contents depend on SoI boundary: humans, AI, tools, work objects, state, roles, authority, interfaces and surrounding processes.

This remains the primary candidate entity being investigated.

## 3.2 Human–AI Operating Model

**Question:** How is a particular organization/person/context configured to create value through roles, decision rights, processes, capabilities, platforms, information and metrics?

An operating model is best treated as a **configuration/realization bridge**, not as the general root class.

Relevant external anchors include MIT CISR operating-model and enterprise-architecture research, where operating models specify organizing choices such as integration/standardization and, in current AI-era work, accountabilities, processes, platforms, metrics, behavior, modularity/reuse and innovation velocity.

Potential use here:
- organizational/personal configuration profile;
- strategy-to-execution bridge;
- decision-rights and capability arrangement;
- scaling/reuse model;
- possible realization of a Human–AI Work System at a chosen scope.

## 3.3 Management System

**Question:** How does an organization establish objectives/policies, operate, monitor, evaluate, maintain and continually improve a managed concern?

ISO management-system practice defines management systems through interrelated organizational elements that establish policies/objectives and processes to achieve them. Examples relevant to this program include:

- ISO/IEC 42001 — AI management systems;
- ISO 9001 — quality management systems;
- ISO 30401 — knowledge management systems;
- ISO 56001/56002 — innovation management systems;
- integrated management-system practice.

Potential use here:
- persistence/institutionalization;
- governance and roles;
- objective → operation → evaluation → improvement loops;
- management review;
- capability sustainment;
- risk/opportunity management.

A management system should not be imported as the default everyday work-control loop.

## 3.4 Enterprise / Business Architecture

**Question:** How are strategy, capabilities, value streams, processes, organization, information and technology related across an enterprise or domain?

TOGAF / Business Architecture and MIT CISR Enterprise Architecture are relevant when the Human–AI Work System crosses organizational capabilities, shared platforms, information architectures or transformation portfolios.

Potential use here:
- capability/value-stream mapping;
- cross-domain dependency and integration;
- enterprise-scale SoI variants;
- strategy-to-capability alignment;
- platform/reuse architecture.

Enterprise Architecture is adjacent reference knowledge, not proof that the initial SoI should be an enterprise.

## 3.5 Workflow / Case / Process / Decision Management

**Question:** How is recurring or case-based operational work structured and executed?

Relevant references include BPMN, CMMN and decision-management traditions. CMMN is especially relevant to evolving knowledge-work cases where activity order is not fully predetermined.

Potential use here:
- process/case realization patterns;
- work-state/runtime alternatives;
- event/milestone semantics;
- human judgment in evolving cases.

These are realization patterns, not a universal ontology of work.

## 3.6 AI Operating System / Workspace Platform

The phrase “AI operating system” is currently used inconsistently across products, personal workflows and technical platforms.

Unless a formal reference object is specified, treat it as a **product/metaphor class**, not a stable scientific or architectural primitive.

Potential use here:
- implementation comparison;
- workspace/runtime design;
- integrated surface and capability packaging;
- personal/organizational application profile.

Do not let the label determine the SoI.

---

# 4. Reference Envelope

The reference program uses four relevance zones around the candidate SoI.

These zones are **reference-scope roles**, not architecture layers.

## E1 — Constitutive reference zone

A field belongs in E1 when its constructs can directly change how the Human–AI Work System itself must be understood, bounded, controlled or evaluated across heterogeneous professional work.

Typical v0.3 families:
- R1 Systems/Architecture;
- R2 Work/Activity;
- R3 Human/Cognitive Work;
- R4 Human–AI Interaction/Joint Performance;
- R6 Expertise/Capability Formation;
- R7 Intelligence/Decision/Metareasoning;
- R9 Knowledge/State;
- R12 Evaluation/Assurance;
- R13 Authority/Risk/Control.

E1 does **not** mean every concept belongs in the eventual runtime.

## E2 — Operating / institutionalization reference zone

A field belongs in E2 when it primarily explains how a work system is oriented, coordinated across multiple initiatives, embedded, governed, adopted, sustained or renewed over time.

Typical v0.3 families / bridge clusters:
- R5 Human goals/agency;
- R10 Organization/Economics/Institutions;
- R11 Realization/Adoption/Value;
- R16 Strategy;
- R17 Programme/Portfolio/Management Control;
- Operating Model research;
- Management Systems;
- Enterprise / Business Architecture;
- organizational learning/persistence.

E2 can become constitutive for persistent organizational variants of the SoI but may be largely irrelevant to a small bounded personal work episode.

## E3 — Technical realization / enabling-system reference zone

A field belongs in E3 when it primarily determines how required functions can be implemented or operated on current technical substrates.

Typical v0.3 families:
- R14 AI/Agents/Skills/Context;
- R15 Runtime/Reliability/Interoperability;
- workflow/process engines;
- platform documentation;
- service-management/digital-operations reference architectures.

E3 constrains feasibility but must not silently define conceptual work semantics.

## E4 — Domain / environmental reference zone

This includes knowledge that becomes material only for a configured use context:

- domain professional standards;
- law/regulation;
- sector-specific evidence and methods;
- specific markets/institutions;
- physical/robotic constraints;
- clinical/financial/public-sector controls;
- local organizational policies;
- user-specific goals, resources and relationships.

E4 is retrieved/configured when required rather than exhaustively represented in the general Reference Map.

---

# 5. Bridge-reference clusters

Some useful external bodies should be tracked without becoming new peer Reference Families.

A **Bridge Reference Cluster** is admitted when it integrates multiple existing families around a recognizable operating problem but does not provide a sufficiently distinct root object/mechanism to justify its own family.

Initial clusters:

### BRC-01 — Operating Models
Maps across R1, R10, R16, R17, R11 and sometimes R15.

### BRC-02 — Management Systems
Maps across R1, R10, R11, R12, R13, R6 and L16.

### BRC-03 — Enterprise / Business Architecture
Maps across R1, R10, R16, R17, R9 and R15.

### BRC-04 — Process / Case / Decision Management
Maps across R2, R7, R17 and R15.

### BRC-05 — Service / Digital Operating Management
Maps across R11, R13, R15, R17 and R10; activate for persistent service/operational variants rather than ordinary work by default.

### BRC-06 — Personal AI Operating-System / PKM practice
Maps primarily across R5, R9, R14, R15 and R17. Treat as application/profile evidence, not general-system authority.

Promotion test for a Bridge Cluster → Reference Family:

```text
Distinct unit of analysis
+ distinct mechanism family
+ materially different failure modes
+ can change a major SoI/architecture decision
+ cannot be represented without material loss through current families
```

Otherwise keep it as a bridge.

---

# 6. Depth calibration

Reference Families should **not** receive equal research depth.

Depth is assigned relative to a decision/claim, not as a permanent prestige ranking of disciplines.

## D0 — Map

Know the field exists; record scope, canonical terminology and why it may matter.

Use for:
- frontier watch;
- remote adjacent fields;
- domains without a current discrimination role.

## D1 — Anchor

Establish 1–3 authoritative/foundational sources, primary constructs, unit of analysis and explicit boundary.

Use when:
- a field plausibly informs a concern but no current architecture decision hinges on its internal debates.

## D2 — Conflict

Add serious alternative schools, contradictory evidence, boundary conditions and known failure modes.

Use when:
- selecting one construct could bias the system;
- evidence is mixed;
- neighboring fields answer the same question differently.

## D3 — Architecture discrimination

Trace competing mechanisms into explicit implications for SoI boundary, focal unit, required function, control, performance model or architecture alternatives.

Use when:
- a current architecture decision cannot be made responsibly without the field.

## D4 — Domain deep dive

Full specialist treatment, including domain standards/methods/evidence and configured implementation implications.

Use only when:
- a concrete domain/profile/work product requires it.

---

# 7. Depth rule for the current phase

Do **not** take all 17 families to D3 before synthesis.

The next phase should be driven by the architecture-discriminating questions.

For each question:

1. identify the 2–5 families/bridge clusters capable of changing the answer;
2. take only those to D2/D3;
3. keep supporting families at D1 unless counterevidence forces deeper work;
4. stop when additional reference depth does not create a new mechanism, countermodel, boundary condition or materially different architecture implication.

This preserves rigor without encyclopedic research.

---

# 8. Current discrimination questions and likely reference pressure

| Question | High-pressure references | Supporting / conditional |
|---|---|---|
| **Q1 SoI boundary** | R1, R2, R3, R4, R10 | BRC-01/02/03, R13 |
| **Q2 Focal units / scale** | R1, R2, R17 | R3, R10, BRC-04 |
| **Q3 Work control vs strategy vs portfolio control** | R7, R16, R17 | R2, R10, BRC-01 |
| **Q4 Human/joint cognition & capability formation** | R3, R4, R6 | R5, R12 |
| **Q5 State / knowledge / persistence** | R9, R6, R10 | BRC-02/03/06, R15, L16 |
| **Q6 Authority / action / control** | R4, R13, R10 | R15, BRC-02 |
| **Q7 Performance: work product → outcome/value** | R11, R12, R2 | R5, R10, R17 |
| **Q8 Local/global economics & proportionality** | R7, R10, R17 | R3, R5, R16, R15 |

This table is a routing hypothesis for research, not an accepted architecture map.

---

# 9. Reality-bounding tests

Before admitting or deepening a reference field, ask:

### RB-1 — Object test
What object does this field study? Is it our candidate SoI, a subsystem, an enabling system, the organization around it, or the wider environment?

### RB-2 — Decision test
Which current SoI/architecture decision can this field materially change?

### RB-3 — Mechanism test
Does it contribute a distinct mechanism rather than vocabulary for a mechanism already covered?

### RB-4 — Scale test
Does the field apply to one work episode, persistent personal work, team/organization, enterprise/platform, or only a specific sector?

### RB-5 — Transfer test
What must be true for constructs from the source domain to transfer to heterogeneous Human–AI professional work?

### RB-6 — Complexity test
What decision-quality gain justifies the additional reference/architecture complexity?

### RB-7 — Exit test
What evidence would make us stop researching this field for the current decision?

---

# 10. Depth-imbalance audit

Flag a **depth imbalance** when:

- one field has highly specified objects/processes while a competing field is represented only by labels;
- vendor/runtime references are more detailed than human/work/organizational evidence before implementation selection;
- management/strategy concepts receive architecture-level specificity before the SoI scale requires them;
- a field accumulates methods because prior artifacts already used them rather than because current decisions need them;
- reference volume is mistaken for evidentiary weight.

Repair by reducing the over-deep field to the constructs relevant to the discrimination question or bringing the material competing field to the same decision-relevant depth.

---

# 11. Current calibration verdict

## 11.1 Reference-family topology

**KEEP v0.3: 17 families.**

No new family is justified merely for:
- Operating Models;
- Management Systems;
- Enterprise/Business Architecture;
- Process/Case Management;
- Service Management;
- Personal AI Operating Systems.

Track these as Bridge Reference Clusters unless later conflict analysis demonstrates a distinct missing mechanism family.

## 11.2 Scope

The map should cover knowledge necessary to understand and architect a **general Human–AI Work System and its relevant enabling/operating context**, not become a universal map of organizations, personal life, management, AI, or software.

## 11.3 Depth

Use **question-relative depth**. Do not normalize all 17 families to the same number of papers, standards or constructs.

## 11.4 SoI status

The final SoI boundary remains OPEN. This calibration narrows the reference envelope but does not choose sociotechnical-system boundary hypothesis A or engineered-support-system hypothesis B.

---

# 12. Gate

**REFERENCE COVERAGE ENVELOPE:** QUALIFIED FOR SYNTHESIS  
**REFERENCE DEPTH POLICY:** QUALIFIED FOR SYNTHESIS  
**REFERENCE MAP v0.3:** RETAIN  
**NEW PEER FAMILIES:** NONE FROM OPERATING-MODEL REALITY CHECK  
**BRIDGE CLUSTERS:** ADMIT BRC-01…BRC-06  
**SoI BOUNDARY:** OPEN  
**WORK ENGINE:** BLOCKED

Next allowed work:

> **Cross-Reference Synthesis & Discrimination v0.1**, routed by Q1–Q8 and using the E1–E4 envelope + D0–D4 depth policy.

The first synthesis should start with Q1/Q2/Q3 because boundary, focal unit and control-level separation condition the interpretation of later references.
