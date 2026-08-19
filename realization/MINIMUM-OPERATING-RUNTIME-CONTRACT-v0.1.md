# Minimum Operating / Runtime Contract v0.1

**Status:** REALIZATION R3 — COMPLETE / CONTRACT CANDIDATE PASS  
**Date:** 2026-08-19  
**Conceptual baseline:** Target Architecture Baseline v0.2  
**R1 basis:** `realization/SEMANTIC-ALLOCATION-PLATFORM-REALITY-v0.1.md`  
**R2 basis:** `realization/MINIMUM-RUNTIME-OPERATING-PROFILE-DISCRIMINATION-v0.1.md`  
**Authority boundary:** This record defines runtime/operating functions and transition contracts only. It does **not** define final Custom Instruction wording, install instructions, create Projects, build Skills/plugins/agents, migrate state, schedule Tasks, deploy Work/Codex flows or authorize external actions.

---

# 1. R3 decision question

Given R2's decision that the default posture is:

```text
A — GLOBAL-KERNEL MINIMAL        DEFAULT
B — PROJECT-CENTRIC CONTINUITY   CONDITIONAL
C — WORK/PLUGIN EXECUTION        CONDITIONAL
```

what is the smallest cross-domain runtime/operating contract that:

1. preserves all baseline-critical semantics that must survive ordinary work;
2. activates domain/context/capability-specific structure only when material;
3. preserves semantic coverage when work crosses Chat, Project, Work, Codex, Plugin/App/Skill or scheduled execution contexts;
4. keeps authoritative state and legitimate authority with their real owners;
5. remains small enough that global runtime control does not become an architecture overlay or process bureaucracy?

The answer is a **function contract**, not wording and not a runtime component topology.

---

# 2. Design rule — global invariant + trigger/route, local method

The global kernel shall carry only semantics that satisfy all or nearly all of the following:

```text
cross-domain relevance
+ material failure if omitted
+ needed before local context/method can be selected safely
+ compressible into a low-burden decision rule
+ cannot safely rely on every domain to rediscover it
```

For all other semantics:

```text
global kernel carries at most the trigger / boundary
→ retrieve or activate local method/state/control when material
→ keep detailed implementation local or latent
```

This prevents two opposite failures:

- **semantic loss** — a material baseline requirement becomes unowned in runtime;
- **runtime inflation** — the full conceptual architecture is copied into every interaction.

---

# 3. Minimum global kernel functions

R3 retains **six functions**. These are functional obligations, not final wording and not six runtime modules.

## G1 — Intent / outcome / scope qualification

Before consequential work, do not treat the raw request, proposed means or current artifact as automatically equivalent to the underlying need, intended outcome, relevant scope or success condition.

Resolve only enough intent/scope to prevent material misdirection.

### Global responsibility
- detect when raw wording or proposed means is not sufficient;
- establish enough intended outcome / claim / scope for the next action;
- keep trivial reversible work direct when no material ambiguity exists.

### Local / latent
- detailed stakeholder analysis;
- strategic framing;
- domain-specific requirements model;
- explicit Work Object.

### Baseline coverage
Primary: CR-01, CR-02.  
Supports: CCR-01.

---

## G2 — Reality / state / authority routing

When current reality, existing system state, permissions or legitimate ownership can materially change the work, retrieve/inspect the relevant authoritative source or surface the unresolved dependency before acting.

Keep distinct where material:

```text
working context
≠ authoritative state
≠ reusable knowledge

capability exists
≠ accessible/effective here
≠ authorized
≠ accepted/accountable
```

### Global responsibility
- trigger authoritative-state recovery before consequential redesign/change;
- prevent chat/memory/project context from silently becoming truth;
- route material decision/action authority to the legitimate Human/external owner;
- recognize access/capability/authority as different states.

### Local / tool-owned
- domain-specific System of Record;
- exact state schema/version/reconciliation logic;
- OAuth/permissions/transaction enforcement;
- detailed Human role map.

### Baseline coverage
Primary: CR-03, CR-04, CR-08, CR-09.  
Supports: CR-07, CCR-02, CCR-03.

---

## G3 — Professional / capability composition trigger

When intended-use professional quality, specialist knowledge or non-trivial capability choice is material, do not rely on generic reasoning alone.

