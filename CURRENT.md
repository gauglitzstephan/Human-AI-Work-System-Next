# CURRENT

## Authority snapshot

This file is the current repository state declaration. It reports promotion state; it does not by itself establish Personal Skill installation, runtime activation, runtime fitness, or outcome quality.

- Controlling requirements: `architecture/REQUIREMENTS-v0.2.md`
- Controlling architecture: `architecture/TARGET-ARCHITECTURE-v0.2.md`
- Architecture state: **CLOSED**, unless a documented reopening trigger occurs.
- Canonical reusable-skill source: `skills/`
- Runtime instruction carriers and topology: `realization/runtime/route-b/v0.6-chatgpt-runtime/`

## Repository state

PR #25 is merged into `main`. Its runtime-controller and instruction-carrier changes are repository-promoted. The earlier statement that PR #25 remained a branch Candidate is superseded.

The five reusable skill packages now have one active repository source under `skills/`. Earlier copies under `realization/runtime/route-b/v0.6-chatgpt-runtime/` are removed from the active tree; Git history remains the historical record.

## Skill state

| Skill | Canonical source | Repository state | Installation readback | Runtime fitness |
|---|---|---|---|---|
| `work-formation` | `skills/work-formation/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `research-evidence` | `skills/research-evidence/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `system-development` | `skills/system-development/` | promoted source | retrieved installed content matches promoted source | not generalized from source identity |
| `evaluate-work-product` | `skills/evaluate-work-product/` | promoted source | retrieved installed content matches promoted source | one bounded genuine-use result; implicit discovery remains unverified |
| `decision-analysis` | `skills/decision-analysis/` | promoted source | retrieved installed content matches promoted source | forward runtime validation not started |

`skills/REGISTRY.md` is the portfolio registry. It keeps repository promotion, installed-content readback, runtime behavior, and outcome evidence separate.

## Open realization gap

CCR-01 open framing and exploration is covered by Requirements v0.2 but has no explicit reusable runtime method at this snapshot. This is a realization gap, not an architecture reopening trigger. Any proposed repair must enter as a separate candidate and preserve the boundaries of the five existing skills.

## Next valid transitions

1. Add and review a bounded exploration skill candidate against CCR-01 and the existing portfolio boundaries.
2. Merge only after static semantic review and repository coherence checks pass.
3. Treat Personal Skill deployment as a separate transition requiring installed-content readback.
4. Treat runtime fitness as a further transition requiring genuine work evidence.

## Superseded declarations

Any older repository artifact that calls PR #25 unmerged, treats the three former runtime-package directories as the canonical reusable-skill source, or treats `methods/METHOD-REGISTRY-v0.1.md` as the active runtime registry is historical rather than current authority.
