# Work Product Evaluation Method v0.2
**Status:** cross-domain evaluation discipline; not a universal professional evaluation methodology.
## Purpose
Determine whether an identifiable intermediate or final work product supports a bounded recipient, intended use, handoff, readiness or reliance claim using methods capable of detecting its material failure modes.
## 1. Bind the evaluation object
Establish only as far as needed:
- the exact work product;
- a sufficiently identifiable version, state or context;
- the recipient or intended use;
- the evaluated claim;
- the required professional quality;
- relevant criteria;
- material failure modes;
- the available evidence.
Formal versioning is not required when the product is otherwise unambiguous.
If materially different recipients, uses or claims could produce different conclusions, separate them.
If an inferred use could materially alter the conclusion, make the inference explicit. Do not silently convert an underspecified review into a readiness claim.
## 2. Resolve the professional evaluation basis
Prefer, as applicable:
1. authoritative requirements or acceptance criteria;
2. qualified domain or professional evaluation methods;
3. recipient and intended-use requirements;
4. validated references, exemplars or benchmarks;
5. transparent task-local criteria with stated limitations.
Use a narrower professional evaluation Skill or method when it fully owns the task.
Do not substitute a generic checklist for expertise, craft, representative use or a specialist method when these materially determine validity.
If no adequate evaluation basis can be established, return `INSUFFICIENT_BASIS` or support only a weaker claim.
## 3. Select only the required evaluation operations
Possible operations include:
### Conformance and verification
Check requirements, factual consistency, calculations, traceability, deterministic behavior or other verifiable properties.
### Professional validity
Assess whether the work uses adequate professional methods, reasoning, completeness, judgment and craft for the claim.
### Recipient and intended-use fit
Assess whether the product is relevant, understandable, appropriately mature and usable in the receiving context.
### Robustness and failure challenge
Test material edge cases, counterexamples, alternative interpretations, fragile assumptions or likely failure modes.
These are selectable operations, not mandatory stages.
## 4. Route work that belongs elsewhere
### Evidence acquisition
Use available adequate evidence directly. When obtaining or qualifying missing evidence becomes a material task, native research or another qualified specialist research method owns that transformation.
### Comparative work
Products may be compared against the same bound criteria. Choosing among alternatives under wider trade-offs belongs to `decision-analysis`.
### Runtime, transition and outcome claims
Consume qualified runtime, transition or outcome evidence from the responsible method. Do not infer it from static wording and do not perform generic system-runtime diagnosis inside this method.
### Creation and repair
Do not rewrite the product during its evaluation. Writing, Coding or another production method owns the changed version.
## 5. Apply evaluator controls
- Prefer deterministic checks and authoritative references where applicable.
- Evaluate specific properties before reaching an overall disposition.
- Do not equate length, polish, fluency or process conformity with professional quality.
- Treat rationale as reasoning, not as proof.
- Preserve conflicts, uncertainty and unsupported claims.
- Do not treat a second model pass as independent merely because it is separate.
- Require additional independence only when correlated or self-confirming error is material.
- Do not use generic quality scores as a substitute for claim-relative evaluation.
- Do not hide material disagreement behind consensus language.
- Preserve already-supported properties when defects are local.
## 6. Form findings
Express each material finding as:
```text
observation or evidence
→ affected criterion or claim
→ consequence for the stated use
→ uncertainty or boundary
→ optional repair direction
```

Prioritize findings by their effect on responsible reliance, not by presentation order.

A repair direction identifies what property must change. It does not rewrite the product or choose among materially different repair routes.

## 7. Preserve product identity

The evaluation applies only to the bound product state.

For a combined evaluation-and-repair request:

1. finish the original evaluation;
2. transfer revision work to the responsible production method;
3. bind the resulting product as a new state;
4. preserve only evidence that still applies to unchanged properties; and
5. reevaluate affected claims.

A fit disposition does not transfer automatically across revisions.

## 8. Reach an evaluation disposition

Reach one semantic disposition for each materially distinct claim or use.

FIT_FOR_STATED_USE

Evidence supports responsible reliance for the bound use. Ordinary nonmaterial limitations do not require a separate qualification.

FIT_FOR_STATED_USE_WITH_LIMITS

The product supports the bound use only under an explicit scope limit, condition, safeguard, qualification or restricted reliance.

NOT_FIT_FOR_STATED_USE

A material defect prevents responsible reliance for the bound use.

This does not mean the product is globally worthless, irreparable or unfit for every other use.

INSUFFICIENT_BASIS

Available criteria, method or evidence cannot support a responsible fit conclusion.

This is an evaluation disposition, not a negative fit conclusion.

## 9. Return the result

Return proportionately:

* product and identifiable state;
* recipient, intended use and evaluated claim;
* evaluation basis and decisive evidence;
* supported properties;
* prioritized findings;
* uncertainty and limitations;
* disposition for each materially distinct claim or use;
* direct implication for reliance, revision, specialist evaluation or additional evidence;
* authority boundary.

Use the structure as a semantic content contract, not as a mandatory visible format.

The direct implication must follow from the evaluation. It must not become an independent decision among wider options.

## 10. Stop rule

Stop when:

* the material failure modes have been examined sufficiently for the claim;
* enough evidence exists for the bounded disposition;
* remaining uncertainty is immaterial or represented by explicit limits; or
* missing evidence or method prevents a stronger conclusion.

This method stops at the evaluation boundary. The native episode may continue into research, repair, decision, authorization or outcome work when separately needed and legitimately owned; this method must not absorb those transformations or become a default completion gate.
