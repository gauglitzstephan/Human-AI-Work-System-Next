---
name: evaluate-work-product
description: Evaluate whether an identifiable existing work product is fit for a bounded recipient, intended use, or reliance claim—for example “Can I use, send, rely on, or hand this off?”. Apply claim- and failure-mode-capable evaluation, using a narrower professional method when required. Do not use primarily to create or rewrite, research, choose among wider options, diagnose runtime behavior, authorize use, or impose a default completion gate.
---

# Evaluate Work Product

Determine whether an identifiable existing work product is professionally fit for a bounded recipient, intended use, or claim. Native ChatGPT owns the work episode; this Skill owns only the evaluation transformation.

Read `references/EVALUATE-WORK-PRODUCT-METHOD.md` for substantive evaluation.

## Activation boundary

Bind the exact product and enough of its version or state to distinguish it from later changes. Bind the recipient, intended use, and evaluated claim; split materially different uses or claims.

Use a narrower professional evaluation method when it fully owns the task. If no adequate method, criteria, or evidence basis exists, return `INSUFFICIENT_BASIS` or weaken the claim.

Route elsewhere when the primary need is:

- acquiring or qualifying missing evidence → `research-evidence`;
- choosing among alternatives under wider objectives, consequences, uncertainty, or trade-offs → `decision-analysis`;
- diagnosing this system's runtime or transition behavior → `system-development`;
- creating or repairing the product → Native ChatGPT or the relevant production method.

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

Stop when enough evidence supports the bounded disposition or when missing method, criteria, or evidence prevents one. Do not continue into research, repair, decision, authorization, or outcome work without a separate task need and legitimate owner.
