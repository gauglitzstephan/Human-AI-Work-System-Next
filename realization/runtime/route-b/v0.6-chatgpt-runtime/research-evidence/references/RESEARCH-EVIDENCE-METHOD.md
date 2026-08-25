# Research & Evidence Method v0.1

## Purpose

Produce an evidence basis sufficient for a bounded professional claim, decision, design or diagnosis without drowning the working context in irrelevant material.

Research is justified only when missing evidence can materially change the supported frontier. It is not a mandatory preliminary phase.

## 1. Bind the research mission

Establish only what is needed:
- parent claim/decision/intended use;
- exact research question(s);
- current known state and uncertainty;
- evidence type, freshness and coverage required;
- consequence of being wrong;
- stop condition.

Distinguish questions of fact, mechanism, magnitude, causality, forecast, preference/judgment and current provider/product state because they require different evidence.

## 2. Build an evidence strategy

Choose the smallest source set capable of answering the claim. Prefer, as applicable:

1. direct authoritative state/readback for current system or account facts;
2. primary sources, official documentation, standards, filings, datasets or original research;
3. high-quality independent synthesis or replication;
4. qualified expert/practitioner evidence for tacit or operational knowledge;
5. community/experience evidence where user experience, edge cases or sentiment matter;
6. secondary summaries only when primary evidence is unavailable or unnecessary.

Use mechanism-distinct or independent sources when a single source class can share the same blind spot. Do not equate source count with diversity.

For fast-changing claims, explicitly search for recent authoritative evidence and compare publication date with event/effective date. For historical or stable claims, prioritize authority and methodological fit over recency.

## 3. Search and retrieve progressively

Start with high-signal queries tied to the question, then branch only when evidence reveals a material gap, contradiction or alternative hypothesis.

Use progressive disclosure:
- inspect titles/snippets/metadata first;
- open only promising sources;
- retrieve the minimum relevant section;
- expand when context is necessary to avoid misinterpretation.

Do not load an entire corpus merely because it exists.

Actively seek:
- counterevidence;
- rival mechanisms;
- boundary conditions;
- known failures/limitations;
- evidence that would falsify the current leading hypothesis.

## 4. Qualify each material source

For claims that matter, evaluate enough of:
- authority / authorship;
- provenance / original vs derived;
- publication and effective date;
- scope/population/context;
- methodology and measurement validity;
- incentives/conflicts of interest;
- independence from other cited evidence;
- applicability/transfer distance;
- uncertainty and known limitations.

Provider documentation is authoritative for provider behavior but not automatically for independent performance claims. Company claims are primary evidence of what the company states, not independent proof of impact.

## 5. Reconstruct current reality

When evidence conflicts, do not average it away. Determine whether the conflict is caused by:
- different dates/versions;
- different scopes/definitions;
- different methods/populations;
- stale vs current state;
- measurement error;
- genuine disagreement or uncertainty.

Prefer direct current readback for current-state claims when available. Historical authoritative records remain historical unless evidence shows they are still current.

## 6. Synthesize by claim, not by source

Organize the result around the question/decision rather than summarizing sources one by one.

Separate:
- established facts/observations;
- supported inferences;
- assumptions/hypotheses;
- judgments;
- forecasts/scenarios;
- unresolved conflicts/unknowns.

Explain the mechanism connecting evidence to the conclusion where material. Preserve the strongest counterevidence and boundary conditions.

## 7. Calibrate confidence and decision relevance

Confidence depends on evidence quality, consistency, coverage, method fit and uncertainty—not writing fluency or source volume.

State what the evidence supports, what it does not support, and whether additional information has meaningful decision value.

If uncertainty remains but the decision is reversible/robust, prefer bounded action or scenario treatment over endless research. If a non-compensatory evidence floor is unmet, weaken the claim or WAIT/HANDOFF/STOP.

## 8. Stop rule

Stop when one of these applies:
- the evidence basis is sufficient for the intended claim/decision;
- new sources are no longer changing the conclusion or material uncertainty;
- remaining uncertainty is better handled by robustness/scenarios/reversibility;
- the evidence cannot be obtained with available capability/access;
- information value is below research/delay cost.

Do not continue research to create the appearance of thoroughness.

## 9. Return contract

Return a compact evidence basis containing only material items:

```yaml
research_question: required
supported_findings: required
key_evidence_and_provenance: required
material_counterevidence_or_conflicts: optional
uncertainty_and_limits: optional
implication_for_parent_claim_or_decision: required
remaining_high_value_evidence: optional
```

The return is evidence, not decision/authority.

## Failure modes to detect

- source selection driven by confirmation bias;
- stale/current-state confusion;
- secondary-source cascade with no primary grounding;
- false diversity from many sources repeating one origin;
- provider marketing treated as independent validation;
- correlation or association promoted to causality;
- evidence-slice scope collapse;
- contradictory evidence silently omitted;
- excessive context/research that reduces reasoning quality;
- research completion mistaken for decision readiness.

## Method provenance

Derived from Requirements v0.2 CR-03/04/05/10/11/13 and the Route-B Core Work Functions/Method Contract, informed by current OpenAI guidance favoring lean prompts and representative validation and current context-engineering practice emphasizing progressive disclosure and finite context. This method is a Candidate professional method until validated on representative research work.