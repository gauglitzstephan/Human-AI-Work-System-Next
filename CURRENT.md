# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED TARGET CONCEPTUAL BASELINE v0.2 + STATIC-COMPLETE E2E WORK ARCHITECTURE CANDIDATE v0.1 + RUNTIME DEPLOYMENT REOPENED v0.5  
**Date:** 2026-08-20  
**E2E static package:** promoted via PR #11 — **KEEP CLOSED** absent a named static reopen trigger.  
**Prior Runtime package:** promoted via PR #12 — **REOPENED / DO NOT INSTALL** after deployment-fidelity failure.  
**Repair branch:** `runtime/deployment-mapping-repair-v0.5`  
**Authority boundary:** `main` remains controlling until a repair PR is explicitly accepted/merged. This branch is candidate Runtime repair state. No external ChatGPT settings change is established or authorized by repository state.

## 1. Named Runtime reopen trigger

Deployment review exposed a **CR-13 Runtime / implementation fidelity failure** in the PR #12 package:

> **Runtime type-system collapse + carrier-binding omission.**

The v0.3/v0.2 Runtime pair preserved broad semantic wording but did not cleanly distinguish or bind:

```text
Work Function / Transformation
≠ Control Operator
≠ Method
≠ Capability Provider / Actor
≠ Surface / Environment
≠ State / Knowledge Carrier
≠ Boundary Contract
```

This caused material deployment defects in Method activation, Capability/Provider selection, Handoff/Return, Commitment/Work-Basis and canonical Global/Project compilation.

Static architecture completeness is **not reopened** by this defect.

## 2. Current installation state

```text
Global E2E v0.3 externally installed                 NO
System Weiterentwicklung Project v0.2 installed     NO
Runtime conformance preflight                        NOT STARTED
Representative E2E real-use validation               NOT STARTED
```

**STOP: do not install**:

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.3.md`;
- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.2.md`;
- `realization/E2E-INSTALLATION-BUNDLE-v0.2.md`.

They remain evidence/candidates only.

## 3. Root-cause and requirements reviews

Current repair evidence:

- `reviews/RCA-RUNTIME-DEPLOYMENT-MAPPING-FAILURE-v0.1.md`
- `reviews/E2E-RUNTIME-REQUIREMENTS-AND-DEPLOYMENT-TIEOUT-v0.1.md`

Deployment-level result:

```text
Static E2E architecture                         KEEP / PASS
CR-01–13 semantic ownership                    KEEP
CCR-01–07 semantic ownership                   KEEP
Current PR #12 deployable Runtime              FAIL
CR-13 deployment fidelity                      FAIL
Professional Method deployment mechanism       FAIL in prior package
Capability / Provider type integrity           PARTIAL/FAIL in prior package
Handoff + Return mechanism binding             PARTIAL/FAIL in prior package
Commitment→Work Basis→Authorization binding    PARTIAL in prior package
Global/Project canonical-source relation       FAIL in prior package
```

## 4. Corrected Runtime type model

Current candidate:

- `realization/E2E-RUNTIME-DEPLOYMENT-MODEL-CANDIDATE-v0.1.md`

### T1 — Work Functions / Transformations — WHAT work is needed

```text
Admit / Frame
Formation
Information Acquisition / Evidence Work
Decision
Work / Realization Formation
Execution / Integration
Refinement / Maturity
Assurance / Qualification
Transition / Use
Observation / Evaluation
Learning / Change / Closure
```

These are generic work functions. They are not domain Methods, Skills or product surfaces.

### T2 — Control Operators — WHEN state/responsibility may change

```text
Commitment Design / Commitment State
Authorization
Human Gate / WAIT
Promotion / State Transition
Handoff / Responsibility Transfer
Readback / Reconciliation
Reopen / Close / Stop / Retire
```

### T3 — Methods — HOW selected work is performed professionally

```text
domain / substantive method
professional standard
Formation / framing method
research / evidence method
decision / uncertainty method
artifact / craft method
implementation / transition method
assurance / evaluation method
outcome / benefit evaluation method
```

### T4 — Capability Providers / Actors — WHO/WHAT can perform it

```text
Human
ChatGPT / Chat
Work
Codex
web / Deep Research
tools / Python
apps / connectors
specialist
validated workflow / existing process
```

### T5 — Surface / Environment — WHERE it runs

```text
Chat
Work
Codex
external system / app / environment
```

### T6 — State / Knowledge Carriers — WHERE continuity/knowledge lives

```text
Project context
GitHub / repository
Drive / documents
tracker / database
external System of Record
chat history as working context
method/reference library / Knowledge Capital
```

### T7 — Boundary Contracts — WHAT crosses a boundary

```text
Frontier Handoff Contract
Return Contract
Commitment / Work-Basis Contract
Human Gate Object
Promotion Contract
```

## 5. Capability ↔ Method ↔ Provider ↔ Surface

Concrete mapping:

- `realization/E2E-CAPABILITY-METHOD-PROVIDER-MAP-v0.1.md`

Required order:

```text
next legitimate transition
→ required Work Function(s)
→ required professional Method(s)
→ required capability characteristics
→ available/effective/authorized Provider(s)
→ Surface / Environment
→ Handoff Contract if responsibility/environment changes
→ Execution
→ Return Contract
→ rebind controlling parent state
```

A Skill is a **possible carrier for a Method/workflow**, not the definition of Capability.

`Research` is typed as:

```text
Work Function = Information Acquisition / Evidence Work
Method        = research / source-appraisal / synthesis method
Provider      = web / Deep Research / Human expert / app / data source
Surface       = Chat / Work / external system
```

## 6. Handoff / Commitment / Authorization / Promotion

First-class Runtime contract:

- `realization/E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md`

Preserve:

```text
Decision
≠ Commitment
≠ Authorization
≠ Handoff
≠ Execution
≠ Promotion / State Transition
```

A material multi-surface route may require:

```text
Decision-ready candidate
→ Decision
→ Commitment / Work Basis
→ Authorization
→ Handoff / Dispatch
→ Execution + Integration
→ Return Contract
→ Qualified result / readiness
→ Acceptance / Authorization / Promotion as applicable
→ Transition / Use
```

Work/Codex receive only the bounded frontier and authority explicitly handed off. They do not self-promote or inherit parent authority.

## 7. Method activation

A professional-method requirement is satisfied only by this mechanism:

```text
required Work Function + performance bar
→ required method type
→ find / retrieve method source/package
→ establish availability + provenance + fit + transferability
→ apply proportionately
→ assure method-relevant product / claim properties
```

Possible Method carriers:

```text
Skill/workflow when account supports it
repository / Drive method library
Project source/file for local method
authoritative external reference
task-local retrieval/research
Human specialist
```

Current Pro Runtime must **not depend on Personal Skills** being available. If Skills later become available, they may package the same Methods without changing architecture.

## 8. Canonical Runtime compilation

Current compiler contract:

- `realization/E2E-RUNTIME-CANONICAL-COMPILATION-CONTRACT-v0.1.md`

New invariant:

> **One canonical Runtime semantic source → target-specific compiled views.**

Global Custom Instructions and Project Instructions must not be separately authored co-equal policies.

Compiler outputs may include:

```text
Global Custom Instructions
Project Instructions
Frontier Handoff Contract
Return Contract
Method Pack / Skill / Reference Package
Human Gate / Promotion object
```

For every compiled target preserve semantic trace and actual carrier constraints.

## 9. Product deployment constraints

Current supported product facts for this program:

```text
Pro Global Custom Instructions limit           5,000 characters
Project Instructions override Global CI        YES
Work can run inside Project context             YES
Personal Skills required for Pro Runtime        NO
Numeric Project Instruction limit               UNVERIFIED — must measure actual UI/save/readback
```

There is **no 1,000/1,500-character Global target**. Use the available 5,000-character envelope where it improves semantic fidelity.

## 10. System Development first-project model

Project:

```text
System Weiterentwicklung Projekt
Repository: gauglitzstephan/Human-AI-Work-System-Next
Controlling repository program state: main/CURRENT.md
```

Project-local Method candidates include:

```text
System Architecture / Requirements Method
Existing-System Recovery Method
RCA / Failure Localization Method
Runtime Compilation / Semantic Regression Method
Repository Promotion / Readback Method
Real-Use Validation Method
```

Provider defaults remain conditional:

```text
Chat   → interactive control / Formation / Decision / reconciliation
Work   → long research/analysis/artifact frontier under Handoff Contract
Codex  → repository/software frontier
GitHub → authoritative repository state by defined domain
web/apps/tools → evidence / execution / deterministic capability
Human  → non-substitutable values/judgment/acceptance/authority
```

These are defaults, not architecture identities.

## 11. Current gate / next work

```text
R0 detect deployment defect                         COMPLETE
R1 persist RCA                                      COMPLETE
R2 gather CR-01–13 / CCR-01–07 + prior controls    COMPLETE
R3 correct Runtime type/deployment model            COMPLETE — candidate
R4 bind Capability / Method / Provider / Surface    COMPLETE — candidate
R5 bind Handoff / Return / Commitment / Promotion   COMPLETE — candidate
R6 define one-source compilation contract           COMPLETE — candidate
R7 measure actual Project Instructions constraint   PENDING — product/UI evidence
R8 compile new Global Pro payload ≤5,000            PENDING
R9 compile first Project payload from same source    PENDING after R7
R10 bind first Pro-valid Method Library              PENDING
R11 full mechanism-level deployment regression       PENDING
R12 Human review / repository promotion              PENDING
R13 external installation/readback                   BLOCKED
R14 first real-work validation                       BLOCKED until install/readback
```

**Mode:** RUNTIME DEPLOYMENT REPAIR — DO NOT INSTALL PRIOR v0.3/v0.2 PAIR.
