# Reference Map Red Team v0.1 — Strategy, Intelligence, Portfolio and Operating Management

**Status:** COMPLETE / TARGETED REPAIR CANDIDATE  
**Date:** 2026-08-19  
**Target:** `REFERENCE-MAP.md` v0.2  
**Question:** Does v0.2 cover the full System-of-Interest research surface when work spans strategic direction, intelligence, multiple initiatives, programmes/portfolios, execution steering and organizational persistence?

This is a **coverage red team**, not a literature synthesis and not an architecture change.

---

## 1. Adversarial test

The map is attacked with six cases that should be explainable without forcing one reference family to absorb several distinct problems.

### T1 — Strategy formation
A user or organization must decide **which game to play**, what position/capabilities to build, what not to do, and how to adapt strategy as reality changes.

### T2 — Strategic intelligence
A changing external environment must be monitored, interpreted and coupled to strategic choices and signposts.

### T3 — Initiative portfolio
Twenty-five locally plausible initiatives compete for money, attention, time and organizational capacity. The system must prioritize, sequence, stage, kill, scale and rebalance them.

### T4 — Programme / transformation management
Several interdependent workstreams must jointly produce a strategic outcome that no individual project can deliver alone.

### T5 — Strategy execution / management control
The organization has chosen a strategy, but actual decisions, resource allocations, operational behavior and feedback drift away from it.

### T6 — Organizational persistence
Useful work must persist not merely as documents, but selectively as routines, capabilities, roles, decision rights, processes, knowledge, assets, systems or institutionalized practices—and later be adapted or retired.

Pass condition: each case can be located in the Reference Map without category error, hidden dependence on one oversized family, or premature architecture assumptions.

---

# 2. Verdict

## v0.2 = NO FREEZE

The map remains broadly sound, but the red team exposes **two material reference-family gaps and two cross-cutting lens gaps**.

### Material gap A — Strategy is under-specified

`R7 Decision / Metareasoning` can explain a bounded decision; `R10 Organization / Economics` can explain incentives, markets, assets and allocation conditions; `R11 Realization` can explain implementation and outcomes.

None alone adequately owns the literature on:

- strategic direction and choice;
- positioning and competitive advantage;
- coherent systems of activities / choices;
- capability building and renewal;
- deliberate versus emergent strategy;
- strategy process and formation;
- strategic commitments and resource allocation over time;
- strategic adaptation / renewal;
- the relation between strategy, structure and management control.

This matters because **a sequence of good local decisions does not automatically constitute a good strategy**.

### Material gap B — Multi-initiative management is under-specified

A Work Engine or episode-level work model could make each case locally efficient while the overall system still fails through:

- too many simultaneous initiatives;
- resource fragmentation;
- missing strategic priority;
- unowned dependencies;
- inability to kill weak bets;
- programme-level benefit failure;
- WIP / attention overload;
- local project success with portfolio failure;
- no mechanism to rebalance after new evidence.

`R2 Work Systems`, `R7 OR/decision`, `R10 Organization/Economics`, `R11 Realization` and `R15 Runtime` each cover part of this, but none owns **project–programme–portfolio / initiative management and management-control theory as a coherent reference field**.

---

# 3. Internal evidence that triggered the red team

Internal sources are discovery evidence, not external authority.

## 3.1 Prior strategic-intelligence work

Historical Personal Intelligence System work already distinguished:

- Strategic Terrain and Positioning Map;
- Strategy Coherence Gate;
- Foresight Warning and Signpost Control;
- Option Portfolio and Commitment Control;
- Actor Incentive and Power Map;
- Leverage Point / Intervention Depth;
- Decision Quality / Field Judgment;
- Deliberate / Emergent / Realized Strategy Loop.

It also used the rules `priority before execution`, `terrain before strategy`, and `options before big bets`.

This is evidence that bounded decision quality and strategic-system quality were repeatedly experienced as different problems.

## 3.2 Prior Goal–Outcome Steering

`JOINT_WORK_ARCHITECTURE_v0.3.1_rc.md` contains:

```text
Overarching Goal
→ Outcome Hierarchy
→ Current Gap
→ Active Cases / Bets
→ Episode Target Stage
→ Delivered / Accepted Result
→ Observed Outcome
→ Goal Contribution / Reprioritization
```

