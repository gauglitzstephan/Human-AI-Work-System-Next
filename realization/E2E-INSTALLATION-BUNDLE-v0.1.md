# E2E ChatGPT Installation Bundle v0.1

**Status:** CANDIDATE INSTALLATION PACKAGE — repository-ready; external settings not changed.  
**Date:** 2026-08-20

## Install only after PR #12 is accepted/merged

Repository promotion and ChatGPT settings installation are separate transitions.

## A. Global Custom Instructions

Install the **exact payload** inside:

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.2.md`

Do not install v0.1 or a paraphrase.

Rollback control:

- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt`

After save, read back the visible Global Custom Instructions and verify they equal the reviewed v0.2 payload.

## B. System Weiterentwicklung Project Instructions

Project pre-state:

```text
NONE
```

Install the **exact payload** inside:

- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.1.md`

Rollback control:

- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E.txt`

After save, read back the visible Project Instructions and verify they equal the reviewed Project v0.1 payload.

## C. Required installation evidence

Record only after actual Human settings changes:

```text
Global installed: YES/NO
Global exact readback: PASS/FAIL
Project installed: YES/NO
Project exact readback: PASS/FAIL
installation time / account context
any save/truncation/product warning
```

Do not infer installation from repository merge.

## D. Conformance preflight after installation

Before quality/outcome interpretation, verify:

1. Project control source resolves to `main/CURRENT.md`.
2. GitHub access/retrieval actually works in the chosen surface.
3. Chat/Work/Codex/tool allocation can be selected without losing parent state.
4. A genuine Human Gate can stop blocked downstream work when one naturally arises; do not manufacture a high-stakes gate solely for a synthetic test.
5. PR/write/readback path works for material promotion/evidence.
6. Bounded direct work remains proportional.

## E. First real work

Only after the installation/readback preflight, start the next genuine work problem and persist material evidence using:

- `evaluation/E2E-REAL-USE-VALIDATION-PROTOCOL-v0.1.md`
- `evaluation/e2e-real-use/`

No additional architecture work is the default.
