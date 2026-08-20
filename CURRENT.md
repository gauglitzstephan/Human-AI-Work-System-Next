# CURRENT — Human–AI Work System Next

**Branch-local status:** CANDIDATE POST-PR13 REPOSITORY HYGIENE / STATE RECONCILIATION — AUTHORIZED POINTS 1–6 IMPLEMENTED + READ BACK; FULL HYGIENE PROMOTION **PENDING HYG-05**.  
**Date:** 2026-08-20  
**Controlling main baseline at branch creation:** PR #13 repository Promotion **COMPLETE**.  
**Static E2E package:** promoted via PR #11 — **KEEP CLOSED** absent a named static reopen trigger.  
**Current Runtime repository package:** PR #13 / Global v0.5 + System Development Project v0.4 + Installation Bundle v0.4.  
**Authority boundary:** until this hygiene branch is explicitly promoted, `main/CURRENT.md` remains repository authority. This branch changes repository navigation/supersession/readback hygiene only; it does not change accepted architecture or Runtime semantics.

## 1. Parent program and accepted state

Parent outcome:

> Realize and validate the Human–AI Work System on genuine work without losing state, authority, professional quality, Human agency or proportionality.

Current accepted / promoted state:

```text
Target Architecture v0.2                         ACCEPTED
Static E2E Work Architecture package             REPOSITORY-PROMOTED / CLOSED BY DEFAULT
Runtime deployment + interaction-control repair  REPOSITORY-PROMOTED via PR #13
External Runtime behavioral effectiveness         NOT ESTABLISHED
Real-use quality / outcomes                       NOT ESTABLISHED
```

The named Runtime reopen trigger addressed by PR #13 was:

> **CR-13 Runtime / implementation fidelity failure — Runtime type-system collapse + carrier-binding omission**, including the Human-facing control-return defect observed on 2026-08-20.

Static architecture completeness remains closed.

## 2. Canonical Runtime source and current compiled views

Canonical semantic source:

- `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`

Current compiled installation views:

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`
- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`
- `realization/E2E-INSTALLATION-BUNDLE-v0.4.md`

Global v0.5 identity:

```text
LF:       4,991
CRLF:     4,997
SHA-256:  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
Carrier:  <= 5,000 characters — PASS
```

Project v0.4 identity:

```text
LF:       5,172
CRLF:     5,181
SHA-256:  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
Observed carrier capacity: 8,000 characters — PASS
```

Older compiled views and bundles remain lineage only and must not be selected for installation. `realization/README.md` is the local realization navigation index in this hygiene candidate.

## 3. Runtime type and control boundaries

Preserve:

```text
Work Function
≠ Control Operator
≠ Method
≠ Capability Provider
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

`Next` means continue the currently bound legitimate frontier. It does **not** imply acceptance, Promotion, Authorization, persistence, scope change or a new commitment.

## 4. Current interaction chain

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

At material interaction boundaries the Human must not have to infer disposition, `Next` safety, persistence/Promotion intent or the exact required action.

## 5. Method carrier

Registry:

- `methods/METHOD-REGISTRY-v0.1.md`

System Development packs remain under `methods/system-development/`.

The branch-local `methods/system-development/REPOSITORY-PROMOTION-READBACK-METHOD-v0.1.md` now adds a post-promotion Entry-Point Hygiene Scan. That method change remains Candidate with this branch.

## 6. Repository promotion and external Runtime state

Repository transition:

```text
R17  PR #13 repository Promotion                 COMPLETE
```

External Runtime transition:

```text
R18a current-session effective Global v0.5 load  OBSERVED BY CONTENT
R18a current-session effective Project v0.4 load OBSERVED BY CONTENT
R18b persistent UI save/readback evidence         NOT SEPARATELY RECORDED
R19  runtime conformance preflight                PENDING transition reconciliation
R20  first genuine E2E real-work validation       BLOCKED until R19
```

The current System Development conversation context exposes Global and Project instruction content matching the promoted v0.5 / v0.4 payloads. This is evidence of **effective load in the current session**, not independent evidence of UI save/readback, persistence across future sessions, or behavioral conformance.

Material evidence:

- `evaluation/e2e-real-use/E2E-04-2026-08-20-POST-PR13-RUNTIME-LOAD-AND-HYGIENE.md`

## 7. Authorized post-PR13 hygiene scope — implementation/readback

Human-authorized points 1–6 on `repair/post-pr13-repo-hygiene-v0.1`:

```text
1 CURRENT post-merge normalization                  IMPLEMENTED / READBACK PASS
2 root README synchronization                       IMPLEMENTED / READBACK PASS
3 realization/README current-vs-history navigation  IMPLEMENTED / READBACK PASS
4 Bundle v0.1 + v0.2 tombstones                     IMPLEMENTED / READBACK PASS
5 Promotion/Readback hygiene assurance extension    IMPLEMENTED / READBACK PASS
6 material Runtime/hygiene evidence record          IMPLEMENTED / READBACK PASS
```

No architecture/requirements change, Runtime payload recompile, external settings mutation, branch cleanup, PR creation or merge was performed.

## 8. Assurance finding HYG-05 — outside authorized write scope

The newly added Entry-Point Hygiene Scan identified a remaining contradiction in three **current** package metadata/status surfaces:

- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md` still says `not externally installed`;
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md` still says `external save/readback not performed`;
- `E2E-INSTALLATION-BUNDLE-v0.4.md` still says `repository promotion candidate; external installation not performed`.

Those statements predate the current-session effective-load observation. The supported state is more precise:

> **effective v0.5/v0.4 load observed by content in the current session; independent persistent UI save/readback not separately recorded.**

Repairing these three files was **not** part of the authorized points 1–6, so no write was made to them.

Assurance verdict:

```text
authorized points 1–6                         PASS
written-file readback                         PASS
root navigation / old-bundle safety           PASS within scope
full current-package entry-point coherence     FAIL / PENDING HYG-05
repository hygiene Promotion readiness         NOT YET ESTABLISHED
```

## 9. Current gate

This branch is not yet ready for a merge decision because HYG-05 is a detected, AI-resolvable defect outside the current write authorization.

Minimum next frontier:

```text
metadata-only reconcile current Global v0.5 status
+ metadata-only reconcile current Project v0.4 status
+ metadata/transition reconcile Bundle v0.4
→ readback current package
→ re-run entry-point coherence check
→ only then return to Human repository Promotion gate
```

No compiled payload text needs to change; no Runtime semantic recompile is indicated.

**Current disposition:** HUMAN GATE — WAIT.  
**Exact Human authorization required:** allow metadata-only reconciliation of Global v0.5, Project v0.4 and Installation Bundle v0.4 on this existing hygiene branch, with **no payload recompile, no external settings change, no PR creation and no merge**.
