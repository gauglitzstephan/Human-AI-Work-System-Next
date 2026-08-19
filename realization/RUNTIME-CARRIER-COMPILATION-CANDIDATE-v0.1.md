# Runtime Carrier & Compilation Candidate v0.1

**Status:** REALIZATION R4 — COMPLETE / CARRIER CANDIDATE PASS  
**Date:** 2026-08-19  
**Conceptual baseline:** Target Architecture Baseline v0.2  
**R3 basis:** `realization/MINIMUM-OPERATING-RUNTIME-CONTRACT-v0.1.md`  
**Authority boundary:** This record allocates R3 functions to concrete carrier classes and runs a semantic regression/burden test. It does **not** install or change Custom Instructions, Project Instructions, Skills/plugins, Projects, state stores, Scheduled Tasks, Work/Codex flows or external actions.

---

# 1. Decision question

Given R3's six global functions:

```text
G1 — Intent / outcome / scope qualification
G2 — Reality / state / authority routing
G3 — Professional / capability composition trigger
G4 — Adaptive sufficiency / preservation / dependency control
G5 — Claim / assurance / realization boundary
G6 — Execution-context conformance and return
```

which functions should be carried by global Custom Instructions, which should be only triggered globally and realized elsewhere, and what is the smallest Project / Work / Codex / Plugin-App-Skill transition package that preserves semantics without copying the architecture into every runtime?

The answer must satisfy two competing constraints:

```text
NO UNOWNED SEMANTIC LOSS
AND
NO GLOBAL RUNTIME INFLATION
```

---

# 2. Current carrier reality relevant to R4

Official OpenAI product documentation reviewed 2026-08-19 establishes current implementation constraints used only as realization evidence:

1. Custom Instructions are a broad ChatGPT control surface. Current documented limits are 1,500 characters for Free/Go and 5,000 for Plus/Pro/Enterprise/Business/Edu. Changes apply to future conversations rather than retroactively changing prior chat history.
2. Project Instructions apply only in their Project and override global Custom Instructions. Moving a chat into a Project makes it inherit the Project's instructions and file context.
3. Project-only memory can prevent Project chats from referencing saved memories and conversations outside that Project. Continuity therefore cannot be assumed across Project boundaries.
4. Chat, Work and Codex are distinct execution surfaces. Work is oriented to longer multi-step tasks/deliverables; Codex to software/technical work. Work can use Project context; Codex retains a separate workflow/history and different technical capabilities.
5. Plugins package repeatable workflow capabilities and may contain Skills and Apps. Apps connect to external data/actions, but plugin availability and app-backed capability depend on plan/workspace/role/surface/region/configuration. Source-system permissions remain authoritative; plugin installation does not grant new data/action authority.

These constraints may change and do not become conceptual architecture invariants.

---

# 3. Carrier decision — one semantic kernel, multiple realizations

R4 separates four things:

```text
FUNCTION       what must happen (G1…G6)
SEMANTIC KERNEL what must remain cross-domain
CARRIER        where the semantic is active
METHOD/STATE   local implementation and authoritative data
```

The default realization candidate is:

```text
GLOBAL CUSTOM INSTRUCTIONS
  compact semantic kernel only

PROJECT INSTRUCTIONS [conditional]
  local method/context
  + kernel-compatibility stub when local instructions override global CI

WORK / CODEX / PLUGIN-APP-SKILL [conditional]
  transient execution contract generated for the actual transition

AUTHORITATIVE STATE / PERMISSIONS
  legitimate external/domain systems and owners

ASSURANCE
  claim/failure-mode-specific local mechanism

REPOSITORY / KNOWLEDGE CAPITAL
  detailed architecture, methods, references, reusable patterns
  retrieved only when triggered
```

No carrier is permitted to infer ownership it does not legitimately have.

---

# 4. G1–G6 carrier allocation

Legend:
- `FULL` — the global kernel should directly carry the essential rule.
- `TRIGGER` — global kernel carries only detection/routing; detailed realization is local.
- `LOCAL` — normally not encoded globally.

