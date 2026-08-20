# E2E Runtime Requirements & Deployment Tie-Out v0.1

**Status:** DEPLOYMENT-LEVEL REVIEW — current `main` Runtime package v0.4 = FAIL / REOPENED; corrected deployment model v0.1 = conceptually owned, compilation still pending.  
**Date:** 2026-08-20  
**Scope:** all material requirements and previously qualified control semantics relevant to current ChatGPT Pro Runtime realization.

## 1. Review question

Does the current deployable Runtime map every material requirement to an actual semantic type, mechanism, provider/carrier and boundary contract — rather than merely mention the requirement in instruction text?

A deployment PASS requires:

```text
requirement
→ architecture owner
→ runtime semantic type
→ activation condition
→ method if needed
→ provider / surface
→ state / authority source
→ boundary contract if crossing responsibility/environment
→ enforcement / evidence
```

A phrase in a prompt is not enough.

## 2. Requirements basis

Normative / controlling architecture basis:

- `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` — CR-01–13 / CCR-01–07;
- `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`;
- `architecture/E2E-WORK-ARCHITECTURE-CANDIDATE-v0.1.md`;
- `realization/E2E-OPERATING-RUNTIME-CONTRACT-CANDIDATE-v0.1.md`;
- `reviews/E2E-STATIC-CLOSURE-REVIEW-v0.1.md`.

Qualified prior semantics still explicitly relied upon by the merged architecture:

- `Human-AI-Work-System/core/orchestration-model.md` v0.5;
- `Human-AI-Work-System/core/dynamic-work-model.md` v0.5;
- Parent-Work Continuity amendment;
- historical failure-family regressions summarized in the E2E Static Closure Review.

Current product facts are separately verified from official OpenAI documentation.

## 3. Core Requirements CR-01–13

| Requirement | Required deployment semantics | Current main v0.4 | Corrected deployment owner |
|---|---|---|---|
| **CR-01 Outcome before means** | Human input/proposed means must not become full requirement/decision; Formation must be activatable before consequential route commitment | **PARTIAL/PASS semantics** — present in prompt | Work Function: Formation; Controller activation; Decision/Commitment control |
| **CR-02 Claim-relative scope** | Scope must travel with claim/decision/action and not silently transfer across project/surface/provider boundaries | **PARTIAL** — scope language exists, Handoff binding incomplete | Typed state + Frontier Handoff / Return contracts |
| **CR-03 Reality / epistemic integrity** | authoritative/current reality, provenance, freshness, fact/inference/forecast distinction | **PASS semantic / carrier incomplete** | State carrier + retrieval provider + invariant; Return Contract preserves source/evidence |
| **CR-04 Current state before change** | existing-system repair/change starts from actual authoritative baseline | **PASS semantic** | Controller + Information Acquisition + state carrier (e.g. GitHub) |
| **CR-05 Professional sufficiency + evidence-qualified reuse** | identify performance bar; resolve/apply substantive/craft/evidence methods; qualified reuse | **FAIL deployment** — method policy mentioned but no bound method source/access/invocation mechanism | Method Activation Contract + method library/Skill when available/task-local retrieval + assurance |
| **CR-06 Comparative Human–AI composition** | required-function-first then capability/provider comparison with actual access/effectiveness/authority | **PARTIAL** — provider comparisons exist but `capability` type conflated with work functions/method | Capability/Provider Orchestration Contract |
| **CR-07 Human agency / legitimate contribution / legibility** | Human only where non-substitutable; material state/decision/gate legible | **PARTIAL** — Human Gate semantics present; cross-surface handoff/return not fully bound | Human Gate + Handoff/Return + shared-state legibility |
| **CR-08 Capability/access/authority integrity** | capability existence/access/effectiveness/authority separate; proposal/decision/acceptance/authorization/execution distinct | **PARTIAL** — semantic list present; provider and transition controls incompletely typed | Provider model + Authorization + Commitment + Promotion + Return Contract |
| **CR-09 State / knowledge integrity** | working context ≠ authoritative operational state ≠ reusable knowledge; owner/write path per domain | **PARTIAL** — GitHub mapping exists but Project/Global policy duplication risks state/policy divergence | State/Knowledge carrier model + canonical Runtime source + promotion/readback |
| **CR-10 Minimum sufficient work / preservation / transition integrity** | activate only value-bearing work; preserve qualified state; no dependency collapse | **PARTIAL** — minimum frontier strong, but duplicate Global/Project Runtime policies and untyped capability catalog create unnecessary/control burden | Controller selects Work Functions; canonical compiled views; boundary contracts only when needed |
| **CR-11 Claim-matched detection-capable assurance** | exact claim/scope + capable assurance actually applied; representative validation when inspection insufficient | **PARTIAL** — assurance semantics strong; method/provider binding incomplete | Assurance Work Function + Assurance Method + provider + evidence in Return Contract |
| **CR-12 Realization / outcome integrity** | Work Product→receiving context→transition→use→mechanism→outcome→value; no downstream inference | **PASS semantic / handoff partial** | Transition/Use Work Function + receiving-context Handoff + observation/outcome owner |
| **CR-13 Runtime / implementation fidelity** | actual instruction precedence, state/context access, methods, tools, permissions, surfaces; no semantic loss under compilation | **FAIL** | Corrected Deployment Model + canonical compiler + product constraint readback + mechanism-level conformance |

