# E2E Interaction / Frontier Compilation Contract v0.2 — Entry-Dispatch Repair Candidate

**Status:** R20 ENTRY-ACTIVATION REPAIR CANDIDATE — branch-only boundary contract; not externally installed or repository-promoted.  
**Date:** 2026-08-21  
**Branch:** `repair/r20-entry-dispatch-v0.2`  
**Canonical source:** `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.2.md` on this branch.  
**Behavioral basis:** `evaluation/e2e-real-use/E2E-04-R20-2026-08-21-BEHAVIORAL-VALIDATION.md`.

## 1. Purpose

Define how every Human message becomes controlled work before substantive execution without turning ordinary use into visible workflow ceremony.

R20 established two failure modes that this contract must prevent:

1. a new open professional Work Object can enter substantive Solution work before Admission/Formation activates;
2. a valid existing Parent does not imply that every new or materially changed child claim under that Parent is already admitted.

The executable input relation is therefore:

```text
Human trigger
→ BIND CONTEXT
→ RELATE trigger to bound work
   → BOUND continuation
   → NEW/CHANGED CLAIM
→ if NEW/CHANGED: DIRECT / FORMATION
→ selected legitimate frontier
→ substantive work
```

Entry Dispatch is not a new architecture stage or Work Function. It is the first Runtime control operation selecting which existing Work Function may execute.

## 2. Interaction types

### M0 — Entry Dispatch

Every Human trigger enters this dispatch before substantive Work-Function execution.

#### M0.1 Bind context

```text
existing legitimate Parent/frontier controls request
→ bind/recover Parent outcome + state/gate
  + active child contribution + allowed operation

no established Parent controls request
→ establish only enough provisional Parent/outcome/allowed operation
  for the requested next claim
→ no persistent boundary by default
```

Current chat/thread/artifact/branch never becomes root implicitly. If established control state is materially unclear, recover/reconcile before local continuation.

#### M0.2 Relate trigger to bound work

After context is bound, classify the message itself:

```text
BOUND CONTINUATION
= continues the already admitted current frontier
  without materially changing claim, scope, requirements,
  means, decision object or authority

NEW/CHANGED CLAIM
= new Work Object
  OR new child claim under an existing Parent
  OR material change to claim/scope/requirements/means/decision object
```

An established Parent is continuity context, not blanket Admission authority for every child claim.

`Next`, `continue`, or equivalent wording is BOUND only if the substance does not introduce a material new/changed claim. Continuation wording never hides a scope/requirements/means change.

#### M0.3 Admission for NEW/CHANGED CLAIM

```text
DIRECT
iff unresolved upstream
  reality / outcome / requirements / performance /
  professional-reference intelligence / evidence /
  persistence context
cannot materially change the exact requested claim/product class,
its evaluation or feasibility

otherwise
→ FORMATION
```

DIRECT is claim-relative, not complexity-relative.

Examples:

```text
translate supplied paragraph               → DIRECT
write short birthday card                  → DIRECT
five wild beer-comic ideas                 → DIRECT exploration
write one yeast-narrator scene             → DIRECT bounded execution
new beer-history Graphic Novel initiative  → FORMATION
new evaluation dashboard inside Project    → FORMATION if performance/requirements open
small bounded repo readback inside Parent   → DIRECT child claim
material scope change during execution      → NEW/CHANGED → re-admit
```

Explicit exploration may execute directly when exploration itself is the requested Work Product. Its outputs remain exploration/probes unless later qualified.

#### M0.4 Priority rule

```text
ENTRY / ADMISSION INTEGRITY
precedes
requested Work-Product execution
and shallowest-route execution
```

Work Product fidelity cannot be used to bypass an upstream Admission prerequisite.

### M1 — Human input / trigger

```text
Human message
= intent evidence / trigger / contribution
≠ complete requirements
≠ decision
≠ commitment
≠ authorization
≠ Handoff Contract
```

The message is processed through M0 before substantive work.

### M2 — Chat control / interactive work

Chat is the default interactive surface for:

- Entry Dispatch and state rebind/recovery;
- Formation and information work benefiting from Human interaction;
- recommendation/Decision/Commitment discussion;
- Human Gate and authority interactions;
- bounded execution/repair;
- Handoff compilation;
- Provider Return/readback/reconciliation;
- Human-facing Control Return.

Chat need not narrate internal Entry/control state. Surface only what the Human needs for judgment, authority, reliance or next action.

### M3 — Frontier dispatch

When active responsibility/environment changes, compile `BC-02 Frontier Handoff Contract` from current admitted state:

```text
parent outcome/state/gate
exact transformation + child→parent contribution
sources/inputs + requirements
applicable method/source
current Work Basis/commitment
allowed operations/authorization
assumptions/dependencies
output + assurance/return condition
blocked transitions/Human Gate
write/persistence path
```