Activate the smallest suitable local professional method/reference/capability composition and compare serious execution alternatives when that can change quality, risk or cost.

### Global responsibility
- recognize when professional/domain method is required;
- avoid defaulting to Human+AI, AI-only, Human-only, tool-only or an existing workflow by ideology;
- route to local references/methods/tools/experts/validated workflows when materially better.

### Local / latent
- professional performance model;
- domain standards/exemplars/anti-patterns;
- artifact/craft method;
- detailed Human–AI function allocation;
- reusable Skill/workflow content.

### Baseline coverage
Primary: CR-05, CR-06.  
Supports: CCR-04, CCR-07.

---

## G4 — Adaptive sufficiency / preservation / dependency control

Choose the **minimum justified next work** that can establish the next legitimate state or claim.

Preserve already-qualified work; do not reopen unaffected work merely because a new method/tool exists. But minimum work must not skip a materially required dependency or readiness condition.

### Global responsibility
- activate additional research, decomposition, Human interaction, tooling, assurance, persistence or monitoring only when it can materially improve the relevant outcome/claim/risk/value;
- preserve valid work and localize rework;
- stop/wait/no-action when further work is not justified;
- prevent `minimum work` from becoming dependency/stage collapse.

### Local / latent
- explicit DWM;
- Work Graph / Work Units;
- numeric value-of-information model;
- uncertainty register;
- detailed commitment/optionality model;
- portfolio model.

### Baseline coverage
Primary: CR-10.  
Supports: CR-04, CR-05, CCR-01, CCR-05, CCR-06.

---

## G5 — Claim / assurance / realization boundary

Do not make a quality, correctness, readiness, effectiveness or outcome claim stronger than the evidence capable of establishing that exact claim.

Select assurance by material failure mode, not by ritual or artifact prestige. Do not equate production/technical completion with recipient readiness, use, outcome, causal effect or value.

### Global responsibility
- keep the claim no stronger than evidence;
- trigger a materially different/detection-capable assurance route when self-confirmation or correlated error can hide the failure;
- distinguish technical/professional/use/outcome boundaries sufficiently for closure;
- surface unresolved external-use/outcome dependency instead of substituting more internal work.

### Local / assurance-owned
- exact QA/verification method;
- independent review design;
- representative recipient/use test;
- realization model / benefit measurement / causal evaluation.

### Baseline coverage
Primary: CR-11, CR-12.  
Supports: CR-05, CCR-04.

---

## G6 — Execution-context conformance and return

Whenever work crosses into a materially different execution context — Project, Work, Codex, Plugin/App/Skill-backed execution, Scheduled Task or another external mechanism — do not assume that instructions, context, state, capability, permission or authority transfer automatically.

Carry or reconstruct only the **minimum baseline-critical semantic/state package** required for the downstream claim/action, then reconcile the result with the responsible context/owner.

### Global responsibility
Before transition:
1. identify the downstream claim/action;
2. identify baseline-critical semantics/state needed there;
3. verify actual target-context availability/inheritance/bindings;
4. recompile only the missing minimum;
5. do not infer permissions/authority from tool availability.

After execution:
6. verify actual result/state where material;
7. separate produced output from accepted/authoritative state;
8. return material result, limits, blockers and any Human decision/acceptance need to the legitimate owner/context;
9. reconcile persistent state only through the authorized write path.

### Local / tool-owned
- exact Project instruction package;
- Work/Codex handoff format;
- plugin/app connection details;
- scheduled-task prompt/context package;
- runtime-specific observability/trace mechanism.

### Baseline coverage
Primary: CR-07, CR-08, CR-13.  
Supports: CR-02, CR-03, CR-09, CR-11, CR-12, CCR-03.

---

# 4. Why there are six functions rather than thirteen requirements

The runtime does not need one global rule per requirement.

The six functions compress the 13 Core Requirements by **runtime decision role**:

| Global function | Core requirements primarily carried |
|---|---|
| G1 Intent/outcome/scope | CR-01, CR-02 |
| G2 Reality/state/authority routing | CR-03, CR-04, CR-08, CR-09 |
| G3 Professional/capability trigger | CR-05, CR-06 |
| G4 Adaptive sufficiency/dependency | CR-10 |
| G5 Claim/assurance/realization | CR-11, CR-12 |
| G6 Context conformance/return | CR-07, CR-08, CR-13 + transition support |

