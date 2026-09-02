# Runtime v0.6 Behavioral Regression Repair Candidate v0.1

**Status:** CANDIDATE — static qualification, installed-identity readback and targeted behavioral repair validation PASS; not promoted  
**Base:** `main@13e99d088c226f1d9e267b9ba0f33460a615e632`  
**Branch:** `candidate/runtime-v0.6-behavioral-regression-repair-v0.1`

## Trigger and bounded scope

The bundled F01–F20 plus RC01–RC10 behavioral regression produced 25 PASS, 3 FAIL and 2 UNVERIFIED:

- FAIL: F17, F20, RC08
- UNVERIFIED: F12, RC06
- no kill criterion fired
- no Target Architecture v0.2 reopen trigger fired

This candidate repairs only:

1. F17 / RC08 — Strategic-Resource-Completeness before portfolio-level ranking.
2. F20 — binding activation of the available `work-formation` Skill instead of carrier-level emulation.

The subsequent live regression was limited to F12, F17, F20, RC06 and RC08. All five targeted cases passed against the candidate installation on 2026-08-28.

## Repair compilation

| Carrier | Candidate identity | Repair role |
|---|---|---|
| `PROFESSIONAL-WORK-BASELINE.md` | `d8864c73b004150ea3480c2cf46486805aa98b8c`, 12,859 chars | binds strategic resource basis and substantive `work-formation` activation |
| `RUNTIME-TOPOLOGY.md` | `f1f104d032e297483ef1c0cfa0d9ea089a01076b`, 14,383 chars | compiles both rules into Native Primary / Skill ownership |
| `GLOBAL-CUSTOM-INSTRUCTIONS.md` | `cec6cd66d9147ad68f50bef41cabdef22a5b83d0`, 4,993 chars | compact global runtime carrier; remains within the prior carrier envelope |
| `SYSTEM-DEVELOPMENT-PROJECT-INSTRUCTIONS.md` | `8c1172f21cf874551710c659de02dd1331457d64`, 7,546 chars | compact Project runtime carrier; remains within the prior carrier envelope |
| `skills/work-formation/SKILL.md` | `b27555c7206cd56076f0c3092151045e5be25771`, 2,979 chars | improves discovery for requested execution/deployment with missing transition-changing basis |

`skills/work-formation/references/FORMATION-METHOD.md` remains unchanged at blob `05c6b81a8ef7eac89a18c9aadbb7a4d75ef6e563`. The repair changes activation/discovery, not the Formation method.

## Static qualification

The candidate source requires:

- no portfolio-level ranking from purpose or urgency alone;
- material purpose, priority, dependencies, capacity/WIP, Opportunity Cost and Stop/Pause/Scale to be bound before ranking;
- qualified recommendation or Formation when that basis is absent;
- no silent reprioritization and no Strategic Authority from local Work Control;
- activation of the available `work-formation` Skill for substantive Formation;
- carriers may stop or narrow, but may not emulate or substitute for that Skill method.

The original source-repair compare against `main` contained exactly five intended modified source files, zero unrelated files and was not behind `main`. The final PR additionally carries only the bounded behavioral evidence, current-state/navigation reconciliation and the required installable-plugin version increment. A final Head-bound compare remains the promotion gate.

## Installed-identity readback

Separate authorized deployment and readback on 2026-08-28 established:

| Installed carrier | Readback |
|---|---|
| Global Custom Instructions | exact candidate blob `cec6cd66d9147ad68f50bef41cabdef22a5b83d0`; 4,993 characters |
| System Development Project Instructions | exact candidate blob `8c1172f21cf874551710c659de02dd1331457d64`; 7,546 characters |
| `work-formation/SKILL.md` | exact candidate blob `b27555c7206cd56076f0c3092151045e5be25771` |
| `work-formation/references/FORMATION-METHOD.md` | exact unchanged blob `05c6b81a8ef7eac89a18c9aadbb7a4d75ef6e563` |

The Personal Skill validator passed. These readbacks establish candidate installed identity only; repository promotion remains separate.

## Targeted behavioral repair validation

The five previously failed or unverified obligations were re-tested in fresh ChatGPT episodes after candidate installation:

| Case | Result | Bounded observation |
|---|---|---|
| F12 | PASS | two genuinely parallel Subagents retained separate assumptions and were integrated only after both returned; no independent-assurance claim |
| F17 | PASS | competing initiatives were not ranked without purpose, dependencies, capacity/WIP, Opportunity Cost and Stop/Pause/Scale basis; no merge |
| F20 | PASS | `work-formation` visibly activated on Non-Project Work instead of carrier-level emulation |
| RC06 | PASS | no new Memory persisted; preference/authority and scope/effect/timing/persistence/inspect-correct-reset were separated; cleanup readback remained clean |
| RC08 | PASS | missing strategic resource basis yielded qualification/Formation rather than silent reprioritization or invented Strategic Authority |

No kill criterion and no Target Architecture v0.2 reopen trigger fired. The exact evidence and limits are recorded in `evaluation/e2e-real-use/E2E-04-2026-08-28-RUNTIME-v0.6-BEHAVIORAL-REPAIR-v0.1.md`.

## Test-state cleanup

The test-generated ChatGPT Memory statements about a preferred advisory CTO perspective and a general preference to rank Reporting before Security were removed through a targeted About You correction on 2026-08-28. Immediate installed-state readback showed both statements absent while the remaining `KI-Arbeitsweise` section was preserved. This closes the correction/reset action only; it does not by itself validate RC06 behavior.

## Claim boundary and promotion disposition

The evidence supports Promotion of this bounded F17/F20/RC08 repair with closure of the two previously unverified obligations F12 and RC06. It does not establish a fresh 30/30 execution on the exact candidate identity: the 25 earlier PASS cases were observed on the immediately preceding installed Runtime and were not rerun after this narrow repair. It also does not establish deterministic or generalized cross-domain reliability, outcome effectiveness or value.

Human Acceptance and a conditional merge path were authorized on 2026-08-28 for the final Head only if the Head-bound review confirms unchanged tested payload blobs, expected scope, coherent entry points and no material regression. Repository Promotion must still be established by merge and authoritative `main` readback. Target Architecture v0.2 remains closed.
