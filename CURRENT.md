# CURRENT

## Authority snapshot

This file is the current repository state declaration. It reports promotion state; it does not by itself establish Personal Skill installation, runtime activation, runtime fitness, or outcome quality.

- Controlling requirements: `foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md`
- Controlling architecture: `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`
- Architecture state: **CLOSED**, unless a documented reopening trigger occurs.
- Canonical reusable-skill source: `skills/`
- Runtime instruction carriers and topology: `realization/runtime/route-b/v0.6-chatgpt-runtime/`

## Repository state

PR #25 and the skill-source normalization repair are merged into `main`. Their repository changes are promoted. External ChatGPT installation or runtime behavior does not change merely because repository source is merged.

The six reusable skill packages have one active repository source under `skills/`. Earlier copies under `realization/runtime/route-b/v0.6-chatgpt-runtime/` remain absent from the active tree; Git history is the historical record.

## Skill state

| Skill | Canonical source | Repository state | Installation readback | Runtime fitness |
|---|---|---|---|---|
| `work-formation` | `skills/work-formation/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `research-evidence` | `skills/research-evidence/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `system-development` | `skills/system-development/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `evaluate-work-product` | `skills/evaluate-work-product/` | promoted source | retrieved installed content matches promoted source | one bounded genuine-use result; implicit discovery remains unverified |
| `decision-analysis` | `skills/decision-analysis/` | promoted source | retrieved installed content matches promoted source | forward runtime validation not started |
| `adaptive-exploration` | `skills/adaptive-exploration/` | promoted source | not deployed or read back in this transition | unverified |

`skills/REGISTRY.md` is the portfolio registry. It keeps repository promotion, installed-content readback, runtime behavior, and outcome evidence separate.

## CCR-01 disposition

CCR-01 open framing and exploration now has an explicit repository realization in `adaptive-exploration`. The Skill is orthogonal to `work-formation`, not a mandatory predecessor. This closes the repository-source realization gap only; runtime discoverability and fitness remain unpromoted.

## Next valid transitions

1. Deploy `adaptive-exploration` from the exact package on `main` through a supported Personal Skill installation surface.
2. Read the installed package back and compare it with the promoted source.
3. Observe implicit activation and method behavior on genuine open-space work.
4. Promote runtime claims only from bounded evidence; repair the lowest responsible mechanism if a material defect appears.

## Superseded declarations

Any older repository artifact that calls PR #25 unmerged, treats former runtime-package directories as the canonical reusable-skill source, treats `methods/METHOD-REGISTRY-v0.1.md` as active, or calls CCR-01 unrealized at repository-source level is historical rather than current authority.
