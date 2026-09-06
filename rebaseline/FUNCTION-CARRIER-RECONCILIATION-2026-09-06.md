# Function / Carrier Reconciliation — 2026-09-06

**Status:** CANDIDATE reconciliation on `candidate/joint-cognitive-work-architecture-2026-09-06`; no merge, product mutation, CI mutation or architecture promotion implied.  
**Bound repository base:** `main@78ab1b13c8a2bc15802a1d1e2dc5ecf4627113ed`.  
**Purpose:** determine which qualified functions from the prior Human–AI Work System still need active realization, which are already sufficiently owned by the reduced rebaseline, which were correctly demoted with their former mechanisms, and which material activation relations were weakened or lost.

## 1. Executive conclusion

The 2026-09-02 rebaseline direction was substantially correct:

- remove universal Runtime controllers, provider/surface routers, mandatory Formation/Exploration, universal QWS/Work Graph/lifecycle and persistence/assurance by default;
- prefer native ChatGPT for general conversation, reasoning, planning, tool/provider use and product surfaces;
- preserve qualified methods only where they add a differentiated professional transformation;
- preserve durable work semantics independently from the mechanisms that once carried them.

The recurring post-rebaseline failures do **not** justify rebuilding the old architecture.

However, the reduction left one structural weakness:

> **canonical cooperation/work semantics became too tightly coupled to individual runtime carriers, especially Global CI.**

The historical architecture already separated:

```text
canonical semantics
→ product/context-specific compiled views
```

and explicitly treated Global CI, Project Instructions, Handoffs, Provider Returns and Human-facing returns as different realizations. The historical Runtime controller/compiler was overbuilt; the **semantic-source / carrier separation was not**.

Current product reality reinforces this distinction: OpenAI documents Global Custom Instructions as account-level response/behavior preferences, while Project Instructions apply only inside their Project and **override Global Custom Instructions**. GPT-5.6 guidance also favors lean prompts, better intent inference and outcome/context/constraint/success-criteria specification over prescribing every reasoning step.

The smallest coherent future architecture is therefore:

```text
CANONICAL JOINT-WORK SEMANTICS
vendor/product-independent work/cooperation obligations

        ↓ design-time compilation / mapping

PRODUCT / CONTEXT REALIZATION PROFILES
Global CI | Project Instructions | local prompt | Work transition |
Skills/methods | memory/context | domain state / external systems

        ↓

NATIVE RUNTIME EXECUTION
ChatGPT / Work / tools / providers
```

This is **not** a runtime Semantic Compiler, controller or stage machine. `system-development` already owns claim-bounded semantic compilation/reconciliation when a carrier changes.

---

## 2. Source set recovered for this audit

### Current / reduced system

- `baseline/OPERATING-BASELINE.md`
- `baseline/NATIVE-WORK-TRANSITION.md`
- `baseline/SYSTEM-LEARNING.md`
- `baseline/GENUINE-USE-LEARNINGS.md`
- `inventory/PRESERVATION-COVERAGE.md`
- active `decision-analysis`, `evaluate-work-product`, `system-development`
- current Global-CI candidate/review line including PR #60
- `rebaseline/JOINT-COGNITIVE-WORK-ARCHITECTURE-RECONCILIATION-2026-09-06.md`

### Qualified historical semantics / evidence

- `legacy/archive-2026-09-02/foundation/SYSTEM-OF-INTEREST.md`
- `legacy/archive-2026-09-02/foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md`
- `legacy/archive-2026-09-02/architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`
- `legacy/archive-2026-09-02/architecture/ARCHITECTURE-PRINCIPLES-v0.1.md`
- `legacy/archive-2026-09-02/realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`
- `legacy/archive-2026-09-02/realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md`
- `legacy/archive-2026-09-02/evidence/REQUIREMENTS-v0.3-INTERACTION-GAP-CHALLENGE-v0.1.md`
- `legacy/archive-2026-09-02/reviews/GLOBAL-CI-SOLUTION-FORMATION-REGRESSION-REVIEW-v0.1.md`
- `legacy/archive-2026-09-02/reviews/GLOBAL-CI-SOLUTION-FORMING-OWNERSHIP-REGRESSION-REVIEW-v0.2.md`
- demoted `work-formation` and `adaptive-exploration` methods
- rebaseline `DURABLE-LEARNINGS-SEPARATION-2026-09-02.md`

These historical sources remain evidence, not current executable authority.

---