| Function | Global CI | Project/local | Tool/Execution | Assurance/external | Disposition |
|---|---|---|---|---|---|
| G1 Intent/outcome/scope | **FULL** | detail only | - | - | Global qualification rule |
| G2 Reality/state/authority | **TRIGGER + boundary** | state/domain semantics | authoritative read/write/permissions | Human/external owner | Global routing, local truth |
| G3 Professional/capability composition | **TRIGGER** | **FULL local method/reference** | actual capability | expert/assurance where needed | Never globalize professional method |
| G4 Adaptive sufficiency/preservation/dependency | **FULL** | dependency detail | execution as selected | - | Core global work-control rule |
| G5 Claim/assurance/realization | **TRIGGER + boundary** | claim/use criteria | deterministic checks | **FULL local assurance/outcome evidence** | Claim discipline global, method local |
| G6 Context conformance/return | **TRIGGER + invariant** | Project compatibility | transient execution contract | legitimate return owner | Global crossing rule, local package |

## R4 conclusion

All six G-functions need a **global semantic anchor**, but only **G1 and G4** require nearly their full cross-domain logic in active global instructions.

G2, G3, G5 and G6 should be globally compressed to boundary/trigger semantics and realized through the actual domain/state/method/execution/assurance carrier when activated.

This avoids both a domain-agnostic generic quality model and a global architecture overlay.

---

# 5. Global Custom Instruction compilation candidate — semantic clauses, not final wording

R4 does **not** freeze final user-visible Custom Instruction text. It defines a five-clause compilation target capable of carrying G1–G6.

## K1 — QUALIFY
Carry G1.

Semantic obligation:
> Treat a request, proposed means or current artifact as sufficient only when it is adequate for the material next action; otherwise resolve enough intended outcome, scope and success condition to avoid misdirection.

## K2 — GROUND / AUTHORITY
Carry the global portion of G2.

Semantic obligation:
> When current reality/state/ownership materially changes the work, inspect the legitimate source or surface the unresolved dependency; distinguish working context from authoritative state/knowledge and capability/access from legitimate authority.

## K3 — COMPOSE / MINIMIZE
Compile G3 + G4.

Semantic obligation:
> Activate local professional method, references, Human/AI/tool capability and additional structure only when they materially improve quality/risk/value; choose the minimum justified next work, preserve qualified work and never skip required dependencies/readiness.

Human participation belongs here only when judgment, learning/authorship, exclusive information or legitimate authority is materially non-substitutable.

## K4 — QUALIFY CLAIM / CLOSE
Carry the global portion of G5.

Semantic obligation:
> Do not claim more than the evidence can establish; use assurance capable of detecting the material failure mode, distinguish technical/professional/use/outcome boundaries, and stop at the strongest supported closure rather than generating substitute internal work.

## K5 — TRANSITION / RETURN
Carry the global portion of G6.

Semantic obligation:
> When moving across Project/Work/Codex/Plugin-App-Skill/Task contexts, do not assume instructions, state, capability, permission or authority transfer; reconstruct only the missing minimum, verify the result/state, and return/reconcile material outcomes with the legitimate owner/context.

### Compilation budget

Candidate target for the later wording step:

```text
5 clauses
≤ 1,200 characters preferred
no domain method
no architecture vocabulary required for the user
no fixed stage sequence
no mandatory explicit narration
```

The `≤1,200` target is a portability/burden constraint, not a conceptual requirement. It leaves margin under the currently documented 1,500-character Free/Go Custom Instruction limit and prevents using larger-plan limits as an excuse for kernel inflation.

---

# 6. Project carrier candidate

Projects remain conditional continuity/context carriers.

## 6.1 Default

Do **not** add Project Instructions merely because a Project exists. If project context/files alone are sufficient, retain the global kernel as the cross-domain control carrier and keep local state/method in sources/context.

## 6.2 When Project Instructions are materially useful

Use Project Instructions for:
- domain-specific purpose/non-goals;
- local professional method/reference use;
- local terminology/quality constraints;
- legitimate state/authority pointers;
- recurring return/acceptance conventions.

Do not copy the full conceptual baseline or all G1–G6 prose.

## 6.3 Kernel compatibility stub

Because current Project Instructions override global Custom Instructions, any Project with material Project Instructions must preserve the minimum cross-domain semantics locally.

R4 candidate stub contains only three semantic bundles:

```text
P1  qualify outcome/scope + use authoritative current state/authority
P2  use local professional method and minimum sufficient work; preserve dependencies
P3  claim only what evidence supports; verify cross-context execution and return to legitimate owner
```

This is a **semantic stub specification**, not frozen wording.

If Project-only memory is used, any personal/domain context required by the work must be explicitly available inside the Project rather than assumed to transfer from saved memory or outside conversations.

---

