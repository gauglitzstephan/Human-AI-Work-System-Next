# E2E Interaction / Frontier Compilation Contract v0.1

**Status:** CANDIDATE RUNTIME BOUNDARY CONTRACT — no external installation.  
**Date:** 2026-08-20  
**Canonical source:** `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`

## 1. Purpose

Define how ordinary Human messages become controlled work without treating every message as a complete Work Order and without losing state across Chat → Work/Codex/provider transitions.

## 2. Interaction types

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

The Controller interprets the message against controlling parent/state/authority and decides the minimum next frontier.

### M2 — Chat control / interactive work

Chat is the default interactive surface for:

- state rebind/recovery;
- Formation and information work benefiting from Human interaction;
- recommendation/Decision/Commitment discussion;
- Human Gate and authority interactions;
- bounded execution/repair;
- Handoff compilation;
- Return/readback/reconciliation.

Chat need not narrate internal control state. Surface only state needed for Human judgment, authority, reliance or next action.

### M3 — Frontier dispatch

When active responsibility/environment changes, the Controller compiles `BC-02 Frontier Handoff Contract` from current state.

A dispatch is not a prose paraphrase of the whole Project. It contains only the state required for the bounded frontier:

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

### M4 — Provider execution

Work/Codex/Human/tool executes only the bounded frontier and allowed operations. Internal provider decomposition/tool use may vary, but it cannot silently cross a new Commitment, Human Gate, Authorization, acceptance/release or Promotion boundary.

### M5 — Return

Provider returns `BC-03 Return Contract`:

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
→ select next frontier
```

### M6 — Human decision / authority event

When Human contribution is materially required, present the mature decision/work object plus the exact decision/acceptance/authorization/commitment requested. Do not cross the blocked downstream transition before the event.

### M7 — Promotion / persistence event

A Human or other legitimate authority event may authorize a target semantic/status change. Execute only the authorized promotion/write and then read back/reconcile. Repository merge, settings save, external send/deployment and outcome observation are distinct events.

## 3. Surface relation

```text
Chat = interactive control surface by default
Work = long bounded frontier provider/environment
Codex = repo/software frontier provider/environment
Project = persistent initiative/context boundary
GitHub/Drive/etc. = state/method/evidence carriers by domain
```

No relation above is an architecture-stage identity.

## 4. Handoff elision rule

Do not create ceremonial Handoff objects for trivial internal tool calls when active responsibility, authority and required state remain safely inside the same bounded frontier.

Compile an explicit Handoff when a surface/provider transition can materially lose or alter:

- parent outcome/state/gate;
- decision/commitment;
- authority/allowed operation;
- method;
- assumptions/evidence;
- required output/readiness/return condition.

## 5. Failure signals

- user message treated as complete specification/authorization;
- Work receives a vague Project-level mandate rather than bounded frontier;
- provider returns plausible artifact without method/evidence/readiness state;
- Human Gate appears only after blocked downstream work already happened;
- Work/Codex branch/commit treated as accepted parent state;
- Return does not rebind `main/CURRENT.md` or other controlling source;
- Handoff state becomes an unowned duplicate truth store.