A dispatch is not a paraphrase of the whole Project.

### M4 — Provider execution

Work/Codex/Human/tool executes only the admitted bounded frontier and allowed operations. Internal decomposition/tool use may vary, but the provider cannot silently cross a new Admission, Commitment, Human Gate, Authorization, acceptance/release or Promotion boundary.

If execution discovers a material change to claim/scope/requirements/means, return/rebind or locally re-enter M0 rather than treating it as silently admitted continuation.

### M5 — Provider Return

Provider returns `BC-03 Provider Return Contract`:

```text
work/delta
sources/evidence
method applied
assumptions/blockers
assurance + exact supported claim/readiness
actions/writes
Human/authority need
recommended next frontier
```

Then Controller:

```text
READBACK material effects
→ REBIND parent/state/gate
→ INTEGRATE child contribution
→ QUALIFY exact parent state
→ run Entry relation on any proposed new/changed next claim
```

Provider Return is not Human-facing completion or Promotion.

### M6 — Human-facing Control Return

At every material interaction boundary, compile `BC-06 Human-facing Control Return` from qualified parent state.

Minimum visible content only where material:

```text
achieved result / exact qualified state
persistence state / requirement
promotion state / requirement
next legitimate frontier
next actor
exact Human contribution, if any
disposition:
  CLOSE / CONTINUE / HUMAN GATE / PROMOTION GATE /
  HANDOFF / WAIT / MONITOR
```

Rules:

- if Human contribution is required, state the exact decision/acceptance/authorization/commitment/action and WAIT where blocked;
- if none is required, do not manufacture a question;
- do not make the Human infer whether result is Working/Candidate/qualified, whether persistence/Promotion is intended, whether `Next` is safe, or what response is required;
- obvious bounded one-shot answers may collapse to an implicit/brief CLOSE.

### M7 — Human decision / authority event

When Human contribution materially blocks a transition, present the mature decision/work object plus exact requested contribution. Do not cross the blocked downstream transition before the event.

A Human instruction may itself introduce NEW/CHANGED CLAIM content; authority to request work does not waive Entry Admission for that claim.

### M8 — Promotion / persistence event

Persistence and Promotion remain distinct:

```text
PERSIST = durable write/storage ≠ stronger semantic/control status
PROMOTE = legitimate semantic/status/control change
```

Execute only authorized promotion/write then read back/reconcile. Repository merge, settings save, external send/deployment and outcome observation are distinct events.

## 3. Continuation semantics

```text
NEXT
= BOUND continuation of currently admitted legitimate frontier

NEXT ≠ acceptance
NEXT ≠ promotion
NEXT ≠ authorization
NEXT ≠ persistence
NEXT ≠ scope change
NEXT ≠ new commitment
```

Before `Next` crosses a material Work Unit/Gate/state/responsibility/surface boundary:

```text
integrate current delta
→ qualify exact state
→ determine persistence/promotion need
→ expose Human Gate if required
→ continue or WAIT
```

If the actual content changes claim/scope/requirements/means materially, classify it NEW/CHANGED and re-admit even if the message says `Next`.

## 4. Surface relation

```text
Chat = interactive Entry/control surface by default
Work = long bounded frontier provider/environment
Codex = repo/software frontier provider/environment
Project = persistent initiative/context boundary
GitHub/Drive/etc. = state/method/evidence carriers by domain
```

No relation above is an architecture-stage identity.

## 5. Handoff elision

Do not create ceremonial Handoff objects for trivial internal tool calls when responsibility, authority and state remain safely inside the admitted frontier.

Compile explicit Handoff when a surface/provider transition can materially lose/alter Parent state, commitment, authority, method, assumptions/evidence or required return/readiness.

## 6. Failure signals

- substantive work occurs before M0 Entry relation;
- existing Parent is treated as blanket Admission for a new child claim;
- material scope/requirements/means change is treated as BOUND continuation;
- simple bounded work enters visible Formation ceremony without decision value;
- explicit exploration is incorrectly blocked from direct probe generation;
- Work receives vague Project-level mandate rather than bounded frontier;
- Provider Return fails to rebind controlling state;
- child output becomes parent completion/Promotion implicitly;
- Human Gate appears only after blocked downstream work;
- material response ends without usable disposition;
- Human must infer whether `Next` is safe or what action is required.

## 7. Behavioral validation boundary

Static wording is insufficient. Actual-carrier validation must observe for each material trial:

```text
Entry policy present?
context bound correctly?
trigger relation classified?
DIRECT/FORMATION decision correct?
downstream work permitted/withheld correctly?
Human burden / ceremony acceptable?
```

Required regression classes include root cold start, bounded DIRECT work, explicit exploration, established BOUND continuation, nested new professional child claim, nested bounded direct child claim and material claim/scope change.