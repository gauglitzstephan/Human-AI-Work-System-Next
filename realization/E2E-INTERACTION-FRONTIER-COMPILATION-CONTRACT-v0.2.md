# E2E Interaction / Frontier Compilation Contract v0.2 — Entry-Dispatch Repair Candidate

**Status:** R20 ENTRY-ACTIVATION REPAIR CANDIDATE — branch-only boundary contract; not externally installed or repository-promoted.  
**Date:** 2026-08-21  
**Branch:** `repair/r20-entry-dispatch-v0.2`  
**Canonical source:** `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.2.md` on this branch.  
**Behavioral basis:** `evaluation/e2e-real-use/E2E-04-R20-2026-08-21-BEHAVIORAL-VALIDATION.md`.

## 1. Purpose

Define how every Human message enters controlled work before substantive execution, without turning ordinary use into visible workflow ceremony.

The v0.1 contract already treated a Human message as a trigger rather than a complete Work Order. R20 showed that this was not enough: the Controller could still begin ordinary generative solution work before the conditional Admission guard activated.

v0.2 therefore makes the input boundary executable as an **Entry Dispatch**:

```text
Human trigger
→ ENTRY DISPATCH
→ ESTABLISHED / NEW
→ if NEW: DIRECT / FORMATION
→ selected legitimate frontier
→ substantive work
```

Entry Dispatch is not a new architecture stage or Work Function. It is the first Runtime control operation that selects which existing Work Function may execute.

## 2. Interaction types

### M0 — Entry Dispatch

Every Human trigger enters this dispatch before substantive Work-Function execution.

#### M0.1 ESTABLISHED vs NEW

```text
ESTABLISHED
= message continues/revises/acts on a legitimately bound Parent Work Object/frontier
→ bind/recover parent outcome + state/gate + child contribution + allowed operation
→ preserve `Next`/continuation semantics

NEW
= no established Parent Work Object legitimately controls the requested next claim
→ establish only enough provisional Parent/outcome/allowed operation
→ no persistent boundary by default
→ classify DIRECT vs FORMATION
```

Current chat, latest artifact, branch or locally salient hypothesis never becomes root implicitly.

#### M0.2 DIRECT vs FORMATION for NEW work

```text
DIRECT
iff unresolved upstream
  reality / outcome / requirements / performance /
  professional-reference / evidence / persistence
cannot materially change the exact requested claim/Work-Product class,
its evaluation or feasibility.

otherwise:
FORMATION
```

This classification is claim-relative rather than complexity-relative.

Examples:

```text
"translate this paragraph"                         → DIRECT
"write a short birthday card"                     → DIRECT
"give me five wild Graphic-Novel ideas"           → DIRECT exploration
"write a scene with yeast as narrator"            → DIRECT bounded execution
"I want to design a professional beer-history
 Graphic Novel"                                    → FORMATION
"should I buy an EV in 2026 or 2027?"             → FORMATION / evidence
"repair this existing repo"                       → ESTABLISHED recovery
"Next" within bound work                           → ESTABLISHED continuation
```

Explicit exploration is a legitimate Work Product:

```text
idea / option / scene as requested exploration
≠ qualified Candidate
≠ selected route
≠ design basis
```

#### M0.3 Priority relation

```text
ENTRY / ADMISSION INTEGRITY
precedes
REQUESTED WORK PRODUCT / SHALLOWEST SUBSTANTIVE EXECUTION
```

This relation prevents direct-help / minimum-work / Work-Product-fidelity semantics from bypassing materially required upstream readiness.

M0 need not be narrated to the Human. For DIRECT work it should collapse to essentially zero visible ceremony.

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

M1 always passes through M0 before substantive work.

### M2 — Chat control / interactive work

Chat remains the default interactive surface for Entry Dispatch, state rebind/recovery, Formation, bounded evidence work, Decision/Commitment discussion, Human Gates, bounded execution/repair, Handoff compilation, Return reconciliation and Human-facing Control Return.

Chat need not narrate internal control state. Surface only what the Human needs for judgment, authority, reliance or next action.

