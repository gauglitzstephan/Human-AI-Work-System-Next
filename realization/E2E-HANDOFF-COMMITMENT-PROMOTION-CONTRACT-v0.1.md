# E2E Handoff / Commitment / Authorization / Promotion Contract v0.1

**Status:** CANDIDATE — first-class Runtime control contract; no external installation.  
**Date:** 2026-08-20  
**Basis:** merged E2E architecture + E2E Operating Runtime Contract + qualified Orchestration Model v0.5 + Surface Allocation v0.1.

## 1. Purpose

Make four historically conflated controls executable and keep them distinct:

```text
Commitment
≠ Authorization
≠ Handoff
≠ Promotion / State Transition
```

A fifth mechanism, **Return / Rebind**, closes the responsibility/environment loop after a Handoff.

These are Control Operators / Boundary Contracts. They are not Work Functions, professional Methods, provider Capabilities or product Surfaces.

## 2. Control sequence

A consequential multi-surface route can require:

```text
DECISION-READY CANDIDATE
        ↓
DECISION
        ↓
COMMITMENT
        ↓
SELECTED / COMMITTED WORK BASIS
        ↓
AUTHORIZATION
        ↓
HANDOFF / DISPATCH if responsibility or environment changes
        ↓
EXECUTION + INTEGRATION
        ↓
RETURN CONTRACT
        ↓
QUALIFIED RESULT / READINESS
        ↓
ACCEPT / AUTHORIZE / PROMOTE as applicable
        ↓
TRANSITION / USE
```

Not every bounded task activates every control.

## 3. Commitment Contract

### 3.1 Question

> How far are we choosing and activating this route now, given evidence, uncertainty, downside, information value and option value?

### 3.2 Commitment modes

Local vocabulary may vary; preserve the semantic distinction among:

```text
WAIT
PILOT / TEST
STAGED COMMITMENT
REVERSIBLE ACTION
ACTION THAT GENERATES INFORMATION
FULL COMMITMENT
```

### 3.3 Minimum Commitment / Work-Basis state

Where material:

```text
Decision object / decision question
Selected route / option
Commitment mode
Decision owner / authority
Material assumptions / uncertainty
Requirements / Performance Model / success floor
Expected Work Product / next-use target
Known dependencies / blockers
Relevant horizon
Stop / switch / expand / recommit signposts where material
Residual open decisions
```

### 3.4 Commitment does not do

Commitment does **not** automatically:

- authorize an external action;
- authorize a repository/state write;
- accept a result;
- promote candidate state;
- establish completion/readiness/outcome;
- give the receiving provider unlimited discretion.

## 4. Authorization Contract

### 4.1 Question

> What exact action, transition or state write may this actor/provider perform now?

### 4.2 Minimum authorization state

```text
Actor / provider
Allowed operation
Object / system / state domain
Scope / constraints
Point-of-effect conditions
Write/action path
Forbidden or blocked transitions
Expiration / revalidation condition where material
```

Authorization must be revalidated before material effect when runtime state, consequence, identity, permission or assumptions may have changed.

Technical ability is not authorization.

## 5. Frontier Handoff Contract

### 5.1 Trigger

Compile a Handoff Contract when **active responsibility or execution environment materially changes**, including dispatch to:

- Work;
- Codex;
- Human/specialist;
- external execution environment;
- another agent/workflow where context is not safely implicit.

A trivial internal tool call inside an already-bounded frontier does not require ceremony if the necessary state remains intact.

### 5.2 Required Handoff state

Use the minimum sufficient subset of:

```text
Parent outcome / Work Object
Current parent state / gate
Exact Work Unit / transformation
Expected child→parent contribution
Current Commitment / Work Basis
Authoritative inputs / source pointers
Binding requirements / Performance Model
Applicable professional Method / source
Allowed operations / Authorization
Relevant assumptions / uncertainty / signposts
Dependencies / interfaces
Required output / version
Assurance / return condition
Blocked transitions / Human Gate conditions
Persistence / write path if any
```

### 5.3 Handoff rule

```text
Handoff ≠ delegation of parent authority
Handoff ≠ acceptance
Handoff ≠ promotion
```

The receiving provider owns only the bounded frontier and authority explicitly transferred.

