# Inquiry State Schema v2

**Role:** normalized logical schema for the Intent Formation & Orientation Worker.  
**Authority:** companion carrier of `INTENT_FORMATION_WORKER_SEMANTIC_CONTRACT_v2.md`.  
**Not:** a user questionnaire, required database layout, or instruction to display YAML in ordinary dialogue.

## 1. Schema invariant

Conversation is evidence. State is a defeasible interpretation. User commitments, external claims, AI interpretations and AI advice remain distinguishable by record type, authority, epistemic basis and legal transition.

## 2. Canonical logical schema

```yaml
formation_case:
  inquiry_id: string
  schema_version: "2.0"
  state_version: integer
  subject: string
  requested_contribution: string | null
  intended_downstream_use: string | null
  lifecycle: ACTIVE | PAUSED | HANDED_OFF | REOPENED | CLOSED
  disposition: CONTINUE_FORMATION | INSUFFICIENT_ORIENTATION |
               PARENT_OUTCOME_UNDER_REVIEW | FORMATION_PAUSED |
               READY_FOR_DOWNSTREAM | READY_WITH_DOWNSTREAM_RESEARCH
  scope:
    included: [string]
    excluded: [string]
    horizon: string | null
  reliance_context:
    stakes: LOW | MODERATE | HIGH | CRITICAL | UNKNOWN
    reversibility: EASY | COSTLY | HARD_TO_REVERSE | UNKNOWN
    urgency: LOW | MODERATE | HIGH | UNKNOWN
    evidence_need: ORIENTATION_ONLY | ORDINARY | STRONG | DOMAIN_AUTHORITY | UNKNOWN
    permitted_ai_roles: [REFLECTIVE | ORIENTING | CHALLENGING |
                         PROVISIONAL_ADVISORY]

evidence_ledger:
  - evidence_id: string
    origin: USER_TURN | USER_ARTIFACT | EXTERNAL_ORIENTATION | DOWNSTREAM_RETURN
    source_ref: string
    act: ASSERTION | CORRECTION | REJECTION | CONFIRMATION | QUESTION |
         EXAMPLE | CONTRAST | REACTION | FINDING
    content: string
    scope: string | null
    observed_at: string | null
    source_fitness:
      intended_claim: string | null
      competence_fit: HIGH | MEDIUM | LOW | UNKNOWN | NOT_APPLICABLE
      applicability_fit: HIGH | MEDIUM | LOW | UNKNOWN | NOT_APPLICABLE
      currency: CURRENT | AGING | EXPIRED | UNKNOWN | NOT_APPLICABLE
      known_defeaters: [string]
      review_trigger: string | null

actors_and_authority:
  concern_owner: actor_id | null
  values_author: actor_id | null
  decision_owner: actor_id | null
  actors:
    - actor_id: string
      role: USER | DECISION_OWNER | DIRECTLY_AFFECTED | INDIRECTLY_AFFECTED |
            DOMAIN_AUTHORITY | EXECUTION_OWNER
      interests_or_rights: [string]
      authority_scope: string | null
      required_involvement: NONE | INFORM | CONSULT | CONSENT | DECIDE | UNKNOWN
  delegated_latitude:
    delegate: HUMAN | AI | DOWNSTREAM_WORKER | null
    may_decide: [string]
    must_not_decide: [string]
    escalation_conditions: [string]

intent_architecture:
  parent_control:
    active_parent_id: node_id | null
    review_status: STABLE | TRIGGERED | UNDER_REVIEW | AWAITING_OWNER | NOT_APPLICABLE
    trigger_refs: [evidence_id | assumption_id | relation_id | advisory_id]
    candidate_replacement_ids: [node_id]
    last_owner_confirmation_ref: evidence_id | null
  nodes:
    - node_id: string
      node_type: PURPOSE | VISION | OUTCOME | ENABLING_STATE |
                 OUTPUT | MEANS | EVIDENCE | GUARDRAIL
      role: ACTIVE_PARENT | CURRENT | SUPPORTING | SIBLING | NONE
      statement: string
      scope: string | null
      horizon: string | null
      owner_ref: actor_id | null
      parent_lifecycle: NOT_APPLICABLE | PROVISIONAL | ACTIVE |
                        UNDER_REVIEW | SUPERSEDED
      semantics: ClaimSemantics
  relations:
    - relation_id: string
      relation_type: SERVES | CONTRIBUTES_TO | NECESSARY_FOR |
                     OPERATIONALIZES | EVIDENCED_BY | CONFLICTS_WITH |
                     CONSTRAINED_BY | OWNED_BY | ASSUMES
      from_id: string
      to_id: string
      status: HYPOTHESIS | GROUNDED | ACCEPTED | REJECTED | SUPERSEDED
      evidence_refs: [evidence_id]
  contribution_hypotheses:
    - contribution_id: string
      lower_node_id: string
      higher_node_id: string
      mechanism: string | unknown
      intermediate_state_ids: [node_id]
      assumption_refs: [assumption_id]
      external_influencers: [string]
      countereffects: [string]
      evidence_refs: [evidence_id]
      confidence: HIGH | MEDIUM | LOW | UNRATED
      review_triggers: [string]
  alignment_view:
    vertical: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    end_to_end: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    horizontal: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    temporal: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    evidence_proxy: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    authority: PASS | CONCERN | UNKNOWN | NOT_MATERIAL
    rationale: [string]

taste_and_quality:
  criteria:
    - criterion_id: string
      statement: string
      polarity: POSITIVE | ANTI_CRITERION
      scope: string
      maturity: EMERGING | STABLE_HERE | CONTESTED
      semantics: ClaimSemantics
  exemplars:
    - exemplar_id: string
      type: POSITIVE | NEGATIVE | CONTRAST_PAIR
      description: string
      diagnostic_only: boolean
      elicited_judgment: string | null
      evidence_refs: [evidence_id]
  tradeoff_boundaries:
    - boundary_id: string
      statement: string
      status: OPEN | ACCEPTABLE | UNACCEPTABLE | CONTEXT_DEPENDENT
      semantics: ClaimSemantics

orientation_and_frames:
  situation_claims:
    - claim_id: string
      statement: string
      semantics: ClaimSemantics
  frames:
    - frame_id: string
      statement: string
      role: ACTIVE | RIVAL | REJECTED | SUPERSEDED
      explains: [claim_id]
      unexplained_residue: [string]
      applicability_limits: [string]
      semantics: ClaimSemantics
  reference_classes:
    - reference_id: string
      description: string
      similarity_basis: [string]
      disanalogies: [string]
      permitted_use: ORIENTATION_ONLY
      evidence_refs: [evidence_id]

assumptions_and_constraints:
  assumptions:
    - assumption_id: string
      statement: string
      causal_role: string | unknown
      load_bearing: YES | NO | UNKNOWN
      vulnerability: HIGH | MEDIUM | LOW | UNKNOWN
      controllability: CONTROLLED | INFLUENCEABLE | EXTERNAL | UNKNOWN
      signposts: [string]
      semantics: ClaimSemantics
  constraints:
    - constraint_id: string
      statement: string
      constraint_type: INVARIANT | NEGOTIABLE | ASSUMED | UNKNOWN
      controllability: CONTROLLED | INFLUENCEABLE | EXTERNAL | UNKNOWN
      affected_node_ids: [node_id]
      semantics: ClaimSemantics

advisory_assessments:
  - advisory_id: string
    advisory_type: BLIND_SPOT | NEGATIVE_PATH | OPPORTUNITY |
                   CATEGORY_ERROR | MISALIGNMENT | ASSUMPTION_CHALLENGE
    object_refs: [string]
    provisional_assessment: string
    basis:
      user_evidence_refs: [evidence_id]
      external_evidence_refs: [evidence_id]
      ai_inference: string | null
    material_consequence: string
    applicability_and_uncertainty: [string]
    reversal_conditions: [string]
    user_response: UNADDRESSED | ADOPTED | MODIFIED | REJECTED | DEFERRED
    lifecycle: ACTIVE | RESOLVED | SUPERSEDED

formation_commitments:
  - commitment_id: string
    object_ref: string
    commitment_type: FRAME_ADOPTION | CRITERION_ADOPTION |
                     CURRENT_OUTCOME_ADOPTION | PARENT_OUTCOME_CONFIRMATION |
                     SCOPE_AUTHORIZATION | HANDOFF_AUTHORIZATION
    owner_ref: actor_id
    status: ACCEPTED_AS_WORKING | COMMITTED | REVOKED | SUPERSEDED
    evidence_refs: [evidence_id]

unknowns_and_research:
  - unknown_id: string
    question: string
    resolvability: USER_JUDGMENT | USER_EXPERIENCE | FORMATIVE_ORIENTATION |
                   DOWNSTREAM_RESEARCH | DOMAIN_AUTHORITY | UNRESOLVED
    why_material: string
    affected_state_refs: [string]
    decision_use: string | unknown
    status: ACTIVE_FRONTIER | BACKLOG | READY_TO_RESEARCH |
            ANSWERED_EXTERNALLY | RESOLVED_BY_USER | OBSOLETE
    research_control:
      bounded_query: string | null
      expected_state_effect: [string]
      stopping_condition: string | null
      contamination_risk: LOW | MEDIUM | HIGH | UNKNOWN

policy_control:
  active_frontier:
    issue: string | null
    target_refs: [string]
    live_interpretations: [string]
    why_material: string | null
    answer_source: USER | EXTERNAL_ORIENTATION | DOMAIN_AUTHORITY | NONE | UNKNOWN
  candidate_moves:
    - candidate_id: string
      intervention: MIRROR | ASK | CONTRAST | FRAME | ORIENT | CHALLENGE |
                    ADVISE_PROVISIONALLY | FORMALIZE | STOP_OR_HANDOFF
      focus_operator: NONE | CLASSIFY_LEVEL | LADDER_UP | DEFINE_END_STATE |
                      BACKCAST_STATES | TRACE_FORWARD_EFFECT | CHECK_ACROSS |
                      TEST_PROXY | ALIGN_HANDOFF
      target_refs: [string]
      expected_state_effect: string
      contribution_contract:
        work_object: SITUATION | INTENT | PURPOSE | OUTCOME | FRAME | TASTE |
                     ASSUMPTION | CONSTRAINT | EVIDENCE | OPTION | DECISION | EXECUTION
        purpose: FORM | ORIENT | DELIBERATE | DECIDE | EXECUTE | LEARN
        authority_effect: EVIDENCE_ONLY | AI_HYPOTHESIS | AI_ADVICE |
                          SHARED_GROUNDING | USER_FORMATION_COMMITMENT
        transition_effect: UPDATE_FORMATION | OPEN_PARENT_REVIEW |
                           PREPARE_HANDOFF | DOWNSTREAM_WORK | REENTER_FORMATION
      eligible: boolean
      gate_reason: string
  selected_move:
    candidate_id: string | null
    intervention: string | null
    focus_operator: string | null
    target_refs: [string]
    rationale: string | null
  do_not_repeat: [string]

sufficiency:
  intended_use_named: PASS | FAIL | UNKNOWN
  agency_and_ownership: PASS | FAIL | UNKNOWN
  intent_outcome_coherence: PASS | FAIL | UNKNOWN
  outcome_alignment: PASS | FAIL | UNKNOWN
  taste_adequacy: PASS | FAIL | NOT_MATERIAL | UNKNOWN
  orientation_adequacy: PASS | FAIL | NOT_MATERIAL | UNKNOWN
  assumptions_constraints_contained: PASS | FAIL | UNKNOWN
  authority_stakeholders_contained: PASS | FAIL | NOT_MATERIAL | UNKNOWN
  advisory_coverage: PASS | FAIL | NOT_MATERIAL | UNKNOWN
  grounding_for_use: PASS | FAIL | UNKNOWN
  unknowns_typed: PASS | FAIL | UNKNOWN
  residual_formation_value: MATERIAL | LOW | UNKNOWN
  handoff_executable: PASS | FAIL | UNKNOWN
  disposition: CONTINUE_FORMATION | INSUFFICIENT_ORIENTATION |
               PARENT_OUTCOME_UNDER_REVIEW | FORMATION_PAUSED |
               READY_FOR_DOWNSTREAM | READY_WITH_DOWNSTREAM_RESEARCH
  rationale: [string]

intent_contract:
  status: NOT_READY | DRAFT | ISSUED | SUPERSEDED
  contract_version: integer | null
  derived_from_state_version: integer | null
  intent: string | null
  purpose: string | null
  desired_end_state: string | null
  active_parent_outcome_ref: node_id | null
  contribution_summary: string | null
  substantive_fit:
    criterion_refs: [criterion_id]
    exemplar_refs: [exemplar_id]
    anti_criteria: [string]
  success_and_failure:
    evidence_node_refs: [node_id]
    failure_signals: [string]
    proxy_caveats: [string]
  scope_guardrails_constraints: [string]
  controllability_limits: [string]
  authority:
    decision_owner_ref: actor_id | null
    affected_party_refs: [actor_id]
    required_consultation: [string]
  frames_assumptions_and_evidence_limits: [string]
  unresolved_human_judgments: [string]
  research_questions:
    formative: [unknown_id]
    downstream: [unknown_id]
    domain_authority: [unknown_id]
  downstream_contract:
    next_work_type: RESEARCH | ANALYSIS | DECISION_ANALYSIS |
                    SOLUTION_GENERATION | WORK_PRODUCT_CREATION |
                    EXECUTION | UNKNOWN
    intended_use: string
    authorized_operations: [string]
    prohibited_operations: [string]
    delegated_latitude: [string]
  reentry_triggers: [string]
  protected_corrections: [string]

revision_log:
  - revision_id: string
    from_version: integer
    to_version: integer
    transition: ADD | INTERPRET | GROUND | ADOPT | COMMIT | REVISE |
                CONTEST | RESOLVE | REJECT | SUPERSEDE | OPEN_REVIEW |
                CLOSE_REVIEW | DEFER_TO_RESEARCH | ISSUE_HANDOFF | REENTER
    object_refs: [string]
    basis_refs: [evidence_id]
    actor_ref: actor_id | AI | SYSTEM
    rationale: string
```

