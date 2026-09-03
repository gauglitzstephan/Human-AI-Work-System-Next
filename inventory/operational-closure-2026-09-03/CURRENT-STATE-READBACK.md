# Current State Readback — 2026-09-03

**Status:** Candidate evidence record until merged; observations are bound to the sources and product surface named here.  
**Repository baseline:** `main@d42a1b06614dd9510838750a85ce9690e42e93b5`; tree `79470f56a4e8d9a78270530a081393ef5a3c7b2a`.

| Object | Claim type | Exact readback | Status / limit |
|---|---|---|---|
| Repository `main` | `REPOSITORY_CURRENT` | Default branch points to `d42a1b…`; PR #51 merge `7cd5b5…`; PR #50 merge `d42a1b…` | Exact repository identity; no external-state implication |
| Current CI source | `REPOSITORY_SOURCE` | `rebaseline/CURRENT-GLOBAL-CUSTOM-INSTRUCTIONS-2026-09-03.md`; blob `e0941d…`; payload 4,997 chars | Current intended source |
| Installed Global CI | `INSTALLED_IDENTITY_VERIFIED` | Settings readback: 4,997 chars; exact equality to repository payload; SHA-256 `c73e9ee15b8526bff632cfba0091e674ea9308024ec7704673ea18f6ec1f57f7` | Inspected account/surface only; not general activation/behavior proof |
| Project Instructions | `INSTALLED_CONTENT_VERIFIED` | `Work System Development`: 6,838 chars; SHA-256 `da0f959fce111a6ce6fb740c289ac558971167ff95135c7ea07036723fc61d18` | `LEGACY_OR_CONFLICTING_REMOVE`; contains QWS, Requirements v0.3, Target Architecture v0.2 and retired Skill routes |
| Repository Skills | `REPOSITORY_SOURCE` | Active: `decision-analysis`, `evaluate-work-product`, `system-development`; demoted packages only under Legacy | Exact tree/readback |
| Repository plugin | `REPOSITORY_PACKAGE` | `.codex-plugin/plugin.json` version `0.2.0`, packages `./skills/` | Installable source only |
| Installed plugin package | `PRODUCT_UI_ABSENCE` | Not present in complete installed Plugin list | Supports “not installed on inspected surface”; does not delete repository package |
| Installed active Skills | `INSTALLED_AND_VISIBLE` | Exactly the three active Skills appear under `Installed`; all three are exposed to this Work runtime as remote Skill packages | Standalone Personal/remote deployment copies, not repository-plugin delivery |
| Demoted Skills | `INSTALLED_ABSENCE_VERIFIED` | `adaptive-exploration`, `work-formation`, `research-evidence` appear only under `Created by me` with `Add`; absent from runtime Skill inventory | Saved source remains; absence is surface/date bound |
| `system-development` content | `INSTALLED_IDENTITY_VERIFIED` | Entry file plus six references exactly equal repository source | Exact content identity at current `main` |
| Other active Skill content | `SEMANTIC_MATCH_WITH_BYTE_NOTE` | Both `SKILL.md` files exact; each sole method reference has one extra terminal newline installed | No semantic difference; not byte-identical package-wide |
| Skill activation | `EPISODE_OBSERVED` | `system-development` activated explicitly for this run; other two installed Skills were not needed | Activation is per episode, not inferred from installation |
| Native Work Transition behavior | `BOUNDED_GENUINE_USE_OBSERVATION` | Human supplied qualified Work Object/Architecture; Work executed planning, repository/product readback, method use and gated return | One episode; not general conformance proof |
| Professional fitness / outcome | `UNACCEPTED` | Candidate reports and PRs require Human review; no merge or product-state change performed | No outcome/value claim |

## Skill-by-skill product state

| Skill | repository_source | plugin_package | installed_or_absent | installed_identity_or_content | activation_visibility | current_match | evidence_limit |
|---|---|---|---|---|---|---|---|
| `decision-analysis` | `skills/decision-analysis/`; entry blob `b2efbf0d…`; method blob `d6aec1e1…` | Included in repository package `human-ai-work-system-next@0.2.0`; package itself not installed | Installed as standalone remote Skill `skill-6a8f4b8b299c8191886cfaf1c9e47a7e` | `SKILL.md` exact; method has one additional terminal newline | Installed and available; not invoked in this episode | Semantic match; package-wide byte identity false only for terminal newline | Inspected surface/runtime/date only |
| `evaluate-work-product` | `skills/evaluate-work-product/`; entry blob `5b0c4cd9…`; method blob `faa84f20…` | Included in repository package `human-ai-work-system-next@0.2.0`; package itself not installed | Installed as standalone remote Skill `skill-6a8e772e616c8191969b220807a7ea59` | `SKILL.md` exact; method has one additional terminal newline | Installed and available; not invoked in this episode | Semantic match; package-wide byte identity false only for terminal newline | Inspected surface/runtime/date only |
| `system-development` | `skills/system-development/`; seven repository blobs recorded in this run | Included in repository package `human-ai-work-system-next@0.2.0`; package itself not installed | Installed as standalone remote Skill `skill-6a8ddd367c6c81919fbd86aa685ac949` | All seven files exact | Installed, available and explicitly invoked in this episode | Exact current match at `main@d42a1b…` | Activation and correct use are episode-specific; outcome unproven |
| `adaptive-exploration` | `legacy/archive-2026-09-02/skills/adaptive-exploration/` | Excluded from active repository package/discovery | Absent from `Installed`; retained under `Created by me` with `Add` | No installed content exists to compare; saved source content not requalified | Not available in runtime Skill inventory | Installation state matches demotion intent | Saved-source identity was not treated as installed identity |
| `work-formation` | `legacy/archive-2026-09-02/skills/work-formation/` | Excluded from active repository package/discovery | Absent from `Installed`; retained under `Created by me` with `Add` | No installed content exists to compare; saved source content not requalified | Not available in runtime Skill inventory | Installation state matches demotion intent | Saved-source identity was not treated as installed identity |
| `research-evidence` | `legacy/archive-2026-09-02/skills/research-evidence/` | Excluded from active repository package/discovery | Absent from `Installed`; retained under `Created by me` with `Add` | No installed content exists to compare; saved source content not requalified | Not available in runtime Skill inventory | Installation state matches demotion intent | Saved-source identity was not treated as installed identity |
