# Route B ChatGPT Adapter Compilation Definition v0.5

## Status

- Adapter source status: `CANDIDATE`
- Installation status: `NONE`
- Runtime claim: `NONE`
- Initial provider scope: ChatGPT Chat and Work only
- Codex adapter: outside initial claim

This definition maps provider-neutral Route-B sources to ChatGPT carriers. It does not change Route-B architecture or create a Runtime claim.

## Source inputs

Required inputs:

- `01-CANDIDATE-CONTRACT.md`
- `02-CANONICAL-KERNEL.md`
- `03-FORMATION-METHOD.md`
- `07-CORE-WORK-FUNCTIONS-AND-METHOD-CONTRACT.md`
- a project-local overlay when compiling Project Instructions
- adapter identity and target-surface data for the manifest

Generated payloads are subordinate compiled views. They cannot become independent semantic authorities.

## Effective carrier resolution

| Path | Effective Kernel carrier | Core Method availability | Formation carrier | Operational owner |
|---|---|---|---|---|
| Non-Project Chat | Global Custom Instructions compilation | compiled Core Method hook | focused Formation Skill | Native Primary |
| Non-Project Work | Global Custom Instructions compilation | compiled Core Method hook | focused Formation Skill | Native Primary |
| Project Chat | generated Project Instructions compilation | same Core Method hook plus project context | focused Formation Skill | Native Primary |
| Project Work | generated Project Instructions compilation | same Core Method hook plus project context | focused Formation Skill | Native Primary |

Project Instructions override Global Custom Instructions within Projects. Therefore, the Project compilation must contain the same Kernel semantics plus project-local context and constraints. The configured Global compilation is not a second effective Kernel on a Project path.

Exactly one Kernel compilation must be effective per path.

## Effective instruction and constraint stack

For each claimed path, map provider/system/runtime, Global, Project, Skill/method, Subagent/task and Tool/connector constraints to one effective owner for each semantic responsibility. Lower layers may specialize but not silently duplicate, weaken, override or acquire another owner's Control or Authority. A material unresolved conflict makes that path `BLOCKED` or `OUT_OF_RUNTIME_CLAIM`. This is compilation assurance, not a runtime precedence engine, full registry or copy-everywhere rule.

## Global Custom Instructions compilation

### Current adapter capacity

The dated evidence used by this candidate supports up to 5,000 characters; it does not rely on a 1,500-character limit. Recheck this provider fact before dependent compilation or installation after a material surface/build change.

Capacity is a carrier property, not an architectural reason to split responsibilities. The compiler should optimize for semantic fidelity and interpretability, not maximum compression or maximum fill.

### Required semantics

The Global compilation must preserve every normative `K-01` through `K-12` invariant and every Kernel prohibition that is relevant to execution. It must also include a concise Core Method hook that preserves:

- the composable Work-Function vocabulary;
- Information/Evidence as cross-cutting rather than a mandatory research stage;
- the Method Discovery eligibility formula;
- Native Primary ownership of actual method/provider composition;
- the prohibition on stage machines and mandatory method pipelines.

The Global compilation must not include:

- the Formation Method;
- an independent Formation trigger;
- project-local context;
- a custom operational plan or orchestration loop;
- mandatory Control Return formatting.

If a faithful compilation cannot fit the then-applicable target carrier, do not truncate or weaken semantics. Mark that adapter compilation `BLOCKED` pending a revised compilation or carrier decision. This affects that adapter claim, not Route-B architecture.

## Project Instructions compilation

### Composition

Generate each Project payload from:

```text
CANONICAL_KERNEL_SOURCE
+ PROJECT_LOCAL_OVERLAY
→ PROJECT_INSTRUCTIONS_COMPILATION
```

The Project compilation must preserve the same Kernel semantics and Core Method hook as the Global compilation. Text may differ when needed for the carrier, but semantic responsibility may not differ.

### Project-local overlay

An overlay may add only stable project-local information:

- Project Parent and intended Outcome;
- relevant system boundary;
- local authoritative-source pointers;
- stable constraints and allowed operations;
- local authority, effect or transition boundaries;
- state-carrier pointers and recovery rules when needed.

An overlay must not:

- redefine or weaken a Kernel invariant;
- add a second Formation Activation Owner;
- redefine the Core Work Functions or Method Discovery Contract;
- add a universal stage machine or controller;
- turn volatile Working State into permanent instructions by default;
- claim repository, Project or artifact authority merely from location.

Conflicts between the overlay and Kernel cause compilation failure for that Project. They do not authorize an architecture change.

## Formation Skill compilation

Compile `03-FORMATION-METHOD.md` into one focused supported Skill carrier per target surface. Make `07-CORE-WORK-FUNCTIONS-AND-METHOD-CONTRACT.md` available to that carrier as the canonical method-discovery reference rather than duplicating or independently editing its semantics.

