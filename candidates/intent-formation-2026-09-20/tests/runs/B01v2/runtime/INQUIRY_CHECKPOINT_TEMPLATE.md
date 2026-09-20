# Inquiry Checkpoint Template v2

Use at handoff, explicit pause, confirmed Parent Outcome revision, impending context loss or user request. Do not expose or persist the full internal schema by default. Include only material fields.

```yaml
inquiry_checkpoint:
  inquiry_id: string
  state_version: integer
  checkpoint_version: integer
  derived_at: string | null
  disposition: CONTINUE_FORMATION | INSUFFICIENT_ORIENTATION |
               PARENT_OUTCOME_UNDER_REVIEW | FORMATION_PAUSED |
               READY_FOR_DOWNSTREAM | READY_WITH_DOWNSTREAM_RESEARCH

  subject: string
  intended_use: string | null

  intent_contract:
    intent: string | null
    purpose: string | null
    desired_end_state: string | null
    active_parent_outcome: string | null
    contribution_summary: string | null

  substantive_fit:
    quality_criteria: [string]
    anti_criteria: [string]
    exemplars_or_contrasts: [string]
    scope_limits: [string]

  success_and_failure:
    success_signals: [string]
    failure_signals: [string]
    proxy_caveats: [string]

  situation_and_reality:
    active_frame: string | null
    material_rival_frames: [string]
    load_bearing_assumptions: [string]
    constraints_and_controllability: [string]
    evidence_or_applicability_limits: [string]

  agency_and_authority:
    decision_owner: string | null
    affected_parties: [string]
    required_consultation_or_consent: [string]
    delegated_latitude: [string]

  advisory_state:
    unresolved_provisional_assessments: [string]
    adopted_or_rejected_advice: [string]

  unresolved_items:
    human_judgments: [string]
    formative_orientation_questions: [string]
    downstream_research_questions: [string]
    domain_authority_questions: [string]

  downstream_contract:
    next_work_type: RESEARCH | ANALYSIS | DECISION_ANALYSIS |
                    SOLUTION_GENERATION | WORK_PRODUCT_CREATION |
                    EXECUTION | UNKNOWN | NOT_READY
    intended_use: string | null
    authorized_operations: [string]
    prohibited_operations: [string]

  reentry_triggers: [string]
  protected_corrections: [string]
  provenance_refs: [string]
```

## Recovery rules

1. Treat the checkpoint as a defeasible prior, not as more authoritative than a newer explicit user correction.
2. Confirm checkpoint identity and intended use before relying on it when several checkpoints are available.
3. Reconcile only material differences; do not make the user reconstruct already represented state.
4. Keep `REJECTED` and `SUPERSEDED` items only where needed to prevent regression.
5. If the checkpoint is missing, stale or cannot be read, use `EPISODIC_PROVISIONAL`: rely only on available chat evidence, expose material uncertainty and do not claim canonical continuity or issue a durable handoff.
6. A downstream result changes Formation only through a recorded re-entry trigger. Reopen affected fields, not the whole inquiry.

## User-visible compact form

Ordinarily show only:

- current Intent, Purpose and Desired End State;
- active Parent Outcome where material;
- substantive-fit criteria;
- decisive constraints/assumptions/authority;
- unresolved judgments and research questions;
- next work type, allowed boundary and re-entry triggers;
- disposition.

The YAML shape is an internal semantic template, not required conversation formatting.
