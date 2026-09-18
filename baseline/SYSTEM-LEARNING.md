# System Learning

**Status:** CURRENT on authoritative `main`; CANDIDATE off `main`.  
**Role:** Narrow reusable discipline, not a runtime controller, lifecycle, automatic learner or new Skill.

## Purpose

Learn from material genuine-use evidence **and material external capability/product changes** without converting every defect or release note into permanent system growth.

Use this when observed work evidence, a material candidate/use decision or a product/capability delta could change the working setup. Verify uncertain external changes before relying on them. Routine successful work and ordinary product news need no record.

## Bind the event

State the failed or supported professional/work claim, or the system assumption potentially affected by an external delta; the real-work or product context; the observed evidence; the relevant product/runtime environment; and the claim limit. Missing evidence in the current view is not evidence that the artifact or capability does not exist.

For an external capability delta, distinguish at least:

- `CONFIRMED_PRODUCT_CHANGE` — authoritative or otherwise strong evidence that capability/product behavior changed;
- `OBSERVED_SURFACE_CHANGE` — directly observed UI/surface behavior without sufficient evidence of underlying capability removal/addition;
- `UNVERIFIED_REPORT` — plausible report or secondary description that is not yet strong enough to drive a system change.

Do not infer architecture consequences from UI placement alone when the underlying capability remains available through another native route.

## Classify supported causal contributions

| Class | Diagnostic question | Default implication |
|---|---|---|
| `MISSING_INVARIANT_OR_CAPABILITY` | Is a material need genuinely absent after native and available professional providers are considered? | Compare no action, reuse, adapt and build; absence is one reason to consider a semantic change, not the only route to an adequate intervention. |
| `INVARIANT_NOT_ACTIVATED_OR_APPLIED` | Did an existing valid invariant/method fail to influence the work? | Compare application or execution repair with other adequate mechanisms when recurrence warrants it; do not merely duplicate an already valid invariant. |
| `INACCESSIBLE_CONTEXT_OR_CAPABILITY` | Did the needed basis/provider exist but remain unavailable or undiscovered on the actual surface? | Repair access, recovery or handoff; do not infer nonexistence. |
| `INADEQUATE_PROVIDER_OR_METHOD` | Was the chosen provider/method unable to meet the professional claim? | Compare a better provider/method, a changed mechanism or narrower use; change the registry only when the supported durable need warrants it. |
| `EVIDENCE_OR_REALITY_FAILURE` | Were current state, provenance, scope, freshness, conflict or uncertainty mishandled? | Repair the evidence basis and dependent claims. |
| `EVALUATION_OR_ASSURANCE_FAILURE` | Did review pass because it could not detect the material defect? | Replace or narrow the assurance method; do not call technical success professional fitness. |
| `PRODUCT_OR_SURFACE_LIMITATION` | Does the actual product surface lack or fail a needed transition/capability? | Use an available native route/workaround or document the limit; do not simulate a global router by default. |
| `EXTERNAL_CAPABILITY_DELTA` | Did a verified product/capability change invalidate or materially weaken an active system assumption, provider/surface choice or handoff model? | Change only affected dependencies sufficiently to restore the required performance; prefer adequate native adaptation over custom replacement. |

If evidence supports several classes, distinguish the first observed divergence, causal contributions and intervention choice. Ordering does not make downstream or independent contributions disposable; repair them together when needed. A source/installed version difference is a deployment defect only against a justified operating target, not simply the newest repository candidate.

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

Select the smallest sufficiently effective response by required performance, recurrence, consequences, uncertainty and total burden, including Human correction. Representation and ownership do not prove adequacy. A `CANDIDATE_SEMANTIC_CHANGE` needs a supported missing, invalidated or materially inadequate mechanism/assumption, credible alternatives and a custom delta likely to transfer beyond the episode. Do not require exhaustion of a fixed ladder of smaller patches or predetermine a controller.

Use `TEST` proportionately for causal localization, change/regression verification or qualification before consequential use. The latter two do not require prior damage or an unknown cause. Fix the decision, failure-capable criteria and stopping boundary first; retain observed failures and claim limits.

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

Do not automatically add a CI sentence, Skill, lifecycle, router, architecture object, reviewer, persistent state or synthetic test. Verify affected claims and material regressions after the smallest sufficiently effective repair, then continue genuine work within the qualified boundary and observe recurrence or capability impact.
