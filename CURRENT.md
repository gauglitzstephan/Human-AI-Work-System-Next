# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED CONCEPTUAL ARCHITECTURE BASELINE v0.2 / REALIZATION PROGRAM R4  
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

No concrete runtime carrier has yet been installed.

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

R2 rejects universal Project or Work/plugin topologies and requires context-transition conformance rather than assuming instructions/state/capabilities transfer across surfaces.

## 5. R3 — Minimum Operating / Runtime Contract & Semantic Coverage

**Status: PASS / MINIMUM CONTRACT DEFINED.**

Controlling artifact:
- `realization/MINIMUM-OPERATING-RUNTIME-CONTRACT-v0.1.md`

R3 compresses the accepted architecture into **six global functions**, each carrying only the invariant/trigger needed cross-domain while detailed methods/state remain local or latent:

```text
G1 — Intent / outcome / scope qualification
G2 — Reality / state / authority routing
G3 — Professional / capability composition trigger
G4 — Adaptive sufficiency / preservation / dependency control
G5 — Claim / assurance / realization boundary
G6 — Execution-context conformance and return
```

### R3 coverage

```text
Core Requirements:          PASS — 13/13 owned
Conditional Requirements:   PASS — 7/7 trigger + local path
Project admission/exit:     PASS
Execution admission/return: PASS
Authoritative-state return: PASS
Human/authority return:     PASS
Context conformance:        PASS
Burden/inflation test:      PASS
Runtime installed:          NO
```

No seventh global function is currently justified.

### Global vs local boundary

Global runtime carries only:
- enough intent/scope qualification to prevent material misdirection;
- reality/state/authority routing;
- the trigger for local professional/capability composition;
- minimum-sufficient work/preservation/dependency control;
- claim/assurance/realization boundaries;
- context-transition conformance and return.

Detailed professional methods, DWM/Work Graph, domain rules/references, assurance methods, risk/security controls, uncertainty/commitment methods, portfolio logic, realization models, Project topology and reusable Skill/plugin content remain local/retrievable/conditional until a material trigger justifies them.

## 6. Current gate — R4

**REALIZATION R4 — Runtime Carrier & Compilation Candidate.**

R4 may now design a concrete realization candidate, but must keep separate:

```text
FUNCTION
  G1…G6

CARRIER
  global Custom Instructions / Project-local context / Work-Codex handoff /
  Plugin-Skill / external state-tool enforcement / assurance mechanism

WORDING / CONFIGURATION
  concrete runtime implementation

CONFORMANCE EVIDENCE
  proof that the implementation preserves the intended function
  in the actual execution context
```

R4 should first determine:

1. which subset of G1–G6 genuinely belongs in global Custom Instructions rather than another carrier;
2. how Project Instructions preserve/recompile baseline-critical functions given current override behavior;
3. the minimum preflight/handoff/return contract for Work, Codex and Plugin/App execution;
4. which semantics should be retrieved from this repository/local knowledge rather than encoded in active runtime context;
5. the smallest regression set able to detect semantic loss and global-kernel inflation before deployment.

Do **not** install/change final Custom Instructions, create/restructure Projects, build Skills/plugins/agents, migrate state or schedule automations until the R4 carrier/compilation candidate itself passes.

## 7. Reopen rule

Foundational architecture reopens only for ADR-0002 material triggers. Product limitations or realization friction should first be treated as Runtime/Operating realization problems unless they prove a required conceptual semantic cannot be represented or preserved.