## 3. Shared `ClaimSemantics`

Every material claim-like record uses:

```yaml
ClaimSemantics:
  authority_plane: USER | EXTERNAL | AI | JOINT_WORKING
  epistemic_basis: EXPLICIT | CONFIRMED | INFERRED | HYPOTHESIS |
                   SOURCE_SUPPORTED | UNRESOLVED
  confidence: HIGH | MEDIUM | LOW | UNRATED
  grounding: UNTESTED | INTERPRETED | GROUNDED_ENOUGH
  adoption: NOT_APPLICABLE | NOT_ADOPTED | ACCEPTED_AS_WORKING | COMMITTED
  lifecycle: ACTIVE | CONTESTED | RESOLVED | REJECTED | SUPERSEDED
  evidence_refs: [evidence_id]
  supersedes: [object_id]
  conflicts_with: [object_id]
  scope: string | null
  notes: string | null
```

`authority_plane`, `epistemic_basis`, `grounding`, `adoption` and `confidence` are independent axes.

Within `intent_architecture`, a node of type `EVIDENCE` denotes an outcome indicator or success signal. It is not an `evidence_ledger` item. The ledger records the basis for state claims; the node describes what would indicate that an outcome has occurred.

## 4. Cross-record invariants

1. Every active non-hypothetical material claim has at least one evidence reference.
2. `AI` and `EXTERNAL` records cannot transition to `COMMITTED` without explicit legitimate human-owner evidence.
3. `ADVISE_PROVISIONALLY` can update only `advisory_assessments` until user response evidence exists.
4. An external finding can update frames, assumptions, constraints or evidence status; it cannot directly create a user value, criterion or commitment.
5. Silence or topic continuation cannot set `GROUNDED_ENOUGH`, `ACCEPTED_AS_WORKING` or `COMMITTED` for a consequential AI-added claim.
6. A user correction supersedes incompatible inference; it does not erase the historical evidence.
7. `REJECTED` and `SUPERSEDED` objects are excluded from normal compiled context unless required for regression protection.
8. `ACTIVE_PARENT` follows the protected lifecycle and cannot be replaced by an ordinary reducer update.
9. `EVIDENCE` and `OUTPUT` nodes cannot substitute for `OUTCOME` without an explicit accepted relation.
10. A diagnostic option/example is marked `diagnostic_only=true` and cannot populate downstream candidates automatically.
11. Every research item names its material state effect; downstream research is not executed before handoff.
12. `READY_*` requires an issued or issuable Intent Contract and `residual_formation_value=LOW`.
13. A downstream return changes formation only through `REENTER` and a named trigger.

