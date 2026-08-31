> **Status override — 2026-08-31: SUPERSEDED FOR CURRENT RUNTIME RELIANCE — HISTORICAL PROVENANCE ONLY. DO NOT INSTALL, EXECUTE OR USE AS CURRENT AUTHORITY. Resolve the current package through `../CURRENT.md` and `README.md`. All internal “current”, “ready” or next-action wording below is historical to its dated episode.**
>

# E2E Runtime Migration Manifest v0.1

**Status:** CANDIDATE MIGRATION PLAN — repository realization only; external ChatGPT settings not changed.  
**Date:** 2026-08-20  
**Parent program:** merged PR #11 / current E2E static-completeness candidate.

## 1. Migration objective

Move from the currently live legacy Global Custom Instructions / existing Project Instructions to an E2E-compatible operating runtime **without losing rollback, project-local control, or evidence of what was actually installed**.

This is a runtime migration, not another architecture redesign.

## 2. Current known state

```text
E2E static architecture package on main          YES
E2E Operating Runtime Contract on main            YES — candidate
Global E2E Runtime Kernel compiled                 YES — candidate
Project E2E Operating Template compiled            YES — candidate
Chat/Work/Codex allocation policy compiled         YES — candidate
Current external legacy Global CI still live       HUMAN REPORTED
Exact external legacy Global CI snapshot in repo   NOT ESTABLISHED
Any E2E Global kernel externally installed         NO / NOT ESTABLISHED
Existing Project Instructions inventoried          NO
Any Project migrated to E2E instructions           NO
Representative E2E real-use validation             NOT STARTED
```

## 3. Hard pre-installation blocker — rollback control

**Do not replace the live Global Custom Instructions until the exact currently live text is captured.**

Required artifact:

```text
realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt
```

Record with it:

```text
captured_at
reported account/workspace context
character count / hash
whether personalization/custom instructions were enabled
Human confirmation that this is the exact live pre-E2E payload
```

The repository contains prior Global-CI candidates, but they are not evidence that one of them is the exact currently installed payload. Do not infer rollback identity from candidate lineage.

## 4. Project-instruction blocker

OpenAI currently documents that Project Instructions override Global Custom Instructions inside the respective Project.

Therefore the first real-use validation Project must not be assumed to inherit the new Global kernel.

Before migration of that Project:

1. capture its exact current Project Instructions;
2. classify retained project/domain rules vs obsolete old-runtime rules;
3. install an E2E-compatible Project Operating Policy using `E2E-PROJECT-OPERATING-TEMPLATE-v0.1.md`;
4. record the exact post-install Project Instructions;
5. preserve rollback text.

Do **not** mass-migrate all Projects before one representative Project has shown the operating model is usable.

## 5. Candidate package

### Global kernel

`realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.1.md`

Purpose: cross-context fallback/control policy outside Projects and for contexts where Global Custom Instructions apply.

### Project operating template

`realization/E2E-PROJECT-OPERATING-TEMPLATE-v0.1.md`

Purpose: E2E-compatible local operating policy where Project Instructions supersede Global Custom Instructions.

### Surface allocation

`realization/E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md`

Purpose: dynamic selection among Chat, Work, Codex, apps/tools and external systems without turning product surfaces into architecture stages.

## 6. Installation sequence

### I0 — Repository/static readback

Before external change:

- static regression review of Global kernel against E2E Operating Contract and historical protected functions;
- verify Custom Instructions character envelope;
- verify Project template does not rely on Global CI inside Projects;
- verify Surface Allocation does not reify stages into product boundaries.

### I1 — Capture live rollback state — HUMAN ACTION REQUIRED

Human copies the exact currently live Global Custom Instructions into the rollback artifact or provides them for repository capture.

No external Global-CI replacement before this is done.

### I2 — Select one real Project / initiative for first migration

Choose an **actual active work initiative**, not a synthetic test Project.

Prefer a case likely to exercise meaningful E2E behavior and for which authoritative state can be recovered.

### I3 — Capture Project rollback state

Persist existing Project Instructions and material source/state pointers before changing them.

### I4 — Install Global E2E kernel — HUMAN ACTION REQUIRED

Human replaces the Global Custom Instructions with the exact reviewed payload.

Record:

```text
installed_at
exact payload hash/count
account/workspace context
reported successful save
```

### I5 — Install first Project E2E policy — HUMAN ACTION REQUIRED

Apply the reviewed Project template plus project-specific outcome/state/source pointers.

Record exact installed Project Instructions.

### I6 — Runtime conformance preflight

This is **not** an outcome benchmark. Verify only runtime facts required before interpreting later real work:

- correct Global payload was saved;
- selected Project has the intended Project Instructions;
- Global-vs-Project precedence is understood;
- required sources/connectors/tools are actually accessible;
- authoritative source pointers resolve;
- Human Gate can create an actual wait state in the selected surface where needed;
- persistent write/readback path exists for validation evidence.

Any failure here is a runtime/install defect, not an E2E behavioral-quality failure.

### I7 — First actual E2E work case

Run the next real work problem under the installed composition and persist material evidence using `evaluation/E2E-REAL-USE-VALIDATION-PROTOCOL-v0.1.md`.

## 7. Rollback triggers

Rollback the new runtime, or stop expansion, if:

- the exact installed payload cannot be verified;
- Project Instructions silently remove material E2E controls;
- bounded work becomes materially over-processed;
- Human Gates cannot be enforced where genuinely required;
- parent/authority state is lost across Chat/Work/surface handoffs;
- the new kernel introduces a severe regression in professional quality/state integrity/agency;
- the runtime cannot be debugged because actual instruction/surface state is unknown.

Rollback does not invalidate the static architecture claim; it localizes a realization failure unless evidence shows the architecture itself cannot be realized without semantic distortion.

## 8. Migration expansion rule

Do not migrate every Project immediately.

After the first representative real-use cases:

```text
usable E2E operating behavior
+ no material state/authority regression
+ acceptable coordination burden
+ actual value from Chat/Work allocation
        ↓
expand template to additional Projects selectively
```

Project-specific domain/craft rules remain local. Do not move them into the Global kernel merely for uniformity.

## 9. Promotion boundary

This migration branch may be merged as a **reviewed installation package** without claiming external installation. External installation and behavioral acceptance remain separate Human/runtime evidence events.
