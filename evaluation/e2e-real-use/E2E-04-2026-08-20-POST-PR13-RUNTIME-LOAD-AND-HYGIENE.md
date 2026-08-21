# E2E-04 — Post-PR13 Runtime Load and Repository Hygiene

**Observation date:** 2026-08-20  
**Closure-sync date:** 2026-08-21  
**Promotion-state-handoff repair date:** 2026-08-21  
**Case class:** E2E-04 — persistent multi-turn / multi-surface work program  
**Status:** MATERIAL OBSERVATION + BOUNDED HYGIENE ASSURANCE RECORD — **Promotion-ready evidence on unmerged PR #14; repository-promoted hygiene evidence if this exact state is read on `main` after PR #14 merge**.  
**Parent:** Human–AI Work System Runtime realization / validation program

## 1. Observation boundary

This record captures three distinct facts after PR #13:

1. the promoted Runtime payloads are effectively present in the current System Development Chat session;
2. repository navigation/supersession remained partially stale after repository Promotion and was repaired on a bounded hygiene branch;
3. the resulting hygiene package was repaired so its controlling/navigation/evidence state is valid both before and after the PR #14 repository-Promotion boundary.

It does **not** claim persistent ChatGPT UI readback, cross-session persistence, behavioral conformance, professional-quality improvement or outcome effectiveness.

## 2. Authoritative repository baseline and promotion-state boundary

Repository baseline observed from `main` before PR #14:

- PR #13 `Repair Runtime deployment, handoff and interaction control` — **MERGED** on 2026-08-20;
- `main/CURRENT.md` — PR #13 repository Promotion complete, external installation/readback a separate transition;
- current compiled views:
  - `realization/GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md`;
  - `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`;
  - `realization/E2E-INSTALLATION-BUNDLE-v0.4.md`.

Promotion-state interpretation for this record:

```text
IF read on unmerged PR #14 / repair/post-pr13-repo-hygiene-v0.1:
  this record + hygiene delta = CANDIDATE / PROMOTION-READY
  main remains repository authority

IF this exact state is read on main after PR #14 merge:
  bounded hygiene Promotion = COMPLETE
  this record is repository-promoted evidence for that bounded repair
```

The merge event, not the presence of Candidate text on a branch, determines repository Promotion. PR #14 merge would not authorize external ChatGPT settings changes.

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

### HYG-06 — Promotion-State-Handoff defect in the hygiene candidate

Promotion review of Draft PR #14 found that `CURRENT.md`, root `README.md`, `realization/README.md` and this evidence record were correct only while read on the unmerged branch. A direct merge would have copied Candidate/`main remains authority`/`Promotion NOT AUTHORIZED` wording onto `main`, immediately making the newly promoted repository state self-contradictory.

**Impact:** a technically successful PR #14 merge could have produced a stale authoritative `main` and repeated the same class of post-promotion control-state drift this hygiene repair was intended to prevent.

**Repair:** Human-authorized Promotion-State-Handoff rewrite of the four control/navigation/evidence surfaces so the same persisted text is valid on both sides of the merge boundary:

```text
unmerged PR #14 → Candidate / Human Promotion Gate
main after PR #14 merge → bounded hygiene Promotion COMPLETE / next parent frontier
```

**HYG-06 status:** implemented; final PR-level re-review required before Promotion readiness is re-established.

## 5. Localization

The observed defects are localized to:

> **repository state/navigation/supersession hygiene + Promotion/readback assurance coverage + promotion-state handoff representation**.

No evidence from this audit establishes a new static architecture gap. The accepted architecture therefore remains closed by default.

## 6. Bounded repair implemented

Branch: `repair/post-pr13-repo-hygiene-v0.1`; Draft PR: #14.

Implemented and read back before the final PR-level re-review:

1. normalize `CURRENT.md` to the post-PR13 state — **PASS**;
2. synchronize root `README.md` to Global v0.5 / Project v0.4 / Bundle v0.4 — **PASS**;
3. add `realization/README.md` current-vs-history navigation — **PASS**;
4. tombstone Installation Bundles v0.1 and v0.2 — **PASS**;
5. extend repository Promotion/Readback method with entry-point/supersession hygiene checks — **PASS**;
6. persist this evidence record — **PASS**;
7. reconcile HYG-05 current-package metadata/transition surfaces — **PASS**;
8. closure-sync `CURRENT.md` and this evidence record — **PASS**;
9. create Draft PR #14 for Promotion review — **COMPLETE**;
10. repair HYG-06 Promotion-State-Handoff in `CURRENT.md`, root `README.md`, `realization/README.md` and this record — **IMPLEMENTED / PR-LEVEL RE-REVIEW REQUIRED**.

Out of scope and not performed:

- architecture/requirements changes;
- Runtime semantic recompilation;
- external ChatGPT settings mutation;
- behavioral acceptance;
- branch deletion or repository-wide historical cleanup;
- merge/Promotion of PR #14.

## 7. Assurance state before final PR-level re-review

```text
bounded hygiene implementation                    PASS
written-file readback for HYG-01–05               PASS
HYG-05 current-package metadata coherence          PASS
Global v0.5 / Project v0.4 payload preservation    PASS by commit diff
HYG-06 promotion-state handoff implementation      IMPLEMENTED
HYG-06 PR-level post-repair review                 PENDING
current-session v0.5/v0.4 effective load           OBSERVED BY CONTENT
persistent UI settings readback                    NOT SEPARATELY RECORDED
runtime behavioral conformance                     NOT ESTABLISHED
real-use quality / outcomes                        NOT ESTABLISHED
```

Supported claim before re-review:

> **The bounded hygiene implementation exists and the identified Promotion-State-Handoff defect has been repaired, but PR #14 Promotion readiness must be re-established by reviewing the repaired PR diff/state.**

If final PR-level re-review passes, the supported transition claim becomes:

> **Before merge:** PR #14 is Promotion-ready within the bounded hygiene scope.  
> **If this exact state is read on `main` after an authorized PR #14 merge:** bounded repository-hygiene Promotion is COMPLETE; external Runtime persistence, behavioral conformance and outcome effectiveness remain unestablished.

## 8. Promotion-state handoff / next transition

```text
IF this record is on unmerged PR #14 / its head branch:
  hygiene implementation/readback                COMPLETE
  HYG-06 repair                                   IMPLEMENTED
  PR-level Promotion re-review                    REQUIRED
  repository Promotion                            HUMAN MERGE GATE — WAIT after PASS only

IF this exact state is on main after PR #14 merge:
  bounded hygiene Promotion                       COMPLETE
  persistent external-settings readback           NEXT TRANSITION / NOT YET ESTABLISHED
  Runtime conformance preflight                   PENDING readback reconciliation as required
  first genuine System Development real-work      BLOCKED until preflight
```

No statement in this record authorizes PR #14 merge or any external settings mutation.