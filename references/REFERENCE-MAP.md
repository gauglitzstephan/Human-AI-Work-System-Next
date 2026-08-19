# Reference Map v0.2

**Status:** WORKING MAP / COVERAGE BASELINE  
**Purpose:** Define the external knowledge domains and cross-cutting lenses that must be considered before architectural claims are promoted.  
**Derived from:** external reference-first method + internal coverage audit across the predecessor repository, ChatGPT Library, Notion, Google Drive, prior ChatGPT work, and current AI-work product reality.  

This map is a **research coverage instrument**, not the architecture of the Human–AI Work System.

---

## 1. Reference-first principle

The reconstruction does not derive architecture from intuition, current product surfaces, or the predecessor system alone.

External references are used to answer five questions:

1. **What is already known?**
2. **Which constructs, distinctions, mechanisms, and failure modes are established, and with what evidence?**
3. **Which disciplines use different units of analysis or incompatible assumptions?**
4. **Under what conditions does a mechanism transfer to our candidate System of Interest?**
5. **What remains frontier, contingent, contested, or implementation-specific?**

A reference is evidence, not an instruction. Adoption requires fit to the problem, scope, evidence, intended use, and competing explanations.

### 1.1 Map semantics

Keep distinct:

```text
reference family ≠ architecture component
reference construct ≠ requirement
reference pattern ≠ design decision
current product capability ≠ system invariant
internal precedent ≠ external evidence
conceptual completeness ≠ behavioral effectiveness
```

Reference families are grouped for research economy. Their boundaries are deliberately porous; overlap should be recorded rather than hidden.

---

# 2. Reference landscape

The current map uses **15 reference families in four bands**.

The bands are organizational aids only. They are not architecture layers.

```text
A. SYSTEM / WORK / JOINT-ACTIVITY FOUNDATIONS
   R1  Systems Engineering, Architecture, Requirements & Lifecycle
   R2  Work Systems, Activity, Sociotechnical Work & Adaptive Case Work
   R3  Human Systems Integration, Human Factors & Cognitive Work
   R4  HCI, Human–AI Interaction, Mixed Initiative & Joint Performance

B. HUMAN PERFORMANCE / JUDGMENT / EXPLORATION
   R5  Human Goals, Motivation, Agency, Wellbeing & Cognitive Ergonomics
   R6  Expertise, Learning, Metacognition & Capability Formation
   R7  Sensemaking, Decision, Metareasoning, Foresight & Operations Research
   R8  Design, Creativity, Innovation & Collective Intelligence

C. INFORMATION / ORGANIZATION / VALUE
   R9  Knowledge, Information, Provenance, Context, Memory & State
   R10 Organization, Economics, Institutions, Power, Ownership & Adoption
   R11 Realization, Implementation, Behavior Change, Outcomes & Value

D. ASSURANCE / GOVERNANCE / TECHNICAL REALIZATION
   R12 Quality, Measurement, Evaluation, V&V, Assurance & Causal Attribution
   R13 Safety, Security, Privacy, Resilience, Governance, Rights & Control
   R14 AI/ML, Agents, Workflows, Context & Reusable Capability Engineering
   R15 Software/Platform Runtime, Reliability, Observability & Interoperability
```

---

# 3. Band A — System, work and joint-activity foundations

## R1 — Systems engineering, architecture, requirements and lifecycle

**Primary questions**
- What is the System of Interest, what is its operational environment, and which enabling systems matter?
- How should stakeholders, concerns, requirements, architecture drivers, viewpoints, views, model kinds, interfaces, lifecycle states, and architecture decisions be distinguished?
- How should architecture alternatives be evaluated against intended purpose and quality attributes?
- Which commitments belong in concept definition versus architecture versus implementation?

**Reference schools / seed targets**
- ISO/IEC/IEEE 15288 — system lifecycle;
- ISO/IEC/IEEE 42010 — architecture description;
- ISO/IEC/IEEE 42030 — architecture evaluation;
- SEBoK / INCOSE concept definition and needs/requirements;
- quality-attribute and architecture-evaluation practice;
- AI-specific lifecycle standards where transferable.