It also recognizes project admission/closure when work spans sessions, workstreams, dependencies, monitoring and future outcome review.

## 3.3 Prior portfolio work

Notion `PLAYBOOK: PORTFOLIO OPTIMIZATION` explicitly models a **Decision + Execution Portfolio**, not an investment portfolio, with:

- resource / attention allocation;
- Explore → Validate → Scale → Kill;
- downside and reversibility;
- learning velocity;
- strategic alignment;
- portfolio reallocation after feedback;
- concentration risk and kill discipline.

The object is historically over-specified and not accepted here, but the recurring need is real: **portfolio state is not episode state**.

## 3.4 Prior strategy system

Notion `AI-Native Strategy Development System` explicitly connected strategy to beliefs, external reality, execution friction, decisions, execution feedback and strategy adjustment.

Again, the historical ontology is not imported; the evidence is that strategy repeatedly required its own problem grammar.

---

# 4. External reference challenge

A bounded outside-view check confirms that these are established fields rather than locally invented categories.

## 4.1 Strategic management / strategy process

Candidate anchors:

- Mintzberg & Waters (1985), **Of Strategies, Deliberate and Emergent**, *Strategic Management Journal* — strategy formation spans deliberate and emergent patterns.
  - DOI: https://doi.org/10.1002/SMJ.4250060306
- Noda & Bower (1996), **Strategy Making as Iterated Processes of Resource Allocation**, *Strategic Management Journal* — strategy making in complex firms can be understood as iterated multilevel resource-allocation processes.
  - DOI: https://doi.org/10.1002/smj.4250171011
- Teece, Pisano & Shuen (1997), **Dynamic Capabilities and Strategic Management**, *Strategic Management Journal* — strategic advantage under changing environments depends partly on organizational capabilities to integrate, build and reconfigure competences.
  - DOI: https://doi.org/10.1002/(SICI)1097-0266(199708)18:7%3C509::AID-SMJ882%3E3.0.CO;2-Z
- Simons (1994), **How New Top Managers Use Control Systems as Levers of Strategic Renewal**, *Strategic Management Journal* — formal control systems can be used in strategic change and renewal rather than only operational compliance.
  - DOI: https://doi.org/10.1002/smj.4250150301

These sources answer a different question from ordinary decision analysis: **how direction, commitments, resources, capabilities, organizational attention and emergent learning form strategy over time**.

## 4.2 Strategic intelligence

- ISO 56006:2021, **Innovation management — Tools and methods for strategic intelligence management — Guidance**.
  - https://www.iso.org/standard/72621.html

ISO 56006 explicitly treats strategic intelligence at strategic and operational levels and notes that the discipline is transversal beyond innovation when knowledge is required for strategic decisions and consequent action.

This supports making `Intelligence` highly visible, but does **not** yet justify a separate family from sensemaking/decision/foresight. It can remain inside an expanded R7 unless the Anchor/Conflict Sweep finds a distinct theory boundary.

## 4.3 Project, programme and portfolio management

The ISO/TC 258 family explicitly separates these objects:

- ISO 21500:2021 — context and concepts for project, programme and portfolio management;
- ISO 21502:2020 — project management;
- ISO 21503:2022 — programme management;
- ISO 21504:2022 — portfolio management;
- ISO 21505:2017 — governance;
- ISO 21513:2026 — post-project and post-programme evaluation.

Relevant official pages:
- https://www.iso.org/standard/75704.html
- https://committee.iso.org/sites/tc258/home/projects/published/iso-21503.html
- https://www.iso.org/standard/82867.html
- https://committee.iso.org/sites/tc258/home/projects.html

The existence of distinct standards does not prove that all their practices belong in HAWS. It does establish that **project, programme and portfolio are different management objects with different concerns and should not be collapsed into an episode-level work model**.

---

# 5. Candidate repair

## R7 — rename and sharpen, not split yet

### Current
`Sensemaking, Decision, Metareasoning, Foresight & Operations Research`

### Candidate
`Intelligence, Sensemaking, Decision, Metareasoning, Foresight & Operations Research`

