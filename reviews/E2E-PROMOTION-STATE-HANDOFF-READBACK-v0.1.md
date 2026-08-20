# E2E Promotion-State Handoff Readback v0.1

**Status:** COMPLETE — PASS for repository transition integrity; external installation remains separate.  
**Date:** 2026-08-20  
**PR:** #13 — `runtime/deployment-mapping-repair-v0.5` → `main`

## 1. Defect caught at point of effect

Immediately before the authorized merge, the branch-local `CURRENT.md` was re-read and found to encode only the pre-merge state:

```text
main remains controlling until PR #13 is merged
R17 PR #13 repository Promotion = HUMAN MERGE GATE — WAIT
```

If merged unchanged, that same file would have become controlling on `main` while still claiming the merge had not happened.

This would violate the Runtime's own promotion rule:

```text
PROMOTE / WRITE
→ READBACK
→ RECONCILE controlling parent/domain state
```

The merge was therefore correctly withheld until the state handoff was repaired.

## 2. Repair

`CURRENT.md` now carries a location-sensitive promotion-state handoff:

```text
IF read on unmerged PR #13 branch:
  PR #13 repository Promotion = HUMAN MERGE GATE — WAIT

IF read on main after PR #13 merge:
  PR #13 repository Promotion = COMPLETE
  external Global + Project installation/readback = NEXT HUMAN TRANSITION
```

The authority boundary is also location-sensitive:

- unmerged branch: `main` remains controlling;
- post-merge `main`: the merged state becomes controlling repository state;
- external ChatGPT installation remains unperformed and unauthorised by repository merge alone.

## 3. Claim / boundary checks

```text
pre-merge candidate state remains type-correct              PASS
post-merge main state no longer self-describes as unmerged   PASS
repository Promotion ≠ external installation                 PASS
merge authority does not transfer to settings installation   PASS
next gate after merge is explicit                            PASS
readback after merge still required                          YES
```

## 4. Scope

No architecture, Method, Work Function, carrier compilation, or behavioral claim is changed by this repair.

This is a bounded promotion-state reconciliation fix required so that the approved PR merge does not create an immediately stale controlling state.

## 5. Verdict

> **PASS for PR #13 repository transition integrity, subject to final point-of-effect head/mergeability revalidation and post-merge `main/CURRENT.md` readback.**

The next authorized repository action is Squash Merge of PR #13 if its current head remains mergeable and no new dependency appears. External installation remains blocked pending a separate Human action after repository readback.
