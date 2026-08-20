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

## 4. Repository hygiene defect observed after Promotion

A bounded post-PR13 audit found:

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

## 5. Localization

The observed defect is localized to:

> **repository state/navigation/supersession hygiene + Promotion/readback assurance coverage**.

No evidence from this audit establishes a new static architecture gap. The accepted architecture therefore remains closed by default.

## 6. Bounded candidate repair

Authorized candidate scope on branch `repair/post-pr13-repo-hygiene-v0.1`:

1. normalize branch-local `CURRENT.md` to the post-PR13 state;
2. synchronize root `README.md` to Global v0.5 / Project v0.4 / Bundle v0.4;
3. add `realization/README.md` current-vs-history navigation;
4. tombstone Installation Bundles v0.1 and v0.2;
5. extend the repository Promotion/Readback method with entry-point/supersession hygiene checks;
6. persist this evidence record.

Out of scope:

- architecture/requirements changes;
- Runtime semantic recompilation;
- external ChatGPT settings mutation;
- behavioral acceptance;
- branch deletion or repository-wide historical cleanup;
- merge/Promotion of this hygiene candidate.

## 7. Supported state after candidate implementation

If branch readback confirms the bounded writes:

```text
post-PR13 root navigation coherence          CANDIDATE PASS
current-vs-history realization navigation    CANDIDATE PASS
obsolete Bundle v0.1/v0.2 action safety      CANDIDATE PASS
promotion-method hygiene coverage             CANDIDATE PASS
current-session v0.5/v0.4 effective load      OBSERVED BY CONTENT
persistent UI settings readback               STILL NOT SEPARATELY RECORDED
runtime behavioral conformance                STILL NOT ESTABLISHED
```

## 8. Next legitimate transition

After this hygiene candidate is independently read back and, only with separate Human authority, promoted:

```text
record/complete persistent external-settings readback where required
→ Runtime conformance preflight
→ first genuine System Development real-work validation
```

This evidence record does not authorize that Promotion or any external settings change.