## 6. Return Contract

Every material Handoff must define how control returns.

Return:

```text
Work actually performed
Output / state delta
Exact child→parent contribution
Sources / evidence used
Method actually applied
Assumptions made / changed
Unresolved blockers / dependencies
Assurance actually applied
Exact supported claim / readiness
Actions / writes actually performed
Current transition/use state if changed
Human contribution / new authority required
Recommended next frontier
```

On return:

```text
RECEIVE
→ READBACK material writes/actions
→ REBIND parent Work Object/state/gate
→ INTEGRATE child result
→ QUALIFY exact parent state
→ choose next frontier
```

No child/provider result self-promotes to parent completion.

## 7. Human Gate Contract

### 7.1 Trigger

A Human Gate exists only when a material transition cannot legitimately/effectively occur without Human-exclusive:

```text
truth / context
values / judgment
expertise
authorship / learning
acceptance / responsibility
authority / commitment
```

### 7.2 Required Gate object

```text
Blocked transition
Current mature decision/work object
Exact Human contribution needed
Why AI/retrieval/robust proceeding cannot substitute
Relevant evidence / trade-offs
What can continue safely in parallel, if anything
WAIT / blocked downstream execution
Re-entry condition
```

Human Gate is not a generic review request.

## 8. Promotion / State-Transition Contract

### 8.1 Question

> May this working/candidate state acquire a stronger semantic or controlling status?

### 8.2 Required promotion state

```text
Source / controlling baseline
Exact delta
Target semantic status
Object / state domain / version
Applicable requirements / assurance
Material dependencies / reopen implications
Decision / acceptance / promotion authority
Authorized write path if persistent
```

Then:

```text
PROMOTE / WRITE
→ READBACK
→ RECONCILE controlling parent/domain state
```

Possible target status includes selected, accepted, authorized, controlling, released, deployed or authoritative-for-defined-domain.

Never default target status to generic `authoritative`.

## 9. Interaction with Chat / Work / Codex

### Chat

Default control surface for:

- Decision and Commitment discussion;
- Human Gate;
- Handoff compilation;
- Return reconciliation;
- acceptance/authorization/promotion interaction;
- bounded execution where no handoff is needed.

### Work

Receives a bounded Handoff Contract for long multi-step frontiers.

Work may internally perform research/analysis/creation/tool use within its authority, but must return/wait before crossing a blocked:

```text
new commitment boundary
Human Gate
new external action authorization
acceptance/release boundary
promotion / controlling-state write
```

unless that authority was explicitly delegated.

### Codex

Same contract semantics, specialized for repository/software work.

A Codex change/branch/commit does not imply acceptance/merge/promotion.

## 10. Example — System Development Runtime repair

```text
Parent outcome:
repair E2E Runtime deployment fidelity without reopening static architecture.

Decision:
separate Work Function / Method / Provider / Surface / Control Operator semantics.

Commitment:
STAGED — repair deployment model and compile candidate; do not externally install yet.

Authorization:
AI may create candidate branch/files/PR; may not merge or change external ChatGPT settings without Human authority.

Handoff to Codex/Work if used:
exact repo frontier + requirements + method + allowed writes + return condition.

Return:
files/commits + regression result + unresolved product constraints.

Promotion:
Human reviews candidate PR; merge promotes repo Runtime program only.

External installation:
separate Human-authorized transition after exact payload/readback.
```

## 11. Failure modes this contract prevents

- **Handoff amnesia** — state/decision/authority lost between Chat/Work/Codex;
- **Approval collapse** — Human review asked after downstream execution already crossed the gate;
- **Commitment collapse** — selected route treated as full/irreversible authorization;
- **Promotion collapse** — generated artifact/branch/write treated as accepted/controlling;
- **Authorization collapse** — technical capability mistaken for permission;
- **Child-root drift** — receiving Work/Codex frontier silently becomes controlling parent;
- **Return ambiguity** — plausible output returned without exact supported state/claim.

## 12. Deployment requirement

A new Global/Project Runtime compilation cannot receive deployment PASS unless its controller explicitly invokes these contracts when their triggers occur, or binds to an equally enforceable mechanism.

`Contract documented somewhere in repo` is not sufficient.
