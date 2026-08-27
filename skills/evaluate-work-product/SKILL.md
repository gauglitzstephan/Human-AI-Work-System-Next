---
name: evaluate-work-product
description: Evaluate, review, audit, or quality-check an identifiable existing work product—such as a report, analysis, plan, application, design, or implementation—for a stated or materially inferable recipient, intended use, or claim, including questions like “Can I rely on, use, send, or hand off this?”. Bind the product state and evaluate it with claim- and failure-mode-capable methods. Use a narrower professional evaluation Skill when it fully owns the task. Do not use primarily to create or rewrite, acquire missing evidence, choose among alternatives, diagnose system failure or runtime behavior, proofread, authorize use, or impose a default completion gate.
---
# Evaluate Work Product
Evaluate whether an identifiable existing work product is professionally fit for a bounded recipient, intended use or claim.
The Native ChatGPT runtime owns the work episode, method integration and final response. This Skill owns only the bounded evaluation transformation.
Read `references/EVALUATE-WORK-PRODUCT-METHOD.md` for substantive evaluation.
## Method
1. Bind the exact work product and enough of its version, state or context to distinguish it from later changes. Do not require formal versioning when the object is otherwise unambiguous.
2. Bind the recipient, intended use and evaluated claim. If an inference could materially change the result, state it as an assumption rather than silently fixing the use.
3. Split materially different uses or claims instead of hiding them behind one overall conclusion.
4. Select the shallowest adequate evaluation basis capable of detecting the material failure modes of the claim.
5. Use deterministic checks, authoritative requirements and qualified specialist methods before generic judgment where applicable.
6. Preserve valid properties and evidence while identifying material defects, uncertainty and limits.
7. Reach one bounded evaluation disposition per materially distinct claim or use.
8. Return findings in order of their consequence for the stated use.
## Professional-method boundary
Use a narrower professional evaluation Skill or method when it fully owns the task.
Use this Skill when its cross-domain discipline or bounded fit-for-use synthesis materially improves the evaluation. Do not turn it into a universal review method or evaluator orchestrator.
If professional validity depends on a specialist method that is unavailable, return `INSUFFICIENT_BASIS` or weaken the claim.
## Evidence boundary
Use available evidence that is adequate for the evaluation.
When acquiring, updating, reconciling or qualifying missing evidence becomes a material primary task, use `research-evidence` or another qualified research method. Do not silently expand the evaluation into open-ended research.
## Runtime and outcome boundary
Do not infer runtime behavior, transition success, use, adoption or outcome from a static artifact.
When the evaluated claim depends on runtime, transition or outcome evidence, use evidence produced by the responsible system or domain method. `system-development` owns failure localization and real-use evaluation for this Human–AI Work System.
## Comparison and decision boundary
Compare products only against the same bound use or criteria.
When the task is to choose among alternatives using goals, trade-offs, uncertainty, risk, reversibility or opportunity cost, hand off to `decision-analysis`.
A next-step implication may state the direct consequence of the evaluation. It must not become an independent option decision.
## Product identity and repair
Keep the evaluated product unchanged during its evaluation.
For a combined evaluation-and-revision request:
1. close the evaluation of the original product;
2. hand the revision to Native ChatGPT or the appropriate Writing, Coding or specialist method;
3. treat the revision as a new product state; and
4. reevaluate affected claims when needed.
Do not transfer a prior fit disposition automatically to a changed version.
## Return
Return proportionately:
- evaluated product and sufficiently identifiable state;
- recipient, intended use and evaluated claim;
- methods, criteria and decisive evidence;
- supported properties worth preserving;
- prioritized findings and their consequence for use;
- material uncertainty or missing basis;
- one evaluation disposition per materially distinct claim or use;
- direct next-step implication;
- authority and claim limits.
Present the result naturally for the user. Do not force a visible schema or process report when a concise professional evaluation is sufficient.
## Evaluation dispositions
- `FIT_FOR_STATED_USE`
- `FIT_FOR_STATED_USE_WITH_LIMITS`
- `NOT_FIT_FOR_STATED_USE`
- `INSUFFICIENT_BASIS`
These are evaluation dispositions, not Acceptance, Approval, Authorization, Commitment, execution or outcome claims.
## Stop
Stop when enough evidence exists for the bounded evaluation disposition or when the missing basis prevents one.
Do not create a new research, repair, decision, approval or governance frontier merely because further work is possible.