## 3. Current OpenAI product / prompting constraints relevant to carrier design

### 3.1 Global Custom Instructions

Current OpenAI Help documentation describes Custom Instructions as account-level information/instructions ChatGPT should consider in responses. Plus/Pro/Enterprise/Business/Edu currently support up to 5,000 characters.

Use Global CI for **stable cross-context response/cooperation defaults**, not task/domain state, detailed methods, mutable product mechanics or long project briefs.

Official source: https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt

### 3.2 Projects and Project Instructions

Current OpenAI documentation states:

- Projects keep chats, files, instructions and memory/context together for ongoing work;
- Project Instructions apply only in that Project;
- **Project Instructions override Global Custom Instructions**;
- Project memory/context behavior depends on Project memory mode and plan;
- product capabilities available inside Projects may vary with those settings.

Therefore Global CI cannot be assumed to be the active cooperation carrier in every Project context.

Official source: https://help.openai.com/en/articles/10169521-projects-in-chatgpt

### 3.3 Current GPT-5.6 prompting direction

Current GPT-5.6 model guidance says the model has stronger intent understanding and can often infer the user's underlying goal/level of work from context. It recommends continuing to provide material domain context, hard constraints, approval boundaries and success criteria, and explicitly identifying when an important ambiguity should trigger a question.

It also recommends **leaner prompts**, stating each instruction once and removing repeated instructions/examples where evaluations show no benefit.

Official source: https://developers.openai.com/api/docs/guides/latest-model

### Product implication

```text
more semantic coverage
≠ more text in every active carrier

canonical semantic completeness
≠ runtime prompt maximalism
```

The architecture must preserve semantics while allowing lean target-specific realizations.

---

## 4. Function families and lowest suitable owners

`GLOBAL` means a compact stable cooperation invariant is justified in the Global-CI profile where that carrier applies. `CANONICAL` means the semantic belongs in the vendor-independent cooperation source even if a runtime carrier may rely partly on native/local realization.