**Import role**
System boundary discipline, concern/view separation, requirements traceability, architecture evaluation, lifecycle and change control.

**Boundary**
Systems-engineering discipline does not by itself explain professional cognition, human purpose, organizational power, collaborative work, or the economics of AI-mediated knowledge work.

---

## R2 — Work systems, activity, sociotechnical work and adaptive case work

**Primary questions**
- What is the object of work, and how is it transformed through activity?
- When is the useful focal unit an interaction, task, case, workflow, activity system, team, organization, or larger system?
- How do people, information, technology, rules, community, division of labor, infrastructure, customers/recipients, and history shape work?
- How should open-ended knowledge work differ from predetermined process execution?
- How should work be redesigned rather than merely automated?

**Reference schools / seed targets**
- Work System Theory;
- sociotechnical systems and work design;
- Cultural-Historical Activity Theory and practice theory;
- adaptive case management / OMG CMMN;
- knowledge-work and professional-work research;
- operations/workflow design where the work object is evolving.

**Import role**
Work-object semantics, object-oriented activity, work redesign, non-predetermined cases, social/technical coupling and multiple units of analysis.

**Boundary**
No single work/activity theory should become the universal root ontology. Classic organizational theories may underrepresent platforms, AI infrastructure, adversarial settings, and open institutional environments.

---

## R3 — Human systems integration, human factors and cognitive work

**Primary questions**
- What human capabilities, limitations, workload, attention, situation awareness, expertise, fatigue, and recovery properties materially constrain system performance?
- Is performance located in an individual actor or distributed across a joint cognitive system?
- What work-domain constraints, control tasks, strategies, social organization, and competencies are required?
- What creates automation bias, brittle takeover, loss of situation awareness, or unworkable human burden?
- How must training, maintenance, fallback, and human readiness be integrated across the lifecycle?

**Reference schools / seed targets**
- Human Systems Integration;
- Human Factors / Ergonomics;
- Cognitive Systems Engineering;
- Cognitive Work Analysis;
- Joint Cognitive Systems;
- Distributed Cognition;
- supervisory control, adaptive automation and function allocation;
- resilience engineering where human adaptation is load-bearing.

**Import role**
Human operating constraints, adaptive control, cognitive coupling, work-domain analysis, total-system performance and realistic human fallback/takeover.

**Boundary**
Safety-critical control-room practice is not automatically transferable to ordinary knowledge work. Human factors also does not settle institutional legitimacy, economic ownership, or AI component design.

---

## R4 — HCI, Human–AI interaction, mixed initiative and joint performance

**Primary questions**
- What interaction patterns support accurate mental models, correction, common ground, appropriate reliance, calibrated trust, and legible system status?
- When should initiative move between human and AI, and along which dimensions?
- When does Human+AI outperform Human-only, AI-only, a specialist tool, or an existing process?
- How should handoffs, shared situation awareness, role allocation, feedback and repair be designed?
- When does collaboration structure improve performance and when does it add coordination cost?

**Reference schools / seed targets**
- Human-Centered Design / ISO 9241-210;
- HCI and Human–AI Interaction;
- Mixed-Initiative Interaction;
- Human–AI Teaming / Hybrid Intelligence;
- Coactive Design;
- CSCW, common ground, team cognition and shared mental models;
- appropriate reliance, automation bias and trust calibration;
- comparative Human–AI performance research.

**Import role**
Interaction over time, common ground, initiative allocation, coordination, correction, reliance and joint-performance evidence.

**Boundary**
Good interaction is not equivalent to good professional work or good total-system outcomes. Human–AI complementarity must remain an empirical claim, not a design assumption.

---

# 4. Band B — Human performance, judgment and exploration

## R5 — Human goals, motivation, agency, wellbeing and cognitive ergonomics

