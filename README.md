# Human–AI Work System Next

> Build a Human–AI Work System that turns real needs into intended-use-sufficient working solutions with strong reality, state, authority, quality and Human-agency control — without unnecessary meta-work.

## Start here

**[`CURRENT.md`](CURRENT.md) is the controlling repository state and operating entry point for the tree in which it is read.**

Do not infer the current program from historical `Next` sections, newest-looking files, old installation bundles, or closed/unmerged branches.

Promotion-state rule:

```text
if read on unmerged PR #14 / repair/post-pr13-repo-hygiene-v0.1
→ main/CURRENT.md remains repository authority
→ hygiene package remains Candidate at Human Promotion Gate

if this exact state is read on main after PR #14 merge
→ bounded hygiene Promotion is COMPLETE
→ CURRENT.md in this tree is controlling
→ next parent frontier is external-settings readback reconciliation / Runtime conformance preflight
```

## Current status

```text
Target Architecture v0.2                         ACCEPTED
Static E2E Work Architecture                     REPOSITORY-PROMOTED / CLOSED BY DEFAULT
Runtime deployment + interaction-control repair  REPOSITORY-PROMOTED via PR #13
Current Global compiled view                     v0.5
Current System Development Project view          v0.4
Current Installation Bundle                      v0.4
Current-session effective v0.5/v0.4 load         OBSERVED BY CONTENT
Persistent UI save/readback evidence              NOT SEPARATELY RECORDED
Runtime behavioral conformance                    NOT ESTABLISHED
```

PR #14 changes only repository hygiene/state coherence. Before merge it is a reviewed Candidate whose final Promotion readiness is determined by the latest PR-level review of the current head; if this exact state is read on `main` after an authorized PR #14 merge, that bounded hygiene package is repository-promoted. Neither state changes the Runtime semantic payloads or the external-settings claim boundary.

## Accepted conceptual baseline

[`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md) retains three structural commitments:

```text
DISTINCT RESPONSIBILITIES
DISTRIBUTED TYPED STATE
ADAPTIVE WORK SELECTION
```

These are responsibilities/contracts, not mandatory runtime layers, agents, stores, ontologies or stage machines.

Static architecture stays closed unless a named Runtime/real-use trigger or legitimate requirement/scope change establishes a reason to reopen it.

## Current Runtime realization

Canonical semantic source:

- [`realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`](realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md)

Current compiled views:

- [`realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`](realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md) — Global Custom Instructions view
- [`realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`](realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md) — System Development Project view
- [`realization/E2E-INSTALLATION-BUNDLE-v0.4.md`](realization/E2E-INSTALLATION-BUNDLE-v0.4.md) — current external-transition bundle
- [`realization/README.md`](realization/README.md) — current-vs-history realization navigation

Global v0.5:

```text
LF:       4,991
CRLF:     4,997
SHA-256:  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
```

System Development Project v0.4:

```text
LF:       5,172
CRLF:     5,181
SHA-256:  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Do **not** select earlier Global, Project or Installation-Bundle versions for installation. They are lineage/history unless `CURRENT.md` explicitly re-promotes them.

## Runtime control model

Keep distinct:

```text
Work Function
≠ Control Operator
≠ Method
≠ Provider
≠ Surface / Environment
≠ State / Knowledge Carrier
≠ Boundary Contract
```

and:

```text
Decision
≠ Commitment
≠ Authorization
≠ Handoff
≠ Execution
≠ Provider Return
≠ Human-facing Control Return
≠ Promotion / State Transition
```

`Persistence ≠ Promotion`.

`Next` continues only the currently bound legitimate frontier. It does not by itself accept, promote, authorize, persist, change scope or create a new commitment.

## Interaction chain

```text
Human trigger
→ Controller / bound parent + frontier
→ Handoff if responsibility/environment changes
→ provider execution
→ Provider Return
→ readback / rebind / integrate / qualify parent
→ Human-facing Control Return
→ CLOSE / CONTINUE / HUMAN GATE / PROMOTION GATE /
   HANDOFF / WAIT / MONITOR
```

A material result must leave the Human able to tell what is established, what remains unverified, whether persistence/Promotion is intended, who acts next and what exact Human contribution is required if any.

## Method carrier

Repository-backed method registry:

- [`methods/METHOD-REGISTRY-v0.1.md`](methods/METHOD-REGISTRY-v0.1.md)

System Development Method Packs are under `methods/system-development/`.

A registry entry is not automatically applicable; provenance, fit and claim-specific assurance still matter.

## Current external-transition state

PR #13 was repository Promotion only. It did not itself establish ChatGPT UI installation or behavioral acceptance.

The current System Development session exposes Global and Project instruction content matching the promoted v0.5 / v0.4 payloads. This establishes **current-session effective load by content observation**. It does not independently establish persistent UI save/readback, future-session persistence or behavioral conformance.

Evidence record:

- [`evaluation/e2e-real-use/E2E-04-2026-08-20-POST-PR13-RUNTIME-LOAD-AND-HYGIENE.md`](evaluation/e2e-real-use/E2E-04-2026-08-20-POST-PR13-RUNTIME-LOAD-AND-HYGIENE.md)

## Key current documents

- [`CURRENT.md`](CURRENT.md) — controlling program state for the current tree
- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md) — accepted concern/requirements basis
- [`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md) — accepted conceptual baseline
- [`architecture/E2E-WORK-ARCHITECTURE-CANDIDATE-v0.1.md`](architecture/E2E-WORK-ARCHITECTURE-CANDIDATE-v0.1.md) — repository-promoted static E2E architecture package
- [`architecture/ARCHITECTURE-METHOD.md`](architecture/ARCHITECTURE-METHOD.md) — lineage/reopen/failure-localization discipline
- [`methods/METHOD-REGISTRY-v0.1.md`](methods/METHOD-REGISTRY-v0.1.md) — method carrier
- [`evaluation/E2E-REAL-USE-VALIDATION-PROTOCOL-v0.1.md`](evaluation/E2E-REAL-USE-VALIDATION-PROTOCOL-v0.1.md) — real-use validation protocol
- [`realization/README.md`](realization/README.md) — realization navigation and supersession map

## Promotion-state handoff / current gate

The Promotion-State-Handoff rewrite is persisted and read back across `CURRENT.md`, this root README, `realization/README.md` and the E2E-04 record. The transient PR-level verdict is intentionally not hard-coded here; the latest review of the current PR head controls Promotion readiness.

```text
IF read on unmerged PR #14 / its head branch:
  bounded hygiene implementation/readback       COMPLETE / PASS
  promotion-state handoff repair                 IMPLEMENTED / READBACK PASS
  PR #14 Promotion verdict                       CHECK LATEST REVIEW OF CURRENT PR HEAD
  PR #14 repository Promotion                    HUMAN MERGE GATE — only after PASS

IF this exact state is read on main after PR #14 merge:
  bounded hygiene Promotion                      COMPLETE
  persistent external-settings readback          NEXT TRANSITION / NOT YET ESTABLISHED
  Runtime conformance preflight                  PENDING readback reconciliation as required
  first genuine System Development real-work     BLOCKED until preflight
```

A PR #14 merge would not authorize external ChatGPT settings mutation and would not establish persistent settings readback, Runtime behavioral conformance or outcome effectiveness.