| Function family | Current need | Lowest suitable owner / carrier | Audit disposition |
|---|---|---|---|
| Purpose / outcome before means | Cross-context | CANONICAL + GLOBAL compact cue | KEEP |
| Problem-Space Sufficiency / current focus ≠ controlling problem | Cross-context for substantial local optimization | CANONICAL; likely compact GLOBAL activation; actual Parent Outcome/context is local/Project/domain state | **RECOVER / SHARPEN** |
| Shared thinking / Joint Intelligence | Cross-context interaction quality | GLOBAL where applicable | KEEP |
| Frame stability + selective reframing | Cross-context | GLOBAL compact cue; native reasoning | KEEP |
| Open exploration / mechanism-distinct alternatives | Conditional | GLOBAL minimal anti-premature-collapse cue; native reasoning; specialist exploration method only when genuinely needed | KEEP COMPACT / NO SKILL DEFAULT |
| Knowledge/reuse/solution intelligence | Cross-context principle | GLOBAL compact fit/reuse cue; native research/providers; domain methods | KEEP / SHARPEN ACTIVATION |
| Solution-form / shallowest adequate realization | Conditional | CANONICAL/native reasoning; task/system-specific method when needed; not a lifecycle | **WATCH — DO NOT BUILD NEW OWNER** |
| Quality-before-simplification | Cross-context | GLOBAL high salience | KEEP |
| Complete Work Product / success conditions / recipient/use maturity | Task-relative | GLOBAL only quality/use principle; actual success criteria in local task/Work Object; Work/evaluator for maturity | MOVE DETAIL LOCAL/WORK |
| Professional method where validity depends | Cross-context trigger, task-specific realization | GLOBAL trigger; Skill/native/domain provider owns actual method | KEEP BOUNDARY |
| Human–AI contribution allocation | Cross-context | GLOBAL principle; task/Work realizes allocation | KEEP |
| Human capability / learning effects | Conditional | GLOBAL small conditional cue; Study/local learning mode or method owns actual pedagogy | KEEP COMPACT |
| Human attention / interaction economics | Cross-context system concern | Operating Baseline + GLOBAL question/offload discipline | KEEP WITHOUT METRICS |
| Common ground / continuity | Cross-context and Project-dependent | GLOBAL where applicable; Project memory/context and local state supply actual basis | KEEP |
| Observability of material state/initiative changes | Cross-context joint activity | GLOBAL compact cue; Work return / UI where applicable | KEEP |
| Predictability / continuation (`Go`, `Next`) | Cross-context joint activity | GLOBAL compact authorization/continuation semantics | KEEP |
| Directability / correction / stop / re-entry | Cross-context | GLOBAL correction boundary; native product control; Work transition for material surface changes | KEEP |
| Human-facing Control Return | Material boundaries only | Native Chat response behavior + `NATIVE-WORK-TRANSITION` return contract; no universal template | DELEGATE / KEEP AS CANONICAL INTERACTION SEMANTIC |
| Recovery of actual accessible state | Cross-context substantial work | GLOBAL trigger + native retrieval/Project context/domain sources | KEEP / HIGH SALIENCE |
| Relevant not maximal context | Cross-context | Operating Baseline + GLOBAL expected-value/convergence cue | KEEP |
| Reality / evidence / uncertainty integrity | Cross-context hard floor | GLOBAL | KEEP |
| Context / retrieved content ≠ authority | Cross-context hard floor | GLOBAL | KEEP |
| Capability/access/effectiveness/authority distinctions | Cross-context hard floor where reliance matters | GLOBAL compact claim boundary; actual product/permissions native | KEEP |
| Fallback / no simulated execution | Cross-context hard floor | GLOBAL | KEEP |
| Source/install/activation/behavior/outcome separation | System-development claims | `system-development`, CURRENT/deployment evidence; not ordinary Global CI except generic claim integrity | KEEP OUT OF ORDINARY CI |
| Minimum sufficient work / upstream prerequisites | Cross-context work selection | CANONICAL + Operating Baseline; compact GLOBAL question/convergence/direct-work cues | **RECOVER RELATION THROUGH PROBLEM-SPACE SUFFICIENCY** |
| Information value / robustness / staged commitment | Conditional decision/uncertainty work | `decision-analysis`, native reasoning, domain method | KEEP OUT OF GLOBAL DETAIL |
| Work decomposition / dependencies / parallelization | Execution architecture | native Work / local Work Architecture | KEEP OUT OF GLOBAL CI |
| Chat→Work transition | Product-specific realization | compact carrier cue only where reliable; `NATIVE-WORK-TRANSITION` owns detailed semantics; dated product profile owns current surface facts | KEEP PRODUCT-BOUND |
| Provider/tool selection | Runtime capability integration | native ChatGPT/Work; Skill/domain method defines need | DO NOT REBUILD ROUTER |
| Project-specific sources / constraints / authority | Persistent initiative context | Project sources/instructions where appropriate + domain-owned authority | KEEP LOCAL |
| Memory / personal context | Persistent personal context | native Memory; evidence/context, not authoritative policy/state | KEEP OUT OF CI POLICY |
| Strategy / portfolio / competing initiatives | Persistent Operating/Strategic context | Human/domain owner + Decision/portfolio methods; not ordinary CI | KEEP OUT OF GLOBAL CI |
| Transition / adoption / outcome / value | Work/domain lifecycle | Work/domain/evaluation methods; GLOBAL only claim distinction | KEEP OUT OF GLOBAL DETAIL |
| Assurance / intended-use evaluation | Claim-relative | `evaluate-work-product` or narrower evaluator; GLOBAL only completion/self-check boundary | KEEP METHOD-OWNED |
| System learning / architecture mutation | System-specific | `SYSTEM-LEARNING` + `system-development` + Human gate | KEEP OUT OF ORDINARY CI |

---

## 5. Materially weakened or forgotten relations

### FCR-01 — Canonical cooperation semantics lost first-class ownership

The current reduced system has durable principles and exact CI sources, but no compact first-class current object that cleanly separates:

```text
what cooperation must mean
from
how ChatGPT currently carries it
```

This has repeatedly caused semantic review to operate directly on a nearly full 5,000-character carrier, making compression loss look like architecture loss and vice versa.

**Recommended direction:** introduce one compact canonical Joint-Work / Cooperation semantic source after review. It must be richer than a runtime prompt but dramatically smaller and less operational than the old 20k+ Runtime semantic/controller source.

It is a **design basis**, not an always-loaded prompt or controller.

### FCR-02 — Product carrier precedence must be explicit

Historical source `E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md` already recorded:

```text
Project Instructions override Global CI
Project view = canonical semantics + local bindings
```

Current official OpenAI documentation still states the override behavior.

Therefore:

- Global CI is not a universal carrier inside every Project;
- Project Instructions must not become an independently authored policy fork;
- Project Instructions should be avoided when no project-specific behavioral instruction is needed;
- when materially needed, they should be a **derived project realization** of the canonical cooperation subset plus genuinely project-specific bindings.

