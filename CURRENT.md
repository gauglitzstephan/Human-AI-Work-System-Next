# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / ARCHITECTURE → RUNTIME / OPERATING REALIZATION  
**Date:** 2026-08-20  
**Acceptance event:** PR #3 merged on 2026-08-19 as `0b2dc8f3d369cc5d0e5c8ec502449ccf11c7464e`  
**Authority boundary:** this file controls repository navigation and current program state. Normative architecture/requirement meaning remains in the accepted baseline documents referenced below.

## 1. Parent system and parent work

### System of Interest

The default System of Interest remains the **Human–AI Work System** defined in `foundation/SYSTEM-OF-INTEREST.md`:

> the socio-technical configuration of Human actor(s), AI capabilities, tools/workflows, relevant methods, state/knowledge, authority/control mechanisms and interfaces that jointly perform the work.

Boundary selection remains claim-relative: narrower technical/runtime or wider operating/organizational scope is used only when the claim requires it.

### Parent program / Work Object

The repository-level parent program is:

> **Develop, realize and evaluate a general Human–AI Work System that improves real professional work by composing Human judgment and agency, AI capabilities, tools, methods, knowledge/state, authority, assurance and operating mechanisms appropriately for the situation, while preserving proportionality, recoverability and learning.**

A runtime mechanism, Skill, Project topology, state-control mechanism, Semantic Compiler, Work Graph or other child construct does **not** become the parent merely because it is the current topic.

---

## 2. Program path and completed state

The repository was initialized with this development path:

```text
Purpose / Problem / Operational Context
+ External reference landscape
+ Internal / real-use evidence
↓
Concerns & Requirements
↓
Conceptual alternatives / discrimination
↓
Candidate architecture
↓
Verification / falsification
↓
Accepted conceptual architecture
↓
Runtime / Operating Realization
↓
Behavioral + implementation evaluation
↓
Evidence-driven improvement / selective reopen
```

Current state:

```text
System / SoI foundation                         ESTABLISHED FOR CURRENT CLAIM BOUNDARY
Reference + predecessor / real-use evidence     ESTABLISHED AS BASELINE EVIDENCE
Concerns & Requirements v0.1                    ACCEPTED BASELINE VIA PR #3
Target Architecture v0.2                        ACCEPTED BASELINE VIA PR #3
Foundational architecture expansion             CLOSED BY DEFAULT
Current program                                 ARCHITECTURE → RUNTIME / OPERATING REALIZATION
Behavioral superiority / runtime effectiveness  NOT ESTABLISHED
```

---

## 3. Controlling baseline documents

Use these for current normative meaning:

1. `CURRENT.md` — repository program/navigation state.
2. `foundation/SYSTEM-OF-INTEREST.md` — parent problem / default claim-relative SoI and boundary semantics.
3. `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` — 11 Concerns / 13 Core Requirements / 7 Conditional Requirements.
4. `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md` — accepted conceptual architecture baseline.
5. `decisions/ADR-0002-target-conceptual-baseline.md` — acceptance boundary, consequences and reopen triggers.
6. `architecture/ARCHITECTURE-METHOD.md` — lineage/reopen/change discipline.
7. `evaluation/EVALUATION-STRATEGY.md` — evaluation claim classes, baselines and promotion discipline.
8. `evidence/EVIDENCE-MAP.md` plus predecessor/lineage artifacts — evidence/provenance, not independent current-program authority.

`Concerns & Requirements v0.1`, `Target Architecture v0.2` and ADR-0002 retain pre-merge `PROPOSED` metadata for provenance. Their containing PR #3 was explicitly merged; ADR-0002 defines that merge as the acceptance event. Do not reinterpret those files as unaccepted because their embedded pre-merge header was not rewritten.

Historical bootstrap/reference/differential artifacts may retain old `Next`, `Current gate` or candidate language. Those statements are provenance unless explicitly promoted here.

---

## 4. Accepted conceptual architecture

Target Architecture v0.2 makes three structural commitments:

```text
A. DISTINCT RESPONSIBILITIES
   Strategic / Operating / Work / Execution / Learning-Change

B. DISTRIBUTED TYPED STATE
   authoritative state remains with legitimate owners/stores;
   working context is composed as needed

C. ADAPTIVE WORK-SELECTION CONTRACT
   for admitted/triggered work, select the minimum justified next work
   from current reality, intended outcome/claim, requirements, preserved state,
   dependencies, capability/authority/runtime reality, consequence, uncertainty
   and economics
```