**Core verdict:** current main v0.4 cannot be externally installed as a conformant Runtime because **CR-13 fails** and causes partial ownership defects in CR-05/06/07/08/09/10/11.

The static architecture itself remains unaffected.

## 4. Conditional Requirements CCR-01–07

| Conditional Requirement | Deployment trigger / mechanism | Current main v0.4 | Corrected owner |
|---|---|---|---|
| **CCR-01 Open framing/search** | when frame/solution route open, activate Formation + Evidence Work + distinct alternatives/counterevidence/simpler/no-action | **PASS semantic** | Formation / Decision Work Functions + evidence/decision methods |
| **CCR-02 Persistent/divergent state** | multi-turn/multi-surface divergence → authoritative source/owner/write/freshness/reconciliation | **PARTIAL** | State carrier model + Handoff/Return + readback/reconciliation |
| **CCR-03 Consequential risk/control** | consequence/irreversibility/privacy/security → authority, containment, rollback/recovery | **PARTIAL/PASS semantic** | Control Operators + provider/environment selection + transition method |
| **CCR-04 Recipient/use-dependent maturity** | candidate≠recipient-ready → product transformation then re-assure | **PASS semantic** | Refinement Work Function + craft method + recipient/assurance provider |
| **CCR-05 Future uncertainty/commitment** | material external uncertainty → learn/robustify/stage/signpost; explicit commitment mode | **PARTIAL** — modes present, connection to Work Basis/Handoff under-specified | Decision + uncertainty method + Commitment/Work-Basis Contract |
| **CCR-06 Competing initiatives/resources** | local work competes for strategic resources → higher-level priority/opportunity-cost authority | **PARTIAL** | Strategic/Operating context; Controller cannot silently own portfolio decision |
| **CCR-07 Human capability formation** | Human learning/authorship/future capability is outcome/delegation risk → allocation considers it | **PASS semantic** | Capability/Provider selection + Human contribution class |

## 5. Architecture-derived control requirements that must survive deployment

These are not new CRs; they are explicit architecture/runtime obligations already accepted or qualified.

### AR-01 — Commitment ≠ Promotion ≠ Authorization ≠ Execution

Required:

```text
Decision
→ Commitment state
→ Work Basis
→ Authorization for exact action
→ Execution
→ Result/readiness
→ Promotion / State Transition when status/control changes
```

**Current main:** PARTIAL. Commitment modes and Promotion exist, but dispatch/Handoff does not explicitly consume the Work Basis/commitment state.

### AR-02 — Orchestrator is cross-cutting

Required: select next legitimate frontier across framing, evidence, decision, work, execution, assurance, transition, learning, stop/no-action.

**Current main:** PASS semantics; deployment type system must keep Controller separate from provider/surface.

### AR-03 — Parent-Work Continuity

Required:

```text
parent outcome / Work Object
+ current parent state/gate
+ child contribution
+ allowed operation
```

must survive continuation and handoff.

**Current main:** PARTIAL — Controller has fields; Handoff contract not active/bound.

### AR-04 — Professional Method activation is a mechanism

Required:

```text
method needed
→ resolve/retrieve source
→ establish access/applicability
→ apply
→ assure method-relevant result
```

**Current main:** FAIL deployment mechanism.

### AR-05 — Capability selection does not replace method

Required by qualified Orchestration Model v0.5.

**Current main:** FAIL type integrity because `Method` and multiple Work Functions were grouped under `conditional capabilities`.

### AR-06 — Handoff is responsibility/environment transfer

Required minimum state includes objective/parent outcome, evidence/artifacts, completed work, assumptions/constraints, dependencies, readiness, commitment/adaptation state, realization/transition state, next contribution/action and authority boundary.

**Current main:** Handoff contract exists in `E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md`, but active Runtime instructions do not bind its use. **PARTIAL / mechanism not closed.**

### AR-07 — Return / reintegration after Handoff

Required: output/delta/evidence/method/assurance/writes/blockers → rebind parent → decide next frontier.

**Current main:** documented, not bound. **PARTIAL.**

### AR-08 — Human Gate must enforce WAIT

Required: blocked transition + exact Human contribution + mature decision object + no blocked downstream execution + re-entry.

**Current main:** semantic PASS; behavior unverified. Corrected model preserves as Control Operator.

### AR-09 — Work Product fidelity

Required: produce requested Work Product, not a framework/process substitute unless intended.

**Current main:** PASS semantic.

### AR-10 — Next-use refinement ≠ assurance

Required: refinement transforms product; assurance evaluates claim.

**Current main:** PASS semantic.

### AR-11 — Surface ≠ architecture function

Required:

```text
Formation ≠ Chat
Execution ≠ Work
Assurance ≠ separate room
Project ≠ lifecycle stage
Work Unit ≠ Work run
```

**Current main:** stated correctly in surface allocation. Corrected deployment model preserves dynamic selection.

### AR-12 — Project ≠ authoritative state store by default

Required: Project is context boundary; authoritative records remain domain-owned.

**Current main:** generally PASS; project/runtime prompt duplication creates policy-state divergence risk.

### AR-13 — Learning ≠ automatic Change

Required: evidence → learning/change candidate → legitimate owner/decision/promotion.

**Current main:** PASS semantic.

### AR-14 — Closure/Handoff/Wait/Stop are legitimate frontiers

Required: no work merely because possible.

**Current main:** PASS semantic.

## 6. Qualified Orchestration requirements recovered from prior core

The merged E2E architecture explicitly preserves prior ownership from the qualified Orchestration Model; therefore these semantics remain deployment-relevant.

### QO-01 Initiative modes

```text
AI ACTS
AI PROPOSES
AI ASKS
AI HANDS OFF
AI MONITORS / CHECKS
AI STOPS / ESCALATES
```

Selection depends on objective clarity, capability, authority, Human contribution, reversibility, verification and receiving-system readiness.

### QO-02 Handoff continuity

A responsibility/environment handoff must preserve enough state to prevent `handoff amnesia`.

### QO-03 Capability orchestration

```text
Outcome + requirements + quality
→ Work Units / realization needs
→ required capability
→ provider options
→ selected actor/environment
→ execution + integration + transition + assurance composition
```

### QO-04 Method orchestration

Capability does not replace method. Method types include domain, standards, artifact/craft, evidence, evaluation, decision/uncertainty, implementation/transition and outcome/benefit evaluation.

### QO-05 Surface/environment orchestration

Environment is selected from Work-Unit requirements. Movement between environments is a state/Handoff transition.

### QO-06 Commitment Design

```text
LEARN
ROBUSTIFY
STAGE / PRESERVE OPTION
COMMIT
```

with WAIT/PILOT/STAGED/REVERSIBLE/FULL commitment semantics where material.

### QO-07 Representative-use validation

When inspection cannot establish intended-use fitness, use a realistic test/pilot/shadow run/scenario/user rehearsal/end-to-end test/limited rollout/first-use monitoring proportionately.