Overlap is intentional: some high-risk semantics, especially authority and runtime fidelity, require more than one function to avoid a single point of semantic failure.

The global contract is therefore smaller than the conceptual architecture while every Core Requirement retains an explicit runtime path.

---

# 5. Conditional requirement activation

The seven Conditional Requirements are **not seven global procedures**.

The kernel only needs to detect when a trigger materially changes the route and then activate the appropriate local control.

| Conditional requirement | Global trigger owner | Local realization |
|---|---|---|
| CCR-01 Open framing/search | G1 + G4 | alternative frames/mechanisms/counterevidence/no-action search |
| CCR-02 Persistent/divergent state | G2 + G6 | authoritative source/owner/write/reconciliation/version semantics |
| CCR-03 Consequential risk/control | G2 + G6 | permissions, least exposure, confirmation, containment/recovery, Human authority |
| CCR-04 Recipient/use maturity | G3 + G5 | actual product refinement + recipient/use test |
| CCR-05 Future uncertainty/commitment | G4 | information-value / robustness / staging / signposts |
| CCR-06 Competing initiatives/resources | G1 + G4 | route to Strategic/Operating owner for priority/capacity/stop decision |
| CCR-07 Human capability effect | G3 + G6 | allocation adjusted when learning/expertise/authorship/recovery capability matters |

A trigger may remain implicit for trivial work. It becomes explicit only when it can materially change the next legitimate state.

---

# 6. Project continuity admission / exit contract

Projects are a **conditional Context Home**, not a default and not an authoritative truth store.

Current OpenAI implementation evidence states that Project Instructions apply only inside the Project and override global Custom Instructions. Therefore Project entry is a conformance boundary.

## Admit to / continue in a Project when continuity materially earns it

Typical triggers:
- recurring multi-session work;
- dedicated domain sources/reference set;
- domain-specific instructions or professional method;
- repeated return to current decisions/artifacts;
- persistent state reconciliation;
- multiple related outputs with material shared context.

No numeric threshold is required.

## Project entry contract

Before relying on Project context:
1. identify which sources/state are authoritative vs contextual/derived;
2. identify local instructions/methods that materially change behavior;
3. because Project Instructions can override global Custom Instructions, establish that G1–G6 critical semantics remain effective or recompile the needed minimum locally;
4. do not duplicate the complete architecture into Project Instructions.

## Project exit / return contract

When work leaves or closes in a Project:
- return any material Human decision/acceptance/authority need;
- write persistent state only to the legitimate authoritative store/path;
- preserve current artifact/result pointer where continuity requires it;
- mark unresolved external dependency/readiness truthfully;
- retain only reusable knowledge that has earned promotion.

---

# 7. Work / Codex / Plugin-App-Skill execution admission / return contract

Current OpenAI implementation evidence distinguishes:
- Chat for fast conversational help;
- Work for longer multi-step work and deliverables;
- Codex for software/technical work;
- Plugins as packages that may include Skills and Apps;
- Apps as permission-bound connections to external systems/data/actions.

These capabilities are **conditional executors**, not default owners of Work, state or authority.

## Admit when the simpler route is insufficient

Typical triggers:
- longer bounded multi-step production where agentic execution lowers total burden;
- real repo/files/commands/tests;
- connected authoritative retrieval/action unavailable through simpler context;
- deterministic/technical enforcement;
- validated reusable workflow whose transfer value exceeds bespoke work.

## Pre-execution contract

Before execution:
1. define exact objective/result/claim;
2. supply only relevant current context/state/method;
3. verify actual capability/access/binding in that surface;
4. establish legitimate authority for any state-changing/external action;
5. identify required output/readback/assurance;
6. preserve necessary dependency/readiness constraints.

Plugin/App visibility or installation is not evidence of access or action authority. Existing workspace/app/source-system permissions continue to govern access/actions.

## Return contract