## 5. Legal transition table

| Event | Permitted transition | Prohibited shortcut |
|---|---|---|
| model parses user input | `UNTESTED → INTERPRETED` | inferred claim becomes user-confirmed |
| user demonstrates shared meaning | `INTERPRETED → GROUNDED_ENOUGH` | politeness or silence counted as grounding |
| user adopts working wording/frame/criterion | `NOT_ADOPTED → ACCEPTED_AS_WORKING` | polished AI wording counted as adoption |
| legitimate owner authorizes reliance | `ACCEPTED_AS_WORKING → COMMITTED` | AI assigns commitment |
| explicit correction | old object `SUPERSEDED` or `REJECTED`; corrected object active | source observation overwritten |
| unresolved contradiction | both objects remain `CONTESTED` with relation | premature forced synthesis |
| Parent trigger fires | `ACTIVE → UNDER_REVIEW` | immediate replacement |
| owner confirms Parent revision | old `SUPERSEDED`; replacement `ACTIVE` | AI-only revision |
| advice offered | new `ACTIVE/UNADDRESSED` advisory | user intent changed |
| user responds to advice | `ADOPTED/MODIFIED/REJECTED/DEFERRED` | non-response treated as adoption |
| formative research gate passes | external evidence and relevant frame/assumption update | solution candidates created |
| sufficiency passes | `ISSUE_HANDOFF` and `READY_*` | same-response downstream execution |
| re-entry trigger fires | `HANDED_OFF → REOPENED`; affected records reopened | whole state discarded or silently rewritten |

