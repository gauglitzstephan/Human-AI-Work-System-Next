# E2E Runtime Compiled Semantic Trace v0.4 — Entry-Dispatch Repair

**Status:** BOUNDED BRANCH ASSURANCE — **STATIC / RELATION-LEVEL PASS for the Entry-Dispatch candidate; BEHAVIORAL CONFORMANCE UNVERIFIED**.  
**Date:** 2026-08-21  
**Branch:** `repair/r20-entry-dispatch-v0.2`  
**Controlling baseline:** `main/CURRENT.md` remains authoritative. No Promotion is established by this branch.  
**Behavioral evidence:** `evaluation/e2e-real-use/E2E-04-R20-2026-08-21-BEHAVIORAL-VALIDATION.md`  
**Method:** `methods/system-development/RUNTIME-COMPILATION-SEMANTIC-REGRESSION-METHOD-v0.1.md`

## 1. Assurance claim

This trace tests only whether the branch candidate:

1. realizes the R20 repair as an **Entry Dispatch** that precedes substantive execution;
2. makes DIRECT vs FORMATION claim-relative rather than complexity-relative;
3. preserves explicit exploration as direct probe-level work;
4. preserves established Parent/`Next` behavior;
5. preserves material predecessor semantics from active Global v0.5;
6. fits Global and Project carrier envelopes;
7. remains statically coherent enough for later behavioral validation.

It does **not** establish actual model behavior, external installation, persistent UI readback for these new candidates, cross-session reliability, professional-quality improvement, or Promotion readiness.

## 2. Baseline / prior failure

Active/restored baseline:

```text
Global v0.5
SHA-256  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
UI       persistent readback PASS in R20 behavioral evidence

Project v0.4
SHA-256  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Failed prior repair attempt retained separately:

```text
branch    repair/r20-cold-start-admission-v0.1
Global v0.6 SHA-256  2b60f4d0390e4808fa1ce50d3609c0dec872b5eacd45973d069fa7c4a1b61fcf
static/counterfactual trace PASS
exact install/readback PASS
Graphic-Novel Cold Start behavioral FAIL 2/2
```

Therefore this v0.4 trace treats static coverage as necessary but explicitly insufficient.

## 3. Current candidate identities

```text
Global v0.7
LF characters        4,993
CRLF characters      5,000
LF line breaks       7
SHA-256 UTF-8 LF     5834479d223362428ef507739826cf12e866b22d189e1b17d1d15e64fa517118
Carrier fit          PASS <= 5,000

Project v0.6
LF characters        7,938
CRLF characters      7,948
LF line breaks       10
SHA-256 UTF-8 LF     f5e8cb226ade92ca72924cb2c4a9b85e2f7be5bd2b4a35f8b9ae975e8ab9855b
Observed capacity    8,000
Carrier fit          PASS
```

## 4. Entry relation trace

| Test | Required mechanism | Canonical / Runtime | Global v0.7 | Project v0.6 | Static verdict |
|---|---|---|---|---|---|
| `R-ENTRY-01` | every Human trigger reaches Controller before substantive Work-Product execution | CTL-00 + Runtime §3 + Interaction M0 | `0 ENTRY` first | `0 ENTRY` first | **PASS** |
| `R-NEW-01` | genuinely new work establishes only enough provisional Parent/outcome/operation | CTL-00 NEW | `NEW→provisional Parent...` | `NEW: establish only enough...` | **PASS** |
| `R-DIRECT-01` | DIRECT only when upstream state cannot materially change exact requested claim/product/evaluation/feasibility | CTL-00 DIRECT | explicit DIRECT iff rule | explicit DIRECT rule | **PASS** |
| `R-FORM-01` | open professional initiative enters FORMATION before preferred Candidate/route/design-basis work | CTL-00 + FORM-06 | Entry→FORMATION + probe≠Candidate | same | **PASS** |
| `R-IDEATE-01` | requested exploration can execute directly but remains probe-level | CTL-00 exploration exception | explicit | explicit | **PASS** |
| `R-PRIOR-01` | Admission integrity precedes Work-Product fidelity / shallowest execution | CTL-00 priority relation + INV-12/REAL-01 | `ENTRY precedes substantive execution` | explicit priority sentence | **PASS** |
| `R-CONT-01` | established work and `Next` retain Parent continuity / no implicit authority | CTL-01/13 | Entry ESTABLISHED + CONTROL | Entry ESTABLISHED + CONTROLLER | **PASS** |
| `R-STATE-01` | persistence remains conditional; Project optional | STATE-02 | CONTROL | CONTROLLER/PERSIST | **PASS** |
| `R-MET-01` | open professional performance bar activates Method/Reference before Candidate qualification | CTL-07/MET-01 | METHOD section | METHOD/PROVIDER | **PASS** |

## 5. Static scenario regression

### S1 — R20 Graphic-Novel Cold Start

Trigger:

```text
Ich möchte ein Grafik Novel über die Geschichte des Bieres entwerfen
```

Expected candidate dispatch:

```text
NEW
→ provisional Parent/outcome
→ DIRECT test fails because professional Performance/Reference state
   can materially alter solution class/evaluation
