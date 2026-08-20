# E2E Chat / Work / Codex Surface Allocation v0.1

**Status:** CANDIDATE OPERATING POLICY — product-realization guidance, not architecture.  
**Date:** 2026-08-20

## 1. Product reality

Current OpenAI product documentation distinguishes:

- **Chat** — fast conversational assistance, questions, search, brainstorming and quick help;
- **Work** — an agent for longer, multi-step work and finished deliverables, including research, analysis and artifact creation;
- **Codex** — software-development / technical work;
- **Projects** — persistent workspaces containing chats, files and Project Instructions; Project Instructions override Global Custom Instructions.

Official references:

- https://help.openai.com/en/articles/20001275/
- https://help.openai.com/en/articles/10169521-projects-in-chatgpt

These are current product facts, not durable architecture identities.

## 2. Architecture rule

Do **not** map logical E2E architecture stages directly to product surfaces.

```text
Formation ≠ Chat
Execution ≠ Work
Assurance ≠ separate chat
Project ≠ lifecycle stage
Work Unit ≠ Work run
```

Instead:

```text
current controlling state
+ next legitimate frontier
+ interaction requirement
+ capability/environment need
+ authority/risk
+ expected duration/complexity
        ↓
select surface/carrier
```

## 3. Default surface roles

### Chat — interactive control surface by default

Prefer Chat when the next frontier is:

- quick/bounded;
- highly interactive;
- framing/formation requiring rapid Human feedback;
- a decision or commitment discussion;
- a Human Gate / acceptance / promotion decision;
- a small execution or repair that can be completed reliably in the conversation;
- a readback/reconciliation step after material Work/tool execution.

Chat may also perform substantial work. It is not limited to Formation.

### Work — longer autonomous/multi-step frontier by default

Prefer Work when:

- the parent outcome and current frontier are sufficiently specified;
- the work needs sustained research, analysis, creation or multi-step tool use;
- a finished document/spreadsheet/presentation/report/Site or other substantial deliverable is the intended Work Product;
- the frontier can proceed for a meaningful interval without continuous Human judgment;
- return conditions and blocked Human transitions are clear.

Work is not automatically authorized to cross Human/Promotion/Release gates merely because it can continue technically.

### Codex — software/repository technical work

Prefer Codex for software-development, codebase/repository engineering and technical implementation where that specialized environment is materially better suited.

### Apps / tools / connectors

Use when the next frontier requires authoritative retrieval, external-system action, deterministic computation/verification, or a capability unavailable in the conversational surface.

## 4. Frontier handoff contract

A Work/Codex/tool handoff should contain only the state needed to execute the frontier safely:

```text
Parent outcome / Work Object
Current parent state / gate
Exact Work Unit / transformation
Expected parent contribution
Authoritative inputs / source pointers
Binding requirements / Performance Model
Allowed operations / authority
Relevant assumptions / uncertainty
Required output / version
Assurance / return condition
Blocked transitions / Human Gate conditions
Persistence / write path if any
```

Do not hand off an entire architecture dossier when a smaller contract is sufficient.

## 5. Return contract

A Work/Codex/tool run returns:

```text
work actually performed
output / state delta
sources/evidence used
assumptions / unresolved blockers
assurance actually applied
exact claim/readiness supported
writes/actions actually performed
Human contribution needed, if any
recommended next legitimate frontier
```

The Orchestrator then rebinds parent state and decides the next frontier. A tool/Work result does not self-promote.

## 6. Human Gate behavior in Work

If a required Human contribution blocks the frontier:

```text
mature decision object
+ exact Human contribution
+ reason AI cannot substitute
+ no blocked downstream execution
+ re-entry condition
```

Work must wait rather than produce a final downstream artifact and ask for review afterward.

## 7. Operating cadence heuristic

This is a default cadence, not a timer or stage machine.

### Control loop — usually minutes

Chat or equivalent:

```text
rebind controlling state
→ identify what materially changed
→ select next legitimate frontier
→ make/obtain required decision or commitment
→ dispatch or execute
```

Target: short enough that control does not become ceremony. For trivial work this collapses almost completely.

### Production loop — minutes to hours

Chat/Work/Codex/tool depending on frontier:

```text
execute bounded frontier
→ integrate
→ local verification/refinement
→ return exact supported state
```

Duration is task-driven, not fixed.

### Promotion / reconciliation loop — usually minutes

After a material candidate/result/write:

```text
assure exact claim
→ Human/authority decision only if required
→ promote/write through legitimate path
→ readback/reconcile
```

### Outcome loop — event/horizon-driven

Only when real use/outcome matters:

```text
observe evidence at meaningful horizon
→ evaluate mechanism/outcome
→ learn
→ change candidate / keep / adapt / stop
```

## 8. Project pattern

For persistent initiatives, the preferred pattern is one Project or other justified context boundary containing multiple Chat/Work frontiers, not one Project/room per stage.

```text
PROJECT / INITIATIVE CONTEXT
    ↕
CHAT control/interactive work
    ↔ WORK longer frontiers
    ↔ CODEX technical frontiers
    ↔ APPS/TOOLS external reality/action
    ↕
authoritative external/domain state as required
```

A new persistent surface/boundary must earn its handoff, duplication, synchronization and governance cost.

## 9. Validation boundary

This allocation policy is a candidate. Real-use validation must observe whether:

- Chat remains sufficiently direct for bounded work;
- Work receives well-formed frontiers rather than vague project-level mandates;
- Human Gates actually stop blocked downstream work;
- results return to controlling parent state without losing lineage/authority;
- surface switching improves net work rather than adding coordination overhead.
