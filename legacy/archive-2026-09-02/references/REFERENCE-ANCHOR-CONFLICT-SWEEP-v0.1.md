# Reference Anchor & Conflict Sweep v0.1

**Status:** COMPLETE FOR RED-TEAM DISPUTED AREAS / EXTERNAL ANCHOR PASS  
**Date:** 2026-08-19  
**Purpose:** Resolve the four open coverage questions created by `REFERENCE-MAP-RED-TEAM-v0.1.md` before further architecture work.

## Executive disposition

| Question | Decision | Confidence |
|---|---|---|
| Strategy: separate family or merge into Decision/Economics? | **PROMOTE separate R16** | High |
| Project/Programme/Portfolio/Initiative/Management Control: separate family or merge? | **PROMOTE separate R17** | High |
| Intelligence: separate family or part of R7? | **MERGE / EXPAND R7** | Medium-high |
| Organizational Persistence: separate family or cross-cutting lens? | **PROMOTE L16 lens, not family** | High |
| Strategy/Portfolio/Initiative coherence as a cross-cutting concern? | **PROMOTE L15 lens** | High |

The sweep therefore supports a `REFERENCE-MAP v0.3` working baseline with 17 reference families and 16 coverage lenses. This remains a research map, not system architecture.

---

# 1. Decision rule used in this sweep

A candidate receives its own **Reference Family** only if it satisfies all of the following:

1. it has an established external body of knowledge or professional discipline;
2. it answers a materially distinct class of questions not adequately represented by existing families;
3. omission can change the System-of-Interest boundary, work-control model, performance model, or architectural alternatives;
4. the field's constructs cannot be represented adequately as a cross-cutting lens or a subfield of another family without loss of discrimination;
5. the new family reduces category error more than it increases reference-map complexity.

A candidate becomes a **Coverage Lens** when the phenomenon must be checked across multiple reference families and system scales, but no single independent body of knowledge owns the whole question.

A candidate is **merged** when it is important but its core mechanisms are already contained within an existing family and adjacent families provide the missing parts.

---

# 2. C1 — Strategy

## Question

Should `Strategy` be treated merely as part of R7 Decision/Sensemaking and R10 Organization/Economics, or does it merit its own external Reference Family?

## External anchors

### A1 — Mintzberg & Waters (1985), *Of strategies, deliberate and emergent*

Source: Strategic Management Journal.  
DOI: https://doi.org/10.1002/smj.4250060306

Anchor contribution:
- real strategies can lie on a continuum between deliberate and emergent;
- strategy therefore cannot be reduced to a one-time explicit decision or plan;
- realized strategy can emerge from patterns of action over time.

### A2 — Noda & Bower (1996), *Strategy making as iterated processes of resource allocation*

Source: Strategic Management Journal.  
DOI: https://doi.org/10.1002/smj.4250171011

Anchor contribution:
- field evidence models strategy making as multi-level, iterated resource allocation;
- early results influence escalation/de-escalation of strategic commitment;
- strategic intent, initiatives and resource commitment co-evolve.

### A3 — Teece, Pisano & Shuen (1997), *Dynamic capabilities and strategic management*

Source: Strategic Management Journal.  
DOI: https://doi.org/10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z

Anchor contribution:
- competitive advantage under change depends on processes of coordination/reconfiguration, asset positions and path dependencies;
- strategy therefore includes capability configuration and renewal, not only option selection.

### Supporting process evidence

Burgelman (1996), *A process model of strategic business exit*, reinforces an evolutionary/process view of strategy and strategic commitment/exit.

## Conflict test

### Argument for MERGE into R7

R7 already covers:
- framing;
- alternatives;
- uncertainty;
- commitment;
- foresight;
- decision quality.

If strategy were only “high-stakes decision making”, a separate family would be redundant.

### Why that merge fails

The strategy anchors add mechanisms not captured by local decision analysis:

```text
pattern over multiple decisions and actions
strategic position / terrain
coherence among choices
resource commitment over time
capability building and reconfiguration
path dependence
strategic renewal
emergence vs deliberate intent
what not to pursue
```

A sequence of locally rational decisions can still produce an incoherent or strategically weak whole.

### Argument for MERGE into R10

R10 already covers industrial organization, resources, capabilities, institutions, incentives, ownership and economics.

### Why that merge also fails

R10 primarily explains **constraints, incentives, structure and value capture**. Strategy asks how an actor forms and updates a coherent direction and position **using** those mechanisms.

Economics is an input to strategy; it is not equivalent to strategy formation.

## Decision

# PROMOTE — R16

**R16 — Strategic Management, Strategy Formation & Strategic Renewal**

