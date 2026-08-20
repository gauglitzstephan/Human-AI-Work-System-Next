# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED TARGET CONCEPTUAL BASELINE v0.2 + STATIC-COMPLETE E2E WORK ARCHITECTURE CANDIDATE v0.1 + REVIEWED RUNTIME DEPLOYMENT / INTERACTION-CONTROL REPAIR CANDIDATE v0.6  
**Date:** 2026-08-20  
**E2E static package:** promoted via PR #11 — **KEEP CLOSED** absent a named static reopen trigger.  
**Prior Runtime package:** promoted via PR #12 — **REOPENED / DO NOT INSTALL** after deployment-fidelity failure.  
**Repair branch / PR:** `runtime/deployment-mapping-repair-v0.5` / PR #13.  
**Superseded parallel PR:** #10 **CLOSED / NOT MERGED**.  
**Authority boundary:** if this file is read on the unmerged repair branch, `main` remains controlling and PR #13 is still at the Human merge gate. If this exact state is read on `main` after PR #13 merge, repository promotion is **COMPLETE**, this file is the controlling post-promotion repository state, and external ChatGPT installation/readback remains a separate Human transition not established by the merge.

## 1. Named Runtime reopen trigger

> **CR-13 Runtime / implementation fidelity failure — Runtime type-system collapse + carrier-binding omission.**

PR #13 repairs the Runtime realization while preserving:

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

Static architecture completeness remains closed.

## 2. Additional real-use Runtime defect captured inside PR #13

Observed on 2026-08-20 during ordinary professional interaction:

```text
material answer/result exists
BUT Human must infer:
- is this finished / Candidate / qualified?
- is `Next` safe?
- is persistence or Promotion intended?
- is a Human decision/authorization required?
- what exact response/action is needed?
```

Localization:

> **Runtime interaction/control-return defect, not a demonstrated static-architecture ownership gap.**

Repair semantics now include:

- `CTL-12 Human-facing Control Return`;
- `CTL-13 continuation / Next semantics`;
- `BC-06 Human-facing Control Return Contract`;
- `Provider Return ≠ Human-facing Control Return`;
- `Persistence ≠ Promotion`.

## 3. Canonical Runtime source and boundary mechanisms

Canonical source:

- `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`

Core boundary contracts:

- `realization/E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md`;
- `realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md`.

Current interaction chain:

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

`Next` means continue the currently bound legitimate frontier. It does **not** imply acceptance, Promotion, Authorization, persistence, scope change or a new commitment.

## 4. Current Global Pro compiled candidate

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`

```text
LF:       4,991
CRLF:     4,997
SHA-256:  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
```

Verified Pro Global carrier: **<= 5,000 characters**.  
Carrier fit: **PASS**.  
External save/readback: **NOT PERFORMED**.

Global v0.4 is superseded for installation.

## 5. Current System Development Project compiled candidate

- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`

```text
LF:       5,172
CRLF:     5,181
SHA-256:  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Human-observed Project Instructions carrier: **8,000 characters**.  
Carrier-size fit: **PASS**.  
External save/readback: **NOT PERFORMED**.

Project v0.3 is superseded for installation.

## 6. Method carrier

Registry:

- `methods/METHOD-REGISTRY-v0.1.md`

System Development packs remain under `methods/system-development/`.

No Personal Skills dependency is required.

## 7. Current verification package

- `reviews/E2E-RUNTIME-COMPILED-SEMANTIC-TRACE-v0.2.md`;
- `reviews/E2E-RUNTIME-MECHANISM-DEPLOYMENT-REGRESSION-v0.2.md`;
- `reviews/E2E-RUNTIME-REPAIR-PACKAGE-READBACK-v0.2.md`;
- `reviews/E2E-PROMOTION-STATE-HANDOFF-READBACK-v0.1.md`;
- `reviews/E2E-PROJECT-CARRIER-BOUNDARY-RECHECK-v0.1.md`.

Supported verdict:

```text
Runtime type-system repair                    PASS
canonical one-source compilation              PASS
Global v0.5 carrier fit                       PASS
Project v0.4 carrier fit                      PASS
Method carrier binding                       PASS static
Handoff / Provider Return binding             PASS static
Human-facing Control Return binding           PASS static
Next continuation semantics                   PASS static
Persistence≠Promotion                         PASS static
Commitment/Authorization/Promotion binding    PASS static
promotion-state handoff                       PASS for repository transition
repository promotion eligibility              PASS
external installation/readback                NOT PERFORMED
behavioral/cross-surface effectiveness         NOT ESTABLISHED
real-use quality/outcomes                     NOT ESTABLISHED
```

The observed 2026-08-20 interaction failure is evidence against the prior Runtime UX; it is not positive behavioral evidence for the repaired candidate.

## 8. Current installation package

- `realization/E2E-INSTALLATION-BUNDLE-v0.4.md`

This bundle supersedes all earlier installation bundles for future external installation if PR #13 is promoted.

## 9. Dependency / PR state

```text
PR #10        CLOSED / NOT MERGED / superseded by #13
PR #13        active repair line before merge; repository-promoted line after merge
other competing Runtime PR dependency         NONE IDENTIFIED at promotion review
main behind candidate branch                  0 commits at pre-promotion dependency check
```

Mergeability and head identity are point-in-time state and must be revalidated immediately before effect.

## 10. Promotion-state handoff / current gate

The same persisted state is intentionally valid on both sides of the repository transition:

```text
IF this file is on unmerged PR #13 branch:
  R17 PR #13 repository Promotion              HUMAN MERGE GATE — WAIT
  R18 external Global + Project install        BLOCKED until R17

IF this file is on main after PR #13 merge:
  R17 PR #13 repository Promotion              COMPLETE
  R18 external Global + Project installation/readback
                                                NEXT HUMAN TRANSITION — NOT YET PERFORMED
  R19 runtime conformance preflight             BLOCKED until R18
  R20 first genuine E2E real-work validation    BLOCKED until R19
```

A PR merge authorizes and establishes only repository promotion. It does **not** authorize or establish external ChatGPT settings installation.

**Mode before merge:** PROMOTION GATE — PR #13.  
**Mode after merge on `main`:** REPOSITORY PROMOTION COMPLETE → WAIT FOR SEPARATE EXTERNAL INSTALLATION/READBACK AUTHORITY.