### M3 — Frontier dispatch

When active responsibility/environment changes, compile `BC-02 Frontier Handoff Contract` from the selected frontier:

```text
parent outcome/state/gate
exact transformation + child→parent contribution
sources/inputs + requirements
applicable method/source
Work Basis / commitment
allowed operations / authorization
assumptions/dependencies
output + assurance/return
blocked transitions/Human Gate
write/persistence path
```

### M4 — Provider execution

Work/Codex/Human/tool executes only the bounded frontier and allowed operations. Internal decomposition/tool use cannot silently cross Commitment, Human Gate, Authorization, acceptance/release or Promotion boundaries.

### M5 — Provider Return

Provider returns:

```text
work/delta
sources/evidence
method applied
assumptions/blockers
assurance + exact claim/readiness
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

Provider Return ≠ Human-facing Control Return.

### M6 — Human-facing Control Return

At every material interaction boundary expose only where material:

```text
achieved result / exact qualified state
persistence state / requirement
promotion state / requirement
next legitimate frontier
next actor
exact Human contribution, if any
CLOSE / CONTINUE / HUMAN GATE / PROMOTION GATE /
HANDOFF / WAIT / MONITOR
```

If Human contribution is required, state the exact action and WAIT where blocked. If none is required, do not manufacture a question. For obvious bounded one-shot work, Control Return may collapse to implicit/brief CLOSE.

### M7 — Human decision / authority event

When Human contribution materially blocks a transition, present the mature decision/work object + exact decision/acceptance/authorization/commitment requested. Do not cross the blocked transition first.

### M8 — Promotion / persistence event

```text
PERSIST = durable write/storage ≠ stronger semantic/control status
PROMOTE = legitimate semantic/status/control change
```

Repository merge, settings save, external send/deployment and outcome observation remain distinct events.

## 3. `Next` / continuation semantics

```text
NEXT
= continue currently bound legitimate frontier

NEXT ≠ acceptance
NEXT ≠ promotion
NEXT ≠ authorization
NEXT ≠ persistence
NEXT ≠ scope change
NEXT ≠ new commitment
```

Before crossing a material Work Unit, Gate, state, responsibility or surface boundary:

```text
integrate current delta
→ qualify exact state
→ determine persistence/promotion need
→ expose Human Gate if required
→ continue or wait
```

## 4. Surface relation

```text
Chat = Entry/control/interactive work by default
Work = long bounded frontier provider/environment
Codex = repo/software frontier provider/environment
Project = optional persistent initiative/context boundary
GitHub/Drive/etc. = state/method/evidence carriers by domain
```

No relation above is an architecture-stage identity.

## 5. Handoff elision

Do not create ceremonial Handoff objects for trivial internal tool calls. Compile explicit Handoff when a responsibility/provider/environment transition can materially lose parent outcome/state/gate, decision/commitment, authority, method, assumptions/evidence, output/readiness or return condition.

## 6. Entry-Dispatch assurance

Static wording is not sufficient.

Minimum relation-level tests:

```text
R-ENTRY-01   every new trigger reaches Entry Dispatch before substantive work
R-DIRECT-01  bounded direct work exits DIRECT without ceremony
R-IDEATE-01  requested exploration may execute directly but remains probe-level
R-FORM-01    open professional initiative enters FORMATION before preferred-route work
R-PRIOR-01   Work-Product fidelity/shallowest execution cannot bypass Admission
R-CONT-01    established continuation/recovery remains intact
```

Deployment/behavioral PASS requires representative actual-carrier execution; static trace alone remains insufficient.

## 7. Failure signals

- substantive solution generation occurs before M0 dispatch;
- DIRECT is inferred from prompt brevity rather than requested-claim readiness;
- explicit exploration is blocked by unnecessary Formation ceremony;
- an exploratory idea silently becomes qualified Candidate/design basis;
- Project creation or Human intake is required by default;
- established work loses Parent continuity;
- user message becomes implicit authorization;
- Provider Return fails to rebind parent;
- Human Gate appears after blocked downstream work;
- material response leaves disposition/next action implicit.
