# RCA — Runtime Deployment Mapping Failure v0.1

**Status:** MATERIAL RUNTIME REALIZATION DEFECT FOUND — current `main` Runtime migration package v0.4 must not be externally installed until repaired.  
**Date:** 2026-08-20  
**Static architecture:** remains closed; this RCA does not reopen PR #11's static completeness claim.  
**Trigger:** deployment review exposed inconsistent Global/Project instruction packaging, conflation of Capability and Method, and under-bound Handoff/Commitment semantics despite a prior static Runtime PASS.

## 1. Failure statement

The repository currently contains a semantically broad Runtime package, but the deployment model is not sufficiently typed or bound to actual ChatGPT carriers to support installation.

The failure is **not** "the architecture lacks Formation/Decision/Handoff/Commitment". Those semantics exist in the accepted/qualified architecture and prior orchestration model.

The failure is:

> **Runtime type-system collapse + carrier-binding omission.**

The v0.3/v0.2 compilation flattened several fundamentally different semantic kinds under `CONDITIONALLY ACTIVATED CAPABILITIES`, then treated presence in a prompt/package as sufficient realization evidence.

That repeats a known historical failure mode:

```text
semantic presence
≠ activation
≠ accessible method/capability
≠ transition enforcement
≠ deployable runtime mechanism
```

## 2. Normative evidence that the current mapping is wrong

### Requirements baseline

`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` explicitly requires:

- CR-05: applicable professional methods/practices, references, craft and intended-use bar;
- CR-06: comparative composition across Human/AI/tools/experts/workflows/existing process;
- CR-08: capability existence ≠ access ≠ effective capability ≠ authority ≠ verified performance and proposal/decision/acceptance/authorization/execution distinctions;
- CR-10: minimum sufficient work without stage/dependency collapse;
- CR-13: implementation/runtime fidelity and **no unowned material semantic loss**;
- CCR-02: state ownership/write/reconciliation when surfaces diverge;
- CCR-05: future uncertainty / commitment design.

The baseline also says:

```text
requirement ≠ architecture mechanism
architecture mechanism ≠ runtime implementation
```

and does not prescribe a Skill, Project, surface or deployment topology.

### Target Architecture v0.2

The accepted architecture requires:

```text
DISTINCT RESPONSIBILITIES
+ DISTRIBUTED TYPED STATE
+ ADAPTIVE WORK-SELECTION CONTRACT
```

and explicitly states that the architecture-to-runtime program must allocate semantics to actual Humans, AI, tools, state stores, instructions, Skills/workflows and projects/contexts **without copying the whole architecture or losing required semantics**.

### E2E architecture / Runtime Contract

The merged E2E architecture states:

```text
architecture function ≠ product surface
```

and requires runtime evidence for feature existence, account availability, access/binding, effectiveness and authority.

The E2E Operating Runtime Contract further states:

```text
Outcome + requirements + quality
→ required functions / Work Units
→ required capability per function
→ available/effective/authorized modes
→ simplest adequate composition
```

and separately defines:

- Formation activation;
- Professional method / craft activation;
- Capability / teaming allocation;
- Human Gate enforcement;
- Promotion / State Transition;
- Execution / Integration;
- Assurance;
- Transition / Use;
- Learning / Closure;
- runtime carrier allocation.

### Qualified prior Orchestration Model v0.5

`Human-AI-Work-System/core/orchestration-model.md` is even more explicit:

- **Capability selection does not replace method.**
- Method orchestration distinguishes substantive domain method, professional standards, artifact/craft method, evidence method, decision/uncertainty method, implementation/transition method and outcome/benefit evaluation method.
- Capability orchestration distinguishes required capability from actual provider/environment.
- Handoff transfers active responsibility and must preserve a defined minimum state.
- Surface/environment orchestration is selected from Work-Unit requirements, not habit.
- Commitment Design distinguishes WAIT / PILOT / STAGED / REVERSIBLE / FULL COMMIT.