The Skill metadata makes the Formation Method available and relevant. Inside that same carrier, the method performs the claim-relative sufficiency decision. This remains one Formation Activation Owner.

The Skill must not embed an independent copy of the full Kernel, operate as an episode controller, prescribe Primary self-execution, require native Subagents universally, execute the Professional Method, or convert the Work Functions into stages.

## Core Method Layer compilation

The Core Method Layer is neither a second Kernel nor a second controller.

For direct Non-Project paths, compile its minimum operational hook into Global Custom Instructions alongside the Kernel compilation. For Project paths, compile the same hook into Project Instructions alongside the same Kernel semantics and the project-local overlay.

Load only the Core/Domain Method or reference slice needed for the bounded claim, just in time when the basis is inadequate. It remains non-Control, non-Authority and no registry gateway; compiled views retain `07-CORE-WORK-FUNCTIONS-AND-METHOD-CONTRACT.md` as source identity.

The hook must enable the Native Primary to distinguish Work Function, method, provider and surface and to choose eligible Professional Methods without creating a mandatory method-selection ceremony for straightforward work.

If the Skill is absent or its exact identity is not read back on a target surface, that surface has no complete Route-B Runtime claim. There is no silent Global-CI-only fallback for materially underformed work.

## Native runtime responsibilities

Do not replace native planning/replanning, Tool routing, direct execution, Subagent delegation, waiting, synthesis/integration, permission enforcement, sandboxing or Tool availability.

The Native Primary remains sole episode, composition, integration and final-answer owner. Apply Candidate Contract eligibility, dispatch binding, least-privilege fallback, semantic stale-return reconciliation and assurance-diversity semantics without reproducing native orchestration. Compile no mandatory Spawn/Wait, Return/Rebind, Reviewer, permission emulator or episode controller.

## Source-to-output identity

Each generated payload must record outside the effective instruction text where necessary:

- canonical source ID, version and hash;
- Core Method source ID, version and hash;
- compiler profile and version;
- output hash;
- target carrier;
- for Projects, overlay ID, version and hash;
- generation timestamp;
- dated provider/surface compatibility evidence, evidence owner, freshness/recheck trigger and retirement condition for superseded assumptions;
- installation/readback status.

Do not patch generated outputs directly. Change the source or overlay, regenerate, install under separate authority, read back and reconcile.

## Surface-specific Skill identity

Personal Skill installation and identity must be established separately for desktop and web/mobile surfaces. Do not infer synchronization.

The manifest must key claims by the exact combination of:

- account/workspace;
- app surface and build where available;
- Chat or Work;
- Project or Non-Project;
- Project identity where applicable;
- effective Kernel payload identity;
- Formation Skill ID/version/hash;
- readback evidence and timestamp.

Missing or mismatched identity yields `OUT_OF_RUNTIME_CLAIM` for that exact path.

## Platform compatibility lifecycle

Execution establishes current provider/surface facts; Operating owns their compatibility lifecycle. Recheck before dependent compile/install/readback or after a named invalidating delta, retire superseded assumptions, and require no continuous polling or episode-wide compatibility context.

## Compilation acceptance conditions

A ChatGPT adapter source compilation is `INSTALLATION-DECISION READY` only when:

1. generated Global and relevant Project payloads preserve the canonical Kernel;
2. each path has one effective Kernel compilation;
3. the Formation Skill is the sole Formation Activation Owner;
4. the Skill does not duplicate native operational ownership;
5. the Core Method hook preserves composable functions, evidence semantics and method eligibility without a stage machine;
6. target surfaces and Projects are explicitly bounded;
7. exact payload and Skill identities can be installed and read back separately;
8. v0.8 preservation and rollback remain feasible;
9. conditional stale-return reconciliation is preserved without a universal Return/Rebind flow;
10. mixed-runtime execution can be prevented during cutover;
11. the effective instruction/constraint stack has one semantic owner per responsibility and no unresolved material conflict;
12. Method and reference loading is JIT and scoped, without a Control/Authority owner or mandatory registry gateway;
13. Subagent context, actual permission mode, permitted Tools/operations and action authority can be bound before material dispatch;
14. stale-world reconciliation preserves evidence, assumptions, caveats and dependencies, not only identity labels;
15. dated platform assumptions have an owner, recheck trigger and retirement condition.

These conditions govern a later installation decision. This source package does not establish them.

## Non-goals

This adapter does not provide:

- installation scripts;
- Runtime code or API orchestration;
- Project cleanup or migration;
- v0.8 disablement;
- runtime testing;
- promotion evidence;
- a Codex adapter.
