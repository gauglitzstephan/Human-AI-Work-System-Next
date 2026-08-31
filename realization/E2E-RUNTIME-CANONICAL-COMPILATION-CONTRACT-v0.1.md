> **Status override — 2026-08-31: SUPERSEDED FOR CURRENT RUNTIME RELIANCE — HISTORICAL PROVENANCE ONLY. DO NOT INSTALL, EXECUTE OR USE AS CURRENT AUTHORITY. Resolve the current package through `../CURRENT.md` and `README.md`. All internal “current”, “ready” or next-action wording below is historical to its dated episode.**
>

# E2E Runtime Canonical Compilation Contract v0.1

**Status:** CANDIDATE — deployment compiler contract; no external installation.  
**Date:** 2026-08-20  
**Parent:** `realization/E2E-RUNTIME-DEPLOYMENT-MODEL-CANDIDATE-v0.1.md`.

## 1. Problem solved

The prior Runtime package created a Global prompt and a Project prompt as separately authored policy documents. Because Project Instructions override Global Custom Instructions, both attempted to carry near-complete E2E semantics and then drifted in wording/structure.

The repair is:

> **One canonical Runtime semantic source → multiple target-specific compiled views.**

The canonical source is the combination of:

1. accepted requirements / architecture semantics;
2. E2E Operating Runtime Contract;
3. Runtime Deployment Model / type system;
4. qualified prior orchestration semantics explicitly inherited by the merged E2E architecture.

Compiled payloads are derived artifacts, never co-equal policy sources.

## 2. Canonical semantic layers

The canonical source is organized by semantic type, not product surface.

### Layer A — Permanent invariants

- intended outcome / incomplete-input semantics;
- reality, provenance, freshness, uncertainty;
- state/knowledge distinctions;
- capability/access/effectiveness/authority distinctions;
- no downstream-state inference;
- Human agency / non-substitutable contribution;
- minimum sufficient work / preserve qualified state;
- Work Product fidelity;
- claim scope / readiness integrity.

### Layer B — Work Controller

- Parent-Work Continuity;
- next legitimate transition/claim;
- blocker detection;
- Work Function selection;
- method need identification;
- provider/surface selection;
- proportional depth/tooling/decomposition/persistence/assurance;
- close/wait/handoff/stop/no-action.

### Layer C — Control Operators

- Commitment Design / Work Basis;
- Authorization;
- Human Gate / WAIT;
- Handoff / Return;
- Promotion / State Transition;
- Readback / Reconcile;
- Reopen / Close / Stop / Retire.

### Layer D — Conditional Work Functions

- Formation;
- Information Acquisition / Evidence Work;
- Decision;
- Work / Realization Formation;
- Execution / Integration;
- Refinement;
- Assurance;
- Transition / Use;
- Observation / Evaluation;
- Learning / Change.

### Layer E — Method orchestration

- identify required method type;
- source / retrieval;
- access / applicability / fit;
- application;
- method-relevant assurance.

### Layer F — Capability / Provider orchestration

- derive required capability after Work Function + Method;
- compare Human / AI / Work / Codex / tools / specialists / workflows / existing process;
- verify access/effectiveness/authority;
- choose simplest adequate provider/environment.

### Layer G — State / persistence

- authoritative source/owner/write path by state domain;
- working/derived state;
- Project context;
- Knowledge Capital / method library;
- promotion/readback.

## 3. Compiler outputs

### O1 — Global Custom Instructions

Target: ChatGPT Pro Global Custom Instructions.

Purpose: cross-context operating kernel where Global Custom Instructions are active.

Must include enough of Layers A–F to:

- control generic work correctly;
- invoke Handoff/Commitment/Promotion semantics;
- select Method and Provider correctly;
- avoid depending on domain-specific method text.

May reference generic concepts such as `applicable method/source`, but cannot depend on a specific Project state store.

**Target envelope:** up to the current verified Pro limit of 5,000 characters. Do not introduce an arbitrary 1,000/1,500 target.

### O2 — Project Instructions

Target: one Project.

Purpose: local Runtime policy + project bindings in a context where Project Instructions override Global Custom Instructions.

Input:

```text
canonical universal Runtime semantics
+ project outcome/boundary
+ authoritative state pointers
+ local authority/promotion path
+ local constraints
+ local persistence/evidence rules
+ method/reference activation pointers where useful
+ surface defaults where useful
```

The Project payload is generated from the **same canonical semantics**, not rewritten from scratch.

The compiler may compress/rephrase universal semantics for the Project target, but semantic trace must show equivalence.

**Target envelope:** actual Project UI limit must be measured/read back; no assumed numeric limit.

### O3 — Frontier Handoff Contract

Target: Work / Codex / Human / specialist / external environment dispatch.

Generated from current controlling state, not persistent prompt text.

Required fields:

```text
Parent outcome / Work Object
Current state / gate
Exact Work Unit / transformation
Expected parent contribution
Authoritative inputs / pointers
Binding requirements / Performance Model
Applicable method / source
Allowed operations / authority
Relevant assumptions / uncertainty
Commitment / adaptation state where material
Required output / version
Assurance / return condition
Blocked transitions / Human Gate conditions
Persistence / write path if any
```

### O4 — Return Contract

Target: return from Work/Codex/tool/Human provider.

```text
work performed
output / state delta
sources/evidence
method applied
assumptions / blockers
assurance applied
exact supported claim/readiness
writes/actions performed
Human/authority need
recommended next frontier
```