Core research questions:
- What game/arena/problem space should be engaged at all?
- What position, theory of advantage or guiding logic should govern choices?
- Which mutually reinforcing choices/bets/actions create coherence?
- Which capabilities, assets and relationships must be built, preserved or abandoned?
- What is deliberately excluded or stopped?
- How do deliberate intent, emergent patterns and realized strategy interact?
- How should strategy change with evidence, capability development and environmental change?

Boundary:
- R16 does not own every decision.
- R16 does not replace R7 decision quality, R10 economics/power, or R11 realization.
- Routine execution should not invoke strategic analysis unless future position, resource commitment, coherence or renewal is material.

---

# 3. C2 — Project / Programme / Portfolio / Initiative / Management Control

## Question

Can multi-work coordination be represented adequately through R2 Work Systems, R7 resource allocation and R10 Organization/Economics, or is a separate management reference family required?

## External anchors

### A4 — ISO 21500:2021

*Project, programme and portfolio management — Context and concepts*  
https://www.iso.org/standard/75704.html

Anchor contribution:
- explicitly distinguishes project, programme and portfolio management within an organizational context;
- points to separate guidance for project, programme, portfolio and governance.

### A5 — ISO 21503:2022

*Guidance on programme management*  
https://www.iso.org/standard/82868.html

Anchor contribution:
- programme management has its own concepts, prerequisites, practices, roles and responsibilities;
- it is not simply a large project.

### A6 — ISO 21504:2022

*Guidance on portfolio management*  
https://www.iso.org/standard/82867.html

Anchor contribution:
- project/programme portfolio management is a distinct management object;
- the standard explicitly separates portfolio management from project and programme management.

### A7 — ISO 21505:2017

*Guidance on governance*  
https://www.iso.org/standard/63578.html

Anchor contribution:
- governance of projects/programmes/portfolios is a distinct executive concern.

### A8 — ISO 21513:2026

*Guidance on post-project and post-programme evaluation*  
https://www.iso.org/standard/63585.html

Anchor contribution:
- post-project/programme evaluation should examine objectives, actual outcomes, benefits realization and governance/management effectiveness;
- completion of execution is therefore not the end of the management object.

### A9 — Malmi & Brown (2008), Management Control Systems as a Package

Source: Management Accounting Research.  
DOI: https://doi.org/10.1016/j.mar.2008.09.003

Anchor contribution:
- management control is broader than individual decision making;
- planning, cybernetic, reward/compensation, administrative and cultural controls can operate as a package;
- explicitly distinguishes decision-making from controls used to direct organizational behaviour.

## Conflict test

### Argument for MERGE into R2 Work Systems

Projects and programmes are forms of work organization.

### Why this is insufficient

R2 can explain the work object and sociotechnical activity, but does not by itself provide the management semantics for:

```text
multiple simultaneous initiatives
programme-level dependency and benefit coordination
portfolio admission / prioritization / balancing
resource allocation across initiatives
WIP and capacity
scale / pause / kill / terminate
governance across multiple work objects
post-completion benefit review
management-control feedback
```

### Argument for MERGE into R7

R7 includes portfolio-capacity allocation and value-of-information logic.

### Why this is insufficient

R7 is primarily a reasoning/decision/uncertainty discipline. Multi-initiative management includes organizational roles, persistent commitments, governance, scheduling/dependency, benefit coordination and feedback systems that continue after the local decision is made.

### Argument for MERGE into R16 Strategy

Portfolio allocation is part of strategy making.

### Why this is insufficient

Noda & Bower show a strong coupling between strategy and resource allocation, but standards and management-control research still distinguish the **management of the initiative portfolio** from the **formation of strategy**. Strategy can exist without a formal programme/portfolio; programme/portfolio management can implement a strategy without owning its legitimate purpose.

## Decision

# PROMOTE — R17

**R17 — Project, Programme, Portfolio, Initiative & Management Control**

Core research questions:
- When does work become a project, programme, portfolio or persistent initiative rather than a local work episode?
- How are initiatives admitted, prioritized, funded, sequenced, coordinated, paused, scaled and stopped?
- How are dependencies, capacity, WIP and scarce attention managed across work objects?
- How are strategic objectives translated into portfolios without making the portfolio the strategy owner?
- How are progress, outcomes, benefits and residual work reviewed?
- What control system is sufficient to align execution while preserving local adaptation?
- How is administrative/control burden kept below the value it creates?

Boundary:
- no PMO ceremony for ordinary direct work;
- project/programme/portfolio are distinct focal units, not universal maturity levels;
- management control does not own purpose, values or strategic legitimacy;
- R17 complements, but does not replace, R2, R7, R10, R11 or R16.

---

# 4. C3 — Intelligence

## Question

Does Intelligence Production / Strategic Intelligence require a separate Reference Family, or should R7 be expanded?

## External anchors

### A10 — ISO 56006:2021

*Innovation management — Tools and methods for strategic intelligence management — Guidance*  
https://www.iso.org/standard/72621.html