The current Runtime package did not preserve these type boundaries cleanly.

## 3. Exact type errors in Runtime package v0.4

### E1 — `Capability` became a catch-all

Current compilation groups as conditional capabilities:

```text
Formation / Decision / Method / Realization /
Assurance / Promotion / Human Gate /
Transition / Learning / Closure
```

These are not one semantic type.

They include:

- work transformations/functions (`Formation`, `Decision`, `Realization`, `Assurance`, `Transition`, `Learning`);
- control operators/conditions (`Promotion`, `Human Gate`, `Closure`);
- method orchestration (`Method`).

This makes activation, ownership and carrier selection ambiguous.

### E2 — Method policy passed without a method-carrier mechanism

The Runtime says to resolve/apply professional method, but the installation package does not establish:

```text
required method type
→ actual method source/package
→ availability/access
→ applicability/fit
→ method invocation/application
→ assurance of method-relevant product properties
```

Therefore `Professional-method activation PASS` in the prior static review was too strong.

### E3 — Handoff exists in a file but is not bound to the active controller

`realization/E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md` correctly defines a Frontier Handoff Contract and Return Contract.

But the Global/Project compiled instructions do not make that contract an obligatory mechanism whenever responsibility/environment changes.

So:

```text
handoff contract documented
≠ handoff contract activated
```

This is the same label/mechanism problem already identified historically.

### E4 — Commitment, Promotion, Authorization and Handoff lost their distinct control roles

The static architecture correctly distinguishes:

```text
Commitment
≠ Promotion / State Transition
≠ Authorization
≠ Execution
```

But the Runtime compilation does not define a complete transition-control grammar connecting:

```text
Decision-ready candidate
→ Commitment state
→ selected/committed Work Basis
→ authorized frontier
→ Handoff
→ execution
→ return/readiness
→ Promotion / Transition
```

Commitment modes remain mentioned, but the **control relationship to dispatch/handoff and downstream allowed operations is under-specified**.

### E5 — Global + Project payloads were independently authored instead of compiled from one canonical Runtime source

Project Instructions override Global Custom Instructions. That product fact is real.

The repository responded by authoring a second nearly complete 5k Project Runtime policy.

This created two problems:

1. divergence/maintenance risk between Global and Project semantics;
2. no canonical source/compiler relation proving that both payloads are equivalent where they must be and different only where project-local bindings require it.

The defect is not that two product payloads can exist. The defect is that they became **two separately authored Runtime definitions**.

### E6 — Static regression tested semantic coverage, not deployable mechanism closure

`reviews/E2E-RUNTIME-COMPILATION-FULL-STATIC-REGRESSION-v0.3.md` marked many items PASS because a high-level phrase or owner existed.

The missing review question was:

> For every material semantic, what exact runtime object/carrier invokes it, where does required state/method/capability come from, what crosses a surface boundary, and what evidence proves that the mechanism can execute?

That is the CR-13 conformance question.

## 4. Correct runtime type system

The deployment model must keep at least these semantic types distinct.

### T1 — Work Function / Transformation

**What work must happen?**

Examples:

- Admit / Frame;
- Formation;
- Information Acquisition / Evidence Work;
- Decision;
- Work / Realization Formation;
- Execution / Integration;
- Refinement;
- Assurance / Qualification;
- Transition / Use;
- Observation / Evaluation;
- Learning / Change / Closure.

### T2 — Control Operator / Transition Control

**What may change state/responsibility, under what conditions and authority?**

Examples:

- Commitment Design / commitment state;
- Authorization;
- Human Gate / WAIT;
- Promotion / State Transition;
- Handoff / responsibility transfer;
- Readback / reconciliation;
- Reopen / close / stop / retire.

These are not professional methods and not provider capabilities.

### T3 — Method

**How is a selected Work Function performed professionally?**

Examples:

- substantive domain method;
- decision / uncertainty method;
- research / evidence method;
- artifact / craft method;
- assurance / evaluation method;
- implementation / transition method;
- outcome / benefit evaluation method.

