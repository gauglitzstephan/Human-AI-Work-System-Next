# Minimum Runtime / Operating Profile Discrimination v0.1

**Status:** REALIZATION R2 — COMPLETE / CANDIDATE DISPOSITION  
**Date:** 2026-08-19  
**Conceptual baseline:** Target Architecture Baseline v0.2  
**R1 basis:** `realization/SEMANTIC-ALLOCATION-PLATFORM-REALITY-v0.1.md`  
**Authority boundary:** This record chooses default realization placement only. It does not install Custom Instructions, create/restructure Projects, build Skills/plugins/agents, migrate state, schedule Tasks, deploy Work/Codex flows or authorize external actions.

---

# 1. Decision question

Which realization profile should be the **default operating posture** for the accepted Human–AI Work System, given that the conceptual architecture requires:

- distinct responsibilities without mandatory subsystem topology;
- distributed typed state rather than one universal state store;
- one adaptive work-selection contract for admitted/triggered work;
- professional method and authoritative state to remain local where appropriate;
- runtime/context fidelity and semantic preservation;
- aggressive proportionality for ordinary work?

Compare only:

```text
A — GLOBAL-KERNEL MINIMAL
    thin cross-domain runtime control; ordinary Chat remains the default entry;
    domain context/state/method is loaded or activated only when material

B — PROJECT-CENTRIC CONTINUITY
    Project becomes the default Context Home for continuing work;
    project files/chats/instructions/memory carry continuity

C — WORK / PLUGIN-ORCHESTRATED EXECUTION
    longer Work plus Plugins/Apps/Skills become the default execution/orchestration carrier
```

These are realization profiles, not conceptual architecture alternatives.

---

# 2. Current product reality relevant to R2

Official OpenAI documentation checked 2026-08-19 establishes:

1. **Custom Instructions** are a broad ChatGPT-level control surface and are available across plans. They are mutable runtime configuration, not architecture authority.
2. **Projects** group chats/files/instructions/context for continuing work. Project Instructions apply only inside a Project and **override global Custom Instructions**. Projects therefore improve locality/continuity but create a semantic-preservation boundary whenever local instructions are present.
3. **Work** is an agent for longer, multi-step work and finished deliverables; Chat remains the fast conversational surface. Work availability is plan/workspace dependent.
4. **Plugins** package Skills and Apps. App-backed capabilities remain constrained by workspace/role/surface/region availability, app settings and the user's permissions in the underlying source system. Plugin installation does not itself grant data/action authority.
5. **Scheduled Tasks** have a distinct execution context; a task created in a Project cannot currently access that Project's files. Scheduling therefore cannot be assumed to preserve interactive Project context.
6. **Memory/chat history** provides useful selective personalization/context but is not a complete operational record.

These are current implementation facts, not stable architecture invariants.

---

# 3. Evaluation criteria

Each profile is evaluated against:

1. 13 Core + 7 Conditional Requirement coverage;
2. ordinary-work cognitive/coordination burden;
3. state and authority integrity;
4. runtime/context fidelity;
5. professional-method locality;
6. portability/exit;
7. observability/debuggability;
8. failure containment/blast radius;
9. dependence on mutable product capability.

The question is not which profile has the most features. It is which profile is the smallest safe **default**, with other profiles activated only where they add decision value.

---

# 4. Candidate A — Global-kernel minimal

## Shape

```text
ordinary input
→ Chat / current surface
→ thin cross-domain control semantics
→ retrieve/activate domain context only when needed
→ use tools/Work/Project/external state conditionally
```

The global kernel carries only semantics that repeatedly matter across domains and are expensive to rediscover or omit, e.g.:

- raw input/proposed means is not automatically the requirement/outcome;
- current reality/authority before consequential redesign;
- capability/access/authority distinction;
- minimum sufficient work / bounded reopening;
- exact claim does not exceed evidence;
- runtime-context differences cannot be assumed away.

It does **not** carry domain methods, live project state, Work Graphs/DWM objects, artifact methods, portfolio data or full architecture prose.

## Requirement coverage

**High as a default posture, incomplete as a standalone system.**

A can activate the accepted work-selection semantics with the lowest standing burden, while delegating/pulling:
- authoritative state from legitimate stores;
- professional method from work/domain context;
- persistent continuity from Projects/external systems only when required;
- technical execution from tools/Work/Codex/Apps;
- assurance according to claim/failure mode.

This is compatible with distributed state and conditional structure.

## Strengths

- lowest ordinary-work burden;
- preserves direct Chat usefulness;
- lowest risk of making every input a project/workflow;
- strong method locality and proportionality;
- smallest dependence on specialist product features;
- easiest conceptual portability to other surfaces/providers;
- most consistent with `latent unless material` semantics.

## Material risks

### A-R1 — broad blast radius
A defective global kernel affects many work classes.

Mitigation requirement: keep it thin, stable, semantic rather than domain-specific, and change only with strong evidence.

### A-R2 — semantic loss inside Projects
Project Instructions override global Custom Instructions. A Project with local instructions therefore cannot simply be assumed to inherit the global kernel.