### O5 — Method Pack / Skill / Reference Package

Target depends on product availability:

- Skill when supported;
- Project source/file for local method;
- repository/Drive method library for reusable method;
- task-local retrieval where no reusable pack exists.

A method pack contains professional method logic, examples/criteria/reference as appropriate. It does **not** carry global authority/state policy unless explicitly part of the method's legitimate scope.

### O6 — Promotion / Human Gate object

Generated only when a material transition requires explicit decision/acceptance/authorization/promotion.

## 4. Compilation rules

### C1 — No semantic-type collapse

Do not compile:

```text
Work Function + Control Operator + Method + Provider + Surface
```

into one undifferentiated concept such as `Capability`.

### C2 — No independent policy forks

Global and Project payloads may differ in length/wording, but every universal semantic must trace to the same canonical source version.

### C3 — Carrier reality first

Before compiling to a target carrier, verify:

```text
feature exists
account/workspace availability
actual field/runtime constraint
precedence
context/state access
tool/app availability
write/permission path
```

### C4 — Reallocate, do not silently drop

If target carrier capacity/enforcement is insufficient:

1. reduce wording without semantic loss;
2. move method/reference detail to an accessible Method Pack;
3. move state detail to authoritative source/context;
4. move execution to capable surface/tool;
5. keep claim UNVERIFIED if required semantics cannot be realized.

Do not declare PASS because a high-level label remains.

### C5 — Handoff is compiled dynamically

Do not store every Work handoff in permanent instructions. Permanent instructions define **when and how to compile the Handoff Contract**; the current contract is generated from current state.

### C6 — Commitment travels with Work Basis

When commitment changes allowed downstream work, the Handoff Contract includes the current Commitment / Work Basis and any stop/switch/expand triggers.

### C7 — Promotion never travels as implicit capability

A provider may be technically able to write/execute without owning acceptance/promotion authority. The Handoff Contract must distinguish allowed execution from allowed persistent/control promotion.

### C8 — Method invocation must be resolvable

A compiled Runtime cannot claim `Professional Method activation` unless it defines how the required method source/package is found and accessed in the target context.

## 5. Semantic trace required for every compiled prompt

For each material canonical semantic record:

```text
ID / semantic
canonical source
activation condition
compiled wording/location
external mechanism if not in prompt
provider/state dependency
verification status
```

Statuses:

```text
EMBEDDED
DELEGATED + BOUND
EXTERNAL MECHANISM + VERIFIED
UNVERIFIED
NOT APPLICABLE
```

`DELEGATED` without a bound accessible target is not PASS.

## 6. Product-specific target model

### Global Pro

Current verified constraint:

```text
Custom Instructions maximum: 5,000 characters
```

Use the envelope based on semantic value. Compression is not itself a quality goal.

### Project

Current verified product fact:

```text
Project Instructions override Global Custom Instructions.
```

Therefore Project compilation must preserve necessary universal Runtime semantics locally or through another **proven effective** mechanism.

No numeric Project limit is accepted until actual UI/save/readback evidence establishes it.

### Work

Work is not the global Orchestrator. It is a provider/environment capable of internally orchestrating the **authorized Frontier Contract** it receives.

### Chat

Chat is the default interactive control surface for state rebind, Formation/Decision/Human contribution and bounded work, but not the exclusive owner of those functions.

### Codex

Codex is the preferred specialized provider/environment for software/repository technical work when it fits the frontier.

### Skills

Skills are Method/workflow carriers when available. The current Pro deployment does not assume Personal Skills availability.

## 7. First Project compilation profile — System Weiterentwicklung

Project delta to canonical Runtime:

```text
Outcome:
realize and validate the Human–AI Work System on real work.

Controlling repository state:
main/CURRENT.md

Authoritative state domains:
GitHub paths / decisions / evaluation records as defined.

Promotion path:
candidate branch/artifact
→ assurance/review
→ legitimate Human decision/authority where required
→ PR/merge or authorized write
→ readback/reconcile

Local methods likely to activate:
requirements traceability
architecture review
RCA / failure localization
runtime compilation
regression review
repository/software method
real-use evaluation

Provider defaults:
Chat — interactive control/formation/decision/reconciliation
Work — long multi-step research/analysis/artifacts under Frontier Contract
Codex — repo/software work
GitHub — authoritative repository state/write path
web/apps/tools — retrieval/execution where needed
```

The exact Project Instructions payload is a compiled view of this delta + canonical universal semantics, not a manually maintained second Runtime.

## 8. Acceptance tests for the compiler

Before any new installation package is promoted:

1. Global payload ≤ verified 5,000-char limit;
2. Project payload fits **measured** Project limit;
3. both trace to one canonical source;
4. CR-01–13 / CCR-01–07 deployment tie-out PASS;
5. Commitment / Authorization / Promotion distinct and bound;
6. Handoff + Return contract activation bound;
7. method source/access/application mechanism bound;
8. provider/surface selection follows Work Function + Method;
9. Project/Global precedence tested by readback;
10. no historical protected function regressed;
11. no `label = mechanism` PASS;
12. external installation remains a separate Human transition.

## 9. Current gate

The previous install bundle is superseded for installation.

Next legitimate work:

```text
compile new canonical Global payload
+ measure/confirm Project carrier constraint
+ compile System Development Project payload from same source
+ bind Pro-valid Method Library
+ full deployment regression
+ Human review/merge
```
