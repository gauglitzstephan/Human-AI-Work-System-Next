# E2E Runtime Compiled Semantic Trace v0.4 — Entry-Dispatch Repair

**Status:** BOUNDED BRANCH ASSURANCE — **STATIC / RELATION-LEVEL PASS for the amended Entry-Dispatch candidate; BEHAVIORAL CONFORMANCE UNVERIFIED**.  
**Date:** 2026-08-21  
**Branch:** `repair/r20-entry-dispatch-v0.2`  
**Controlling baseline:** `main/CURRENT.md` remains authoritative. No Promotion is established by this branch.  
**Behavioral evidence:** `evaluation/e2e-real-use/E2E-04-R20-2026-08-21-BEHAVIORAL-VALIDATION.md`  
**Method:** `methods/system-development/RUNTIME-COMPILATION-SEMANTIC-REGRESSION-METHOD-v0.1.md`

## 1. Assurance claim

This amended trace tests whether the branch candidate:

1. makes every Human trigger enter Entry Dispatch before substantive execution;
2. separates **Parent/context binding** from **Claim Admission**;
3. distinguishes BOUND continuation from NEW/CHANGED CLAIM even under an established Parent;
4. sends NEW/CHANGED claims through claim-relative DIRECT vs FORMATION;
5. preserves explicit exploration as direct probe-level work;
6. preserves established Parent/`Next` semantics without allowing continuation wording to hide material change;
7. preserves material predecessor semantics from active Global v0.5;
8. fits Global and Project carrier envelopes;
9. is statically coherent enough for actual-carrier behavioral validation.

It does **not** establish actual model behavior, external installation, persistent UI readback for these candidates, cross-session reliability, professional-quality improvement or Promotion readiness.

## 2. Why v0.4 was amended before behavioral deployment

The first persisted Entry-Dispatch candidate correctly tested root NEW work but defined DIRECT vs FORMATION only inside the `NEW` branch after `ESTABLISHED vs NEW`.

Validation formation exposed a material gap:

```text
established Parent
+ new or materially changed child claim
≠ already admitted child work
```

Without a second relation step, a valid Parent could become blanket Admission for new child work and reproduce the same self-trigger failure inside persistent projects/programs.

The candidate was therefore amended in-place on the same bounded branch before any external installation. Branch history preserves the earlier intermediate state.

## 3. Baseline / prior behavioral failure

Active/restored baseline:

```text
Global v0.5
SHA-256  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
UI       persistent readback PASS in R20 behavioral evidence

Project v0.4
SHA-256  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Prior failed repair:

```text
Global v0.6 exact install/readback     PASS
Graphic-Novel Cold Start              FAIL 2/2
Local explicit Admission isolation    PASS
```

Therefore static semantic presence cannot establish Entry enforcement.

## 4. Amended candidate identities

```text
Global v0.7
LF characters        4,992
CRLF characters      4,999
LF line breaks       7
SHA-256 UTF-8 LF     02d58d921b369525d5cdfc43f7a7755ef11876ab75bf12871d8dab2dd7c1cea1
Carrier fit          PASS

Project v0.6
LF characters        7,952
CRLF characters      7,962
LF line breaks       10
SHA-256 UTF-8 LF     60d24a69c2d76075adcfaae0acc9493ad6aa39c46ff8b28b1deb685d2dc2b2a8
Observed capacity    8,000
Carrier fit          PASS
```

Source-side candidate:

- `realization/E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.2.md`
- `realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.2.md`
- `realization/E2E-OPERATING-RUNTIME-CONTRACT-CANDIDATE-v0.2.md`

Derived carriers:

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.7.md`
- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.6.md`

## 5. Corrected relation chain

```text
HUMAN TRIGGER
      ↓
BIND CONTEXT
  existing legitimate Parent/frontier
  OR provisional Parent/outcome/operation
      ↓
RELATE TRIGGER TO BOUND WORK
  BOUND CONTINUATION
  OR NEW/CHANGED CLAIM
      ↓ if NEW/CHANGED
DIRECT vs FORMATION
      ↓