### T4 — Capability Provider / Actor

**Who/what can perform the function with the required method?**

Examples:

- Human;
- ChatGPT model in Chat;
- Work agent;
- Codex;
- specialist;
- deterministic tool;
- web/deep research capability;
- app/connector;
- validated workflow / existing process.

### T5 — Surface / Environment

**Where does work execute and what interaction/control affordances exist?**

Examples:

- Chat;
- Work;
- Codex;
- external application/system.

`Project` is primarily a persistent context boundary, not a Work Function or lifecycle stage.

### T6 — State / Knowledge Carrier

**Where does state or reusable knowledge live?**

Examples:

- GitHub / repository;
- Drive;
- tracker / database;
- Project context/files;
- chat history as working context;
- Knowledge Capital / method/reference library.

### T7 — Boundary Contract

**What state must cross a responsibility/environment boundary?**

Examples:

- Frontier Handoff Contract;
- Return Contract;
- Human Gate object;
- Commitment/Work-Basis contract;
- Promotion contract.

## 5. Correct relation among Capability, Method and Surface

The required ordering is:

```text
NEXT LEGITIMATE TRANSITION
        ↓
required Work Function(s)
        ↓
required professional Method(s)
        ↓
required capability characteristics
        ↓
available/effective/authorized Providers
        ↓
Surface / Environment
        ↓
Handoff Contract if responsibility/environment changes
        ↓
Execution
        ↓
Return Contract
        ↓
rebind controlling state
```

A `Skill` is therefore best understood as a **possible carrier/package for a reusable Method or workflow**, not as the definition of capability itself.

## 6. Product facts relevant to the repair

Current official OpenAI documentation establishes:

- Pro Global Custom Instructions support up to **5,000 characters**;
- Project Instructions apply only inside a Project and override Global Custom Instructions;
- Work can run inside a Project and uses that Project's context;
- Chat is intended for quick conversational work;
- Work is intended for longer multi-step work / finished deliverables;
- Codex is the software-development environment;
- Skills are reusable workflow packages that can be automatically used when helpful, but Personal Skills are currently generally documented for Business/Enterprise/Healthcare/Edu, so the Pro Runtime must **not depend on Personal Skills being available**.

No arbitrary 1,000/1,500-character Global target is justified for the Pro deployment. The Global deployment envelope remains up to 5,000 characters.

The current official Project documentation does not publish a Project-Instruction character limit in the reviewed material; the Runtime must measure/verify the actual account UI instead of assuming one.

## 7. What remains valid

Keep:

- Requirements CR-01–13 / CCR-01–07;
- Target Architecture v0.2;
- merged E2E static architecture and transition contracts;
- Commitment ≠ Promotion;
- cross-cutting Orchestrator;
- Parent-Work Continuity;
- typed state and authority distinctions;
- Handoff/Return contract content in `E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md`;
- exact pre-E2E Global rollback snapshot;
- real-use validation protocol.

Do **not** install as controlling Runtime until repaired:

- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.3.md`;
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.2.md`;
- migration/install guidance that treats that pair as installation-ready.

They remain useful evidence/candidates, not the current deployable solution.

## 8. Repair boundary

This is a **Runtime realization defect**, not evidence that the static E2E architecture lacks another conceptual box.

The repair must now produce:

1. one canonical Runtime deployment model/type system;
2. explicit Capability ↔ Method ↔ Provider ↔ Surface mapping;
3. first-class Commitment / Authorization / Promotion / Handoff contracts;
4. one canonical semantic source from which Global and Project instruction payloads are compiled rather than independently authored;
5. a Pro-valid method activation path that does not depend on Personal Skills;
6. a deployment-level CR-01–13 / CCR-01–07 tie-out;
7. readback proving actual product constraints and carrier bindings before installation.

**Current external installation gate: STOP / DO NOT INSTALL v0.3/v0.2.**
