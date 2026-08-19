# Reference Map v0.3

**Status:** WORKING COVERAGE BASELINE / PRE-ARCHITECTURE  
**Date:** 2026-08-19  
**Purpose:** Define the external knowledge domains and cross-cutting challenge lenses that must be considered before architectural claims are promoted.  
**Promotion basis:** `REFERENCE-MAP-COVERAGE-AUDIT-v0.1.md` + `REFERENCE-MAP-RED-TEAM-v0.1.md` + `REFERENCE-ANCHOR-CONFLICT-SWEEP-v0.1.md`.

This map is a **research coverage instrument**, not the architecture of the Human–AI Work System.

---

# 1. Reference-first principle

The reconstruction does not derive architecture from intuition, current product surfaces, or the predecessor system alone.

For a material concern, external references should help establish:

1. what is already known;
2. which constructs, mechanisms and failure modes are established;
3. which units of analysis and assumptions differ across disciplines;
4. which evidence supports or challenges a candidate mechanism;
5. under what conditions the mechanism transfers to our System of Interest;
6. what remains frontier, contingent, disputed or implementation-specific.

Keep distinct:

```text
reference family ≠ architecture component
reference construct ≠ requirement
reference pattern ≠ design decision
current product capability ≠ system invariant
internal precedent ≠ external evidence
conceptual completeness ≠ behavioral effectiveness
```

Reference families are deliberately overlapping. Overlap is recorded and reconciled rather than hidden.

---

# 2. Reference landscape

The current baseline contains **17 Reference Families in five research bands**.

The bands are organizational aids only. They are **not architecture layers**.

```text
A. SYSTEM / WORK / JOINT-ACTIVITY FOUNDATIONS
   R1  Systems Engineering, Architecture, Requirements & Lifecycle
   R2  Work Systems, Activity, Sociotechnical Work & Adaptive Case Work
   R3  Human Systems Integration, Human Factors & Cognitive Work
   R4  HCI, Human–AI Interaction, Mixed Initiative & Joint Performance

B. HUMAN PERFORMANCE / JUDGMENT / EXPLORATION
   R5  Human Goals, Motivation, Agency, Wellbeing & Cognitive Ergonomics
   R6  Expertise, Learning, Metacognition & Capability Formation
   R7  Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research
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

E. STRATEGY / PORTFOLIO / MANAGEMENT CONTROL
   R16 Strategic Management, Strategy Formation & Strategic Renewal
   R17 Project, Programme, Portfolio, Initiative & Management Control
```

---

# 3. Family records

## R1 — Systems Engineering, Architecture, Requirements & Lifecycle

**Questions:** System of Interest; environment; stakeholders; concerns; requirements; architecture drivers; viewpoints/views; interfaces; alternatives; lifecycle; verification/validation; retirement.  
**Seed fields:** ISO/IEC/IEEE 15288, 42010, 42030; SEBoK/INCOSE; quality-attribute architecture evaluation.  
**Import role:** boundary discipline, requirements/traceability, architecture evaluation, lifecycle.  
**Boundary:** does not by itself explain cognition, professional practice, strategy, power or economics.

## R2 — Work Systems, Activity, Sociotechnical Work & Adaptive Case Work

**Questions:** work object; activity; focal unit; division of labor; rules/community; open-ended case work; work redesign; workflow vs activity system.  
**Seed fields:** Work System Theory; sociotechnical systems; Activity Theory/practice theory; CMMN/adaptive case work; knowledge/professional work.  
**Import role:** work-object semantics, non-predetermined work, social/technical coupling.  
**Boundary:** no single work/activity theory is the universal root ontology.

## R3 — Human Systems Integration, Human Factors & Cognitive Work

**Questions:** human capability/limitation; workload; attention; situation awareness; cognitive work; function allocation; fallback/takeover; adaptive control; resilience.  
**Seed fields:** Human Systems Integration; Human Factors/Ergonomics; Cognitive Systems Engineering; Cognitive Work Analysis; Joint Cognitive Systems; Distributed Cognition; supervisory/adaptive automation.  
**Import role:** total-system human performance and realistic operating burden.  
**Boundary:** safety-critical practice is not transferred wholesale into ordinary knowledge work.

## R4 — HCI, Human–AI Interaction, Mixed Initiative & Joint Performance