# 7. Work / Codex / Plugin-App-Skill execution carrier

These surfaces/packages do not receive persistent copies of the global kernel by default.

Instead, context transition creates a **transient Execution Contract** only when a real cross-context transfer occurs.

## Minimum Execution Contract

```text
1. OBJECTIVE / CLAIM
   exact result or state transition expected

2. AUTHORITATIVE INPUTS
   current state/pointers/evidence needed for this execution

3. BINDING REQUIREMENTS / METHOD
   only constraints/professional method required for the task

4. CAPABILITY / ACCESS / AUTHORITY
   actual target capability and permissions;
   Human/external authorization where required

5. OUTPUT / ASSURANCE / READBACK
   what output/state must exist and how material success is checked

6. RETURN / RECONCILIATION OWNER
   where the result, limitations, decisions and persistent state go next
```

This contract may remain implicit for simple same-context tool calls. It becomes explicit only when context/state/authority/assurance can materially diverge.

## Work
Use when longer multi-step execution lowers total burden or supports a substantial deliverable. Project context may be supplied where available, but output/readiness still returns to the responsible domain/Human.

## Codex
Use when success depends on real repositories/files/commands/tests/technical diffs. Technical PASS is not substantive acceptance.

## Plugins / Apps / Skills
- Skill = reusable workflow/method carrier only after transfer value is qualified.
- App = capability/data/action binding under actual app/source-system permissions.
- Plugin = packaging/discovery, not authority or state ownership.

A plugin/skill must not become the hidden owner of G1–G6; it operates under the current objective/state/authority/claim contract.

## Scheduled/triggered execution
Use the same Execution Contract plus an explicit observation source and notification/mutation authority. If required project/source context is unavailable in the task's actual execution environment, the task is not qualified for that monitoring/action claim.

---

# 8. What remains repository/local rather than active runtime

Do not compile these into global CI or every Project stub:

- full Target Architecture / 11 Concerns / 13+7 Requirements;
- five Responsibility descriptions;
- DWM / Work Graph / B.6;
- detailed professional performance models;
- domain standards/reference libraries;
- detailed evidence-qualified reuse procedure;
- assurance ladder / reviewer topology;
- risk/security/privacy control catalogues;
- foresight/robustness/commitment methods;
- portfolio/WIP/capacity method;
- Human capability formation model;
- realization/benefit/causal model;
- surface-specific tool instructions and connection details.

The global kernel needs only the trigger/route required to retrieve or activate these when material.

Repository artifacts remain architecture/method Knowledge Capital, not automatically active instructions.

---

# 9. Semantic regression set

R4 tests carrier semantics rather than model wording. A PASS means the carrier allocation contains a route capable of preventing the known failure without requiring unnecessary standing structure.

| Case | Expected carrier behavior | Result |
|---|---|---|
| T1 — trivial rewrite / simple answer | K1 sees no material ambiguity; K3 keeps direct path; no Project/Work/graph/research | **PASS** |
| T2 — user proposes a potentially wrong solution | K1 qualifies outcome/scope before commitment; local alternative search only if decision-relevant | **PASS** |
| T3 — repair existing repo/process/artifact | K2 triggers authoritative current-state recovery; K3/K4 preserve valid work and localize repair | **PASS** |
| T4 — S-Payment-style professional artifact | K3 routes to real professional/recipient method; K4 requires detection-capable assurance, not checklist/process completion | **PASS** |
| T5 — Bergfreunde binding timing / live-use constraint | local artifact method + deterministic/representative assurance; minimum work cannot skip binding dependency | **PASS** |
| T6 — recurring domain with persistent context | Project admitted conditionally; state remains authoritative in legitimate store; Project instructions use compatibility stub if present | **PASS** |
| T7 — Project Instructions override global CI | compatibility stub becomes mandatory for material local instructions; no assumption of global inheritance | **PASS** |
| T8 — Codex repo change | transient Execution Contract carries objective/current repo state/constraints/authority/tests/return; technical PASS ≠ Human acceptance | **PASS** |
| T9 — Plugin/App external write | availability/access checked; source-system permission ≠ legitimate business decision authority; readback + owner reconciliation | **PASS** |
| T10 — Scheduled Task lacks required project/source context | G6/Execution Contract exposes missing observation path; automation remains unqualified rather than fabricating monitoring | **PASS** |
| T11 — material future uncertainty | K3 invokes only the local uncertainty/commitment method when it can change route/value; no global foresight ceremony | **PASS** |
| T12 — competing initiatives / portfolio pressure | K1/K3 detect that local work lacks strategic priority authority and route to Human/Operating owner rather than silently optimizing locally | **PASS** |
| T13 — local defect after substantial valid work | K3 preserves unaffected qualified work; no global restart | **PASS** |
| T14 — Human is asked to review everything | K3/K4 keep Human gates only for non-substitutable judgment/authority or genuinely stronger assurance | **PASS** |

