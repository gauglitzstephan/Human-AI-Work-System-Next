# Reference Map Coverage Audit v0.1

**Status:** COMPLETE FOR BOOTSTRAP COVERAGE / NOT A LITERATURE SYNTHESIS  
**Date:** 2026-08-19  
**Target:** `references/REFERENCE-MAP.md` v0.1 → v0.2  
**Purpose:** Test whether the initial external Reference Map covers the material concerns implied by the provisional System of Interest and by prior internal research, without importing prior architecture as truth.

---

## 1. Audit question

> Does Reference Map v0.1 expose the disciplines and challenge lenses needed to reconstruct a general Human–AI Work System, or does it hide material concerns inside overly broad families?

This audit checks **coverage**, not whether any candidate architecture is correct.

---

## 2. Evidence spaces inspected

### 2.1 ChatGPT Library

High-signal sources inspected/searched include:

- `HAWS_REFERENCE_ARCHITECTURE_v1.0.md`;
- `HASA_cross_case_validated_reference_architecture_v0_5.md`;
- `00_HASA_OVERVIEW_MAP_v1.0.md` and v1.0.1 material;
- `HASA_architecture_viewpoints_traceability_v0_4.md`;
- `P4p_RESULTS_v0.1.json`;
- `DEEP_RESEARCH_HANDOVER_HUMAN_AI_JOINT_WORK_ARCHITECTURE_v0.1.md`;
- historical CI / Joint Work artifacts where they expose missing concerns or operating failure modes.

These sources are **internal research artifacts**. They may reveal reference fields, constructs, counterexamples and prior source work; they are not external evidence merely because they contain citations.

### 2.2 Notion

High-signal pages inspected/searched include:

- `AI Work Operating System` v1.5.0;
- `AI WORKSPACE — SYSTEM ARCHITECTURE`;
- `AI WORKSPACE — TARGET ARCHITECTURE V1.1`;
- `AI Workspace OS Architecture Specification`;
- `Decision & Learning Capability Framework`;
- `Capability System Specification` and capability-taxonomy material;
- `Human Goal Model` / related personal operating-model work;
- recent instruction/Work Product/Human–AI allocation notes.

Notion contributes historical design hypotheses and lived operating concerns: intent alignment, cognitive friction, consent/data/tool boundaries, organizational memory, capability testing, human goals, learning and decision ownership.

### 2.3 Google Drive

High-signal sources inspected/searched include:

- `JAIWS_Whole_System_Architecture_and_Possibility_Topology_v0.1_CANDIDATE`;
- `Human–AI Capability Reference Model v0.3 — Accepted Working Reference`;
- `AMM-ART-001 Adaptive Socio-Technical Work Metamodel...`;
- `R0c3 Holistic Pre-Architecture Decision Viewpoint Audit`;
- repository/bootstrap/canonicalization and joint-work constitution artifacts;
- real-use application cases and operating-model pilots where relevant.

Drive material exposes previously investigated whole-system concerns including purpose/rights, reality/domain epistemics, possibility formation, capability development, decision/commitment, execution, state/continuity, effects/learning/capital, human fit, security, time/capacity and portability.

### 2.4 Prior ChatGPT chats / projects

Prior work was searched for reference-led Human–AI system design and repeated blind spots.

Recovered themes include:

- field-led scans before architecture design;
- intelligence analysis and analytic assurance;
- Cognitive Systems Engineering / Cognitive Work Analysis / Joint Cognitive Systems;
- Human Systems Integration;
- common ground / CSCW / Distributed Cognition;
- Mixed-Initiative Interaction, Human supervisory control and adaptive automation;
- Work System Theory and socio-technical systems;
- Naturalistic Decision Making and sensemaking;
- knowledge management, provenance and source-of-truth semantics;
- evaluation, risk, security and governance;
- economics, value chains, complementary assets and organizational design;
- repeated warnings against tool-first architecture, chat-only state, unbounded autonomy, missing evals, absent durable assets and ontology inflation.

### 2.5 Current AI-work product reality

Current official OpenAI documentation was checked as an implementation/frontier-use reference for:

- Projects and project memory;
- Apps and connected data/action surfaces;
- Deep Research and source scoping;
- Skills as reusable workflows/capabilities;
- Workspace Agents as repeatable workflow systems;
- Scheduled Tasks / monitoring;
- Codex / repo-backed execution.

These are mutable product capabilities, not architecture authority.

