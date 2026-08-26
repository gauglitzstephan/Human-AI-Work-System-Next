---
name: decision-analysis
description: Analyze a sufficiently bounded material choice with identifiable object, owner, outcome and decision level, even if viable alternatives still need to be formed. Compare options—including no action, delay, staged commitment or a reversible test—using objectives, constraints, consequences, uncertainty, risk, trade-offs, reversibility, opportunity cost and information value. Use for “Which option should I choose?”, “Should I proceed, wait, test, park or stop?”, or “What would change the recommendation?”. Do not use merely to compare work products against the same recipient, intended use or criteria; use evaluate-work-product. Do not use when the decision itself, intended outcome, decision level or required method class is materially unformed; use work-formation. Do not use primarily to acquire evidence, explore an unformed space, create an execution plan, make a routine low-consequence choice, or authorize, commit to or execute an action. Use a narrower professional decision method when it fully owns the domain.
---

# Decision Analysis

Develop a responsible recommendation for a bounded material choice.

The Native ChatGPT runtime owns the work episode, method integration and final response. This Skill owns only the bounded decision-analysis transformation.

Read `references/DECISION-ANALYSIS-METHOD.md` for substantive analysis.

## Method

1. Bind the exact material decision, Decision Owner, authority boundary, horizon and current state.
2. Bind intended outcomes, hard constraints, preferences, means and materially affected parties without inventing Human values or stakeholder weights.
3. Select the shallowest adequate decision regime based on stakes, time pressure, reversibility, complexity and the structure of uncertainty.
4. Form a viable option set at the correct decision level, including status quo, no action, delay, staged commitment, reversible tests or adaptive options where relevant.
5. Exclude options that fail genuine hard constraints. Do not disguise preferences as constraints.
6. Consume qualified evidence, forecasts and work-product evaluations without taking over their professional methods.
7. Select only the decision operations and formal tools capable of changing or testing the recommendation.
8. Compare consequences, trade-offs, downside, opportunity cost, dependencies, path dependence, reversibility and material distributional effects.
9. Distinguish adequately characterizable risk from model uncertainty and deep uncertainty. Prefer robustness, adaptability and preserved options when precise optimization is not defensible.
10. Challenge the leading option against its strongest credible rival and identify the material switching condition.
11. Determine whether additional information or a reversible test has positive decision value after accounting for delay and acquisition cost.
12. Return one bounded analytical recommendation or state why no responsible recommendation is supported.

## Professional-method boundary

Use a narrower qualified decision method when it fully owns the domain or when validity depends on specialist models, standards or judgment.

Examples may include investment underwriting, clinical shared decision-making, legal strategy, safety engineering, formal cost-benefit analysis, portfolio optimization or regulated risk decisions.

Do not stretch this cross-domain discipline into a universal professional decision methodology. If the required method is unavailable, return `INSUFFICIENT_BASIS` or support only a weaker recommendation.

## Evaluation and comparison boundary

Use `evaluate-work-product` to determine how one or more identifiable work products support the same bound recipient, intended use or criteria, including which version better supports that same use.

Use this Skill only when choosing among alternatives materially depends on wider objectives, consequences, uncertainty, risk, opportunity cost, reversibility or trade-offs beyond same-use product fit.

Consume qualified evaluation dispositions as evidence. Do not silently reevaluate the work products or treat product fit as sufficient proof that an option should be chosen.

## Evidence boundary

Use available adequate evidence directly.

When acquiring, updating, reconciling or qualifying missing evidence becomes a material primary task, use `research-evidence` or another qualified research method.

Decision Analysis may identify the exact information or test that could change the recommendation. It must not silently expand into open-ended research.

## Formation and exploration boundary

Decision Analysis owns forming a viable option set once the decision object, Decision Owner, intended outcome and material decision level are sufficiently bound. The options do not need to be fully enumerated in advance.

Use `work-formation` only when missing basis could materially change whether the decision exists, what outcome is sought, which decision level is legitimate or which professional method class is required.

Do not route ordinary option formation to Formation. Do not force an unformed opportunity or exploration space into premature ranking.

## Planning and execution boundary

A recommendation may include its direct decision implication, material condition, safeguard or revisit trigger.

Creating an implementation roadmap, project plan or operating workflow belongs to Native Planning or the relevant specialist method.

Recommendation is not decision acceptance, commitment, authorization, execution or outcome.

## Human authority

Use stated or adequately supported Human goals, preferences, constraints and risk tolerances.

If an inferred preference, constraint, obligation or risk tolerance could materially change the recommendation, expose it as an assumption and make the recommendation conditional. Do not silently fix it.

Request Human input only when the missing contribution is genuinely non-substitutable. A recommendation does not constitute Human acceptance, commitment, authorization, execution or outcome.

## Return

Return proportionately:

- the bound decision, Decision Owner, horizon and authority boundary;
- intended outcomes, hard constraints, material assumptions and affected parties;
- viable alternatives at the same decision level;
- the selected decision regime and method, when material;
- decisive evidence and qualified upstream evaluations;
- consequences, trade-offs, downside, opportunity cost and distributional effects;
- uncertainty, robustness, reversibility and lost or preserved options;
- the strongest credible rival and the condition that would switch the recommendation;
- the value of additional information or a reversible test;
- one analytical disposition and the named recommended option, if supported;
- conditions, safeguards, signposts, falsifiers or revisit points;
- claim and authority limits.

Present the result naturally. Do not force a scorecard, decision matrix or visible process report when a concise recommendation is professionally sufficient.

## Dispositions

- `RECOMMEND_OPTION` — one option is robustly preferable for the bound decision.
- `RECOMMEND_OPTION_WITH_CONDITIONS` — one option is preferable only under named conditions, safeguards or limits.
- `RECOMMEND_REVERSIBLE_TEST` — a bounded reversible test has greater decision value than immediate commitment. State the decision-relevant uncertainty and evidence threshold, not a full test plan or authorization to execute it.
- `RECOMMEND_DEFER` — waiting for a named event, condition or information gain is preferable and the cost of delay remains acceptable. Uncertainty alone does not justify deferral.
- `RECOMMEND_NO_ACTION` — no action or continuation of the status quo is preferable for the bound horizon.
- `NO_ROBUST_PREFERENCE` — the basis is adequate, but no option remains robustly preferable or the result depends materially on unresolved preferences.
- `INSUFFICIENT_BASIS` — evidence, method or non-substitutable Decision-Owner input is inadequate for a responsible recommendation.

Each disposition must name the relevant option, condition or missing basis.

These are analytical recommendations, not Human acceptance, commitment, authorization, execution or outcome claims.

## Stop

Stop when:

- one option is sufficiently supported for the bounded decision;
- a conditional or reversible route responsibly contains the remaining uncertainty;
- additional information has greater decision value than its cost and delay;
- no material preference among viable options is supported;
- missing evidence, preferences or specialist method prevents a recommendation; or
- no material decision is required.

Do not continue into research, product evaluation, planning, implementation, authorization or governance merely because further work is possible.