**Primary questions**
- Whose goals, interests, values, constraints and protected conditions define successful work?
- How do autonomy, competence, motivation, ownership, identity, energy, attention and cognitive load affect sustained system use?
- When does AI reduce friction versus create dependency, overload, avoidance, loss of authorship or learned passivity?
- How should the system distinguish immediate productivity from human wellbeing and durable agency?

**Reference schools / seed targets**
- motivation and self-determination research;
- cognitive load / cognitive ergonomics;
- behavioral self-regulation and implementation research;
- human agency and capability approaches;
- occupational wellbeing and sustainable work design;
- cognitive offloading where relevant.

**Import role**
Human purpose fit, motivational and cognitive sustainability, authorship, self-efficacy, attention/energy constraints and durable agency.

**Boundary**
Personal goals or preferences are contextual state, not universal architecture requirements. Wellbeing constructs require care against simplistic proxying or paternalistic inference.

---

## R6 — Expertise, learning, metacognition and capability formation

**Primary questions**
- What distinguishes information access from situated professional competence?
- How are tacit knowledge, pattern recognition, adaptive expertise, methodological craft and professional taste acquired and maintained?
- How does delegation to AI alter practice, learning pathways, junior-to-senior expertise formation, metacognition and future human control capability?
- When should AI support learning rather than substitute for the cognitive work that creates competence?
- When does repeated successful work become a validated reusable capability rather than stored text?

**Reference schools / seed targets**
- expertise and skill-acquisition research;
- adaptive expertise and transfer;
- Naturalistic Decision Making and recognition-primed expertise where relevant;
- reflective professional practice;
- learning sciences, apprenticeship and workplace learning;
- metacognition and AI-assisted learning;
- organizational learning / capability formation;
- deskilling and automation effects.

**Import role**
Professional competence, tacit/craft knowledge, learning effects of delegation, formation paths, capability maturity and Human review competence.

**Boundary**
Expertise is domain- and context-dependent. No fixed list of permanently human competences should be assumed.

---

## R7 — Sensemaking, decision, metareasoning, foresight and operations research

**Primary questions**
- What problem or decision deserves attention, and how should frames be challenged or reopened?
- How should evidence, uncertainty, alternatives, trade-offs, causal models and preferences be combined?
- When is more information or computation worth its cost?
- When should the system search, simulate, experiment, stage, defer, commit, stop or preserve option value?
- How should deep uncertainty, regime change, robustness and adaptation be handled without pretending to forecast what is not forecastable?
- How should scarce time, attention, compute and portfolio capacity be allocated?

**Reference schools / seed targets**
- decision analysis and judgment/decision-making;
- Naturalistic Decision Making and macrocognition;
- intelligence analysis and structured analytic tradecraft;
- rational metareasoning / value of information / value of computation;
- robust decision making / decision making under deep uncertainty;
- real options and reversible commitment;
- forecasting and calibration;
- systems dynamics, simulation, operations research and control/cybernetic perspectives where useful.

**Import role**
Framing, option quality, evidence sufficiency, work-selection economics, uncertainty treatment, commitment design, resource allocation and stopping.

**Boundary**
Analytical decision models should not displace expert recognition, values, politics, legitimacy or action where those are constitutive of the decision.

---

## R8 — Design, creativity, innovation and collective intelligence

**Primary questions**
- How should problem discovery, divergence, convergence, reframing, recombination, critique and selection interact?
- How can AI widen rather than homogenize a solution space?
- When do independent branches, multiple models, adversarial perspectives, external search, simulation or human diversity add value?
- How do AI collaboration patterns affect originality, voice, creative ownership, motivation and collective diversity?
- How should novelty be distinguished from useful innovation?

**Reference schools / seed targets**
- design thinking / Double Diamond / systemic design;
- problem framing and reflective design;
- computational creativity and co-creativity;
- innovation and search/recombination research;
- collective intelligence, diversity and ensemble decision-making;
- creativity-support systems.

**Import role**
Divergence/convergence, frame innovation, alternative generation, diversity preservation, creative collaboration and solution-space quality.

**Boundary**
Design frameworks are not universal work lifecycles. More alternatives or more novelty are not automatically better.

