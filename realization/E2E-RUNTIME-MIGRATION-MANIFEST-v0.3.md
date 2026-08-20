# E2E Runtime Migration Manifest v0.3

**Status:** INSTALLATION PACKAGE READY — Human installation/readback still required.  
**Date:** 2026-08-20  
**Parent program:** merged PR #11 / static-complete E2E architecture candidate.

## 1. Current state

```text
E2E static architecture package on main                 YES
E2E Operating Runtime Contract on main                   YES — candidate
Exact pre-E2E live Global CI rollback captured           YES
Global E2E kernel v0.2 compiled + static reviewed         YES
Global E2E kernel externally installed                    NO
First real Project selected                               YES — System Weiterentwicklung
Pre-E2E Project Instructions captured                     YES — NONE
Project E2E policy instantiated + static reviewed         YES
Project E2E policy externally installed                   NO
Representative E2E real-use validation                    NOT STARTED
```

## 2. Rollback controls

Global:
- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt`
- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT-METADATA.md`

Project:
- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E.txt`
- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E-METADATA.md`

Project pre-migration value is Human-confirmed `NONE`.

## 3. Exact installation candidates

Global:
- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.2.md`
- reviews: `reviews/E2E-GLOBAL-KERNEL-STATIC-REGRESSION-REVIEW-v0.2.md` and `reviews/E2E-KERNEL-LIVE-CONTROL-AND-SIX-PRIMITIVE-REVIEW-v0.1.md`

Project:
- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.1.md`
- review: `reviews/E2E-FIRST-PROJECT-INSTRUCTIONS-STATIC-REVIEW-v0.1.md`

Do not install paraphrases. Use the exact reviewed payloads and then read them back from ChatGPT settings.

## 4. Installation sequence

```text
I0 repository/static architecture                  COMPLETE
I1 exact Global rollback capture                   COMPLETE
I2 select first real Project                       COMPLETE
I3 capture first Project Instructions              COMPLETE — NONE
I4 instantiate/review Project E2E policy           COMPLETE
I5 repository promotion of migration package       HUMAN PR/MERGE
I6 install Global kernel v0.2                      HUMAN SETTINGS ACTION
I7 install Project policy v0.1                     HUMAN PROJECT SETTINGS ACTION
I8 installation/readback conformance preflight     PENDING
I9 first actual E2E real-work case                 PENDING
```

Repository merge and external installation remain different state transitions.

## 5. Installation readback record

After Global installation record:

```text
installed Global payload = exact v0.2 candidate?
save succeeded?
visible settings text read back?
reported account/workspace context
installation time
```

After Project installation record:

```text
Project = System Weiterentwicklung Projekt
pre-state = NONE
installed payload = exact Project v0.1 candidate?
save succeeded?
visible Project Instructions read back?
```

Persist the installation evidence before attributing later behavior to the E2E runtime.

## 6. Runtime conformance preflight

Before interpreting real-work quality, establish only runtime facts:
- exact Global payload is saved/read back;
- exact Project payload is saved/read back;
- Project override semantics are accounted for;
- repository/source pointers resolve;
- required GitHub/tools/surfaces are actually accessible/effective;
- a material Human Gate can produce a real WAIT/no blocked downstream execution where required;
- promotion/write/readback path is effective;
- validation evidence has a persistent repository path.

A preflight failure is a runtime/install defect, not an E2E outcome-quality verdict.

## 7. First real-use boundary

After preflight, use the next genuine System-Weiterentwicklung work problem or another actual work problem chosen by the controlling program. Do not create a synthetic benchmark merely to prove the architecture.

Persist material evidence via `evaluation/E2E-REAL-USE-VALIDATION-PROTOCOL-v0.1.md` under `evaluation/e2e-real-use/`.

## 8. Expansion rule

Do not mass-migrate other Projects. Expand only after real-use evidence shows acceptable coordination burden, state/authority integrity, useful Chat/Work allocation and no material professional-quality regression.