Mitigation requirement:

```text
enter Project / local instruction context
→ establish whether baseline-critical global semantics remain effective
→ if not, recompile only the required semantic minimum locally
→ never copy the full architecture by default
```

### A-R3 — insufficient continuity for persistent work
A plain chat/global kernel cannot itself guarantee durable domain context/state.

Mitigation: activate B only when continuity/state/local-policy value is material.

## Burden

**LOW standing burden.**

Main burden is semantic compression/conformance, not user ceremony.

---

# 5. Candidate B — Project-centric continuity

## Shape

```text
material domain / continuing initiative
→ Project as Context Home
→ project instructions + sources + chats/memory
→ Chat or Work executes inside that context
→ external authoritative state remains authoritative
```

## Requirement coverage

**High for persistence/locality; unnecessary for ordinary bounded work.**

Strongest for:
- CR-04 current state before change;
- CR-05 local professional method/reference;
- CR-09 state/knowledge continuity;
- CR-13 runtime-context specificity;
- CCR-02 persistent/divergent state;
- recurring domain work.

But a Project does not by itself satisfy authoritative state, freshness, acceptance, external action authority or outcome evidence.

## Strengths

- lower context re-entry cost for continuing work;
- strong locality for domain instructions/method/reference;
- domain-level failure containment relative to global instructions;
- easier human legibility of continuing work;
- good fit for repeated/evolving work where the same sources/decisions recur.

## Material risks

### B-R1 — Project-as-truth confusion
Files/chats/project memory may be stale, partial or derived. Project presence does not establish authority.

### B-R2 — instruction override / semantic regression
Project Instructions override global Custom Instructions. Local specialization can therefore silently remove global baseline semantics if conformance is not explicit.

### B-R3 — project proliferation
Making Project the default for ordinary work recreates persistence/coordination burden and risks formalizing transient work.

### B-R4 — portability/context lock-in
Continuity becomes tied to a product-specific container unless essential state/method remains externally understandable/exportable.

## Burden

**MEDIUM**, justified only when domain continuity, local instructions/sources, recurring work, state reconciliation or return obligations materially reduce total work cost/risk.

## Scope decision

**NOT DEFAULT. CONDITIONAL CONTEXT HOME.**

Activate when one or more material conditions exist, such as:
- recurring multi-session work;
- dedicated professional/reference sources;
- domain-specific instructions/constraints;
- continuing decisions/current artifacts requiring return;
- persistent state that must be repeatedly reconciled;
- multiple related outputs whose shared context materially reduces rework.

No fixed numeric admission threshold is required.

---

# 6. Candidate C — Work / Plugin-orchestrated execution

## Shape

```text
bounded work with meaningful execution/capability need
→ Work / Codex / Plugin/Skill/App chosen for actual required capability
→ tool/app reads/actions under real permissions
→ output/state returned to responsible context/owner
```

## Requirement coverage

**Strong execution capability; weak as a whole operating default.**

C is strongest for:
- CR-06 comparative composition;
- CR-08 actual capability/access;
- CR-11 tool/detection-capable assurance;
- CR-13 runtime fidelity;
- consequential technical execution where real tools/files/actions are required.

But it does not inherently own:
- legitimate purpose/strategic priority;
- authoritative domain state;
- professional method quality;
- Human acceptance/commitment;
- outcome/value observation.

## Strengths

- high leverage for longer multi-step production;
- access to connected data/actions where explicitly available;
- reusable Skills can encode proven repeated methods;
- Codex offers strong technical execution/test capability;
- Work supports longer bounded deliverable production and human redirection/approval.

## Material risks

### C-R1 — mutable capability dependency
Availability varies by plan, workspace, role, surface, region and app configuration.

### C-R2 — capability ≠ authority
Plugin/App availability does not grant source-system permission or legitimate decision authority. Existing app permissions and source-system permissions still control access/actions.

### C-R3 — workflow cargo-culting
A repeatable package can freeze local assumptions into a reusable default before transfer value is established.

### C-R4 — orchestration inflation
Using Work/plugins for tasks Chat can handle directly adds coordination, latency and debugging surface without necessarily improving quality.

### C-R5 — surface/state discontinuity
Work/Codex/Tasks/Plugins may not share identical context/state/tool access. Returning results to the correct context/state owner remains necessary.

## Burden

**MEDIUM-HIGH to HIGH**, varying by execution mode, connections, approvals and tool/runtime complexity.

## Scope decision

**NOT DEFAULT. CONDITIONAL EXECUTION/CAPABILITY PROFILE.**

Activate only when the current work requires one or more of:
- longer autonomous/multi-step production whose coordination burden is lower than interactive Chat;
- real files/repos/commands/tests;
- connected authoritative retrieval unavailable in plain context;
- external actions through an authorized App;
- a validated reusable Skill/workflow whose transfer value exceeds bespoke work;
- claim-specific technical enforcement/observability that the simpler surface cannot provide.

---

# 7. Comparative decision matrix