---

# 5. Band C — Information, organization and value

## R9 — Knowledge, information, provenance, context, memory and state

**Primary questions**
- What must remain distinct among raw data, observations, evidence, claims, models, context, current state, authoritative records, memory, references, artifacts and reusable knowledge?
- Where does a state live, who may update it, how is freshness established, and how are conflicts reconciled?
- What belongs in active inference context versus retrieved just in time versus persisted durably?
- How should semantic lineage survive across chats, files, apps, repositories and models?
- When does formal knowledge representation or ontology add value?

**Reference schools / seed targets**
- knowledge management and organizational memory;
- personal knowledge management;
- information science and information architecture;
- knowledge representation / ontology engineering;
- W3C provenance / data lineage / records-management concepts;
- data governance and authoritative-source patterns;
- context engineering and retrieval;
- memory systems for AI, clearly separating frontier implementation from stable information principles.

**Import role**
Provenance, state authority, retrieval, memory boundaries, promotion/supersession, semantic lineage and information lifecycle.

**Boundary**
Formal consistency is not empirical truth. Memory is not automatically a source of truth, and a single universal state store should not be assumed.

---

## R10 — Organization, economics, institutions, power, ownership and adoption

**Primary questions**
- How do specialization, coordination, transaction cost, incentives, decision rights, principal–agent problems and organizational structure alter Human–AI work?
- Who owns or controls data, models, platforms, artifacts, relationships, distribution and residual rights?
- Who creates value, bears risk and captures gains?
- How do technical capability, organizational diffusion, regulation, customer acceptance and installed systems mediate actual adoption?
- When does AI change work rather than simply substitute tasks?
- How do lock-in, switching cost, bargaining power and portability affect architectural choices?

**Reference schools / seed targets**
- organization design and coordination theory;
- transaction-cost economics / principal–agent theory / decision rights;
- economics of tasks, firms, platforms and institutions;
- resource-based view, complementary assets and dynamic capabilities where useful;
- innovation diffusion and technology adoption;
- algorithmic management / future-of-work research;
- ownership, power, rents and distribution;
- platform economics and ecosystem strategy.

**Import role**
Coordination economics, incentives, adoption, appropriation, ownership/control, dependency, institutional conditions and work-allocation diffusion.

**Boundary**
Productivity or efficiency is not equivalent to welfare, legitimacy, human capability or distributive fairness.

---

## R11 — Realization, implementation, behavior change, outcomes and value

**Primary questions**
- What must happen after an answer, decision, or artifact exists for real use and value to occur?
- How do receiving context, adoption, behavior, workflow integration, incentives, capability, change and feedback affect realization?
- How should output, transition, use, in-use performance, outcome, causal contribution, benefit, asset formation and externalities be distinguished?
- What effects matter for recipients, organizations, affected parties and the human’s future capability?
- When should work stop at an artifact boundary versus continue into implementation or operation?

**Reference schools / seed targets**
- implementation science and implementation research;
- behavior change and adoption;
- service design / user journey where receiving context matters;
- organizational change and technology implementation;
- outcome and impact evaluation;
- value realization / benefits realization;
- externality and stakeholder-impact mapping;
- capability/asset formation and sustainment.

**Import role**
Transition into use, adoption mechanisms, outcome chains, value realization, sustained operation and external effects.

**Boundary**
Implementation frameworks do not establish causality by themselves. A delivered artifact, observed outcome and caused benefit remain different claims.

---

# 6. Band D — Assurance, governance and technical realization

## R12 — Quality, measurement, evaluation, V&V, assurance and causal attribution

**Primary questions**
- What is the exact claim being qualified, and which evidence/method can establish it?
- What is the difference among review, verification, validation, evaluation, monitoring, red teaming, representative-use testing and independent assurance?
- How should professional quality, joint performance, usability, reliability, efficiency, Human burden and real outcomes be measured?
- How should causal attribution distinguish observed association from effect caused by the system?
- When are structured assurance cases, adversarial evaluation or independent review justified?