## Known failure-class coverage

```text
S-Payment professional-quality/self-confirmation      PASS
Bergfreunde binding constraint / representative use   PASS
room/handoff ceremony inflation                       PASS
existing-system regeneration instead of recovery      PASS
project/context override semantic loss                PASS
capability/access/authority conflation                 PASS
local defect → global restart                         PASS
simple work → process bureaucracy                     PASS
```

---

# 10. Burden / inflation test

## Global standing burden

Candidate global active content:
- five short semantic clauses;
- no architecture taxonomy;
- no domain method;
- no mandatory visible workflow;
- no persistent Work Object/state schema.

**Result: PASS candidate.**

## Project burden

Project compatibility stub activates only when material Project Instructions exist; ordinary Projects do not automatically receive additional instruction scaffolding.

**Result: PASS candidate.**

## Execution burden

Execution Contract is generated only on material context transitions. Same-context simple tool calls may remain implicit.

**Result: PASS candidate.**

## Product dependence

Custom Instructions are the current preferred global carrier, but the semantic kernel remains provider/surface-independent. If CI behavior/limits change, the same five semantic clauses can be relocated to another top-level instruction/control carrier without reopening the conceptual architecture.

**Result: PASS with runtime-version dependency explicit.**

---

# 11. Residual risks before deployment

R4 semantic PASS is not behavioral proof.

Remaining risks:

## RR1 — Wording compression failure
Five correct semantic clauses may be phrased too vaguely, too densely or with salience conflicts. Exact wording requires shadow testing.

## RR2 — Current Custom Instruction collision
The user's existing Custom Instructions may already contain valuable work-style, professional or control semantics. Installing a new kernel without recovering and reconciling the actual current CI could cause regression even if the new kernel is internally sound.

## RR3 — Project compatibility wording
A three-bundle Project stub may still lose one global semantic in practice. It requires a project-override shadow test.

## RR4 — Execution Contract over-formalization
If made visible/mandatory for ordinary transitions, the six-field contract could become the next handoff bureaucracy. Runtime realization must keep it implicit unless divergence risk is material.

## RR5 — Model/surface behavior
Instruction precedence, model behavior and available tools can change. Behavioral conformance must be tested in the actual target contexts rather than inferred from this specification.

---

# 12. R4 verdict

```text
Global carrier candidate:
Custom Instructions — YES, compact semantic kernel only

Global compilation shape:
5 clauses carrying G1–G6 — PASS candidate

Project carrier:
local method/context + compatibility stub only when Project Instructions exist

Work/Codex/Plugin/App/Skill carrier:
transient Execution Contract on material context transition

Authoritative state:
external/domain legitimate stores — unchanged

Assurance:
claim/failure-mode local — unchanged

Semantic regression set:
14/14 PASS at carrier/specification level

Burden test:
PASS

Final wording installed:
NO

Runtime behavioral effectiveness:
NOT ESTABLISHED
```

R4 therefore **PASSES as a carrier/compilation candidate** and does not authorize deployment.

---

# 13. Next gate

**REALIZATION R5 — Current Runtime Reconciliation & Shadow Compilation.**

Before installing anything:

1. recover the **actual current Custom Instructions / active global work-style controls** and classify each existing element as `KEEP / COVERED BY K1–K5 / MOVE LOCAL / REMOVE / CONFLICT / UNKNOWN`;
2. compile one exact global CI candidate from K1–K5 within the chosen character budget;
3. compile one exact Project compatibility stub and one minimal transient Execution Contract template;
4. run the exact wording in **shadow** against the R4 regression set plus representative ordinary-use cases;
5. compare baseline/current-CI behavior vs candidate for semantic coverage, professional-work quality, Human burden and over-processing;
6. install nothing unless the candidate demonstrates no material regression and a clear burden/quality advantage.

Existing Custom Instructions are evidence/current runtime state, not disposable legacy text. R5 must reconcile them before any replacement.