Anchor contribution:
- recognizes strategic intelligence management as a formal organizational practice;
- links intelligence processes to strategic decision support in an innovation-management context.

### A11 — ODNI / ICD 203 Analytic Standards

Official ODNI overview: https://www.dni.gov/index.php/ic-legal-reference-book/123-about

Anchor contribution:
- intelligence analysis is explicitly decision-support rather than policy decision ownership;
- analytic tradecraft requires source-quality characterization, uncertainty, separation of information from assumptions/judgments, alternatives, customer relevance, logical argument and explanation of changed judgments;
- review/evaluation of analytic products is part of the discipline.

## Conflict test

### Argument for separate family

Intelligence has mature professional traditions involving:
- intelligence requirements;
- collection/source portfolios;
- analytic tradecraft;
- dissemination;
- warning;
- monitoring;
- review/evaluation.

It is not merely “research”.

### Why a separate family is not yet justified

Its core mechanisms are jointly owned by existing families:

- **R7:** sensemaking, analytic judgment, alternatives, uncertainty, foresight, decision support;
- **R9:** sources, provenance, information lifecycle, state, retention;
- **R12:** analytic standards, quality, evaluation and assurance;
- **R16:** strategic requirement/use when intelligence serves strategy.

The distinctive intelligence contribution is primarily a **configured operating discipline linking information acquisition to decision/action/monitor needs**, rather than an independent whole-system concern family.

Creating R18 now would likely duplicate R7/R9/R12 and recreate ontology inflation.

## Decision

# MERGE — EXPAND R7

Rename:

**R7 — Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research**

R7 should explicitly include:

```text
intelligence requirements
coverage/source portfolios
collection/acquisition strategy
structured analytic tradecraft
situation models
warning/signposts
monitor conditions
decision/action coupling
changed-judgment explanation
```

Boundary:
- intelligence informs decisions; it does not automatically own policy, strategy or commitment;
- intelligence is activated where heterogeneous/changing information and future monitoring materially matter, not as a mandatory research phase.

Re-entry trigger for separate-family reconsideration:
- if future architecture needs a persistent intelligence subsystem with distinct lifecycle, actors, collection infrastructure and operating doctrine whose concerns cannot be represented through R7/R9/R12/R16.

---

# 5. C4 — Organizational Persistence / Institutionalization

## Question

Should organizational persistence become a separate Reference Family, or a cross-cutting lens across learning, knowledge, organization, realization and runtime?

## External anchors

### A12 — Crossan, Lane & White (1999)

*An Organizational Learning Framework: From Intuition to Institution*  
Academy of Management Review.  
DOI: https://doi.org/10.5465/amr.1999.2202135

Anchor contribution:
- organizational learning crosses individual, group and organizational levels;
- institutionalizing is a distinct process from individual intuition/interpretation and group integration.

### A13 — Argote, Lee & Park (2020)

*Organizational Learning Processes and Outcomes: Major Findings and Future Research Directions*  
Management Science.  
DOI: https://doi.org/10.1287/mnsc.2020.3693

Anchor contribution:
- separates search, knowledge creation, knowledge retention and knowledge transfer;
- persistence therefore cannot be equated with initial learning or document storage.

### A14 — Cohen & Bacdayan (1994)

*Organizational Routines Are Stored as Procedural Memory: Evidence from a Laboratory Study*  
Organization Science.  
DOI: https://doi.org/10.1287/orsc.5.4.554

Anchor contribution:
- organizational routines can embody procedural memory distributed across participants;
- durable organizational capability is not reducible to explicit documentation.

### A15 — Pentland, Hærem & Hillison (2011)

*The (N)Ever-Changing World: Stability and Change in Organizational Routines*  
Organization Science.  
DOI: https://doi.org/10.1287/orsc.1110.0624

Anchor contribution:
- routines can provide both stability and change;
- persistence should not be modeled as freezing one canonical procedure.

### Supporting standard — ISO 30401:2018

*Knowledge management systems — Requirements*  
https://www.iso.org/standard/68683.html

Note: ISO currently has a DIS revision intended to replace the 2018 edition; use it as evidence of the management-system concern, not as a frozen current design recipe.

## Conflict test

### Argument for a new family

Persistence is obviously important to a durable Human–AI Work System.

### Why that does not imply a new family

What persists can be fundamentally different:

```text
knowledge
routine
skill / professional capability
role / responsibility
policy / decision right
relationship / trust
process
software / automation
state / record
asset / IP
organizational structure
```

No single literature owns all of these. The mechanisms live across:

- R6 Expertise/Learning/Capability Formation;
- R9 Knowledge/State/Memory;
- R10 Organization/Institutions/Ownership;
- R11 Realization/Adoption/Sustainment;
- R15 Runtime/Technical Persistence;
- R17 Management Control where routines become operating management.