**Reference schools / seed targets**
- systems/software V&V;
- NIST AI TEVV and AI RMF measurement guidance;
- structured assurance cases / OMG SACM;
- experiment design, causal inference and evaluation science;
- professional quality assurance and testing;
- AI benchmark/eval methodology and red teaming;
- reliability/calibration measurement;
- representative-use and longitudinal evaluation.

**Import role**
Claim–evidence discipline, fit-for-purpose measurement, behavioral evaluation, causal validity, independent challenge and confidence bounds.

**Boundary**
No universal metric suite is assumed. Measured proxies may fail to represent intended professional or real-world performance.

---

## R13 — Safety, security, privacy, resilience, governance, rights and control

**Primary questions**
- What can go wrong through failure, attack, excessive agency, unsafe permission, stale state, manipulation, or unavailable fallback?
- What are the assets, threat/trust boundaries, rights, affected parties, residual risks and legitimate control points?
- How should permissions, least privilege, approvals, escalation, override, rollback, fallback and safe stop work?
- How should privacy, confidentiality, consent, data minimization, retention, deletion and third-party rights be handled?
- What constitutes meaningful human control, contestability, accountability and legitimate authority?

**Reference schools / seed targets**
- safety and resilience engineering;
- control and graceful-degradation practice;
- security engineering / threat modeling / secure development;
- OWASP GenAI / MITRE ATLAS where relevant;
- privacy engineering and data-governance frameworks;
- NIST AI RMF / AI governance;
- meaningful human control, accountability and contestability research;
- applicable law and sector regulation only when the operating context requires it.

**Import role**
Trust boundaries, permissions, failure containment, recovery, data/rights protection, authority constraints and residual-risk ownership.

**Boundary**
Governance and security controls must be proportional. Compliance does not establish good work design, technical feasibility or beneficial outcomes.

---

## R14 — AI/ML, agents, workflows, context and reusable capability engineering

**Primary questions**
- What can current AI systems actually do, with which reliability envelope and tool access?
- When is direct model use sufficient versus workflow, agent, multi-agent, deterministic tool or hybrid composition?
- How should instructions, tools, context, handoffs, approvals, exit conditions, evals and traces be composed?
- How should successful repeatable work be packaged as a reusable capability/skill rather than repeated prompting?
- How should context be selected, renewed, compacted and scoped for inference?

**Reference schools / seed targets**
- model capability and agent research;
- OpenAI / Anthropic / comparable agent-engineering guidance as implementation evidence;
- ReAct and related tool/reasoning patterns where still relevant;
- context engineering;
- agent skills / reusable workflow specifications;
- multi-agent and human-agent systems research;
- current model/tool benchmark and long-horizon task evidence.

**Import role**
Current technical capability, model/tool orchestration, context control, reusable capability packaging and agent-runtime patterns.

**Boundary**
Vendor products and agent frameworks are implementation references, not neutral ontologies of professional work. Frontier capabilities require freshness and empirical verification.

---

## R15 — Software/platform runtime, reliability, observability and interoperability

**Primary questions**
- How should abstract work-control semantics be realized across prompts, code, files, apps, APIs, event systems and persistent services?
- Which constraints require deterministic enforcement rather than language-model compliance?
- How should versioning, immutable identity, transactions, concurrency, retries, idempotency, rollback, recovery and exception handling work?
- How should state and authority cross multiple product surfaces without assuming shared context or atomicity?
- How should observability, telemetry, cost, drift, failure modes and platform capability changes be handled?
- How do portability, lock-in, migration and fallback affect runtime design?

**Reference schools / seed targets**
- software architecture and distributed systems;
- durable workflow / state-machine / event-driven systems;
- observability, SRE and incident/recovery practice;
- authorization / policy enforcement;
- version control and configuration management;
- interoperability and protocol design;
- current platform documentation for ChatGPT, Codex, apps, projects, memory, tasks and comparable work surfaces.

