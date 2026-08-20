# CURRENT — Human–AI Work System Next

**Status:** ACCEPTED TARGET CONCEPTUAL BASELINE v0.2 + STATIC-COMPLETE E2E WORK ARCHITECTURE CANDIDATE v0.1 + E2E RUNTIME MIGRATION CANDIDATE v0.3  
**Date:** 2026-08-20  
**E2E static package:** promoted to `main` via merged PR #11  
**Current candidate branch:** `runtime/e2e-migration-v0.1`  
**Authority boundary:** `main` controls the accepted repository program. This branch contains the reviewed runtime-migration/install package only. External ChatGPT installation and behavioral effectiveness remain separate evidence.

## Controlling program

Static architecture is closed by default. Current program:

```text
STATIC E2E PACKAGE ON MAIN
→ concrete runtime carriers compiled/reviewed
→ exact Global + Project rollback state preserved
→ one real Project instantiated
→ Human promotes migration package
→ Human installs exact Global + Project configuration
→ runtime conformance preflight
→ first actual representative E2E work case
→ persist evidence outside chat history
```

## Global rollback / candidate

Exact pre-E2E live Global CI is persisted in `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt` with metadata. Current installation candidate is `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.2.md`; v0.1 is superseded / do not install. External installation: **NOT PERFORMED**.

## First Project

Selected: **System Weiterentwicklung Projekt** / `gauglitzstephan/Human-AI-Work-System-Next`.

Human-confirmed pre-E2E Project Instructions:

```text
NONE
```

Rollback:
- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E.txt`
- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E-METADATA.md`

Project installation candidate:
- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.1.md`
- review: `reviews/E2E-FIRST-PROJECT-INSTRUCTIONS-STATIC-REVIEW-v0.1.md`

External Project installation: **NOT PERFORMED**.

## Installation package

- `realization/E2E-RUNTIME-MIGRATION-MANIFEST-v0.3.md`
- `realization/E2E-INSTALLATION-BUNDLE-v0.1.md`
- `realization/E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md`

State:

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

## Next legitimate gate

**Mode:** RUNTIME MIGRATION PACKAGE READY → HUMAN PROMOTION / INSTALLATION.

```text
Human reviews/merges PR #12
→ install exact Global kernel v0.2
→ install exact System Weiterentwicklung Project policy v0.1
→ read back both settings and persist installation evidence
→ run runtime conformance preflight
→ begin first actual E2E real-work case
```

Until installation/readback, do not attribute ordinary ChatGPT behavior to the new E2E Runtime.
