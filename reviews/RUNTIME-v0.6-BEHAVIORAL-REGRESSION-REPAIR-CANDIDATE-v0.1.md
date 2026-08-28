# Runtime v0.6 Behavioral Regression Repair Candidate v0.1

**Status:** CANDIDATE SOURCE ONLY — not installed, not behaviorally validated, not promoted  
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

The subsequent live regression remains limited to F12, F17, F20, RC06 and RC08.

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

Compare readback against `main`: five intended modified source files, zero unrelated files, branch not behind `main`.

## Claim boundary and next transition

Static source qualification does not establish installed identity or Runtime behavior. F17, F20 and RC08 cannot be validly re-tested against this candidate until the affected Global/Project UI carriers and personal `work-formation` Skill package are separately authorized, deployed and read back.

After installed-identity readback, run one targeted behavioral bundle: F12, F17, F20, RC06 and RC08. Test-memory correction/reset is a separate authorized cloud-state action and must be read back independently.

No merge, installation, promotion, architecture change or Requirements change is authorized by this evidence.
