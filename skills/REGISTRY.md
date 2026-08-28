# Reusable Skill Portfolio Registry

## Purpose

`skills/` is the single active repository source for reusable skill packages. This registry reports lifecycle evidence without duplicating each skill's invocation contract or method.

Discovery and deployment mechanics are defined in `skills/DEPLOYMENT-CONTRACT.md`. Personal Skill deployments, `.agents/skills/*`, and the optional plugin package expose the canonical packages without becoming independent sources.

Repository promotion, installed-content identity, runtime activation, runtime fitness, and outcome quality are separate states.

## Portfolio

| Skill | Canonical package | Repository source | Installed-content readback | Runtime evidence |
|---|---|---|---|---|
| `adaptive-exploration` | `skills/adaptive-exploration/` | Requirements-v0.3 pointer promoted through PR #35 after merge/readback | 2026-08-27 readback predates the v0.3 pointer change; updated installed identity unverified | unverified |
| `work-formation` | `skills/work-formation/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | not established by identity alone |
| `research-evidence` | `skills/research-evidence/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | not established by identity alone |
| `system-development` | `skills/system-development/` | promoted repaired source | personal Skill matched promoted package at 2026-08-27 readback | not established by identity alone |
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