substantive Work Function(s)
```

Key non-equivalence:

```text
Parent continuity
≠ Claim Admission
```

A new child claim or material change to claim/scope/requirements/means/decision object is NEW/CHANGED even when the Parent remains unchanged.

## 6. Relation-level semantic trace

| Test | Required mechanism | Canonical / Runtime | Global v0.7 | Project v0.6 | Verdict |
|---|---|---|---|---|---|
| `R-ENTRY-01` | every Human trigger enters Entry before substantive work | CTL-00 / Runtime §3 | `0 ENTRY` | `0 ENTRY` | **PASS static** |
| `R-CONTEXT-01` | bind existing legitimate Parent or minimal provisional Parent without root drift | CTL-00.1 | `BIND CONTEXT` | `BIND CONTEXT` | **PASS static** |
| `R-BOUND-01` | already-admitted same frontier can continue without re-Formation | CTL-00.2 | `BOUND` | `BOUND` | **PASS static** |
| `R-NESTED-01` | existing Parent + new open professional child claim → NEW/CHANGED → FORMATION | CTL-00.2/3 | `NEW/CHANGED→DIRECT vs FORMATION` | same | **PASS static** |
| `R-NESTED-DIRECT-01` | existing Parent + bounded sufficiently specified child claim → NEW/CHANGED → DIRECT | CTL-00.2/3 | claim-relative DIRECT | same | **PASS static** |
| `R-CHANGE-01` | material claim/scope/requirements/means change cannot ride as silent continuation | CTL-00.2 + CTL-13 | explicit `Material ... change→NEW/CHANGED` | explicit | **PASS static** |
| `R-DIRECT-01` | bounded one-shot work exits DIRECT without ceremony | CTL-00.3 / INV-11 | DIRECT rule | DIRECT rule | **PASS static** |
| `R-IDEATE-01` | explicit exploration may execute directly but remains probe state | CTL-00.4 | exploration DIRECT; probe≠Candidate | same | **PASS static** |
| `R-FORM-01` | open professional claim with solution-changing upstream state enters Formation | CTL-00.3 + FORM-06 | FORMATION | FORMATION | **PASS static** |
| `R-MET-01` | open professional Performance Bar activates Method/Reference before Candidate qualification | CTL-07/MET-01 | METHOD section | METHOD/PROVIDER | **PASS static** |
| `R-PRIOR-01` | Entry/Admission precedes Work-Product and shallowest execution | CTL-00.5 / INV-12 / REAL-01 | `ENTRY precedes` + `after ENTRY` | explicit priority | **PASS static** |
| `R-NEXT-01` | `Next` continues BOUND frontier only; substantive change re-admits | CTL-13 | `Next` BOUND; scope change NEW/CHANGED | same | **PASS static** |
| `R-STATE-01` | persistent/divergent state selects minimum carrier; Project optional | STATE-02 | CONTROL | PERSIST | **PASS static** |

## 7. Static scenario regression

### S1 — R20 root Graphic-Novel cold start

Trigger:

```text
Ich möchte ein Grafik Novel über die Geschichte des Bieres entwerfen
```

Expected:

```text
no controlling Parent
→ provisional Parent/outcome
→ NEW/CHANGED CLAIM
→ DIRECT fails because professional Performance/Reference state
   can materially change solution class/evaluation