## 6. Minimal compiled view

The runtime need not carry the full schema in every turn. The Context Compiler should materialize:

```yaml
compiled_frontier:
  intended_use: string | null
  active_parent_outcome: string | null
  current_outcome: string | null
  contribution_or_alignment_concern: string | null
  relevant_taste: [string]
  active_frame_and_rivals: [string]
  load_bearing_assumptions_or_constraints: [string]
  authority_or_stakeholder_issue: string | null
  unresolved_advice: [string]
  active_unknown: string | null
  newest_corrections_and_protected_rejections: [string]
  applicable_gates: [string]
  selected_intervention: string
  sufficiency_blockers: [string]
```

This view is disposable policy context, not additional evidence or canonical state.

## 7. Minimal checkpoint view

```yaml
intent_contract_checkpoint:
  intent: string
  purpose: string | omitted_if_not_material
  desired_end_state: string
  parent_outcome_and_contribution: string | omitted_if_not_material
  substantive_fit: [string]
  success_failure_and_proxy_limits: [string]
  scope_guardrails_constraints: [string]
  authority_and_affected_parties: [string]
  frames_assumptions_evidence_limits: [string]
  unresolved_human_judgments: [string]
  research_questions:
    formative: [string]
    downstream: [string]
    domain_authority: [string]
  downstream_work_contract:
    next_work_type: string
    intended_use: string
    authorized_operations: [string]
    prohibited_operations: [string]
    delegated_latitude: [string]
  reentry_triggers: [string]
  protected_corrections: [string]
  disposition: READY_FOR_DOWNSTREAM | READY_WITH_DOWNSTREAM_RESEARCH |
               PARENT_OUTCOME_UNDER_REVIEW | FORMATION_PAUSED |
               INSUFFICIENT_ORIENTATION
```

Only material fields are shown to the user. Omission means immaterial or unavailable, not implicitly satisfied.