A separate family would likely become a grab-bag.

## Decision

# PROMOTE — L16 COVERAGE LENS

**L16 — Organizational Persistence / Institutionalization**

Question:

> If a result must survive the current person, interaction or work episode, what exactly must persist, through which mechanism, with what owner, invocation/use path, authority, maintenance burden, update rule and retirement condition?

Required distinctions where material:

```text
stored information ≠ organizational memory
organizational memory ≠ routine
routine ≠ validated capability
capability ≠ role/authority
policy ≠ actual practice
technical persistence ≠ institutional adoption
repeatability ≠ sustained value
```

Persistence should be evaluated for both **retention** and **adaptability**.

---

# 6. Cross-cutting coherence decision

The sweep also confirms a gap between local work quality and system-level allocation.

A local Work Engine could repeatedly select good next actions while the whole portfolio remains strategically incoherent or overloaded.

## Decision

# PROMOTE — L15 COVERAGE LENS

**L15 — Strategy / Portfolio / Initiative Coherence**

Question:

> Does this work or commitment deserve resources relative to the active strategy, alternative bets, constraints, dependencies and opportunity cost—and what should be stopped, delayed, combined or reallocated?

Check where material:
- strategic contribution;
- portfolio role;
- competing initiatives;
- WIP / capacity / attention;
- dependencies;
- resource commitment;
- reversibility and learning value;
- scale / pause / kill thresholds;
- explicit non-priorities;
- observed outcomes → reprioritization.

This lens is not a requirement to maintain a formal portfolio for ordinary work.

---

# 7. Resulting reference taxonomy

The validated candidate structure is now:

```text
A. SYSTEM / WORK / JOINT-ACTIVITY FOUNDATIONS
R1–R4

B. HUMAN PERFORMANCE / JUDGMENT / EXPLORATION
R5–R8

C. INFORMATION / ORGANIZATION / VALUE
R9–R11

D. ASSURANCE / GOVERNANCE / TECHNICAL REALIZATION
R12–R15

E. STRATEGY / PORTFOLIO / MANAGEMENT CONTROL
R16 Strategic Management, Strategy Formation & Strategic Renewal
R17 Project, Programme, Portfolio, Initiative & Management Control
```

R7 becomes:

`Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research`.

Coverage lenses expand from L1–L14 to:

- L15 Strategy / Portfolio / Initiative Coherence;
- L16 Organizational Persistence / Institutionalization.

Band E is a research-grouping device only. It is **not** a new architectural layer.

---

# 8. Important conflict retained rather than resolved away

Strategy and portfolio management are strongly coupled.

Noda & Bower provide field evidence that strategic commitment emerges through iterative resource allocation. ISO P3M standards separately distinguish programme/portfolio management objects. Management-control research shows feedback/control systems can both shape and be shaped by strategy.

Therefore the correct boundary is not:

```text
Strategy → plan
Portfolio → execute plan
```

but closer to:

```text
Strategic direction / hypotheses
↔ initiative and resource allocation
↔ execution / feedback
↔ realized pattern / outcomes
↔ strategic renewal
```

The architecture must eventually preserve this coupling without collapsing R16 and R17 into one object.

---

# 9. Implications for the System of Interest — but not architecture decisions

This sweep does **not** prove that the final system contains a Strategy Engine, Portfolio Layer, Intelligence Agent or Organizational Memory module.

It establishes only that a general Human–AI Work System may need to explain distinct concerns at multiple scopes:

```text
single work episode
multiple linked work episodes / project
programme / transformation
portfolio of bets and initiatives
strategic direction and renewal
organizational retention / institutionalization
```

This strengthens the hypothesis that the future architecture needs nested focal units and must not infer global optimization from local work optimization.

---

# 10. Gate result

**RED-TEAM DISPUTED REFERENCE COVERAGE:** PASS  
**R16 STRATEGY:** PROMOTE  
**R17 PORTFOLIO/PROGRAMME/INITIATIVE/CONTROL:** PROMOTE  
**INTELLIGENCE:** MERGE INTO EXPANDED R7  
**L15 STRATEGIC/PORTFOLIO COHERENCE:** PROMOTE  
**L16 ORGANIZATIONAL PERSISTENCE:** PROMOTE  
**REFERENCE MAP v0.3:** QUALIFIED FOR WORKING-BASELINE UPDATE  
**WORK ENGINE DESIGN:** STILL BLOCKED

Next:

1. update Reference Map to v0.3;
2. add anchor records for R7/R16/R17/L16 sources;
3. run the broader Anchor & Conflict Sweep across the remaining highest-discrimination families;
4. build the predecessor evidence matrix in parallel;
5. derive `CONCERNS-AND-REQUIREMENTS v0.1` only after those two streams converge.