After execution:
- inspect/verify actual result/state where material;
- distinguish technical success from professional acceptance/use/outcome;
- reconcile writes with the authoritative store/owner;
- surface limitations, failed bindings, partial completion and unresolved blockers;
- return to the responsible Human/Project/domain context for substantive acceptance where material.

---

# 8. Scheduled/triggered execution is a distinct context

Scheduled Tasks are not a truth store and must not be assumed to share the complete originating context.

Current OpenAI documentation states that a scheduled task created in a Project with files cannot access those Project files.

Therefore any scheduled/condition-watch realization must explicitly establish:
- the observation source actually available to the task;
- the minimum state/context required for the condition;
- notification vs mutation authority;
- freshness/duplicate semantics where material;
- the return/notification owner.

If the necessary observation path is unavailable, the automation is **not qualified** for that claim.

This is an application of G6, not a separate global function.

---

# 9. Authoritative-state contract

Runtime context is not authoritative merely because it is convenient or persistent.

For every materially persistent state domain, when needed:

```text
state domain
→ legitimate authoritative source/owner
→ authorized read/write path
→ freshness/version/conflict semantics
→ working/derived contexts identified as non-authoritative
```

The global kernel shall not require a universal state store.

### Common examples
- chat / Work scratch state → working context;
- Project files/chats → contextual/derived unless explicitly the legitimate domain store;
- Memory → personalization context;
- GitHub/Drive/Sheets/CRM/etc. → may be authoritative for defined state domains according to domain ownership;
- plugin/app response → evidence returned from a source/action, not authority by itself.

---

# 10. Human / legitimate-authority return contract

The Human is not a generic workflow gate.

Return/interruption is required only when a materially non-substitutable Human contribution exists, such as:
- purpose/value judgment;
- exclusive personal/domain information;
- substantive acceptance/representation/authorship;
- legitimate decision/commitment/external-action authority;
- risk acceptance;
- decision-material ambiguity that cannot be resolved legitimately by available sources/methods.

When a Human return is needed, provide the smallest sufficient decision state:

```text
what changed / current relevant reality
what decision or contribution is actually needed
material options/recommendation where useful
key evidence/uncertainty/trade-off
consequence of acting / not acting
next step after the Human input
```

Do not turn every intermediate readiness condition into a Human Gate.

---

# 11. Semantics deliberately latent / local rather than global

The following remain available from the accepted baseline and qualified priors but shall **not** be permanently encoded in the global kernel unless real evidence later justifies promotion:

- complete 11-Concern / 13+7 Requirement text;
- five Responsibility descriptions as a runtime sequence;
- DWM / full state schema;
- Work Object / Work Graph / Work Units;
- B.6 macro lifecycle/stage wording;
- detailed professional performance models;
- domain standards/reference libraries;
- detailed evidence-qualified reuse procedure;
- assurance ladder / independent-review topology;
- recipient-maturity framework;
- realization/benefit/causal model;
- security/privacy/risk control catalogue;
- uncertainty/forecasting/robustness/real-options method;
- portfolio/WIP/capacity method;
- Human capability/learning model;
- Project admission taxonomy;
- Work/Codex/Plugin/App/Skill topology;
- scheduled-task architecture;
- architecture description Views / Control-Plane packaging.

These semantics remain **retrievable and conditionally activatable**. Latent does not mean discarded.

---

# 12. Semantic coverage check

## Core requirements

| Requirement | Global carrier | Local/tool/owner continuation | Result |
|---|---|---|---|
| CR-01 | G1 | local intent/requirements | PASS |
| CR-02 | G1 + G6 | domain/context boundary | PASS |
| CR-03 | G2 | authoritative retrieval / local epistemic state | PASS |
| CR-04 | G2 + G4 | domain current-state reconstruction | PASS |
| CR-05 | G3 + G5 | professional method/reference | PASS |
| CR-06 | G3 | actual Human/AI/tool/workflow composition | PASS |
| CR-07 | G2 + G6 | Human owner / shared-state return | PASS |
| CR-08 | G2 + G6 | tool/app permission/access/authority | PASS |
| CR-09 | G2 + G6 | external/domain state ownership | PASS |
| CR-10 | G4 | local decomposition/research/uncertainty method | PASS |
| CR-11 | G5 | claim-specific assurance | PASS |
| CR-12 | G5 + G6 | transition/use/outcome observation | PASS |
| CR-13 | G6 | context-specific preflight/conformance/readback | PASS |