**Import role**
Deterministic enforcement, runtime reliability, cross-surface contracts, observability, recovery and platform reality.

**Boundary**
Implementation infrastructure should not leak upward into the conceptual model unless a real constraint requires it. Current platform limitations are mutable facts, not permanent system principles.

---

# 7. Cross-cutting coverage lenses

Reference families answer **where knowledge comes from**. Coverage lenses answer **what every material architecture concern must be challenged against**.

These lenses are not architecture views yet.

| Lens | Question |
|---|---|
| **L1 Purpose / beneficiary / affected parties** | Whose condition should improve, who bears downside, and whose values or rights are relevant? |
| **L2 Boundary / focal unit / scale** | Interaction, work episode, workflow, person, team, organization, platform, institution, or ecosystem? What changes across scales? |
| **L3 Work object / professional practice / receiving context** | What is actually being transformed, what practice defines quality, and who/what must use the result? |
| **L4 Human capability / cognition / learning** | What must the human understand, judge, practice, notice, learn, or remain capable of doing? |
| **L5 Coordination / initiative / common ground** | Who initiates, frames, generates, plans, executes, challenges, stops, repairs, and persists? With what shared state? |
| **L6 Reality / evidence / uncertainty** | What is observed, inferred, modeled, unknown, forecast, simulated, or contested? |
| **L7 Authority / responsibility / rights / ownership** | Who may decide, authorize, execute, accept, override, own, or bear residual risk? |
| **L8 Information / provenance / state / memory** | Where does information come from, where does state live, who can change it, and how is identity/freshness preserved? |
| **L9 Resources / economics / power** | What are the time, attention, energy, money, compute, coordination, switching, opportunity and maintenance costs; who captures value? |
| **L10 Risk / security / privacy / resilience** | What failures, attacks, misuse, data harms, lockouts or degradation matter, and what fallback exists? |
| **L11 Transition / adoption / outcome / value** | What must happen after production for use, performance, outcome, benefit, asset or externality to occur? |
| **L12 Creativity / diversity / counterframes** | Does the system broaden or collapse the search space, create correlated errors, or suppress minority/novel hypotheses? |
| **L13 Lifecycle / monitoring / adaptation** | How does the system onboard, operate, detect change, recalibrate, recover, evolve, supersede and retire? |
| **L14 Runtime / portability / platform reality** | Which behavior depends on a mutable product surface, permission, plan, model, connector or implementation substrate? |

A major architecture decision should show which lenses are material and which are not, rather than mechanically filling all fourteen.

---

# 8. Frontier watchlist

Some fields are strategically important but too unstable to define architecture invariants without further evidence. Track them as **frontier hypotheses / variation points**:

1. long-horizon autonomous agents and trajectory reliability;
2. persistent AI memory and long-term context synthesis;
3. AI evaluators, critics and automated assurance;
4. multi-agent orchestration and human-agent collectives;
5. self-improving / self-configuring workflows and autonomous capability promotion;
6. AI-native organizations, management and decision rights;
7. synthetic users, stakeholders, organizations and society simulation;
8. embodied AI, robotics and physical-world automation;
9. proactive ambient/monitoring systems that act across time;
10. rapidly changing model, app, skill, agent and interoperability ecosystems.

Promotion rule:

```text
frontier relevance
≠ stable evidence
≠ architecture invariant
```

A frontier mechanism may still be used in a bounded implementation when its local benefit and failure envelope are adequately tested.

---

# 9. Current-product / frontier-user challenge

The program should periodically ask a deliberately practical question:

> If a highly capable contemporary AI user were optimizing for real work rather than prompt craftsmanship, what operating patterns would they exploit that our System of Interest must be able to explain?

This is a **stress test, not an empirical claim about a literal top 1% user population**.

Current product reality suggests testing at least these patterns:

- bounded project/workspace contexts rather than one global conversation;
- connected apps as current-data and action interfaces rather than copy/paste context;
- source-scoped multi-step research with explicit plans and citations;
- reusable Skills/capabilities for recurring methods instead of repeated prompts;
- agents/workflows for repeatable work only after the task and evaluator are stable enough;
- scheduled/conditional monitoring for work that depends on change over time;
- repo-backed/versioned execution for durable technical or configuration work;
- explicit permission/approval boundaries for connected actions;
- memory as personalization/continuity, not an unquestioned authoritative record;
- explicit cross-surface handoffs because projects, tasks, apps, memory, Codex and external systems do not form one guaranteed shared state;
- evaluation, traces, correction loops and behavioral evidence rather than prompt elegance;
- deliberate management of attention, context budget, maintenance burden and stopping conditions.

These patterns should challenge the architecture, but current product surfaces remain mutable implementation evidence.

---

# 10. Reference evidence contract

## 10.1 Source hierarchy

Prefer, where available:

1. systematic reviews and meta-analyses;
2. peer-reviewed primary experiments and field studies;
3. foundational works from established fields;
4. formal standards and authoritative professional guidance;
5. official technical reports with inspectable methods and limitations;
6. high-quality industrial field evidence and documented case studies;
7. preprints for frontier coverage, clearly labeled;
8. vendor/practitioner material for implemented product/runtime reality, not as independent proof of general effectiveness.

Primary sources are preferred for technical and scientific claims.

## 10.2 Reference record schema

Every reference promoted into the knowledge base should record:

```text
Reference ID
Source / authors / organization
Date / version / freshness
Reference family/families
Coverage lens/lenses informed
Question it informs
Relevant claim(s)
Mechanism / construct
Unit of analysis
Evidence type and scope
Boundary conditions
Known limitations / conflicts
Transferability to our System of Interest
Competing reference / counterevidence
Implication, if any
Status: DISCOVERED | REVIEWED | SYNTHESIZED | USED | SUPERSEDED
```

## 10.3 Conflict rule

Do not flatten disagreement into one synthesized statement before identifying why sources differ.

Check whether conflict is caused by:

- different units of analysis;
- different task types or stakes;
- different definitions;
- different time periods / technology frontiers;
- different human expertise;
- different organizational/institutional contexts;
- different outcome metrics;
- normative rather than empirical disagreement.

---

# 11. Coverage rule before architecture promotion

Architecture work should not proceed merely because one relevant discipline supplies a plausible answer.

Before a major architectural commitment:

1. identify the concern and candidate mechanism;
2. select the material coverage lenses;
3. inspect all reference families that can materially change the answer;
4. surface incompatible assumptions and alternative units of analysis;
5. compare the external evidence with internal work evidence;
6. state transfer conditions and residual uncertainty;
7. only then derive candidate requirements or architecture alternatives.

Examples:

- an agent-orchestration proposal must be checked against Human Factors, Human–AI Interaction, Economics, Security, Evaluation and Runtime Reliability;
- a memory/state proposal must be checked against Information/Provenance, Human Cognition, Authority/Ownership, Privacy and platform reality;
- a Human-review proposal must be checked against actual detection competence, cognitive burden, learning effects, comparative Human/AI performance and independence;
- a professional artifact workflow must be checked against domain expertise, receiving-context quality, realization/use and evaluation—not just correctness;
- a productivity claim must be checked against coordination, validation, rework, maintenance, learning, transition and externality costs.

---

# 12. Current gap and next reference gate

The map is now broad enough to serve as a **coverage baseline**, but it is not yet a synthesized knowledge base.

Next reference work should:

1. reconcile this map against the existing internal HAWS/HASA/JAIWS reference work without importing those architectures;
2. populate 2–5 high-quality anchor references per family, with evidence status and transfer boundaries;
3. identify the 8–12 concerns most likely to discriminate the candidate System-of-Interest boundary and future Work-Control architecture;
4. build a cross-reference synthesis by **concern × mechanism × evidence × boundary**, not fifteen isolated literature reviews;
5. run an explicit frontier-user/product-reality challenge against current ChatGPT/Codex/apps/skills/agents/tasks and comparable systems;
6. only then derive a qualified Concerns & Requirements candidate.