No runtime compiler is required. This is a configuration/change discipline.

### FCR-03 — Problem-Space Sufficiency is the strongest currently identified semantic gap

The historical system already contained:

- `current focus ≠ controlling system`;
- `minimum work ≠ prerequisite omission`;
- Work Formation activating when missing basis could change route/use/method/quality/authority;
- Exploration routes that may change the frame or problem owner;
- Parent continuity in the canonical semantic source.

The rebaseline preserved adjacent meanings but weakened their **preventive activation before substantial local optimization**.

The new `JOINT-COGNITIVE-WORK-ARCHITECTURE-RECONCILIATION-2026-09-06.md` correctly sharpens this as Purpose–Problem–Solution Traceability + Problem-Space Sufficiency.

### FCR-04 — Solution-forming activation was previously diagnosed and should not be forgotten again

The 2026-08-20 ownership review found the issue was **not a missing Solution Formation object**. Existing functions already covered current-system review, reuse, alternative mechanisms, commitment, sufficient definition and realization.

The remaining Runtime gap was:

```text
problem
→ decomposition / meta-work
before
current solution review → solution intelligence → route/form choice → sufficient definition
```

The current Knowledge-Leverage semantics recover much of this. Real use should still watch for bespoke design/build bias and unnecessary meta-architecture before reuse/configuration/instantiation.

Do **not** reactivate the former Skill/controller.

### FCR-05 — Human–AI coordination is a real performance object, not UI decoration

The 2026-08-28 interaction challenge found one genuine conditional Requirement gap: ongoing coordination can fail even if individual state/authority ingredients are locally present.

The surviving useful properties are:

- common ground / qualified continuity;
- observability of material state, initiative and effects;
- predictability of next contribution / continuation;
- directability through correction, stop, recovery and re-entry;
- no manufactured Human Gate or generic question when no Human contribution is needed.

Current CI work already carries much of this. The main residual concern is **carrier reliability**, particularly across Projects/surfaces, not a need for an interaction dashboard or control-state object.

### FCR-06 — Human-facing Control Return should remain a semantic, not a template

Historical Runtime required material returns to make achieved state, next legitimate frontier, next actor and exact Human contribution clear. Its visible control object was too heavy as a universal mechanism.

The durable semantic remains useful:

> At a material boundary, the Human should not have to infer whether work is complete/blocked/candidate, what happens next, or what exact contribution is required.

Current question-discipline and Work return semantics cover part of this. Keep it as a candidate Joint-Work interaction semantic; do not require a fixed response footer.

---

## 6. Things the rebaseline was right to remove as default Runtime

Do **not** restore these merely because their historical documents contain valuable semantics:

- Semantic Compiler as runtime subsystem;
- universal controller / Work Engine;
- global provider router;
- global surface router;
- repo-local Skill registry as provider universe;
- universal QWS / Work Contract;
- universal Work Graph;
- universal B.6 lifecycle / closure machine;
- mandatory `work-formation` Skill;
- mandatory `adaptive-exploration` Skill;
- generic `research-evidence` as default provider;
- persistence by default;
- assurance by default;
- explicit role registry / multi-agent persona topology;
- exhaustive architecture/reference context in every prompt.

The correct operation is:

```text
recover semantic
→ assign smallest legitimate owner
→ test active carrier

not

recover old mechanism
→ reinstall it
```

---

## 7. Proposed stable architecture after reconciliation

This is a Candidate description, not yet promoted architecture.

```text
A. WORK DOMAIN / PURPOSE
   Human values, Parent Outcome, environment, success, constraints

B. CANONICAL JOINT-WORK SEMANTICS
   product-independent cooperation / formation / reality / quality /
   continuity / agency / claim / proportionality obligations

C. WORK FUNCTIONS + QUALIFIED METHODS
   native reasoning/work functions; differentiated Skills / domain methods

D. WORK ORGANIZATION
   Human ↔ AI ↔ tools/providers; authority and allocation

E. PRODUCT / CONTEXT REALIZATION
   Global CI
   Project Instructions + Project context
   local task prompt / Work Object
   Native Work Transition
   Skills/providers/tools/apps
   Memory and domain state

F. EVALUATION / LEARNING
   claim-matched real-use evidence → local repair → bounded promotion
```

### Important non-equivalence