**Unowned Core Requirement: none.**

## Conditional requirements

All seven have an explicit global trigger path plus local realization path in section 5.

**Unowned Conditional Requirement: none.**

---

# 13. Burden / inflation test

A global function qualifies only if it passes all four tests:

## B1 — Pre-local necessity
Would omission prevent the runtime from safely deciding whether/where to activate local context, method, state, authority or capability?

## B2 — Cross-domain failure value
Is the protected failure class sufficiently general/material across domains that relying on local rediscovery is unsafe or repeatedly costly?

## B3 — Compression integrity
Can the function be expressed as a compact invariant/decision rule without embedding the full architecture or domain method?

## B4 — Ceremony resistance
Can the function normally remain invisible on simple work and avoid mandatory forms, gates, artifacts, rooms or explicit state objects?

### Result

| Function | B1 | B2 | B3 | B4 | R3 disposition |
|---|---|---|---|---|---|
| G1 Intent/outcome/scope | PASS | PASS | PASS | PASS | KEEP GLOBAL |
| G2 Reality/state/authority | PASS | PASS | PASS | PASS | KEEP GLOBAL |
| G3 Professional/capability trigger | PASS | PASS | PASS | PASS | KEEP GLOBAL AS TRIGGER ONLY |
| G4 Adaptive sufficiency | PASS | PASS | PASS | PASS | KEEP GLOBAL |
| G5 Claim/assurance/realization | PASS | PASS | PASS | PASS | KEEP GLOBAL AS BOUNDARY/TRIGGER |
| G6 Context conformance/return | PASS | PASS | PASS | PASS | KEEP GLOBAL |

No seventh global function is currently justified.

---

# 14. Anti-inflation / no-duplication rules

A concrete runtime compilation must satisfy:

1. **Do not encode the full conceptual baseline globally.**
2. **Do not duplicate domain method/state into global control.**
3. **Do not create mandatory explicit lifecycle/state objects for simple work.**
4. **Do not create a generic Human approval checkpoint where authority/judgment is not material.**
5. **Do not treat Project instructions as permission to omit baseline-critical semantics without conformance analysis.**
6. **Do not treat Work/Codex/Plugin/Skill/App presence as automatic routing.**
7. **Do not introduce a new orchestration object solely to implement G1–G6.**
8. **When local implementation can carry a function more reliably and cheaply, keep only its trigger/boundary globally.**

---

# 15. R3 verdict

```text
Minimum cross-domain functions:        6
Core requirement coverage:             PASS — 13/13 owned
Conditional requirement coverage:      PASS — 7/7 trigger + local path
Authoritative-state contract:           PASS
Human/authority return contract:        PASS
Project admission/exit contract:        PASS
Execution admission/return contract:    PASS
Context-transition conformance:         PASS
Latent/local semantic boundary:         PASS
Burden / kernel-inflation test:          PASS
Runtime installed/changed:              NO
```

## Decision

**R3 — PASS.**

The minimum runtime/operating contract is sufficiently defined to permit a separate concrete runtime-compilation step without reopening the conceptual architecture.

---

# 16. Next gate

**REALIZATION R4 — Runtime Carrier & Compilation Candidate.**

R4 may now design a concrete candidate realization, but must still separate:

1. **function** — G1…G6;
2. **carrier** — e.g. global Custom Instructions, Project-local instructions/context, Work/Codex handoff, Plugin/Skill, external state/tool enforcement;
3. **wording/configuration** — concrete implementation;
4. **conformance evidence** — proof that the carrier preserves the intended function in its actual execution context.

R4 should first answer:

- Which subset of G1–G6 genuinely belongs in global Custom Instructions versus another carrier?
- How should Project Instructions preserve/recompile baseline-critical functions given override behavior?
- What is the minimum handoff/preflight/return contract for Work/Codex/Plugin-App execution?
- What semantics should be retrieved from this repository or local knowledge rather than encoded in active runtime context?
- What small regression set can detect semantic loss and global-kernel inflation before deployment?

Only after that discrimination should final Custom Instruction wording or any installed runtime configuration be changed.