---

## 3. Main finding

# v0.1 was directionally sound but materially under-differentiated.

Its nine families captured the broad territory, but several material concerns were hidden inside umbrella labels such as `Human Factors`, `Professional Work`, `Knowledge`, `Assurance`, or `Runtime`.

That created two risks:

1. **false coverage** — a concern appears nominally included but has no dedicated research question or transfer boundary;
2. **architecture bias** — the dominant vocabulary of one broad family can silently define the model before competing disciplines are heard.

The correct repair is not an encyclopedic list of every discipline. It is:

```text
Reference Families
    = where relevant knowledge comes from

Coverage Lenses
    = recurring questions every material architecture concern must survive

Frontier Watchlist
    = strategically relevant but unstable fields
```

---

## 4. Material gaps found in v0.1

### G1 — Work/activity theory was buried inside `Professional Work`

Prior internal research repeatedly distinguishes work-system, activity-system, professional-practice and adaptive-case views.

Why it matters:
- prevents `workflow` or `task` from becoming the universal unit;
- exposes rules, community, division of labor, infrastructure, history and receiving context;
- supports open-ended knowledge work rather than only predetermined process control.

**Repair:** dedicated R2.

---

### G2 — Distributed cognition / common ground / mixed initiative were underweighted

Human Factors alone does not cover how cognition, initiative and shared representations are distributed across humans, AI and artifacts.

Why it matters:
- function allocation is not enough;
- coordination cost, initiative timing, common ground and repair affect joint performance;
- `Human-in-the-loop` is too coarse for many work situations.

**Repair:** distinguish R3 Cognitive Work from R4 HCI / Mixed Initiative / Joint Performance.

---

### G3 — Human goals, motivation, attention and sustainable agency were nearly absent

Notion and historical work repeatedly model human goals, values, autonomy, cognitive friction, energy/attention and overanalysis as operating constraints.

Why it matters:
- a system can improve output while degrading ownership, motivation, attention or human capability;
- individual productivity is not the complete objective function;
- visible process and review burden can itself be a system failure.

**Repair:** dedicated R5 and Lens L1/L4/L9.

---

### G4 — Expertise and capability formation were not a first-class reference field

The Drive capability model explicitly separates information access from professional competence and identifies a feedback loop:

```text
work allocation
→ human practice
→ capability formation
→ future expertise
→ future delegation/control
```

Why it matters:
- delegation can improve short-run throughput while destroying the practice path that supports future judgment;
- Human review is only valuable when the reviewer can actually detect the relevant failure;
- repeated AI success is not automatically a validated capability.

**Repair:** dedicated R6.

---

### G5 — Creativity, diversity and search-space quality were not explicit

Prior deep-research work identifies anchoring, homogenization, familiar-domain collapse, collective diversity, creative ownership and co-creativity as material Human–AI effects.

Why it matters:
- an apparently efficient work engine may systematically narrow the space of possible frames or solutions;
- independent branches / models / humans may matter specifically because errors and ideas are correlated.

**Repair:** dedicated R8 and Lens L12.

---

### G6 — Economics, power, ownership and appropriation were too weak

Organization Design in v0.1 did not expose:
- transaction/coordination costs;
- decision rights and principal–agent structure;
- ownership and residual control;
- platform dependence and switching costs;
- who captures gains and bears risk;
- diffusion/adoption versus technical capability.

Why it matters:
The System of Interest should improve the economics of work without equating technical productivity with total value or welfare.

**Repair:** dedicated R10 and Lens L9.

---

### G7 — Realization, adoption and outcome/value were missing as an external field

The provisional SoI already distinguishes output from downstream use, but v0.1 had no reference family for implementation, behavior change, adoption, change, benefits realization or externality mapping.

Why it matters:
- Work Product quality is not the same as successful transition or use;
- adoption failure may dominate artifact quality;
- observed outcomes need causal qualification.

**Repair:** dedicated R11.

---

### G8 — Security, privacy, resilience and rights were hidden inside Assurance/Runtime

The R0c3 pre-architecture audit independently found missing threat models, trust boundaries, privacy/data-governance baselines, human operations budgets and cross-surface integrity as architecture-selection blockers.

Why it matters:
- connected tools turn generated cognition into potential external effects;
- prompt injection, excessive permissions, data leakage, account compromise, immutable histories and unavailable fallback are distinct from ordinary output QA;
- authority and permission must remain distinguishable.

