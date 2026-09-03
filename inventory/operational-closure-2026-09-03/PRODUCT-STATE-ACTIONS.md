# Product State Actions — 2026-09-03

## Action 1

```yaml
action: Remove the legacy Work System Development Project Instructions
why_needed: They assert QWS, Requirements v0.3, Target Architecture v0.2 and retired Skill routing that conflict with the promoted reduced system.
current_evidence: Exact product readback; 6,838 characters; SHA-256 da0f959fce111a6ce6fb740c289ac558971167ff95135c7ea07036723fc61d18.
risk_of_no_action: Project sessions may receive duplicate or contradictory semantic ownership and reactivate retired routing/ceremony.
exact_human_step: After accepting this disposition, open Work System Development → Project settings → Instructions, clear the field, and save.
expected_readback: Instructions field is empty; a fresh Project session no longer receives QWS/retired-Skill/old-authority instructions.
```

This action was not executed. It requires a separate Human product-state gate.

## Action 2 — conditional on Skill Candidate promotion

```yaml
action: Update the standalone system-development Personal Skill
why_needed: Only if the separate System-Development Skill Requalification Candidate is accepted and merged, the installed copy will then lag authoritative repository source.
current_evidence: Installed copy currently matches all seven files on main@d42a1b06614dd9510838750a85ce9690e42e93b5 exactly.
risk_of_no_action: None before promotion; after promotion, external capability-delta triggering and proportional compilation/transition evaluation would remain on the old installed method.
exact_human_step: After merge readback only, update the system-development Personal Skill from the promoted package and read back all changed files.
expected_readback: Installed changed files and package version match the promoted repository identities; activation/behavior remain separate claims.
```

No action is required for Global CI, the three demoted Skills, or repository-plugin installation.
