# E2E-04 — Post-PR13 Runtime Load and Repository Hygiene

**Date:** 2026-08-20  
**Case class:** E2E-04 — persistent multi-turn / multi-surface work program  
**Status:** MATERIAL OBSERVATION RECORD — candidate evidence on hygiene repair branch  
**Parent:** Human–AI Work System Runtime realization / validation program

## 1. Observation boundary

This record captures two distinct facts after PR #13:

1. the promoted Runtime payloads are effectively present in the current System Development Chat session;
2. repository navigation/supersession remained partially stale after repository Promotion.

It does **not** claim persistent ChatGPT UI readback, cross-session persistence, behavioral conformance, professional-quality improvement or outcome effectiveness.

## 2. Authoritative repository baseline

Repository state observed from `main`:

- PR #13 `Repair Runtime deployment, handoff and interaction control` — **MERGED** on 2026-08-20;
- `main/CURRENT.md` — repository Promotion complete, external installation/readback a separate transition;
- promoted current compiled views:
  - `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`;
  - `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`;
  - `realization/E2E-INSTALLATION-BUNDLE-v0.4.md`.

## 3. Current-session Runtime observation

Inside the current System Development Project conversation, the effective instruction context exposes:

- Global user Custom Instructions content matching the exact Global v0.5 payload by content;
- Project Instructions content matching the exact System Development Project v0.4 payload by content.

Supported claim:

```text
current-session effective Global v0.5 load   OBSERVED BY CONTENT
current-session effective Project v0.4 load  OBSERVED BY CONTENT
```

Not established by this observation:

```text
independent visible ChatGPT UI save/readback  NOT RECORDED
cryptographic readback from product settings  NOT AVAILABLE IN THIS OBSERVATION
future-session persistence                     NOT ESTABLISHED
behavioral conformance                         NOT ESTABLISHED
quality / outcome effectiveness                NOT ESTABLISHED
```

This distinction prevents both underclaiming (`not installed` despite current effective load) and overclaiming (session content treated as independent persistent settings evidence).

## 4. Repository hygiene defects observed after Promotion

### HYG-01 — stale root navigation

`README.md` still named the older Runtime v0.2 line and installation gate although `main/CURRENT.md` and PR #13 had promoted Global v0.5 / Project v0.4 / Bundle v0.4.

**Impact:** a reader starting from the repository root could select a superseded Runtime package or infer the wrong current gate.

### HYG-02 — superseded executable-looking bundles

`realization/E2E-INSTALLATION-BUNDLE-v0.1.md` and `v0.2.md` still contained active-looking installation instructions whose historical merge preconditions had already become true.

**Impact:** provenance artifacts could be misread as current executable guidance.

### HYG-03 — realization version ambiguity

`realization/` contains multiple generations of Global, Project, Installation Bundle and Migration Manifest artifacts without a local current-vs-history index.

**Impact:** version number/file recency could be mistaken for authority.

### HYG-04 — promotion assurance coverage gap

`methods/system-development/REPOSITORY-PROMOTION-READBACK-METHOD-v0.1.md` required `CURRENT.md` readback and parent reconciliation but did not explicitly require a post-promotion scan of root navigation, action-bearing package pointers and superseded executable-looking artifacts.

**Impact:** PR #13 could be correctly promoted while material entry points remained contradictory.

### HYG-05 — current package metadata still carries pre-observation transition state

The new Entry-Point Hygiene Scan found that the three **current** action-bearing artifacts still carry pre-current-session status wording:

- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`: `not externally installed`;
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`: `external save/readback not performed`;
- `E2E-INSTALLATION-BUNDLE-v0.4.md`: `repository promotion candidate; external installation not performed`.

These statements were valid before the current-session effective-load observation but now conflict with the more precise supported state: **effective load observed in this session; independent persistent UI save/readback not separately recorded**.

**Impact:** full action-bearing entry-point coherence is not yet established.

**Authority boundary:** repairing these three current-package files was not included in the Human-authorized points 1–6 for this branch. They were therefore **not modified** during this bounded implementation.

## 5. Localization

The observed defects are localized to:

> **repository state/navigation/supersession hygiene + Promotion/readback assurance coverage**.

No evidence from this audit establishes a new static architecture gap. The accepted architecture therefore remains closed by default.

## 6. Bounded candidate repair implemented

Authorized candidate scope on branch `repair/post-pr13-repo-hygiene-v0.1`:

1. normalize branch-local `CURRENT.md` to the post-PR13 state — **IMPLEMENTED**;
2. synchronize root `README.md` to Global v0.5 / Project v0.4 / Bundle v0.4 — **IMPLEMENTED**;
3. add `realization/README.md` current-vs-history navigation — **IMPLEMENTED**;
4. tombstone Installation Bundles v0.1 and v0.2 — **IMPLEMENTED**;
5. extend the repository Promotion/Readback method with entry-point/supersession hygiene checks — **IMPLEMENTED**;
6. persist this evidence record — **IMPLEMENTED**.

Readback confirmed the written branch artifacts. The new hygiene scan then exposed HYG-05 outside the authorized write scope.

Out of scope and not performed:

- architecture/requirements changes;
- Runtime semantic recompilation;
- external ChatGPT settings mutation;
- behavioral acceptance;
- branch deletion or repository-wide historical cleanup;
- metadata reconciliation of current Global v0.5 / Project v0.4 / Bundle v0.4;
- merge/Promotion of this hygiene candidate.

## 7. Assurance verdict

```text
points 1–6 implementation                       PASS
written-file readback                            PASS
post-PR13 root README coherence                  PASS within written scope
current-vs-history realization navigation        PASS
obsolete Bundle v0.1/v0.2 action safety          PASS
promotion-method hygiene coverage                PASS
current-session v0.5/v0.4 effective load         OBSERVED BY CONTENT
full current-package entry-point coherence        FAIL / PENDING HYG-05
persistent UI settings readback                   NOT SEPARATELY RECORDED
runtime behavioral conformance                    NOT ESTABLISHED
```

The branch is therefore a valid bounded implementation of the authorized points 1–6, but **not yet Promotion-ready as a complete repository-hygiene repair**.

## 8. Next legitimate transition

The minimum next frontier is a metadata-only extension of this hygiene candidate to reconcile the three current-package status surfaces with the supported Runtime transition state, without changing either compiled prompt payload.

Required additional Human authorization:

```text
Allow metadata-only reconciliation of:
- Global v0.5 current compiled-view status;
- Project v0.4 current compiled-view status;
- Installation Bundle v0.4 transition/status wording;
with no payload recompile, no external settings change and no merge.
```

Only after that extension is written and read back can this hygiene candidate return to a repository Promotion gate. Runtime conformance preflight remains downstream.
