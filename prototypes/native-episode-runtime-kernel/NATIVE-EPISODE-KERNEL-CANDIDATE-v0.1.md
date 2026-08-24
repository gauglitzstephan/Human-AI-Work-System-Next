# Native Episode Runtime Kernel Candidate v0.1

**Status:** CANDIDATE SOURCE — effect-disabled; no installation or Promotion.  
**Parent:** HAWS Operating/Runtime Realization reopen; static architecture remains closed.  
**Canonical basis:** `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`, `realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md`, and `realization/E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md`.

## 1. Native carrier binding

```text
Project / controlling source = initiative context and authoritative pointers
Chat                         = controller, interaction, rebind, control return
Work                         = substantial bounded frontier provider
Codex                        = repository/software frontier provider
native subagent thread       = bounded execution or assurance provider
Skill                        = focused reusable workflow, when installed and matched
files/connectors/tools       = bounded evidence or action providers
validator script             = deterministic packet check, not workflow authority
```

No fixed Chat → Work → Codex pipeline exists. Select the smallest adequate native provider after Work Function and Method are bound. A native subagent is a provider mechanism, not a new architecture stage.

## 2. Activation boundary

Use this kernel only after `material-work-entry` or equivalent control has produced a ready, authorized material frontier whose responsibility or environment will change, or whose return/rebind must be preserved.

Do not activate it for an obvious bounded answer or trivial internal tool call.

The current prototype admits only `PILOT_TEST` episodes with:

- `effects.mode = DISABLED`;
- no write path;
- no persistent write, external action, submission, release, merge, or Promotion;
- an accessible Method admitted for the pilot;
- an identified execution provider and distinct assurance provider;
- a claim narrow enough for the configured assurance.

Missing or unverified Method, Provider, state, authority, or assurance produces `STOP` or `WAIT`, never improvised execution.

## 3. Episode compilation

Compile `episode.schema.json` from authoritative parent state. The packet is derived working runtime state; it does not replace its parent source.

Bind:

```text
Parent Work Object / outcome / controlling source / version / gate / frontier
Trigger relation
Exact Work Unit and child→parent contribution
Work Basis
Method source, status, and pilot fit
Provider / surface / capability status
Assurance provider, mode, and claim
Action-specific authorization basis
Inputs / requirements / output / return condition
Allowed return claims
Blocked effects and transitions
```

`CONTINUE`, `NEXT`, or equivalent continuation may retain a previously admitted frontier. It never becomes the source of new authorization, scope, persistence, acceptance, or Promotion.

Run the deterministic validator where a native file/shell provider is available. A missing validator run leaves packet integrity `UNVERIFIED`; it does not silently pass.

## 4. Admission

Admit only when all non-compensatory checks pass:

1. parent identifier, version, gate, and active frontier are present;
2. continuation remains inside the active frontier and relies on an existing Work Basis or explicit authorization;
3. Method status is `QUALIFIED`, or `CANDIDATE`/`PILOT_ONLY` specifically admitted for `PILOT_TEST`;
4. execution and assurance providers are accessible for the episode and not the same responsibility;
5. authorization covers only the stated non-effectful operations;
6. write path is null and every material effect remains blocked;
7. intended claim and return claims are explicit and assurance-compatible.

If the application/career Method remains unavailable, an application-production episode is not admissible.

## 5. Native handoff and execution

When an adequate native subagent is available and responsibility can return inside the current loop, the controller must actually spawn it with only the validated Episode packet and authoritative inputs it references. A displayed handoff packet is not execution. Use one execution subagent by default; parallelize only independent read-heavy frontiers and avoid parallel writes.

When dispatching to Work, Codex, or another external provider, apply the same bounded contract. The provider owns the bounded transformation, not the parent outcome or its status. If no provider can run now, return an external `HANDOFF` with the actor and re-entry condition instead of simulating a completed dispatch.

The provider must not:

- broaden the Work Unit;
- treat technical capability as authorization;
- use persistent-write or external-action tools;
- claim parent completion or readiness;
- turn local checks into professional or intended-use qualification;
- continue into a new Work Unit, Gate, or surface without returning control.

Native permission/sandbox settings remain an independent deployment control. This Candidate does not claim that instructions or the validator can mechanically remove a connector or tool from the model's environment.

## 6. Provider Return

The provider returns `provider_return.schema.json` before any next frontier. The return records actual work, evidence, Method, assumptions, blockers, checks, operations, exact supported claim, authority need, and recommended next frontier.

Reject the return if it contains any write/external action, parent-status claim, Promotion claim, stale parent version, unbound Method, unexposed operation, or out-of-scope claim.

Provider Return is not Qualification.

## 7. Parent rebind and qualification

The Chat/controller reads material effects and the controlling parent again after return. If version, gate, frontier, or authority changed, stop and reconcile before integration.

When a material claim is vulnerable to correlated producer self-review, the controller then spawns a different assurance subagent with the rebound parent version, exact claim, actual output, requirements, authoritative sources, and failure-detecting Method. Do not give the reviewer the desired verdict or intended repair. The reviewer may qualify but must not repair the object, set parent status, or issue Promotion.

Qualification uses `qualification.schema.json` and must:

- evaluate the Episode's exact intended claim;
- use the bound assurance provider and declared assurance mode;
- identify actual checks and failure evidence;
- distinguish deterministic validation, separate-context review, independent challenge, and recipient/intended-use validation;
- return `UNVERIFIED` when the method cannot detect the relevant failure;
- make no parent-status or Promotion claim.

The execution provider cannot self-issue a qualification `PASS`. Reviewer `FAIL` or `UNVERIFIED` demotes the claim and blocks dependent transitions; the controller must not average executor and reviewer outputs into `PASS` or permit a silent producer repair/self-pass loop.

## 8. Control return

After valid return, rebind, integration, and qualification, expose:

```text
achieved child result and exact qualified claim
parent state delta, if any
persistence and Promotion state
next legitimate frontier and actor
exact Human contribution or authority required, if any
disposition
```

For this prototype:

```text
effect status       BLOCKED BY DESIGN
Promotion status    BLOCKED BY DESIGN
production status   NOT OPERATIONAL
```

## 9. Required native qualification

Static fixture PASS is necessary but insufficient. Before any broader runtime claim, a real ChatGPT-native, effect-disabled pilot must demonstrate:

1. the kernel activates on a material boundary;
2. `CONTINUE` does not create authority;
3. missing Application Method stops production;
4. an actual Work/Codex/native-subagent provider receives a bounded packet rather than a narrated handoff;
5. Provider Return occurs before further work;
6. Chat rebinds the actual parent;
7. Qualification remains claim-scoped and separate;
8. no effect, write, application artifact, or Promotion occurs.

The first real native subagent pilot on 2026-08-24 demonstrated bounded executor dispatch, Provider Return, Parent rebind, and a different reviewer thread. The control path worked; the reviewer correctly rejected the executor's overbroad/incomplete child claim. This is one effect-disabled behavioral trace, not automatic-activation or production evidence.