**Questions:** common ground; initiative; feedback; correction; trust/reliance; mental models; handoffs; comparative Human/AI/joint performance.  
**Seed fields:** ISO 9241-210; Human–AI Interaction; Mixed Initiative; Coactive Design; Human–AI Teaming; CSCW/team cognition; appropriate reliance.  
**Import role:** interaction over time and joint performance.  
**Boundary:** good interaction is not equivalent to good professional or total-system outcomes.

## R5 — Human Goals, Motivation, Agency, Wellbeing & Cognitive Ergonomics

**Questions:** whose goals matter; autonomy; motivation; ownership; identity; attention/energy; cognitive load; self-efficacy; sustainable use.  
**Seed fields:** self-determination; cognitive load/ergonomics; self-regulation; capability/agency approaches; sustainable work design.  
**Import role:** purpose fit and durable human agency.  
**Boundary:** personal preferences remain contextual state; wellbeing must not become paternalistic proxying.

## R6 — Expertise, Learning, Metacognition & Capability Formation

**Questions:** information vs competence; tacit craft; adaptive expertise; professional taste; learning effects of delegation; deskilling; capability formation and validation.  
**Seed fields:** expertise/skill acquisition; adaptive expertise; workplace learning/apprenticeship; reflective practice; learning sciences; Naturalistic Decision Making where expertise formation matters; organizational learning.  
**Import role:** professional competence and future human capability.  
**Boundary:** no fixed list of permanently human competences.

## R7 — Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research

**Questions:** what deserves attention; intelligence requirement; source/coverage need; framing; alternatives; uncertainty; value of information/computation; simulation; forecasting; staging; robustness; commitment; stopping; resource allocation.  
**Seed fields:** intelligence analysis and analytic tradecraft; decision analysis; judgment/decision making; Naturalistic Decision Making/macrocognition; metareasoning; robust decision making/deep uncertainty; real options; forecasting/calibration; systems dynamics; operations research.  
**Verified anchors:** ISO 56006:2021; ODNI ICD 203 analytic standards.  
**Import role:** evidence-to-situation-model-to-decision/action/monitor coupling and work-selection economics.  
**Boundary:** intelligence informs rather than automatically owns policy, strategy or commitment; analytical models must not displace constitutive values or expert recognition.

## R8 — Design, Creativity, Innovation & Collective Intelligence

**Questions:** problem discovery; divergence/convergence; reframing; recombination; novelty; diversity; correlated error; co-creativity; collective intelligence.  
**Seed fields:** design/systemic design; creativity-support systems; computational creativity/co-creativity; innovation/search; collective intelligence/diversity.  
**Import role:** search-space quality and alternative formation.  
**Boundary:** more novelty or more options is not automatically better.

## R9 — Knowledge, Information, Provenance, Context, Memory & State

**Questions:** data vs evidence vs model vs state vs memory vs knowledge; authority; freshness; lineage; retrieval; refind; promotion; supersession; context engineering; ontology fit.  
**Seed fields:** knowledge management; organizational/personal memory; information science; knowledge representation; provenance/data lineage; records/data governance; context engineering; AI memory research.  
**Import role:** state/knowledge integrity and semantic continuity.  
**Boundary:** formal consistency is not reality; memory is not automatically source of truth.

## R10 — Organization, Economics, Institutions, Power, Ownership & Adoption

**Questions:** specialization; coordination/transaction cost; incentives; principal–agent; decision rights; ownership/control; rents; distribution; platforms; lock-in; diffusion/adoption; institutional conditions.  
**Seed fields:** organization design; transaction-cost economics; principal–agent/decision rights; economics of tasks/firms/platforms; innovation diffusion; complementary assets; algorithmic management; institutional/power analysis.  
**Import role:** organizational/economic feasibility, value capture, dependency and adoption.  
**Boundary:** efficiency/productivity is not equivalent to welfare, legitimacy or human capability.

## R11 — Realization, Implementation, Behavior Change, Outcomes & Value

**Questions:** what happens after artifact/decision; adoption; receiving context; workflow integration; behavior change; benefit/outcome realization; externalities; sustained operation.  
**Seed fields:** implementation science; organizational change; behavior/adoption research; service/use-context design; benefits realization; impact/outcome evaluation; capability/asset formation.  
**Import role:** transition into use and observed value.  
**Boundary:** delivery or observed outcome does not establish causal benefit.

## R12 — Quality, Measurement, Evaluation, V&V, Assurance & Causal Attribution