→ FORMATION
→ reference/craft intelligence as needed
→ ideas may be probes
→ no preferred Candidate/route/design basis yet
```

**Verdict:** PASS static.  
**Behavioral:** UNVERIFIED.

### S2 — translation

```text
Übersetze diesen Absatz ins Englische.
```

Expected: bind minimal context → NEW/CHANGED → DIRECT → translate/check/close.

**Verdict:** PASS static.

### S3 — birthday card

Requested product is the creative text itself.

Expected: NEW/CHANGED → DIRECT → write/close.

**Verdict:** PASS static.

### S4 — explicit ideation

```text
Gib mir fünf verrückte Ideen für eine Graphic Novel über Bier.
```

Expected: NEW/CHANGED → DIRECT exploration; ideas remain probes unless later qualified.

**Verdict:** PASS static.

### S5 — bounded scene with specified mechanism

```text
Schreib eine Szene, in der Hefe als Erzähler spricht.
```

Expected: NEW/CHANGED → DIRECT bounded execution.

**Verdict:** PASS static.

### S6 — consequential decision

```text
Soll ich 2026 oder 2027 ein E-Auto kaufen?
```

Expected: NEW/CHANGED → FORMATION/evidence before decision.

**Verdict:** PASS static.

### S7 — established repository continuation

Known Parent + admitted current repair frontier; message genuinely continues current frontier.

Expected: bind Parent → BOUND → continue current frontier.

**Verdict:** PASS static.

### S8 — `Next`

No material claim/scope change.

Expected: bind Parent → BOUND; no acceptance/Promotion/Authorization/persistence/scope change/new commitment.

**Verdict:** PASS static.

### S9 — `R-NESTED-01`: new professional child claim under established Parent

Context: established System Development program. Trigger:

```text
Wir sollten jetzt ein neues professionelles Evaluations-Dashboard entwickeln.
```

Expected:

```text
bind existing Program Parent
→ message is NEW/CHANGED child claim, not BOUND
→ performance/requirements/reference can change design class
→ FORMATION before preferred dashboard architecture
```

**Verdict:** PASS static.

### S10 — `R-NESTED-DIRECT-01`: bounded child under established Parent

Context: established program. Trigger requests a deterministic readback of one already identified file/hash.

Expected:

```text
bind existing Parent
→ NEW/CHANGED bounded child claim
→ upstream readiness sufficient
→ DIRECT readback/check
→ no visible Formation ceremony
```

**Verdict:** PASS static.

### S11 — `R-CHANGE-01`: material change during admitted execution

Context: Work Product execution underway. Human materially changes target audience, requirements or solution constraints.

Expected:

```text
bind existing Parent
→ material change = NEW/CHANGED CLAIM
→ re-run DIRECT vs FORMATION
→ old Admission cannot silently authorize changed work
```

**Verdict:** PASS static.

## 8. Protected predecessor semantics

Global v0.7 was inspected against material Global-v0.5 controls:

```text
outcome before means / incomplete input                  PASS
reality + provenance/freshness/scope                     PASS
retrieved/tool output ≠ instruction/authority            PASS
no invention/transfer incl capability/access/authority   PASS
working ≠ authoritative ≠ reusable                       PASS
proposal/decision/acceptance/commitment/auth/execution   PASS
completion/transition/use/outcome distinction            PASS
Parent continuity / thread-artifact ≠ root               PASS
full Work-Function selector coverage                     PASS
proportional research/decomposition/persistence/etc.     PASS
Ends before means / alternatives / no-action             PASS
Method source→fit→apply→assure + missing-method downgrade PASS
provider comparison + simplest adequate authorization    PASS
Human non-substitutable / not default QA                 PASS
Decision≠Commitment≠Authorization≠Handoff≠Execution≠Promotion PASS
Promotion→WRITE→READBACK→RECONCILE                       PASS
Human Gate→WAIT→re-entry                                 PASS
Handoff method/source + Work Basis + authority state     PASS
Provider Return includes next frontier                   PASS
child output ≠ parent completion/promotion               PASS
Human-facing Control Return                              PASS
requested Work Product / no process substitute           PASS
shallowest adequate route                                PASS
bounded decomposition + boundary cost                    PASS
AI-resolvable next-use repair / mechanism before polish  PASS
claim/object/version/environment/requirements assurance  PASS
self-review/verification/independent/intended-use distinctions PASS
missing coverage→FAIL/UNVERIFIED/pending                 PASS
representative validation or pending                    PASS
transition/use/performance/mechanism/outcome/value chain PASS
bounded reopen / legitimate control change / closure     PASS
```

## 9. Detection capability note

This validation-formation review detected a material gap **before external installation** that the first static trace missed. The amended assurance therefore demonstrates detection capability for a concrete relation failure:

```text
ESTABLISHED Parent
≠ child claim already admitted
```

The prior intermediate branch state remains Working history only. This PASS applies to the amended branch state and does not erase the need for behavioral validation.

## 10. Behavioral validation requirements

Because Global v0.6 already showed `static PASS ≠ behavioral PASS`, Entry Dispatch must be observed on the actual carrier.

Non-compensatory behavioral gates:

### Admission / enforcement gate

Open professional work must not enter preferred Candidate/route/design-basis execution before decision-changing upstream readiness.

### Directness / proportionality gate

Bounded work and explicit exploration must not acquire unnecessary visible Formation ceremony.

### Nested-claim gate

Under an established Parent:

- new open professional child claim must re-enter Formation;
- bounded sufficiently specified child claim may go DIRECT;
- material change to current claim/scope/requirements/means must re-enter Admission.

For each trial capture:

```text
policy present?
context bound?
BOUND vs NEW/CHANGED decision?
DIRECT vs FORMATION decision where applicable?
substantive work withheld/permitted correctly?
Human burden / ceremony?
```

## 11. Claim boundary

```text
Canonical amended / persisted on branch            PASS
Interaction Contract amended / persisted            PASS
Operating Runtime amended / persisted               PASS
Global v0.7 carrier fit                             PASS
Project v0.6 carrier fit                            PASS
protected predecessor semantics                     PASS static
root cold-start relation                            PASS static
bounded DIRECT / exploration                        PASS static
established continuation                            PASS static
nested new professional child                       PASS static
nested bounded direct child                         PASS static
material changed-claim re-admission                  PASS static
Static Architecture                                 KEEP CLOSED
external settings mutation                          NOT PERFORMED
actual candidate installation                       NOT PERFORMED
behavioral Entry enforcement                        UNVERIFIED
behavioral proportionality                          UNVERIFIED
Promotion readiness                                 NOT ESTABLISHED
```

## 12. Current candidate disposition

The amended branch candidate is **statically coherent and carrier-fit enough for Behavioral Validation Route Formation**, but not for Promotion.

No PR, merge, `main` state change, Promotion or external ChatGPT settings mutation is authorized or performed by this trace.