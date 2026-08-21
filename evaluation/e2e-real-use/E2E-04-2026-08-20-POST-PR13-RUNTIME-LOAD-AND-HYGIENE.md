# E2E-04 — Post-PR13 Runtime Load and Repository Hygiene

**Observation date:** 2026-08-20  
**Closure-sync date:** 2026-08-21  
**Case class:** E2E-04 — persistent multi-turn / multi-surface work program  
**Status:** MATERIAL OBSERVATION + BOUNDED HYGIENE ASSURANCE RECORD — candidate evidence on hygiene repair branch; Promotion-ready within scoped hygiene claim  
**Parent:** Human–AI Work System Runtime realization / validation program

## 1. Observation boundary

This record captures two distinct facts after PR #13:

1. the promoted Runtime payloads are effectively present in the current System Development Chat session;
2. repository navigation/supersession remained partially stale after repository Promotion and was repaired on a bounded hygiene branch.

It does **not** claim persistent ChatGPT UI readback, cross-session persistence, behavioral conformance, professional-quality improvement or outcome effectiveness.

## 2. Authoritative repository baseline

Repository state observed from `main`:

- PR #13 `Repair Runtime deployment, handoff and interaction control` — **MERGED** on 2026-08-20;
- `main/CURRENT.md` — repository Promotion complete, external installation/readback a separate transition;
- promoted current compiled views:
  - `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`;
  - `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`;
  - `realization/E2E-INSTALLATION-BUNDLE-v0.4.md`.

The hygiene branch remains Candidate and does not replace `main` until separately promoted.

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

**Candidate repair:** root README synchronized to the PR #13 package and current transition state.

### HYG-02 — superseded executable-looking bundles

`realization/E2E-INSTALLATION-BUNDLE-v0.1.md` and `v0.2.md` still contained active-looking installation instructions whose historical merge preconditions had already become true.

**Impact:** provenance artifacts could be misread as current executable guidance.

**Candidate repair:** both files converted to explicit `SUPERSEDED / DO NOT INSTALL` tombstones while repository history preserves their original content.

### HYG-03 — realization version ambiguity

`realization/` contains multiple generations of Global, Project, Installation Bundle and Migration Manifest artifacts without a local current-vs-history index.

**Impact:** version number/file recency could be mistaken for authority.

**Candidate repair:** `realization/README.md` added as current-package / history navigation.

### HYG-04 — promotion assurance coverage gap

`methods/system-development/REPOSITORY-PROMOTION-READBACK-METHOD-v0.1.md` required `CURRENT.md` readback and parent reconciliation but did not explicitly require a post-promotion scan of root navigation, action-bearing package pointers and superseded executable-looking artifacts.

**Impact:** PR #13 could be correctly promoted while material entry points remained contradictory.

**Candidate repair:** method extended with Entry-Point Hygiene Scan and supersession-safety checks.

### HYG-05 — current package metadata carried pre-observation transition state

The new Entry-Point Hygiene Scan found that the three **current** action-bearing artifacts still carried pre-current-session status wording:

- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`: `not externally installed`;
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`: `external save/readback not performed`;
- `E2E-INSTALLATION-BUNDLE-v0.4.md`: `repository promotion candidate; external installation not performed`.

Those statements were valid before the current-session effective-load observation but conflicted with the more precise supported state: **effective load observed in this session; independent persistent UI save/readback not separately recorded**.

**Candidate repair:** Human-authorized metadata-only reconciliation of all three current-package status/transition surfaces. Global v0.5 and Project v0.4 exact payload blocks were not changed; commit-diff readback confirmed that only metadata/boundary text changed in those two compiled-view files.

**HYG-05 verdict:** **PASS after write + readback**.

## 5. Localization

The observed defects are localized to:

> **repository state/navigation/supersession hygiene + Promotion/readback assurance coverage**.

No evidence from this audit establishes a new static architecture gap. The accepted architecture therefore remains closed by default.

## 6. Bounded candidate repair implemented

Branch: `repair/post-pr13-repo-hygiene-v0.1`.

Implemented and read back:

1. normalize branch-local `CURRENT.md` to the post-PR13 state — **PASS**;
2. synchronize root `README.md` to Global v0.5 / Project v0.4 / Bundle v0.4 — **PASS**;
3. add `realization/README.md` current-vs-history navigation — **PASS**;
4. tombstone Installation Bundles v0.1 and v0.2 — **PASS**;
5. extend repository Promotion/Readback method with entry-point/supersession hygiene checks — **PASS**;
6. persist this evidence record — **PASS**;
7. reconcile HYG-05 current-package metadata/transition surfaces — **PASS**;
8. closure-sync branch-local `CURRENT.md` and this evidence record — **PASS pending final readback of these two closure-sync writes**.

Out of scope and not performed:

- architecture/requirements changes;
- Runtime semantic recompilation;
- external ChatGPT settings mutation;
- behavioral acceptance;
- branch deletion or repository-wide historical cleanup;
- PR creation;
- merge/Promotion of this hygiene candidate.

## 7. Assurance verdict

Before final closure-sync readback:

```text
bounded hygiene implementation                    PASS
written-file readback for implementation           PASS
post-PR13 root README coherence                    PASS
current-vs-history realization navigation          PASS
obsolete Bundle v0.1/v0.2 action safety            PASS
promotion-method hygiene coverage                  PASS
HYG-05 current-package metadata coherence           PASS
Global v0.5 / Project v0.4 payload preservation    PASS by commit diff
current-session v0.5/v0.4 effective load           OBSERVED BY CONTENT
persistent UI settings readback                    NOT SEPARATELY RECORDED
runtime behavioral conformance                     NOT ESTABLISHED
```

Supported claim subject to final closure-sync readback:

> **The post-PR13 repository-hygiene candidate is Promotion-ready within its bounded navigation, supersession, current-package metadata and promotion-readback-assurance scope.**

This does **not** establish full repository cleanliness, external Runtime persistence, behavioral conformance or outcome effectiveness.

## 8. Next legitimate transition

After final readback confirms this closure-sync and branch-local `CURRENT.md`:

```text
bounded hygiene candidate       PROMOTION-READY
repository Promotion            HUMAN PROMOTION GATE — NOT AUTHORIZED
```

No PR or merge is created by this closure-sync.

If later separately promoted and read back from `main`, the parent program resumes at:

```text
complete/record persistent external-settings readback where required
→ Runtime conformance preflight
→ first genuine System Development real-work validation
```