→ FORMATION
→ reference/craft intelligence as needed
→ ideas may be probes
→ no preferred Candidate/route/design basis yet
```

**Verdict:** PASS static.  
**Behavioral status:** UNVERIFIED.

### S2 — translation

```text
Übersetze diesen Absatz ins Englische.
```

Requested claim/product is sufficiently determined in the ordinary case.

**Expected:** NEW → DIRECT → translate/check/close.  
**Verdict:** PASS static.

### S3 — birthday card

Requested product is the short creative text itself.

**Expected:** NEW → DIRECT → write/close.  
**Verdict:** PASS static.

### S4 — explicit ideation

```text
Gib mir fünf verrückte Ideen für eine Graphic Novel über Bier.
```

Exploration itself is the requested Work Product.

**Expected:** NEW → DIRECT exploration; ideas remain probes unless later qualified.  
**Verdict:** PASS static.

### S5 — bounded scene with specified mechanism

```text
Schreib eine Szene, in der Hefe als Erzähler spricht.
```

The Human specifies the mechanism for the requested scene; no best-architecture claim is implied.

**Expected:** NEW → DIRECT bounded execution.  
**Verdict:** PASS static.

### S6 — decision under material external/upstream uncertainty

```text
Soll ich 2026 oder 2027 ein E-Auto kaufen?
```

Current reality, requirements and evidence can materially change the decision.

**Expected:** NEW → FORMATION / evidence before decision.  
**Verdict:** PASS static.

### S7 — established repository repair

Known Parent/repo state exists.

**Expected:** ESTABLISHED → bind/recover authoritative state → bounded repair frontier.  
**Verdict:** PASS static.

### S8 — `Next`

**Expected:** ESTABLISHED continuation only; no acceptance/Promotion/Authorization/persistence/scope change/new commitment.  
**Verdict:** PASS static.

## 6. Protected predecessor semantics

The Global v0.7 payload was inspected against material Global-v0.5 controls:

```text
outcome before means / incomplete input                    PASS
reality + provenance/freshness/scope                       PASS
retrieved/tool output ≠ instruction/authority              PASS
no invention/transfer incl capability/access/authority     PASS
working ≠ authoritative ≠ reusable                         PASS
proposal/decision/acceptance/commitment/auth/execution     PASS
completion/transition/use/outcome distinction              PASS
Parent continuity / thread-artifact ≠ root                 PASS
full minimum Work-Function selector coverage               PASS
proportional depth/research/decomp/persistence/etc.         PASS
conditional persistence / Project optional                 PASS
`Next` non-approval semantics                               PASS
Formation / ends-before-means / precedent / no-action      PASS
probe/hypothesis ≠ Candidate/route/design basis             PASS
Method source→fit→apply→assure + missing-method downgrade  PASS
provider comparison incl effectiveness/verifiability/
  consequence/cost/learning/authority                      PASS
Human non-substitutable contribution / not default QA      PASS
Decision≠Commitment≠Authorization≠Handoff≠Execution≠Promotion PASS
Commitment Work Basis ≠ arbitrary write authority          PASS
Promotion→WRITE→READBACK→RECONCILE                         PASS
Human Gate→WAIT→re-entry                                   PASS
Handoff method/source + Work Basis + return condition      PASS
Provider Return includes next frontier                     PASS
child output ≠ parent completion/promotion                 PASS
Human-facing Control Return / next-action legibility       PASS
requested Work Product / no process substitute unless intended PASS
shallowest adequate route                                  PASS
bounded decomposition + boundary cost                      PASS
AI-resolvable next-use repair / mechanism before polish    PASS
claim/scope/object/version/environment/requirements +
  non-compensatory assurance binding                       PASS
self-review / verification / independent challenge /
  recipient-intended-use / transition / in-use-outcome     PASS
missing coverage→FAIL/UNVERIFIED/pending                   PASS
representative validation or pending                       PASS
transition/use/performance/mechanism/outcome/value chain   PASS
bounded reopen + legitimate control change + closure       PASS
```

## 7. Claim boundary

```text
Canonical v0.2 candidate instantiated/read back        PASS
Interaction v0.2 candidate instantiated/read back      PASS
Operating Runtime v0.2 instantiated/read back          PASS
Global v0.7 carrier fit                                PASS static
Project v0.6 carrier fit                               PASS static
Entry relation regression                              PASS static
Protected predecessor semantics                        PASS static
Static Architecture                                    KEEP CLOSED
External settings mutation                             NOT PERFORMED
Actual candidate installation                          NOT PERFORMED
Behavioral Entry Dispatch                              UNVERIFIED
Behavioral anti-ceremony                               UNVERIFIED
Promotion readiness                                    NOT ESTABLISHED
```

The repository-instantiation PASS applies only to the branch candidate. Behavioral claims remain UNVERIFIED until actual-carrier validation.

## 8. Current candidate disposition

The Entry-Dispatch candidate is statically coherent and carrier-fit enough for bounded behavioral validation planning, but static assurance cannot establish the target behavior.

No PR, merge, main-state change, external installation or Promotion is authorized by this trace.