**Questions:** exact claim; evidence/method fit; review vs verification vs validation vs evaluation vs monitoring; representative-use test; independent assurance; professional-quality measurement; causal attribution.  
**Seed fields:** V&V; NIST TEVV/AI RMF; structured assurance/SACM; experiment/causal inference; AI eval/red teaming; reliability/calibration.  
**Import role:** claim–evidence qualification and behavioral evaluation.  
**Boundary:** no universal metric suite; easy proxies can miss intended performance.

## R13 — Safety, Security, Privacy, Resilience, Governance, Rights & Control

**Questions:** hazard/threat; trust boundary; permissions; privacy/consent; least privilege; attack/misuse; excessive agency; fallback; override; rollback; safe stop; contestability; accountability; residual risk.  
**Seed fields:** safety/resilience engineering; security/threat modeling; privacy engineering; secure development; NIST AI RMF; OWASP GenAI/MITRE ATLAS where applicable; meaningful human control; sector law when required.  
**Import role:** legitimate and recoverable action/control.  
**Boundary:** governance/compliance does not establish good work design or beneficial outcomes.

## R14 — AI/ML, Agents, Workflows, Context & Reusable Capability Engineering

**Questions:** current AI capability/reliability; direct model vs workflow vs agent vs multi-agent; tools; context; handoffs; approvals; Skills/reusable capabilities; evals/traces; model/tool frontier.  
**Seed fields:** current model/agent research; agent engineering; context engineering; reusable Skills/workflow specification; long-horizon task evidence.  
**Import role:** current technical capability and AI-native realization patterns.  
**Boundary:** vendor products/frameworks are implementation evidence, not neutral work ontology.

## R15 — Software/Platform Runtime, Reliability, Observability & Interoperability

**Questions:** deterministic enforcement; versioning; transactions; concurrency; retries/idempotency; rollback/recovery; observability; authorization; cross-surface state; migration/portability; platform constraints.  
**Seed fields:** software/distributed-systems architecture; durable execution; SRE/observability; policy enforcement; version/configuration management; interoperability/protocols; current platform documentation.  
**Import role:** runtime reliability and cross-surface contracts.  
**Boundary:** mutable platform limitations do not become permanent system principles.

## R16 — Strategic Management, Strategy Formation & Strategic Renewal

**Questions:** which arena/problem deserves strategic commitment; desired position/guiding logic; coherent choices; capability/asset building; deliberate vs emergent strategy; resource commitment; exclusion; strategic renewal under change.  
**Verified anchors:** Mintzberg & Waters (1985); Noda & Bower (1996); Teece, Pisano & Shuen (1997); supporting Burgelman strategy-process work.  
**Import role:** direction, position, coherence, path dependence, capability renewal and patterns across multiple decisions/actions.  
**Boundary:** R16 does not own every important decision and does not replace R7, R10 or R11.

## R17 — Project, Programme, Portfolio, Initiative & Management Control

**Questions:** when work becomes project/programme/portfolio; initiative admission; prioritization; resource allocation; dependencies; WIP/capacity; governance; scale/pause/kill; operating/management control; benefit/outcome review.  
**Verified anchors:** ISO 21500:2021; ISO 21503:2022; ISO 21504:2022; ISO 21505:2017; ISO 21513:2026; Management Control Systems research including Malmi & Brown (2008).  
**Import role:** multi-work coordination and control across persistent initiatives.  
**Boundary:** no project/portfolio ceremony for ordinary work; strategy remains distinct from portfolio management; management control does not own legitimate purpose.

---

# 4. Cross-cutting Coverage Lenses

Reference Families answer **where knowledge comes from**. Coverage Lenses answer **which questions a material architecture claim must survive**.

They are not architecture views yet and are activated only when material.

