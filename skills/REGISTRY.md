# Reusable Skill Portfolio Registry

## Purpose

`skills/` is the single active repository source for reusable skill packages. This registry reports lifecycle evidence without duplicating each skill's invocation contract or method.

Discovery and deployment mechanics are defined in `skills/DEPLOYMENT-CONTRACT.md`. Personal Skill deployments, `.agents/skills/*`, and the optional plugin package expose the canonical packages without becoming independent sources.

Repository promotion, installed-content identity, runtime activation, runtime fitness, and outcome quality are separate states.

## Portfolio

| Skill | Canonical package | Repository source | Installed-content readback | Runtime evidence |
|---|---|---|---|---|
| `adaptive-exploration` | `skills/adaptive-exploration/` | Requirements-v0.3 pointer promoted through PR #35 after merge/readback | all canonical package files matched promoted source at 2026-08-28 readback | bounded genuine-use behavior observed; generalized discoverability and fitness unverified |
| `work-formation` | `skills/work-formation/` | activation/discovery repair promoted through PR #37 | all canonical candidate package files matched at 2026-08-28 readback; preserved blob identity ties the installed package to promoted source | F20 targeted activation PASS on Non-Project Work; generalized fitness unverified |
| `research-evidence` | `skills/research-evidence/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | not established by identity alone |
| `system-development` | `skills/system-development/` | promoted repaired source | all canonical package files matched promoted source at 2026-08-28 readback | not established by identity alone |
| `evaluate-work-product` | `skills/evaluate-work-product/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | one bounded predecessor-use PASS; repaired implicit discovery and general fitness remain unverified |
| `decision-analysis` | `skills/decision-analysis/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | forward runtime validation not started |

## Portfolio boundaries

Use the descriptions in the canonical `SKILL.md` files for activation. At portfolio level:

- explore a materially open frame, opportunity, route, concept, or direction with `adaptive-exploration`;
- form a blocking missing basis with `work-formation`;
- acquire or qualify material evidence with `research-evidence`;
- analyze a bounded material choice with `decision-analysis`;
- evaluate an identifiable existing product with `evaluate-work-product`;
- recover, repair, compile, promote, or validate this system with `system-development`.

Native ChatGPT retains ordinary planning, production, tool use, integration, and execution. Skills are not mandatory stages. `adaptive-exploration` is not a required predecessor to `work-formation`.

## Evidence interpretation

Installation readback establishes only retrieved content equivalence at the recorded inspection. It does not independently establish raw UI-byte identity, automatic invocation, correct execution in every context, or valuable outcomes.

Runtime and outcome claims must point to bounded evidence under `evaluation/`. A future replacement or material update enters as a candidate and is promoted separately.

The bounded PR #37 repair evidence is recorded in `evaluation/e2e-real-use/E2E-04-2026-08-28-RUNTIME-v0.6-BEHAVIORAL-REPAIR-v0.1.md`. It establishes the five targeted cases only; it does not claim a fresh exact-candidate 30/30 run or generalized Runtime fitness.
