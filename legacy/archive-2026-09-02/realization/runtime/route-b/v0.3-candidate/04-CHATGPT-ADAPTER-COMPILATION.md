# Route B ChatGPT Adapter Compilation Definition v0.3

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

## Global Custom Instructions compilation

### Current adapter capacity

For the current implementation context, the applicable carrier capacity is up to 5,000 characters. No 1,500-character constraint exists in this candidate.

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

The complete canonical Core Method source may be bundled as a reference with the Formation carrier or other supported source package, but all compiled views must retain `07-CORE-WORK-FUNCTIONS-AND-METHOD-CONTRACT.md` as their source identity.

The hook must enable the Native Primary to distinguish Work Function, method, provider and surface and to choose eligible Professional Methods without creating a mandatory method-selection ceremony for straightforward work.

If the Skill is absent or its exact identity is not read back on a target surface, that surface has no complete Route-B Runtime claim. There is no silent Global-CI-only fallback for materially underformed work.

## Native runtime responsibilities

Do not compile custom replacements for native:

- planning and replanning;
- Tool routing;
- direct execution;
- delegation to one or multiple native Subagents;
- waiting for native returns;
- synthesis and integration.

The Native Primary remains the single operational owner and selects composition by comparative work value. Native Subagents remain first-class for specialization, parallelism, context isolation and independent challenge.

Preserve native return handling. Add only this conditional integration guard: before a delayed, parallel or potentially stale return updates the Parent or wider state, the Primary compares it with current Parent identity, relevant version/state, Claim/gate/frontier and Authority/effect boundary when concurrent or divergent state could make it stale or mis-scoped.

Do not compile a mandatory Return package, universal Rebind, mandatory Reviewer or episode-wide return controller. Ordinary current, bounded returns remain native integrations without formal ceremony.

## Source-to-output identity

Each generated payload must record outside the effective instruction text where necessary:

- canonical source ID, version and hash;
- Core Method source ID, version and hash;
- compiler profile and version;
- output hash;
- target carrier;
- for Projects, overlay ID, version and hash;
- generation timestamp;
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
10. mixed-runtime execution can be prevented during cutover.

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