| Criterion | A Global-kernel minimal | B Project-centric continuity | C Work/plugin execution |
|---|---|---|---|
| Core requirement coverage as default | **HIGH with conditional delegation** | HIGH for persistent/domain work | MEDIUM as whole-system default / HIGH execution-only |
| Ordinary-work burden | **LOW** | MEDIUM | MEDIUM-HIGH / HIGH |
| State/authority integrity | **HIGH if state stays external/local** | MEDIUM-HIGH; Project-as-truth risk | MEDIUM-HIGH; permissions/action risk |
| Runtime-context fidelity | MEDIUM; needs context preflight | HIGH locally; override boundary critical | HIGH when preflighted; capability highly variable |
| Professional-method locality | **HIGH** | **HIGH** | MEDIUM-HIGH via Skills/local context |
| Portability/exit | **HIGH semantic portability** | MEDIUM | LOW-MEDIUM |
| Observability/debuggability | MEDIUM | MEDIUM | HIGH for tool/technical runs, variable otherwise |
| Failure containment | MEDIUM-HIGH; global-kernel defect broad | **HIGH domain containment** | MEDIUM; capability/action blast radius varies |
| Mutable-product dependency | **LOWEST** | MEDIUM | **HIGHEST** |
| Fit with proportionality | **STRONGEST** | conditional | conditional |

---

# 8. R2 decision

## Default

# **A — GLOBAL-KERNEL MINIMAL: PROMOTE AS DEFAULT OPERATING POSTURE**

Meaning:

```text
ordinary work starts simple
→ thin cross-domain runtime semantics
→ retrieve/activate only the context/capability needed
→ preserve external/domain authority
→ escalate structure only when a material trigger exists
```

A is **not** the entire runtime. It is the default entry/control posture from which B and C are conditionally activated.

## Conditional continuity

# **B — PROJECT-CENTRIC CONTINUITY: RETAIN AS CONDITIONAL CONTEXT PROFILE**

Projects are appropriate when continuity/local instructions/sources/return obligations materially earn their maintenance cost.

Critical rule:

> Project context improves continuity but does not become authoritative truth, and Project Instructions may not silently erase baseline-critical global semantics merely because they override global Custom Instructions.

## Conditional execution

# **C — WORK / PLUGIN-ORCHESTRATED EXECUTION: RETAIN AS CONDITIONAL CAPABILITY PROFILE**

Use Work/Codex/Plugins/Apps/Skills only when required capability, execution depth, connected state/action or proven workflow reuse provides sufficient value over the simpler route.

They never inherit legitimate authority merely from availability.

---

# 9. Resulting minimum operating profile

R2 does **not** introduce a new architecture topology. It establishes default placement:

```text
DEFAULT
  thin cross-domain kernel in ordinary Chat/runtime

WHEN CONTINUITY EARNS IT
  Project/domain Context Home
  + external authoritative state remains external/owned

WHEN EXECUTION/CAPABILITY EARNS IT
  Work / Codex / Plugin / App / Skill / tool
  + actual permissions/runtime preflight

ALWAYS WHERE MATERIAL
  claim-bound assurance
  + result/state returned to legitimate owner/context
```

The profile is progressive only in the ordinary sense that more mechanism is activated when a requirement triggers it. It is not a mandatory stage sequence.

---

# 10. Important semantic-preservation contract exposed by R2

R2 reveals one realization contract that must be explicit before implementation:

## CONTEXT-TRANSITION CONFORMANCE

When work crosses into a Project, Work, Codex, Scheduled Task or Plugin/App-backed execution context, do not assume that instructions, context, state, capability or authority transfer automatically.

For material semantics:

```text
source context
→ identify baseline-critical semantics/state needed downstream
→ verify actual target-context availability/inheritance/binding
→ recompile only the missing minimum
→ execute
→ verify returned result/state
→ reconcile with legitimate owner/context
```

This is not a new conceptual-architecture object. It is the realization consequence of CR-02, CR-08, CR-09 and CR-13.

---

# 11. R2 gate verdict

```text
A Global-kernel minimal           DEFAULT — PROMOTE
B Project-centric continuity      CONDITIONAL — RETAIN
C Work/plugin execution           CONDITIONAL — RETAIN

Universal Project topology        REJECT
Universal Work/plugin topology    REJECT
Project as authoritative truth    REJECT
Plugin/Skill as authority         REJECT
Full architecture in global CI    REJECT
```

No runtime has been installed or changed.

---

# 12. Next gate

**REALIZATION R3 — Minimum Operating/Runtime Contract & Semantic Coverage.**

Do not write final Custom Instructions yet.

R3 should define only:

1. the **minimum cross-domain functions** the global kernel must reliably carry;
2. the **admission/exit contracts** for Project continuity and Work/Codex/Plugin execution;
3. authoritative-state and Human/authority return contracts;
4. context-transition conformance / semantic-preservation requirements;
5. which baseline semantics must remain latent/retrievable rather than encoded globally;
6. a coverage/burden test that can reject global-kernel inflation before wording or deployment.

Only after R3 passes should any concrete instruction/Skill/Project/runtime carrier be designed.