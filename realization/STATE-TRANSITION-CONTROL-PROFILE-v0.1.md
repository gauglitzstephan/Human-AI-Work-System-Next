# State-Transition Control Profile v0.1

**Status:** REALIZATION CANDIDATE / NON-CONTROLLING / NOT INSTALLED  
**Scope:** persistent or state-changing Human–AI work only  
**Parent:** accepted Target Architecture v0.2  
**Purpose:** operationalize existing semantics; do **not** add a new architecture layer, lifecycle, or universal subsystem.

## 1. Problem being solved

The Target Architecture already requires:

- current authoritative state before consequential redesign;
- typed separation of proposal / decision / acceptance / authorization / execution / verification / outcome;
- minimum justified next work;
- legitimate change ownership;
- semantic preservation through runtime realization;
- bounded reopening rather than global restart.

The current failure is not primarily missing conceptual semantics. It is that a conversational model can still generate a locally coherent continuation without reliably enforcing those semantics as a persistent state transition.

A model response is therefore treated as a **candidate computation**, not as a state transition.

This profile introduces one realization contract for mutations:

```text
RECOVER / READ
→ PROPOSE
→ DECIDE / AUTHORIZE
→ EXECUTE
→ VERIFY
→ PROMOTE
→ READBACK / CLOSE
```

These are **transaction states for consequential change**, not a replacement for B.6, not a universal work lifecycle, and not mandatory for bounded non-mutating work.

---

## 2. Placement in Target Architecture v0.2

### Distinct Responsibilities

| Transition function | Primary responsibility | Meaning |
|---|---|---|
| Recover / Read | Work + Execution | retrieve actual authoritative state and runtime facts |
| Propose | Work | create a candidate delta; no authority transfer |
| Decide / Authorize | legitimate owner | accept/reject the exact proposed transition |
| Execute | Execution | perform only the authorized operation in the actual runtime |
| Verify | Work + Learning/Change + applicable assurance | establish what changed and whether the transition claim is supported |
| Promote | legitimate owner + Execution write path | make the verified candidate controlling/accepted where authorized |
| Readback / Close | Work + Execution | re-read the promoted state and establish the new parent state |

`Responsibility ≠ Actor`: the same Human/AI/tool may perform several functions, but state types and authorities remain distinct.

### Distributed Typed State

The persistent control state is represented by a machine-readable **Work-Control Record**. It does not replace domain-owned authoritative state. It records only the minimum control information required to bind a state-changing continuation to the correct parent, authority, base state, allowed delta, verification and promotion event.

### Adaptive Work-Selection Contract

For a material continuation, the next-work selector receives the Work-Control Record plus freshly retrieved runtime state. It may select only work compatible with the current transaction status and `allowed_operation`.

If the record conflicts with authoritative runtime state, first determine whether the conflict is **material to the contemplated transition**.

- If material: state-changing execution/promotion in the affected scope is blocked; conflict recovery or re-authorization is the admissible frontier.
- If not material: explicitly bounded analysis, evidence gathering or isolated candidate work may proceed when it cannot mutate/promote the disputed state and has legitimate authorization.

A plausible interpretation of the conflict is never a substitute for this discrimination.

---

## 3. Work-Control Record

The companion file `WORK-CONTROL-RECORD-v0.1.json` is the candidate persistent representation.

Minimum fields:

```text
control_version
system
runtime_readback
controlling_baseline
active_program
active_transition
conflicts
learning_refs
```

For an active transition, preserve at least:

```text
id
status
parent_ref
parent_state
next_claim_or_transition
allowed_operation
proposed_delta
protected_state
authority
base_ref + base_sha
working_branch
verification_required
promotion_event
```

The record is deliberately small. Architecture documents, evidence, requirements and domain state remain in their legitimate stores and are referenced rather than copied.

---

## 4. Transition contract

### T0 — RECOVER / READ

Required before a material continuation or state-changing operation.

Establish from authoritative sources:

- actual repository / system / object identity;
- actual base ref and immutable version/SHA where available;
- accepted/controlling decisions and their acceptance events;
- active parent program / gate;
- current transition status;
- outstanding conflicts;
- legitimate decision/write authority.

**Output state:** `RECOVERED` or `CONTROL_CONFLICT`.

For each conflict, determine its affected scope. If it materially changes the legality, parent binding, authority, base state or success claim of the contemplated transition, block that transition until recovery/re-authorization. Unaffected isolated work may continue only when explicitly bounded and unable to promote/mutate the disputed state.

### T1 — PROPOSE

A proposal must identify:

- exact unmet claim/problem;
- exact proposed delta;
- why change is needed;
- preserved state / protected semantics;
- alternatives where materially live;
- evidence required to discriminate or verify;
- expected receiving state if successful.

**Output state:** `PROPOSED`.

A model-generated proposal has no acceptance, authorization or promotion authority by itself.

### T2 — DECIDE / AUTHORIZE

A legitimate owner decides the exact delta and operation scope.

The decision must bind:

- accepted/rejected candidate identity;
- authorized operation;
- allowed files/objects/systems or semantic scope;
- protected state;
- required verification;
- promotion authority.

**Output state:** `AUTHORIZED` or `REJECTED`.

For this repository's conceptual architecture, ADR-0002 identifies the Human repository owner as decision owner. Other domains may bind authority differently.

### T3 — EXECUTE

Execution must begin from the exact authorized base state.

Rules:

1. re-read the base ref immediately before mutation when drift is possible;
2. if base SHA/state differs materially for the authorized operation, return to `CONTROL_CONFLICT` or re-authorization;
3. mutate only the authorized delta;
4. do not perform opportunistic redesign/cleanup;
5. preserve execution evidence and actual returned state.