Add explicit questions:
- How are intelligence requirements derived from decisions, strategy, preparation needs or monitoring conditions?
- How should source portfolios, baselines, signals, change/noise, competing explanations and signposts update situation models?
- When should intelligence produce a one-time answer versus a longitudinal watch?

Add seed targets:
- strategic / competitive intelligence;
- intelligence analysis and structured analytic tradecraft;
- ISO 56006:2021 where transferable.

**Reason not to create a separate Intelligence family yet:** intelligence is an epistemic/sensemaking function whose value is downstream decision/action/monitor coupling. The red team has not shown that it requires a sufficiently distinct architecture concern to justify another family.

---

## NEW R16 — Strategic Management, Strategy Formation & Strategic Renewal

**Primary questions**
- What is the strategy actually trying to accomplish, for whom, and over what horizon?
- How are strategic issues/arenas selected before individual initiatives are optimized?
- What choices, positions, activity systems, capabilities, commitments and exclusions create coherence?
- How do deliberate intent and emergent realized patterns interact?
- How should strategy adapt as beliefs, environment, capabilities and outcomes change?
- Which resources and organizational attention must be committed, withheld or reallocated?
- How do competitive dynamics, complementarities, path dependence and option value shape strategy?
- How is strategy distinguished from a goal, plan, portfolio, operating model, decision or list of initiatives?

**Seed schools / targets**
- strategy process and formation;
- competitive strategy / industrial organization;
- resource-based view and isolating mechanisms;
- dynamic capabilities / strategic renewal;
- strategy as choice / coherent activity system;
- corporate strategy and resource allocation;
- real-options logic where commitment matters;
- strategic management control / strategy execution;
- behavioral strategy where managerial cognition materially matters.

**Import role**
Direction, coherent choice, positioning, capability development, strategic commitments, renewal and the relation between intended and realized strategy.

**Boundary**
R16 does not own every decision, every business analysis, project execution, portfolio administration or runtime operation. `Strategy` must not become a universal label for important work.

---

## NEW R17 — Project, Programme, Portfolio, Initiative & Management Control

**Primary questions**
- When should work be managed as a project, programme, portfolio, initiative/bet, continuous operation or ordinary episode?
- How are multiple initiatives admitted, prioritized, sequenced, funded, staffed, constrained, paused, killed, scaled or retired?
- How should shared dependencies, scarce resources, WIP, attention and bottlenecks be managed across work?
- When do multiple projects need programme-level coordination because benefits depend on combined change?
- How does a portfolio express strategy without becoming a static list of projects?
- How should management control connect strategy, resource allocation, execution signals, exceptions and corrective action?
- What is the right cadence and control depth for operational steering without process theatre?
- How are benefits, residual obligations and learning evaluated after completion?

**Seed schools / targets**
- project / programme / portfolio management;
- project portfolio management and innovation portfolio management;
- programme benefits realization;
- management control systems / Levers of Control;
- execution/operating management;
- operations management / theory of constraints where bottlenecks matter;
- portfolio selection under uncertainty / staged experimentation;
- organizational routines and governance where multiple initiatives interact.

**Import role**
Cross-case prioritization, multi-initiative coordination, resource/WIP control, programme integration, portfolio governance, execution steering and post-completion evaluation.

**Boundary**
Do not import enterprise PMO ceremony into small personal work. A project-management method is not the universal Work Engine. Portfolio logic activates only when several competing or interdependent commitments make local optimization insufficient.

---

# 6. New cross-cutting lens candidates

## L15 — Strategy / Portfolio / Initiative Coherence

**Question:** Is the local work worth doing relative to other possible work, and does the set of active commitments form a coherent strategy and resource allocation?

Check where material:
- strategic contribution;
- priority / opportunity cost;
- active-bet portfolio;
- WIP / attention load;
- dependencies and bottlenecks;
- resource allocation;
- explore / validate / scale / stop state;
- kill / pause / reprioritize criteria;
- what explicitly should **not** be done;
- feedback from outcomes into strategy and portfolio.

This lens prevents a locally excellent Work Engine from optimizing the wrong portfolio.

---

## L16 — Organizational Persistence / Institutionalization

**Question:** If something should survive the current episode or people involved, **what exactly should persist, where, under whose ownership, with what maintenance and retirement conditions?**

Candidate persistence forms:

```text
context / working state
knowledge / reference
record / decision
routine / process
method / skill
validated capability
role / responsibility
policy / rule
relationship / trust
technical system / automation
asset / data / IP
organizational or institutional practice
```

Check:
- future-use mechanism;
- refind/invocation path;
- owner / authority;
- validity horizon;
- maintenance burden;
- capability formation / deskilling effect;
- adoption/institutionalization;
- supersession / retirement.

### Why a lens rather than a family

Organizational persistence is already explained by several fields:
- R6 learning/capability formation;
- R9 knowledge/state/memory;
- R10 organization/institutions/ownership;
- R11 realization/adoption/sustainment;
- R15 technical persistence/configuration.

The failure is **cross-field fragmentation**, not absence of external reference domains. A lens forces integration without inventing another discipline.

---

# 7. `Execution Strategy` decomposition

The historical phrase `Execution Strategy` has repeatedly caused level mixing. The red team recommends **not** creating one reference family with that name.

Keep these distinct:

```text
Strategic direction / strategic choices
    → R16 Strategy

Portfolio / programme / initiative allocation and steering
    → R17 Portfolio & Management Control

Work-episode route / method / execution design
    → R2 + R7 + future Work-Control architecture

Implementation / adoption / change into real use
    → R11 Realization

Technical execution / agent / tool composition
    → R14 AI/Agent/Capability Engineering

Runtime reliability / transaction / observability
    → R15 Software/Platform Runtime
```

This separation is expected to resolve part of the recurrent `Strategy ↔ Execution ↔ Work ↔ Runtime` category confusion.

---

# 8. Does the four-band structure survive?

**No as a freeze, yes as a grouping concept.**

The four existing bands were only organizational aids, never architecture. With R16/R17, a fifth research band is cleaner:

```text
E. STRATEGY / PORTFOLIO / OPERATING MANAGEMENT
   R16 Strategic Management, Strategy Formation & Strategic Renewal
   R17 Project, Programme, Portfolio, Initiative & Management Control
```

This does **not** imply a fifth system layer.

A reference family can inform several future architecture views, and a future architecture view can draw from several families.

---

# 9. Stress-test disposition

| Attack case | v0.2 | Repair candidate |
|---|---|---|
| T1 Strategy formation | PARTIAL / fragmented R7+R10 | R16 |
| T2 Strategic intelligence | PARTIAL but structurally fit | sharpen R7 |
| T3 Initiative portfolio | FAIL / no clear owner | R17 + L15 |
| T4 Programme / transformation | PARTIAL / fragmented | R17 |
| T5 Strategy execution / management control | PARTIAL / fragmented R10+R11 | R16 + R17 |
| T6 Organizational persistence | COVERED BUT FRAGMENTED | L16 |

**Result:** TARGETED REPAIR REQUIRED.

---

# 10. Promotion recommendation

Do **not** silently rewrite `REFERENCE-MAP.md` to v0.3 yet.

The proper next step is now slightly sharper than the prior gate:

```text
Reference Map v0.2
+ Red Team v0.1
+ R16/R17/L15/L16 candidate delta
        ↓
Reference Anchor & Conflict Sweep v0.1
        ↓
VERIFY / MODIFY / REJECT the delta
        ↓
Reference Map v0.3 working baseline
```

The Anchor & Conflict Sweep should therefore begin with the four disputed areas:

1. Strategy formation / renewal;
2. project–programme–portfolio / initiative management and management control;
3. intelligence as R7 subfield versus separate family;
4. organizational persistence as cross-cutting lens versus family.

Only after these are resolved should the sweep broaden to the other high-priority reference families.

---

# 11. Current state

```text
Reference Map v0.2                         WORKING BASELINE
Coverage Audit v0.1                       PASS for broad-domain discovery
Targeted Red Team v0.1                    COMPLETE
R16 Strategy                              CANDIDATE
R17 Portfolio/Programme/Initiative        CANDIDATE
R7 Intelligence expansion                CANDIDATE
L15 Strategy/Portfolio coherence          CANDIDATE
L16 Organizational persistence            CANDIDATE
Reference Map v0.3                        NOT YET PROMOTED
Work Engine / conceptual architecture     STILL BLOCKED
```
