> **Status override — 2026-08-31: SUPERSEDED FOR CURRENT RUNTIME RELIANCE — HISTORICAL PROVENANCE ONLY. DO NOT INSTALL, EXECUTE OR USE AS CURRENT AUTHORITY. Resolve the current package through `../CURRENT.md` and `README.md`. All internal “current”, “ready” or next-action wording below is historical to its dated episode.**
>

# E2E Runtime Migration Manifest v0.4

**Status:** REVIEWED CANDIDATE MIGRATION PLAN — activation-topology recompile complete; external ChatGPT settings not changed.  
**Date:** 2026-08-20  
**Parent program:** merged PR #11 / static-complete E2E architecture candidate.

## 1. Current state

```text
E2E static architecture on main                     YES
Exact pre-E2E Global rollback captured              YES
Pre-E2E first-Project Instructions captured         YES — NONE
Global E2E v0.3 compiled                            YES
Project E2E v0.2 compiled                           YES
Full static regression vs E2E + exact live CI       PASS
Activation-topology review                          PASS
External Global installation                        NO
External Project installation                       NO
Runtime conformance preflight                       NOT STARTED
Representative E2E real-use validation              NOT STARTED
```

## 2. Runtime compilation repair

The prior v0.2/v0.1 installation pair is superseded for installation because its flat control-catalog structure could over-activate conditional professional controls.

Current compilation:

```text
PERMANENT INVARIANTS
        ↓
WORK CONTROLLER / ORCHESTRATOR
        ↓
CONDITIONALLY ACTIVATED CAPABILITIES
```

No static-architecture reopen is implied.

## 3. Exact installation candidates

### Global

- `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.3.md`
- review: `reviews/E2E-RUNTIME-COMPILATION-FULL-STATIC-REGRESSION-v0.3.md`

Identity:

```text
LF:       4,975
CRLF:     4,980
SHA-256:  108ff9ad1919779bd9e1fbf027d2c339f1cb2840c1c2447c624df0d23d3bd544
```

### First Project

- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.2.md`

Identity:

```text
LF:       4,983
CRLF:     4,992
SHA-256:  b71a091afe2fc50cbb8edb671446849acd18273d48305c5052d27a0d89c81cda
```

Project pre-state remains Human-confirmed `NONE`.

## 4. Rollback controls

Global:

- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt`
- `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT-METADATA.md`

Project:

- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E.txt`
- `realization/rollback/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-PRE-E2E-METADATA.md`

Do not install a paraphrase or reconstruct rollback state from lineage.

## 5. Promotion / installation sequence

```text
I0 static E2E architecture                           COMPLETE
I1 exact Global rollback capture                     COMPLETE
I2 first Project selected                            COMPLETE
I3 exact Project pre-state captured                  COMPLETE — NONE
I4 Global v0.3 + Project v0.2 compiled               COMPLETE
I5 full static regression/readback                   COMPLETE / PASS
I6 repository promotion of PR #12                    NEXT
I7 Human installs exact Global v0.3                  AFTER MERGE
I8 Human installs exact Project v0.2                 AFTER MERGE
I9 exact visible settings readback                   AFTER INSTALL
I10 runtime conformance preflight                    PENDING
I11 first actual E2E real-work case                  PENDING
```

## 6. Installation readback evidence

After actual settings changes record:

```text
Global installed: YES/NO
Global visible readback: PASS/FAIL
Global saved identity: count/hash where available
Project installed: YES/NO
Project visible readback: PASS/FAIL
Project saved identity: count/hash where available
installation time/account context
save/truncation/product warning if any
```

Repository merge does not establish external installation.

## 7. Runtime conformance preflight

Before interpreting work quality, verify only runtime facts:

- Global v0.3 saved as reviewed;
- Project v0.2 saved as reviewed;
- Project override behavior understood;
- `main/CURRENT.md` and authoritative source pointers resolve;
- GitHub/tools/surfaces actually available/effective;
- parent/state/authority survive Chat/Work/Codex/tool handoffs;
- a naturally occurring material Human Gate can enforce WAIT/no blocked downstream work;
- promotion/write/readback works for material persistent change;
- bounded direct work remains proportional;
- validation evidence can be persisted outside transient chat memory.

Preflight failure is a Runtime realization defect, not an E2E outcome-quality verdict.

## 8. Real-use start rule

Only after successful installation/readback/preflight:

```text
next genuine work problem
→ operate under installed E2E composition
→ persist material evidence under evaluation/e2e-real-use/
→ localize defects to lowest responsible layer
→ reopen static architecture only on named material trigger
```

Do not mass-migrate other Projects before real-use evidence supports expansion.

## 9. Promotion boundary

Merging PR #12 adopts this reviewed Runtime migration/install package as repository guidance. It does not establish external installation, behavioral reliability, cross-surface enforcement effectiveness, professional quality, Quality-in-Use, outcome effectiveness or causal/value superiority.