These are conceptual commitments, not mandatory runtime layers, a central state store, a universal Work Graph, a fixed lifecycle or a required Semantic Compiler subsystem.

Important retained boundaries include:

- input/proposed means ≠ complete requirement/outcome;
- fact/observation ≠ inference/assumption/judgment/forecast/scenario;
- working/context state ≠ authoritative operational state ≠ reusable knowledge;
- capability ≠ access ≠ effective performance ≠ authority ≠ acceptance/accountability;
- professional quality ≠ evidence/assurance about quality;
- Work Product ≠ transition ≠ use ≠ outcome ≠ causal effect ≠ value;
- architecture acceptance ≠ runtime realization ≠ behavioral effectiveness.

---

## 5. Current program — Architecture → Runtime / Operating Realization

The accepted baseline now has to be realized as an actual working system.

The realization problem is:

> determine how the baseline's material semantics are carried by actual Humans, AI/models, Custom/Project Instructions, tools/apps, state stores, capabilities, Skills/workflows, Projects/contexts, permissions, authority, execution mechanisms and operating practices — while preserving qualified existing behavior and avoiding unnecessary implementation structure.

### Current realization entry condition

Before proposing a realization change:

1. recover the **actual current realization / incumbent** from authoritative product/runtime state and qualified predecessor evidence;
2. map accepted requirements/semantics to the carriers that already satisfy them;
3. identify only material unmet, unreliable or unowned realization claims;
4. preserve already-qualified behavior unless a named delta/reopen trigger exists;
5. compare the smallest credible realization alternatives against the incumbent;
6. evaluate behavioral, state/authority, Human-burden, recipient/use and economics effects before promotion.

The current program is therefore **whole-system realization**, not CI compression, Skill creation, agent topology, Project restructuring or any other carrier-specific optimization by default.

### Current gate

> **Establish the current whole-system realization baseline and its material coverage/gaps against the accepted Target Architecture before changing realization.**

A narrower child experiment may be run only when explicitly bound to this parent and when it addresses a demonstrated realization gap.

---

## 6. Qualified predecessor / incumbent discipline

Qualified predecessors remain evidence/design priors within their accepted scope:

- `AI-native-Operating-Model` v0.2;
- `human-ai-work-architecture` v1.3.1;
- `PAOS` as the minimum-complexity/native-surface counter-design;
- `Human-AI-Work-System` later B.6/Core/runtime line and its real-use/failure evidence.

Repository artifacts do not prove that a runtime is currently installed or behaviorally effective. Actual product/runtime state must be read where material.

No prior runtime mechanism is removed, relocated or replaced merely because another carrier is cleaner or smaller. A realization change must earn its delta against the best realistic incumbent.

---

## 7. Historical / non-controlling branches and attempts

- PR #2 — closed/unmerged; its Δ4 decision basis was explicitly retracted and is non-controlling.
- PR #4 — closed/unmerged; any realization claims on that branch are evidence/hypotheses only unless independently re-qualified.
- Other candidate branches/files — existence is not acceptance, installation, promotion or current program authority.

The previous bootstrap sequence `Δ4 → Δ5 → Δ6` is historical after PR #3 acceptance. Individual findings may remain useful evidence, but the sequence no longer controls development.

---

## 8. Reopen and change rule

Foundational architecture reopens only for a named material trigger from ADR-0002:

- changed System of Interest / intended claim;
- new external evidence materially contradicting the baseline;
- repeated/consequential real-use failure not cleanly representable or locally repairable;
- materially simpler rival satisfying the same requirements at lower burden;
- implementation/runtime impossibility or systematic semantic loss;
- unowned requirement / semantic regression / hidden mandatory structure;
- material responsibility/authority contradiction;
- newly established legitimate concern/requirement.

Without such a trigger, repair at realization/method/operating scope and preserve unaffected architecture.

For any state-changing repository work, proposal/decision/authorization/execution/verification/promotion remain distinct. A branch, file, model recommendation or successful write does not by itself become controlling state.

---

## 9. Next higher-level sequence

```text
CURRENT
Architecture → Runtime / Operating Realization
↓
whole-system realization baseline / coverage recovery
↓
only demonstrated realization deltas
↓
behavioral + implementation evaluation on heterogeneous real work
↓
local repair / capability promotion / operating change where evidence supports it
↓
selective architecture reopen only if a named trigger is established
```

This sequence remains subordinate to the parent outcome: a functioning, evidence-improving Human–AI Work System rather than accumulation of architecture or runtime machinery.
