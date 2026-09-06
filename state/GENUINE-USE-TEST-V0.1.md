# Human State Infrastructure — Genuine-Use Test v0.1

**Status:** CANDIDATE TEST CONTRACT

## Claim under test

A thin persistent State Library plus `GET_STATE` / `CAPTURE_STATE` materially reduces reconstruction, state loss and authority confusion in real ChatGPT work without imposing unacceptable Human maintenance or becoming a new work-orchestration layer.

## Test design

Use real work only. Do not create synthetic demos unless needed to isolate a failure.

Run across at least three materially different work domains, initially:

- Career / application work
- Investing / decision work
- Spatzennest / creative artifact work

Marketing/strategy may be added because it stresses research, hypotheses and evolving strategic artifacts.

## Runtime loop

For each genuine work episode:

1. Identify current work intent and scope.
2. `GET_STATE`: retrieve only relevant active/resolved authoritative state from the State Library plus legitimate source systems where needed.
3. Perform the work using native ChatGPT/Work/Research/other suitable capability.
4. Produce real work products at the justified quality level; the State Library does not substitute for artifact/source/knowledge discipline.
5. `CAPTURE_STATE`: record only durable mutations that materially change later work, preserving provenance and authority.
6. Record failures only when decision-relevant; do not expand architecture merely because a behavior is imperfect.

## Important boundary

State Infrastructure does **not** by itself solve poor artifact production, weak research synthesis, missing source management, or failure to extract durable models/analysis. Those are separate outcome/capability problems. The test must observe whether State improves continuity and integration while also revealing which additional information-capital mechanisms are genuinely needed.

## Evidence to collect

For each episode record minimally:

- Human reconstruction required: none / minor / material
- State retrieval: relevant / incomplete / noisy / wrong
- State mutation capture: correct / missing / excessive / authority error
- Artifact continuity: preserved / partially preserved / lost
- Source/research continuity: preserved / partially preserved / lost
- Human maintenance burden: negligible / tolerable / excessive
- outcome note: did the mechanism materially improve work quality or speed?

## Failure interpretation

- If the AI fails to fetch available State despite runtime instruction: runtime/retrieval activation failure.
- If fetched State is wrong/stale: State quality/provenance/lifecycle failure.
- If correct State is available but work quality remains poor: do not blame State; inspect method, evidence, specification, artifact-production or model/tool capability.
- If durable research/models/artifacts still disappear despite correct State: qualify a separate Knowledge/Artifact Capital requirement rather than stuffing all content into State objects.
- If Human maintenance is high: reduce capture scope or automation burden before adding features.

## Promotion gate

Do not promote the State architecture or state-aware CI merely because the schema exists or a single episode succeeds. Promote only after genuine use demonstrates material net value across multiple domains and no unresolved authority/integrity failure makes reliance unsafe.