| Lens | Challenge question |
|---|---|
| **L1 Purpose / beneficiary / affected parties** | Whose condition should improve, who bears downside, whose values/rights matter? |
| **L2 Boundary / focal unit / scale** | Interaction, episode, project, team, organization, platform, institution or ecosystem? |
| **L3 Work object / professional practice / receiving context** | What is transformed, what defines professional quality, who/what must use the result? |
| **L4 Human capability / cognition / learning** | What must the human understand, judge, practice, notice, learn or remain capable of? |
| **L5 Coordination / initiative / common ground** | Who frames, initiates, generates, plans, executes, challenges, stops, repairs and persists? |
| **L6 Reality / evidence / uncertainty** | What is observed, inferred, modeled, simulated, forecast, contested or unknown? |
| **L7 Authority / responsibility / rights / ownership** | Who may decide, authorize, execute, accept, override, own or bear residual risk? |
| **L8 Information / provenance / state / memory** | Where does state live, who can change it, how are identity/freshness/refind preserved? |
| **L9 Resources / economics / power** | What time, attention, energy, money, compute, coordination, opportunity and maintenance cost exists; who captures value? |
| **L10 Risk / security / privacy / resilience** | What failure, attack, misuse, data harm, dependency or degraded mode matters? |
| **L11 Transition / adoption / outcome / value** | What must happen after production for use, performance, outcome, benefit or asset to occur? |
| **L12 Creativity / diversity / counterframes** | Does the system widen or collapse search space and create correlated errors? |
| **L13 Lifecycle / monitoring / adaptation** | How does it onboard, operate, monitor, recalibrate, recover, supersede and retire? |
| **L14 Runtime / portability / platform reality** | What depends on mutable product, permission, plan, model, connector or substrate? |
| **L15 Strategy / portfolio / initiative coherence** | Does this work deserve resources relative to strategy, other bets, WIP, dependencies and opportunity cost; what should be stopped? |
| **L16 Organizational persistence / institutionalization** | If something must survive the current person/episode, what exactly persists, through what mechanism, owner, use path, maintenance and retirement rule? |

Important L16 distinctions:

```text
stored information ≠ organizational memory
organizational memory ≠ routine
routine ≠ validated capability
capability ≠ role / authority
policy ≠ actual practice
technical persistence ≠ institutional adoption
repeatability ≠ sustained value
```

---

# 5. Frontier watchlist

Track but do not treat as stable invariants without evidence:

- long-horizon autonomous agents;
- persistent agent memory and long-term context synthesis;
- AI evaluators/critics and automated assurance;
- multi-agent / human-agent collectives;
- self-configuring or self-improving workflows;
- AI-native organizations and delegated management;
- synthetic users/stakeholders/society simulation;
- embodied AI/robotics;
- proactive ambient monitoring/action;
- rapidly changing model/app/skill/agent/interoperability ecosystems.

Rule:

```text
frontier relevance ≠ stable evidence ≠ architecture invariant
```

---

# 6. Evidence contract

Prefer, where available:

1. systematic reviews/meta-analyses;
2. peer-reviewed primary field/experimental evidence;
3. foundational established works;
4. formal standards and authoritative professional guidance;
5. official technical/research reports with methods/limitations;
6. high-quality industrial field evidence;
7. clearly labeled preprints for frontier coverage;
8. vendor/practitioner material for implementation/product reality, not independent proof of general effectiveness.

Each promoted reference should record:

```text
Reference ID
Source / date / version
Reference family/families
Coverage lens/lenses
Question informed
Claim / mechanism
Unit of analysis
Evidence type / scope
Boundary conditions
Conflicts / counterevidence
Transferability to our SoI
Implication, if any
Status: DISCOVERED | REVIEWED | SYNTHESIZED | USED | SUPERSEDED
```

Do not flatten disagreements before checking whether they arise from different units, tasks, definitions, technology frontiers, expertise levels, contexts, outcome metrics or normative premises.

---

# 7. Coverage rule before architecture promotion

Before a major architecture commitment:

1. identify concern and candidate mechanism;
2. select material coverage lenses;
3. inspect all reference families able to change the answer;
4. surface alternative units of analysis and incompatible assumptions;
5. compare external evidence with internal work evidence;
6. state transfer conditions and residual uncertainty;
7. only then derive candidate requirements or architecture alternatives.

Examples:

- agent orchestration → R3/R4/R10/R12/R13/R14/R15;
- memory/state → R6/R9/R10/R13/R15 + L16;
- human review → R3/R4/R6/R12 + actual detection competence;
- strategic bet → R7/R10/R16/R17 + L15;
- project/initiative continuation → R7/R11/R17 + L9/L15;
- organizational retention → R6/R9/R10/R11/R15/R17 + L16;
- productivity claim → coordination, validation, rework, maintenance, learning, transition and externality costs.

---

# 8. Current gate

**Reference Map coverage:** PASS for v0.3 working baseline.  
**Reference synthesis:** still incomplete.  
**System-of-Interest qualification:** open.  
**Work Engine / control architecture:** blocked.

Next:

1. broaden Anchor & Conflict verification across the remaining highest-discrimination families;
2. build cross-reference synthesis by concern × mechanism × evidence × boundary;
3. build the high-priority predecessor evidence matrix in parallel;
4. derive `CONCERNS-AND-REQUIREMENTS v0.1` only after the two evidence streams converge.
