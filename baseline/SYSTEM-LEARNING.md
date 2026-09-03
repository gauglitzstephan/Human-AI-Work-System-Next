# System Learning

**Status:** CURRENT on authoritative `main`; CANDIDATE off `main`.  
**Role:** Narrow reusable discipline, not a runtime controller, lifecycle, automatic learner or new Skill.

## Purpose

Learn from material genuine-use evidence **and material external capability/product changes** without converting every defect or release note into permanent system growth.

Use this only when an observed work failure/success or a verified product/capability delta could materially change the working setup. Routine successful work and ordinary product news need no record.

## Bind the event

State the failed or supported professional/work claim, or the system assumption potentially affected by an external delta; the real-work or product context; the observed evidence; the relevant product/runtime environment; and the claim limit. Missing evidence in the current view is not evidence that the artifact or capability does not exist.

For an external capability delta, distinguish at least:

- `CONFIRMED_PRODUCT_CHANGE` — authoritative or otherwise strong evidence that capability/product behavior changed;
- `OBSERVED_SURFACE_CHANGE` — directly observed UI/surface behavior without sufficient evidence of underlying capability removal/addition;
- `UNVERIFIED_REPORT` — plausible report or secondary description that is not yet strong enough to drive a system change.

Do not infer architecture consequences from UI placement alone when the underlying capability remains available through another native route.

## Classify the lowest responsible mechanism

| Class | Diagnostic question | Default implication |
|---|---|---|
| `MISSING_INVARIANT_OR_CAPABILITY` | Is a material need genuinely absent after native and available professional providers are considered? | Only class that can justify new semantics; still compare no action, reuse, adapt and build. |
| `INVARIANT_NOT_ACTIVATED_OR_APPLIED` | Did an existing valid invariant/method fail to influence the work? | Repair salience, application or bounded execution; do not duplicate the invariant. |
| `INACCESSIBLE_CONTEXT_OR_CAPABILITY` | Did the needed basis/provider exist but remain unavailable or undiscovered on the actual surface? | Repair access, recovery or handoff; do not infer nonexistence. |
| `INADEQUATE_PROVIDER_OR_METHOD` | Was the chosen provider/method unable to meet the professional claim? | Select a better specialist or weaken the claim; change the registry only if recurrent evidence supports it. |
| `EVIDENCE_OR_REALITY_FAILURE` | Were current state, provenance, scope, freshness, conflict or uncertainty mishandled? | Repair the evidence basis and dependent claims. |
| `EVALUATION_OR_ASSURANCE_FAILURE` | Did review pass because it could not detect the material defect? | Replace or narrow the assurance method; do not call technical success professional fitness. |
| `PRODUCT_OR_SURFACE_LIMITATION` | Does the actual product surface lack or fail a needed transition/capability? | Use an available native route/workaround or document the limit; do not simulate a global router by default. |
| `EXTERNAL_CAPABILITY_DELTA` | Did a verified product/capability change invalidate or materially weaken an active system assumption, provider/surface choice or handoff model? | Change only the smallest dependent assumption; prefer native adaptation over custom replacement. |

If evidence supports several classes, identify the first material divergence and distinguish primary from downstream effects.

## Select the bounded response

Allowed dispositions:

- `NO_SYSTEM_CHANGE`
- `TEST`
- `LOCAL_REPAIR`
- `PROVIDER_OR_METHOD_CHANGE`
- `ACCESS_OR_HANDOFF_REPAIR`
- `EVIDENCE_REPAIR`
- `ASSURANCE_REPAIR`
- `CANDIDATE_SEMANTIC_CHANGE`
- `REOPEN_DEPENDENT_DECISION`

For external capability deltas:

- use `NO_SYSTEM_CHANGE` when the change is informational or already absorbed by native behavior;
- use `TEST` when the observed surface changed but underlying capability impact is uncertain;
- use `CANDIDATE_SEMANTIC_CHANGE` only when a verified delta invalidates an active durable assumption and the smallest adequate repair is semantic;
- use `REOPEN_DEPENDENT_DECISION` only when previously qualified state can no longer be relied on within its original claim boundary.

A `CANDIDATE_SEMANTIC_CHANGE` requires evidence that the invariant/capability is actually missing or invalidated, a smaller existing/native route is inadequate and the custom delta is likely to transfer beyond the single episode.

## External capability-delta intake

A watch, release-note scan or product observation is only a **sensor**. It does not become system state merely because it produced a report.

A delta enters the system only when it identifies a concrete dependent assumption, decision, provider/surface choice or work contract that may materially change. The output is then a compact impact record with:

1. the delta and evidence status;
2. the exact affected assumption or qualified object;
3. the materiality judgment;
4. one bounded disposition from the list above;
5. the target of any required test/change;
6. a claim limit.

Prefer an existing change object, issue, PR or bounded evidence record when persistence is needed. Do not create a standing ledger, lifecycle, router or monitoring subsystem unless repeated use demonstrates additional value.

## Minimal record

```yaml
evidence_type: genuine_use | external_capability_delta
real_work_or_product_context: required
failed_supported_or_affected_claim: required
observed_evidence: required
evidence_status: optional
environment_or_surface: optional
human_correction_or_burden: optional
failure_or_delta_class: required
responsible_mechanism_or_dependency: optional
bounded_disposition: required
target: optional
claim_limit: required
```

Persist the record only when continuity, a concrete change decision or future discrimination requires it.

## Existing method ownership

No new System-Learning or Capability-Watch Skill is justified. The existing `system-development` Skill already supplies scoped real-use validation and failure-localization methods. Native/scheduled monitoring can supply observations; this note supplies only the compact current classification and growth-control rule.

Do not automatically add a CI sentence, Skill, lifecycle, router, architecture object, reviewer, persistent state or synthetic test. Continue genuine work after the smallest supported repair and observe whether the failure recurs or the capability delta proves consequential.
