# CI Continuity Regression Candidate — 2026-09-04

**Status:** CANDIDATE EVIDENCE; not promoted; not a product-state claim.

## Trigger

A live Human-AI Work System episode on 2026-09-04 repeatedly failed to preserve and act on already-qualified multi-turn state. Observed failures included:

- short continuation/approval cues (`Go`, `OK`) causing reframing, stopping, or meta-work instead of continuation of the active next action;
- Human corrections being generalized into new system theories rather than applied locally;
- accessible prior context and already-established product/system facts being re-requested or re-researched;
- Work/native-execution responsibilities being displaced by repository/meta-work.

The Human identified this as a recurrence of a previously observed activation/execution-reliability problem.

## Prior qualified evidence recovered

`legacy/archive-2026-09-02/rebaseline/ACTIVATION-COVERAGE-CHECK-2026-09-02.md` already concluded:

- conceptual coverage was present;
- the remaining problem was activation/execution reliability;
- no additional CI rule, runtime, or generic Skill was justified on that evidence alone.

This means the 2026-09-04 event must not be treated as first discovery of the problem.

## Candidate regression hypothesis

Between `main@8350cff27f53ccceb5e518a76a334e4fc1151cef` and `main@631e8431b862ead245fccd69ecdb77a958822a61`, PR #55 changed only:

1. one Operating Baseline principle sentence; and
2. two semantic regions of the Global CI.

The CI change replaced:

`Treat the initial framing as a starting point, not the presumed problem. Surface a missing premise or better frame when it could materially change the work.`

with:

`Treat initial framing as provisional; structuring it does not make it a commitment. Surface a missing premise, rival frame, or evidence gap that could materially change the work.`

This change is a plausible regression contributor because it strengthens local re-framing permission while the continuity paragraph does not establish an explicit precedence rule that already-qualified state controls the next action.

**Claim limit:** this is a regression hypothesis, not a proven causal attribution. The live failure could still reflect broader activation/execution instability not caused by PR #55.

## Emergency candidate response

Candidate branch:

`candidate/emergency-rollback-pr55-2026-09-04`

The branch restores the two PR-#55-modified active files exactly to their pre-PR-#55 identities:

- `rebaseline/CURRENT-GLOBAL-CUSTOM-INSTRUCTIONS-2026-09-03.md` → blob `e0941d0ed97ff6814ba1fa212be0edfe99ed9269`, 4,997-character CI payload;
- `baseline/OPERATING-BASELINE.md` → blob `d484299743efe5fce7afae6a1c7d5e579b2dd4fb`.

No merge, product configuration change, Skill change, plugin change, permission change, memory change, or installation is authorized by this record.

## Product hotfix boundary

If the Human needs immediate usability, the pre-PR-#55 4,997-character CI may be used as a **temporary product-state hotfix**. That would create product state that intentionally differs from authoritative `main` until the candidate is reviewed and either promoted or rejected.

The hotfix must therefore be treated as:

- reversible;
- explicitly temporary;
- separately observed from repository state;
- not proof that PR #55 caused the failure merely because behavior improves afterward.

## Validation question

The discriminating question is narrow:

> Does restoring the pre-PR-#55 CI materially reduce the observed multi-turn continuity / local-reframing failures under comparable genuine work?

A positive result supports PR #55 as a regression contributor. A negative result weakens that hypothesis and requires failure localization below or outside this semantic delta rather than further blind CI editing.

## Next gate

Human review of the rollback candidate. Merge and any permanent product-state reconciliation remain separately unauthorized.
