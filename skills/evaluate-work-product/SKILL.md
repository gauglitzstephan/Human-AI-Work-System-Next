---
name: evaluate-work-product
description: Evaluate whether an identifiable intermediate or final work product is fit for a bounded recipient, intended use, handoff, readiness, or reliance claim—standalone or inside a larger Work episode when fitness materially affects the next step. Apply claim- and failure-mode-capable evaluation, using a narrower professional method when required. The Skill owns only the evaluation transformation; do not use for ordinary production without a material fitness claim or as a default completion gate.
---

# Evaluate Work Product

Determine whether an identifiable existing work product is professionally fit for a bounded recipient, intended use, handoff, readiness, or reliance claim. Native ChatGPT owns the work episode; this Skill owns only the evaluation transformation.

Read `references/EVALUATE-WORK-PRODUCT-METHOD.md` for substantive evaluation.

## Activation boundary

Bind the exact intermediate or final product and enough of its version or state to distinguish it from later changes. Bind the recipient, intended use, handoff, readiness, or reliance claim; split materially different uses or claims.

The product may arise inside a larger research, design, planning, production, or execution episode. Dedicated evaluation is eligible when fitness for the bound claim materially affects the next step. Ordinary production without such a material fitness or reliance need does not trigger evaluation automatically.

Use a narrower professional evaluation method when it fully owns the task. If no adequate method, criteria, or evidence basis exists, return `INSUFFICIENT_BASIS` or weaken the claim.

Keep adjacent transformations with their current owners:

- acquiring or qualifying missing evidence → native research or a qualified specialist research method;
- choosing among alternatives under wider objectives, consequences, uncertainty, or trade-offs → `decision-analysis`;
- diagnosing this system's runtime or transition behavior → `system-development`;
- creating or repairing the product → Native ChatGPT, native Work, or the relevant production method.

## Essential invariants

- Use claim- and failure-mode-capable methods, deterministic checks, and authoritative requirements where applicable.
- Keep the evaluated product unchanged during evaluation.
- For evaluation plus revision, close the original evaluation first; the revision is a new product state whose affected claims may require reevaluation.
- Preserve supported properties while prioritizing defects by consequence for the stated use.
- Do not infer runtime performance, transition success, use, adoption, or outcome from a static artifact.
- Do not equate polish, fluency, length, process conformity, or a generic score with professional fitness.
- Treat an evaluation disposition as neither approval nor authorization.

## Return

Return proportionately: product/state; recipient, intended use, and claim; evaluation basis and decisive evidence; supported properties; prioritized findings and their consequence; uncertainty or missing basis; one disposition per materially distinct claim/use; direct next implication; and authority limits.

Present the result naturally. Do not force a visible schema when a concise professional evaluation is sufficient.

## Dispositions

- `FIT_FOR_STATED_USE`
- `FIT_FOR_STATED_USE_WITH_LIMITS`
- `NOT_FIT_FOR_STATED_USE`
- `INSUFFICIENT_BASIS`

These are evaluation dispositions, not Acceptance, Approval, Authorization, Commitment, execution, or outcome claims.

## Stop

Stop this transformation when enough evidence supports the bounded disposition or when missing method, criteria, or evidence prevents one. Do not absorb research, repair, decision, authorization, or outcome work merely because the native episode continues, and do not turn evaluation into a universal completion gate.