```text
Canonical Joint-Work Semantics
≠ Global CI
≠ Project Instructions
≠ Work Transition
≠ Skill / method
≠ Product runtime
```

Each carrier is a projection/realization of only the semantics it can reliably own.

---

## 8. Recommended carrier discipline

### Global CI

Keep only stable, cross-context, high-salience cooperation invariants whose recurrent omission materially harms work:

- joint thinking/direct response;
- Problem-Space Sufficiency / selective framing;
- quality-before-simplification;
- qualified knowledge/reuse without research bloat;
- Mixed Initiative and Human judgment/authority boundary;
- recovery/continuity / `Go` continuation;
- material-change legibility + correction;
- reality/claim/fallback hard floors;
- proportional completion / convergence.

Do not place detailed methods, work stages, product-state facts, project context, output templates, role lists, provider mappings or assurance procedures in Global CI.

### Project Instructions

Use only for **project-specific behavioral constraints or local cooperation bindings that genuinely need instruction precedence**.

Because they override Global CI, treat them as a derived carrier rather than an independent policy source. If no such instructions are needed, prefer Project files/context/memory over adding Project Instructions merely to repeat the global baseline.

### Project files / Library / Memory

Use for context and knowledge, not policy or authority by storage alone.

- Project files/chat context → ongoing project basis and source material;
- Memory → personal context/preferences that may improve future responses;
- authoritative domain decisions/state → legitimate domain system/source.

### Local prompt / Work Object

Own the current goal, context, actual constraints, success criteria, deliverable/recipient, local role if useful, and task-specific approval boundaries.

This is where OpenAI's Task/Context/Output/Limits/Check style primarily belongs.

### Native Work Transition

Own context-complete transition into sustained native execution. Global CI may contain only the smallest activation cue that proves behaviorally useful.

### Skills / professional providers

Own repeatable transformations where method choice materially affects validity. Method names and provider availability do not belong in Global CI except as a generic trigger to use a qualified method/provider when needed.

### Dated product-state profile

Own mutable facts such as:

- current Project/Memory behavior;
- surface availability;
- Work access and transition affordances;
- model/plan limits;
- installed Skills/plugins;
- current product precedence rules.

Do not promote mutable vendor behavior into permanent architecture semantics.

---

## 9. What is genuinely still open after this audit

1. **Canonical Joint-Work Semantic Source:** exact compact contents and authority location.
2. **Problem-Space Sufficiency:** exact canonical wording and whether a compact runtime cue measurably improves behavior.
3. **Project realization:** how to preserve the cooperation kernel in Projects that use overriding Project Instructions without creating drifting policy forks.
4. **Human-facing Control Return:** whether current direct-answer/question/Work-return semantics are sufficient or one compact global interaction cue remains valuable.
5. **Solution-form activation:** whether Knowledge Leverage + Problem-Space Sufficiency sufficiently prevent premature decomposition/custom building in genuine use.
6. **Global-CI density:** current GPT-5.6 guidance supports leaner prompts; further removal should happen only against the canonical source and representative real-use evidence, not by ad-hoc deletion.

These are bounded realization questions. They do not justify a new architecture stack.

---

## 10. Recommended next architecture move

Do **not** continue patching Global CI directly.

The next bounded system-development object should be:

> **Canonical Joint-Work Semantics Candidate + Carrier Map**

It should:

1. reconcile DL-01–DL-19;
2. reconcile the interaction/coordination semantic from CCR-05;
3. include the newly sharpened Problem-Space Sufficiency relation;
4. preserve the useful solution-forming activation without restoring its old mechanism;
5. distinguish canonical semantics from target-specific runtime cues;
6. produce a carrier matrix for Global CI / Project Instructions / local prompt / Work Transition / Skills / native capability / domain state;
7. explicitly identify intentionally retired historical functions rather than silently losing them;
8. remain short enough to be inspectable, but not constrained by the 5,000-character product field.

Only after that source is accepted should Global CI be recompiled again.

---

## 11. Claim boundary

This audit supports:

> The rebaseline reduction remains the right architectural direction, but a first-class carrier-independent cooperation semantic source and an explicit product/context carrier map are now justified to prevent recurring semantic loss and product-precedence confusion.

It does **not** establish:

- a new accepted architecture;
- a need for a runtime compiler/controller;
- a need to restore archived Skills;
- a Global-CI repair text;
- Project Instructions for every Project;
- behavioral superiority of any carrier;
- merge or product-state authorization.