**Output state:** `EXECUTED`, never automatically `VERIFIED`.

### T4 — VERIFY

Verification establishes the exact claim supported by the resulting state.

At minimum where applicable:

- exact changed object/files versus authorized delta;
- protected-state regression;
- requirement/semantic coverage affected by the change;
- deterministic constraints;
- professional/intended-use behavior where the claim depends on it;
- state/authority integrity;
- runtime readback.

Producer self-review is used only where it has sufficient detection capability; otherwise use a materially different evaluator/reference/test.

**Output state:** `VERIFIED`, `FAILED`, or `UNVERIFIED`.

### T5 — PROMOTE

Promotion is a separate authorized state transition.

Examples:

- merge an accepted PR;
- update a canonical state pointer;
- install/activate a runtime candidate;
- write an accepted decision to the legitimate source of record.

A file existing on a branch, a successful execution, or a model recommendation is not promotion.

**Output state:** `PROMOTED` only after the actual promotion event is observed.

### T6 — READBACK / CLOSE

After promotion:

1. re-read the authoritative target state;
2. confirm the promotion event and resulting version/ref;
3. update the Work-Control Record parent state;
4. close the transition or bind the next legitimate transition.

If a pointer/document disagrees with the promotion event or actual system state, record `CONTROL_CONFLICT`; do not manufacture closure.

---

## 5. Hard invariants

For work under this profile:

```text
assistant answer ≠ proposal unless explicitly typed as one
proposal ≠ decision
human/model preference ≠ authorization
execution attempt ≠ completion
execution result ≠ verification
verification ≠ acceptance
branch/file existence ≠ promotion
merge/install/write event ≠ successful readback
historical next-step text ≠ current parent state
```

A child task does not become the root program merely because it is the most recent conversational topic.

---

## 6. Runtime enforcement levels

### L0 — Conversational / instruction-only

The model is instructed to recover and bind state before continuation.

Useful, but **not hard enforcement**: the same model can fail to activate or follow the instruction.

### L1 — Tool-backed read/write discipline

Before state-dependent reasoning or mutation, the runtime retrieves the Work-Control Record plus actual system state through tools. Writes are permitted only when the record and authoritative state support the operation and the requested operation is within authorized scope.

This materially reduces reliance on conversational memory.

### L2 — Deterministic transaction guard

An external orchestrator/wrapper enforces:

- mandatory state load;
- base-version/SHA precondition;
- status transition legality;
- conflict-scope discrimination;
- allowed-operation scope;
- write authorization;
- verification requirements;
- promotion/readback preconditions;
- trace retention.

This is the first level that can provide **hard** workflow enforcement rather than policy-by-prompt.

Target Architecture v0.2 does not require L2 for all work. It becomes justified where persistence, consequence, repeated drift or authority divergence makes instruction-only control insufficient.

---

## 7. ChatGPT product implication

ChatGPT Custom Instructions, Project Instructions, memory and conversation history are context/behavior carriers. They can improve activation and continuity but are not by themselves a transactional source of record or a deterministic workflow engine.

Therefore:

- retain load-bearing global behavioral semantics unless evidence supports relocation;
- use external/domain-owned state for facts and decisions;
- use a Work-Control Record for mutation-control continuity when material;
- use tool reads to rehydrate actual state rather than trusting conversational summaries;
- use an external runtime/agent guard only when hard enforcement is worth its cost.

This profile does **not** claim that a Project, Skill, custom GPT, agent, room or repository file automatically solves the problem. Each is only a possible carrier and must be evaluated against actual activation, inheritance, authority and failure behavior.

---

## 8. Iterative improvement loop

Failures improve the system only through evidence-qualified change:

```text
observed failure
→ reconstruct first invalid transition
→ classify failure location:
   architecture / control profile / carrier / activation / execution / assurance / authority
→ propose smallest repair
→ test against incumbent + relevant regression cases
→ authorize
→ implement
→ verify
→ promote only if net-positive
```

Do **not** append a new global rule merely because one response failed.

The persistent learning record should point to concrete evidence/incident artifacts through `learning_refs`; accepted behavioral/runtime changes remain versioned through normal repository decisions/PRs.

---

## 9. Current candidate acceptance criteria

This profile should not become controlling merely because it is conceptually neat.

Before promotion, establish at least:

1. **Continuation test:** a stale/historical `next` instruction cannot override the bound parent/gate.
2. **State-conflict test:** conflicting `CURRENT.md` versus actual acceptance/merge state yields a typed conflict and blocks only affected transitions rather than either guessing or freezing unrelated work.
3. **Unauthorized-write test:** a proposed change cannot execute before explicit authorization.
4. **Scope test:** execution cannot silently expand beyond the authorized delta.
5. **Promotion test:** branch/file existence cannot become accepted state without the real promotion event.
6. **Readback test:** after promotion, the new authoritative state is re-read before further continuation.
7. **Simple-work collapse test:** ordinary bounded non-mutating work does not acquire unnecessary transaction ceremony.
8. **Human-burden test:** the mechanism reduces correction/recovery burden enough to justify its coordination cost.

Until these tests are passed, this file is a **candidate realization mechanism**, not an accepted runtime.

---

## 10. Non-claims

This candidate does not:

- reopen Target Architecture v0.2;
- replace B.6;
- introduce a sixth architecture responsibility;
- require one global state store;
- make `CURRENT.md` epistemic truth;
- guarantee that ChatGPT will obey the protocol in instruction-only mode;
- authorize CI changes, Project changes, Skill installation, agents, automations or external actions;
- authorize a merge or production activation.
