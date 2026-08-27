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

The repository is also an installable skills-only plugin through `.codex-plugin/plugin.json`, with a repository marketplace carrier under `.agents/plugins/marketplace.json`. Repository-local Codex discovery uses symbolic links under `.agents/skills/` that resolve to the same canonical packages. These are optional deployment/discovery views, not duplicate sources.

## Skill state

| Skill | Canonical source | Repository state | Installation readback | Runtime fitness |
|---|---|---|---|---|
| `work-formation` | `skills/work-formation/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | not generalized from source identity |
| `research-evidence` | `skills/research-evidence/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | not generalized from source identity |
| `system-development` | `skills/system-development/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | not generalized from source identity |
| `evaluate-work-product` | `skills/evaluate-work-product/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | one bounded predecessor-use result; repaired discovery remains unverified |
| `decision-analysis` | `skills/decision-analysis/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | forward runtime validation not started |
| `adaptive-exploration` | `skills/adaptive-exploration/` | promoted repaired source | personal Skill package matched promoted source at 2026-08-27 readback | unverified |

`skills/REGISTRY.md` is the portfolio registry. It keeps repository promotion, installed-content readback, runtime behavior, and outcome evidence separate.

## Discovery and deployment disposition

The top-down semantic portfolio and bottom-up technical packaging are reconciled at repository-source level:

- concise trigger-first descriptions support progressive discovery;
- detailed methods remain progressively disclosed under each package's `references/`;
- `.agents/skills/*` supplies repository-local Codex discovery without source duplication;
- six standalone Personal Skills are the current ChatGPT deployment;
- `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` retain an optional bundled distribution route;
- `skills/DEPLOYMENT-CONTRACT.md` defines controlled source→deployment→readback and runtime-evidence→repair→promotion flows.

There is no automatic two-way synchronization. Repository merge does not update installed copies, and runtime evidence cannot silently modify or promote source.

## Candidate branch disposition

The original `candidate/evaluate-work-product-v0.2.1-test-carrier` and `candidate/decision-analysis-v0.1.2-test-carrier` branches are **SUPERSEDED HISTORICAL TEST CARRIERS**. Their skill packages and bounded evidence were promoted into `main` through PR #26 by preserved blob identity.

They are intentionally retained to preserve candidate lineage. They are not active source authority, deployment sources, or pending merge objects. New work starts from `main` and the canonical packages under `skills/`.

## CCR-01 disposition

CCR-01 open framing and exploration now has an explicit repository realization and content-matched Personal Skill deployment in `adaptive-exploration`. The Skill is orthogonal to `work-formation`, not a mandatory predecessor. Runtime discoverability and fitness remain unpromoted.

## Next valid transitions

1. Refresh or open a new conversation so the six current Personal Skills can enter discovery.
2. Run bounded direct and collision-sensitive activation checks without treating them as general runtime proof.
3. Continue genuine work and observe only material discovery, execution, quality, burden, or boundary failures.
4. Promote runtime claims only from bounded evidence; repair the lowest responsible mechanism if a material defect appears.

## Superseded declarations

Any older repository artifact that calls PR #25 unmerged, treats former runtime-package directories or superseded candidate branches as the canonical reusable-skill source, treats `methods/METHOD-REGISTRY-v0.1.md` as active, or calls CCR-01 unrealized at repository-source level is historical rather than current authority.
