# E2E Runtime Compiled Semantic Trace v0.2

**Status:** COMPLETE TRACE FOR CONTROL-RETURN RECOMPILE — carrier/readback facts remain separate.  
**Date:** 2026-08-20  
**Canonical source:** `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md`  
**Global view:** `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`  
**Project view:** `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`

Statuses:

```text
EMBEDDED
DELEGATED + BOUND
EXTERNAL MECHANISM + VERIFIED
UNVERIFIED
NOT APPLICABLE
```

## 1. Global v0.5 trace

| Canonical IDs | Global location / mechanism | Status |
|---|---|---|
| INV-01–14 | opening invariants + `1–6` typed state/claim/Human rules | EMBEDDED |
| CTL-01–11 | `1 CONTROL`, method/provider selection, operators, handoff/return, closure | EMBEDDED |
| **CTL-12** | `5 HANDOFF/RETURN`: material interaction boundary → Control Return | **EMBEDDED** |
| **CTL-13** | `1 CONTROL`: explicit `Next` semantics + material-boundary integration/qualification | **EMBEDDED** |
| WF-01–11 | function selector + `2`, `3`, `6` | EMBEDDED |
| FORM-01–06 | `2 FORM+DECIDE` | EMBEDDED |
| REAL-01–05 | `3` + `6` | EMBEDDED |
| MET-01–07 | `3 METHOD→PROVIDER→SURFACE`; missing method lowers readiness | EMBEDDED / runtime-selected source |
| CAP-01–05 | `3`; authority reinforced in `4` | EMBEDDED |
| CO-01–03 | `4 OPERATORS` | EMBEDDED |
| CO-04–05 | `5 HANDOFF/RETURN` | EMBEDDED |
| CO-06–07 | `4` Promotion + `6` change/closure | EMBEDDED |
| BC-01 | Work Basis semantics in `4/5` | EMBEDDED, compressed |
| BC-02 | minimum Handoff fields in `5` | EMBEDDED |
| BC-03 | Provider Return fields in `5` | EMBEDDED |
| BC-04 | Promotion fields/write/readback in `4` | EMBEDDED |
| BC-05 | Human Gate object in `4` | EMBEDDED |
| **BC-06** | achieved state + persistence/promotion + next frontier/actor + Human action + disposition in `5` | **EMBEDDED** |
| QA-01–05 | `6 REALIZE+ASSURE...` | EMBEDDED |
| OUT-01 | `6` realization chain | EMBEDDED |
| STATE-01–03 | opening state semantics + `4/5`; Persistence≠Promotion protected by typed operators/Control Return | EMBEDDED + runtime-selected source |
| STATE-04–05 | reusable knowledge / evidence persistence selected by Controller/domain owner | DELEGATED TO DOMAIN OWNER |
| PROD-01 | this Global compiled view | EMBEDDED |
| PROD-02 | Project precedence is external product/carrier fact | EXTERNAL PRODUCT FACT |
| PROD-03–06 | `3/5`, including Chat Control Return role | EMBEDDED |
| PROD-07 | no Personal Skills dependency | EMBEDDED BY METHOD RULE |

**Global result:** no new Control-Return/continuation semantic is omitted. Global v0.5 carries the minimum behavior directly because repository access cannot be assumed cross-context.

## 2. System Weiterentwicklung Project v0.4 trace

| Canonical IDs | Project location / mechanism | Status |
|---|---|---|
| INV-01–14 | `CONTROL`, `RUNTIME TYPES`, Controller/Quality/Operators | EMBEDDED / canonical-equivalent |
| CTL-01–11 | `1 CONTROLLER` + `2–6` | EMBEDDED |
| **CTL-12** | `5 CONTROL RETURN` | **EMBEDDED** |
| **CTL-13** | `1 CONTROLLER` explicit `Next` semantics | **EMBEDDED** |
| WF-01–11 | `1` selector + `6 QUALITY/REALIZATION` | EMBEDDED / activated by Controller |
| FORM-01–06 | `6` + Controller/Method rules | EMBEDDED + canonical binding |
| REAL-01–05 | `6 QUALITY/REALIZATION` | EMBEDDED |
| MET-01–07 | `2 METHOD/PROVIDER` → `methods/METHOD-REGISTRY-v0.1.md` | DELEGATED + BOUND |
| CAP-01–05 | `2` + `3` | EMBEDDED |
| CO-01–03 | `3 OPERATORS` | EMBEDDED |
| CO-04–05 | `4 HANDOFF/RETURN` + detailed boundary contract path | DELEGATED + BOUND + minimum embedded |
| CO-06–07 | `3` Promotion + `PERSIST` | EMBEDDED |
| BC-01–05 | `3/4` + `realization/E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md` | DELEGATED + BOUND |
| **BC-06** | `5 CONTROL RETURN` + detailed boundary/interaction contracts | **EMBEDDED + BOUND** |
| QA-01–05 | `6 QUALITY/REALIZATION` | EMBEDDED + METHOD BINDING |
| OUT-01 | `6` delivery/use/outcome distinction | EMBEDDED |
| STATE-01–05 | `CONTROL`, `PERSIST`, `main/CURRENT.md`, evaluation path | EMBEDDED + BOUND |
| PROD-01 | Global does not apply inside Project due precedence | NOT APPLICABLE INSIDE PROJECT |
| PROD-02 | this Project view | EMBEDDED |
| PROD-03–06 | `2/4/5`, including Chat Control Return | EMBEDDED |
| PROD-07 | repository Method Registry; no Personal Skills dependency | EMBEDDED + BOUND |
| SD-01–07 | opening `CONTROL`, `1–6`, `PERSIST` | EMBEDDED + BOUND |

## 3. Boundary mechanism readback

Detailed controls remain bound at:

- `realization/E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md`;
- `realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md`.

The updated interaction chain is:

```text
Human trigger
→ Controller
→ bounded Handoff when required
→ provider execution
→ Provider Return
→ parent readback/rebind/integration/qualification
→ Human-facing Control Return
→ exact Human Gate / Promotion Gate / continuation / closure
```

`Provider Return ≠ Human-facing Control Return` and `Persistence ≠ Promotion` are explicit.

## 4. Carrier facts

```text
Global Pro character envelope       VERIFIED: <= 5,000
Global v0.5                         4,997 CRLF — PASS
Project Instructions precedence     VERIFIED: overrides Global CI
Project observed capacity            8,000
Project v0.4                         5,181 CRLF — PASS
External Global installation        NOT PERFORMED
External Project installation       NOT PERFORMED
Behavioral Control Return            NOT ESTABLISHED until preflight/real use
```

## 5. Verdict

```text
canonical new semantics CTL-12/CTL-13/BC-06       TRACED
Global compilation                                 PASS static
Project compilation                                PASS static
carrier-size fit                                   PASS
provider-return / control-return distinction       PASS static
Next non-promotion semantics                       PASS static
Persistence≠Promotion                              PASS static
behavioral enforcement                             UNVERIFIED / downstream
```