## 7. Product deployment requirements — current official ChatGPT reality

These are runtime constraints, not architecture requirements.

### PD-01 Global Custom Instructions

For Plus/Pro/Enterprise/Business/Education, current official release notes support up to **5,000 characters**.

Deployment implication: **no 1,000/1,500 character target** is justified for the Pro Global Runtime. Use the 5k envelope when it improves semantic fidelity.

### PD-02 Project Instructions precedence

Official Project documentation states Project Instructions apply only inside that Project and **override Global Custom Instructions**.

Deployment implication: Project Runtime semantics cannot assume Global inheritance.

### PD-03 Project context

Projects group chats, files/sources and instructions; Work can start inside a Project and uses Project context.

Deployment implication: do not copy Project state into every Work prompt; hand off only the material frontier state not already reliably present in Project context.

### PD-04 Chat / Work / Codex

Official product roles:

- Chat = fast conversational assistance / questions / search / brainstorming;
- Work = longer multi-step work / research / analysis / finished deliverables;
- Codex = software-development / technical work.

Deployment implication: default routing is useful, but logical functions remain dynamically allocated.

### PD-05 Skills availability

Official Skills documentation says Personal Skills are generally available for Business/Enterprise/Healthcare/Edu. Pro must not depend on Personal Skills being available.

Deployment implication: Method activation requires a Pro-valid fallback such as a reusable method library in repo/Drive/Project sources or task-local retrieval. If Skills become available, they are a method/workflow carrier, not a new architecture function.

### PD-06 Project Instruction limit

No reviewed official product source currently establishes a numeric Project-Instruction character limit.

Deployment implication: **do not assume 5k, 3k, 1.5k or any other value**. Measure actual UI/save/readback before compilation acceptance.

## 8. Current main package failure localization

```text
STATIC ARCHITECTURE                 PASS / KEEP CLOSED
E2E OPERATING RUNTIME CONTRACT      KEEP
SURFACE ALLOCATION + HANDOFF TEXT   KEEP AS QUALIFIED INPUT
GLOBAL v0.3                         EVIDENCE ONLY / DO NOT INSTALL
PROJECT v0.2                        EVIDENCE ONLY / DO NOT INSTALL
STATIC RUNTIME REGRESSION v0.3      SUPERSEDED — wrong PASS question
MIGRATION MANIFEST v0.4             SUPERSEDED FOR INSTALLATION
INSTALL BUNDLE v0.2                 SUPERSEDED FOR INSTALLATION
```

Named trigger for Runtime reopen:

> **CR-13 deployment fidelity failure: type-system collapse and missing carrier/mechanism binding for Method, Capability, Handoff and Commitment/Work-Basis semantics.**

This trigger does not require a static-architecture reopen.

## 9. Corrected Deployment Model status

`realization/E2E-RUNTIME-DEPLOYMENT-MODEL-CANDIDATE-v0.1.md` now assigns:

```text
Work Function
≠ Control Operator
≠ Method
≠ Capability Provider
≠ Surface / Environment
≠ State / Knowledge Carrier
≠ Boundary Contract
```

and defines explicit:

- Method Activation Contract;
- Capability/Provider Orchestration Contract;
- Frontier Handoff Contract;
- Return Contract;
- Commitment / Work-Basis Contract;
- Promotion Contract;
- Message/interaction types;
- Chat/Work/Codex/Project/GitHub product mapping;
- one-canonical-source compilation rule.

**Deployment-model verdict:** conceptual ownership restored; actual compiled prompts/carriers still require a new compilation/readback review before installation.

## 10. Next legitimate program

```text
RCA + complete requirements tie-out
→ canonical Runtime semantic source
→ derive Global Pro payload (≤5,000 actual limit)
→ derive first Project payload from SAME source + project delta, within measured Project limit
→ bind method library / Pro-valid method activation
→ bind Handoff + Return + Commitment/Promotion contracts
→ full mechanism-level deployment regression
→ Human review/merge
→ external installation/readback
→ real work
```

Do not install the current main v0.3/v0.2 pair.
