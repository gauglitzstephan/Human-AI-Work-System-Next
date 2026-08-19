# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / REALIZATION PROGRAM R2  
**Date:** 2026-08-19  
**Accepted conceptual baseline:** PR #3, merge SHA `0b2dc8f3d369cc5d0e5c8ec502449ccf11c7464e`  
**Current branch:** `realization/architecture-runtime-operating-v0.1`

## 1. Controlling baseline

The conceptual baseline is accepted and foundational architecture is **closed by default**:

1. `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`
2. `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`
3. `decisions/ADR-0002-target-conceptual-baseline.md`

The conditional merge clause in ADR-0002 has occurred. `PROPOSED` wording inside those pre-merge artifacts records authoring provenance and does not override the accepted state.

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

The active problem is now **Architecture → Runtime / Operating Realization**, separate from conceptual architecture design.

Realization must allocate baseline semantics to actual Humans, persistent Operating state/policy/capability, runtime context/control, work-local method/context, tools/apps/technical enforcement and assurance/observability while minimizing burden and preventing unowned semantic loss.

No runtime build/deployment is authorized until the realization profile is discriminated and reviewed.

## 3. R1 — Semantic Allocation & Platform Reality Mapping

**Status: PASS AS MAPPING CANDIDATE.**

Controlling artifact:
- `realization/SEMANTIC-ALLOCATION-PLATFORM-REALITY-v0.1.md`

R1 mapped all 13 Core and 7 Conditional Requirements to the smallest plausible realization owners and reviewed current ChatGPT/OpenAI implementation reality for Chat, Work, Projects, Memory, Custom/Project Instructions, Plugins/Apps/Skills, Scheduled Tasks and Codex.

Primary direction from R1:

```text
HUMAN / EXTERNAL OWNER
  purpose, values, material judgment/acceptance/authority

OPERATING / AUTHORITATIVE STATE
  persistent domain truth, ownership, accepted patterns/capabilities

THIN GLOBAL RUNTIME
  only cross-domain control semantics that must reliably survive ordinary work

WORK / PROJECT / DOMAIN LOCAL
  current state, professional method, references, requirements, artifact context

TOOLS / APPS
  real retrieval/write, deterministic checks, computation/actions, permissions

ASSURANCE / OBSERVABILITY
  claim/failure-mode-specific evidence, validation, readback, monitoring

LATENT
  DWM/Work Graph/lifecycle/assurance ledgers/etc. until material triggers justify them
```

R1 explicitly rejects treating ChatGPT Project/Memory/chat as authoritative truth merely because context is available, treating Scheduled Tasks as a truth store, or transferring capability/state claims across Chat/Work/Codex/Task/App contexts without evidence.

## 4. Current gate — R2

**REALIZATION R2 — Minimum Runtime / Operating Profile Discrimination.**

Compare the smallest plausible default ownership profiles:

```text
A — GLOBAL-KERNEL MINIMAL
    tiny cross-domain runtime invariants
    + domain/project/external state retrieved as needed

B — PROJECT-CENTRIC
    minimal global kernel
    + Projects as primary continuity/context carrier
    + external authoritative state

C — WORK/PLUGIN-ORCHESTRATED
    minimal global kernel
    + Work as long-task controller
    + Plugins/Skills/Apps as reusable capability packages
    + external authoritative state
```

These are realization profiles, not new conceptual architectures and not necessarily mutually exclusive products. R2 asks which responsibilities each profile should own **by default** and which remain conditional.

Evaluate only:
- CR-01…CR-13 coverage;
- ordinary-work burden;
- state/authority integrity;
- runtime-context fidelity;
- professional-method locality;
- portability/exit;
- observability/debuggability;
- failure containment;
- dependence on mutable product capability.

Do **not** write Custom Instructions, create/restructure Projects, build Skills/plugins or schedule automations before R2 passes.

## 5. Reopen rule

Foundational architecture reopens only for ADR-0002 material triggers. Product limitations or realization friction should first be treated as Runtime/Operating realization problems unless they prove a required conceptual semantic cannot be represented or preserved.