**Repair:** dedicated R13 plus Lens L10.

---

### G9 — Architecture quality/requirements and behavioral evaluation needed clearer separation

v0.1 grouped assurance broadly but did not sufficiently distinguish:
- architecture drivers / quality attributes;
- requirements traceability;
- review;
- verification;
- validation;
- TEVV;
- professional-quality evaluation;
- representative-use testing;
- causal attribution;
- independent assurance.

**Repair:** R1 owns architectural requirement/evaluation discipline; R12 owns measurement/qualification/evidence methods.

---

### G10 — Current AI-native work is capability-based and multi-surface, not prompt-centric

Current product reality supports:
- bounded Projects;
- connected data/action Apps;
- source-scoped Deep Research;
- reusable Skills;
- repeatable Workspace Agents;
- scheduled/monitoring Tasks;
- Codex/repository execution.

Why it matters:
The architecture must explain **capability discovery, packaging, invocation, state, handoff and promotion across surfaces**, not just instructions inside one conversation.

**Repair:** R14 + R15 and a separate Frontier-User Challenge.

---

### G11 — Platform fragmentation / cross-surface state is a genuine architecture concern

Current and prior platform work repeatedly shows that chat context, project memory, repo state, app state, scheduled tasks and external systems do not constitute one atomic or guaranteed shared state.

Why it matters:
- surface changes can silently invalidate assumptions;
- a durable system needs explicit handoff/version/provenance semantics where material;
- current product constraints must remain implementation facts rather than universal theory.

**Repair:** R9 + R15 + Lens L14.

---

## 5. What was *not* promoted to a new reference family

To prevent reference-map inflation, several important topics remain subfields or cross-cutting lenses:

- **Cybernetics / control theory** → R7/R13/R15 where relevant;
- **System dynamics / simulation / operations research** → R7;
- **Adaptive case management / CMMN** → R2;
- **structured assurance cases** → R12;
- **context engineering** → R9/R14;
- **ontology engineering** → R9;
- **meaningful human control / contestability** → R13;
- **embodiment / robotics** → conditional R3/R14/R13 + Frontier Watchlist;
- **personal knowledge management** → R9;
- **AI-native organizations / multi-agent collectives** → Frontier Watchlist until the SoI requires them.

This is intentional. A reference family must earn its own research boundary by answering a materially different class of questions.

---

## 6. Reference Map v0.2 disposition

| v0.1 family | v0.2 disposition |
|---|---|
| Systems engineering / architecture | EXPANDED → R1 |
| Human factors / cognitive systems | SPLIT → R3 + contributions to R5/R6 |
| Human–AI collaboration / HCI | EXPANDED → R4 |
| Agents / workflows / orchestration | SPLIT → R14 + R15 |
| Decision science / metareasoning / robustness | EXPANDED → R7 |
| Knowledge / information / memory / state | EXPANDED → R9 |
| Assurance / V&V / AI risk | SPLIT → R12 + R13 |
| Professional work / organization design | SPLIT → R2 + R6 + R10 + R11 |
| Runtime architecture / observability | EXPANDED → R15 |
| — | NEW R5 — Human goals / motivation / agency / wellbeing |
| — | NEW R8 — Design / creativity / collective intelligence |

---

## 7. Key epistemic warning

The internal Library/Drive corpus is unusually rich and already contains sophisticated candidate architectures. That is an advantage **and** a contamination risk.

Therefore:

```text
internal artifact says field X matters
→ use it to discover/check field X
→ retrieve external field evidence
→ reconstruct its actual constructs and boundaries
→ compare against internal hypothesis
→ only then derive architecture implication
```

Do not use an internally polished map as proof that its decomposition is correct.

---

## 8. Current gate

**REFERENCE MAP COVERAGE:** PASS FOR v0.2 WORKING BASELINE  
**REFERENCE SYNTHESIS:** NOT YET PASS  
**SYSTEM-OF-INTEREST QUALIFICATION:** STILL OPEN  
**WORK ENGINE / CONTROL ARCHITECTURE:** BLOCKED

Next work:

1. expand and verify the external Seed Reference Register against v0.2;
2. prioritize reference families/lenses by which ones can change the SoI boundary or architecture;
3. synthesize cross-reference conflicts by concern rather than writing fifteen standalone literature reviews;
4. keep current-product frontier use as a separate stress test;
5. derive `CONCERNS-AND-REQUIREMENTS` only after that synthesis.
