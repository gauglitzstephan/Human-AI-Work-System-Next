# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / REALIZATION PROGRAM R3  
**Date:** 2026-08-19  
**Accepted conceptual baseline:** PR #3, merge SHA `0b2dc8f3d369cc5d0e5c8ec502449ccf11c7464e`  
**Current branch:** `realization/architecture-runtime-operating-v0.1`

## 1. Controlling baseline

The conceptual baseline is accepted and foundational architecture is **closed by default**:

1. `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`
2. `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`
3. `decisions/ADR-0002-target-conceptual-baseline.md`

Accepted structural commitments remain:

```text
A. DISTINCT RESPONSIBILITIES
   Strategic / Operating / Work / Execution / Learning-Change

B. DISTRIBUTED TYPED STATE
   authoritative state remains with legitimate owners/stores;
   working context is composed as needed

C. ADAPTIVE WORK-SELECTION CONTRACT
   for admitted/triggered work, select the minimum justified next work
   while preserving reality, qualified state, dependency integrity,
   professional quality, capability/authority/runtime reality,
   assurance, uncertainty and net value
```

No mandatory DWM, Work Graph, B.6 stage machine, Semantic Compiler subsystem, eight-View structure, PAOS topology, Control-Plane modules or fixed runtime topology is accepted.

## 2. Realization program boundary

The active problem is **Architecture → Runtime / Operating Realization**, separate from conceptual architecture design.

Realization allocates baseline semantics to Humans/external owners, persistent Operating state/policy/capability, runtime context/control, work-local method/context, tools/apps/technical enforcement and assurance/observability while minimizing burden and preventing unowned semantic loss.

No concrete runtime carrier is installed by the R1/R2 records.

## 3. R1 — Semantic Allocation & Platform Reality Mapping

**Status: PASS AS MAPPING CANDIDATE.**

Controlling artifact:
- `realization/SEMANTIC-ALLOCATION-PLATFORM-REALITY-v0.1.md`

Primary direction:

```text
HUMAN / EXTERNAL OWNER
  purpose, judgment, acceptance, authority

OPERATING / AUTHORITATIVE STATE
  persistent domain truth, ownership, accepted patterns/capabilities

THIN GLOBAL RUNTIME
  only cross-domain control semantics that must survive ordinary work

WORK / PROJECT / DOMAIN LOCAL
  current context, professional method, references, requirements

TOOLS / APPS
  real retrieval/write, deterministic checks, computation/actions, permissions

ASSURANCE / OBSERVABILITY
  claim/failure-mode-specific evidence and readback

LATENT
  formal DWM/Work Graph/lifecycle/etc. until material triggers justify them
```

## 4. R2 — Minimum Runtime / Operating Profile Discrimination

**Status: PASS / DEFAULT PLACEMENT DECIDED.**

Controlling artifact:
- `realization/MINIMUM-RUNTIME-OPERATING-PROFILE-DISCRIMINATION-v0.1.md`

Decision:

```text
A — GLOBAL-KERNEL MINIMAL
    DEFAULT — PROMOTE

B — PROJECT-CENTRIC CONTINUITY
    CONDITIONAL CONTEXT PROFILE — RETAIN

C — WORK / PLUGIN-ORCHESTRATED EXECUTION
    CONDITIONAL CAPABILITY PROFILE — RETAIN
```

Meaning:

```text
DEFAULT
  ordinary work starts with a thin cross-domain kernel / direct Chat posture

WHEN CONTINUITY EARNS IT
  Project/domain context carries local instructions/sources/continuity
  while authoritative state remains with legitimate owners/stores

WHEN EXECUTION/CAPABILITY EARNS IT
  Work / Codex / Plugin / App / Skill / tool is selected for the actual required capability
  under real access/permission/runtime conditions
```

R2 rejects:
- universal Project topology;
- universal Work/plugin topology;
- Project as authoritative truth merely because context is present;
- Plugin/Skill availability as authority;
- encoding the full conceptual architecture into global instructions.

### Context-transition conformance

When work crosses into a Project, Work, Codex, Scheduled Task or Plugin/App-backed execution context, material instructions/state/capability/authority are not assumed to transfer automatically.

The realization must verify what the target context actually receives, recompile only the missing semantic minimum, then reconcile returned result/state with the legitimate owner/context.

This is particularly material because current Project Instructions override global Custom Instructions and current Scheduled Tasks may not have access to Project files.

## 5. Current gate — R3

**REALIZATION R3 — Minimum Operating/Runtime Contract & Semantic Coverage.**

R3 must define only:

1. the minimum cross-domain functions the global kernel must reliably carry;
2. admission/exit contracts for Project continuity and Work/Codex/Plugin execution;
3. authoritative-state and Human/authority return contracts;
4. context-transition conformance / semantic-preservation requirements;
5. which baseline semantics remain latent/retrievable rather than globally encoded;
6. a coverage/burden test capable of rejecting global-kernel inflation before wording or deployment.

Do **not** yet write/install final Custom Instructions, create/restructure Projects, build Skills/plugins/agents, migrate state or schedule automations.

Only after R3 passes should a concrete runtime carrier candidate be designed.

## 6. Reopen rule

Foundational architecture reopens only for ADR-0002 material triggers. Product limitations or realization friction should first be treated as Runtime/Operating realization problems unless they prove a required conceptual semantic cannot be represented or preserved.
