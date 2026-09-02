# Evaluation Strategy v0.1

**Status:** PROVISIONAL

## Purpose

Evaluation is not a final QA step. It is the mechanism that determines which architectural claims deserve to survive.

## Claim classes

Keep these distinct:

1. **Conceptual coherence** — the architecture is internally consistent and covers stated concerns.
2. **Behavioral performance** — a realized system produces better work on representative tasks.
3. **Efficiency / economics** — improvement is worth the added model, tool, human, latency, and coordination cost.
4. **Human–AI performance** — the composition improves quality without unjustified loss of agency, learning, authorship, or responsibility.
5. **State / authority integrity** — the system does not invent current state, access, completion, or authorization.
6. **Transition / in-use performance** — outputs survive handoff, implementation, adoption, or operation where those are part of the intended outcome.
7. **Robustness** — performance survives relevant variation, changed state, uncertainty, and failure.

Passing one class does not imply another.

## Baseline conditions

For material behavioral claims, compare against meaningful alternatives. Candidate conditions include:

- capable base model with no Human–AI Work System layer;
- base model plus task-local tools / references;
- minimum architecture candidate;
- predecessor runtime / architecture where reproducible;
- richer candidate architecture;
- deterministic or existing-process baseline where appropriate;
- human-only or expert-human baseline where the claim concerns Human–AI composition.

The baseline should represent the best realistic alternative, not an intentionally weak control.

## Task portfolio

Evaluation must span heterogeneous work rather than architecture-specific micro-prompts. Candidate classes include:

- trivial bounded task;
- ambiguous request requiring intent reconstruction;
- existing artifact repair;
- evidence-grounded research;
- open strategic decision;
- quantitative/data analysis;
- multi-tool / external-state work;
- persistent workflow;
- learning/authorship-sensitive work;
- authority-sensitive or difficult-to-reverse action;
- future-uncertain decision;
- work product requiring downstream transition or recipient fit.

Use real or faithfully reconstructed work episodes where possible.

## Outcome measures — candidate set

Depending on task and claim:

- professional outcome / work-product quality;
- critical error rate;
- unsupported or false claims;
- false completion;
- missed requirements;
- unnecessary work / unnecessary clarification;
- human correction burden;
- elapsed turns / tool calls / tokens / latency / compute cost;
- state-recovery success;
- decision quality or calibration;
- recipient / next-use fitness;
- transition or implementation success;
- human learning, authorship, agency, or acceptance where material.

Do not optimize the system to easily measurable proxies when they fail to represent the intended outcome.

## Evaluation methods

Use the simplest adequate combination of:

- deterministic checks for mechanically verifiable constraints;
- blinded model grading for bounded qualitative criteria, with calibration;
- human/domain-expert judgment when expertise or receiving-context judgment is essential;
- pairwise or ranking evaluation when absolute scoring is unreliable;
- task-specific end-state checks;
- execution traces for state, tool, authority, and stopping behavior;
- repeated runs where model variance is material.

Human review counts as assurance only when the reviewer has the context and capability to detect the relevant defect.

## Ablation

When a richer architecture outperforms a simpler one, remove or disable mechanism families to determine which parts actually cause the gain.

A component that adds conceptual elegance but no discriminable performance should be considered for demotion to knowledge/reference or capability-local use.

## Regression and negative evidence

Preserve cases where additional structure makes performance worse. A new mechanism must not be promoted solely because it fixes one failure if it creates larger regressions elsewhere.

## Promotion rule

A mechanism should move toward accepted architecture only when the evidence supports:

- a material concern;
- a plausible mechanism;
- adequate transferability;
- performance or control benefit for its claimed scope;
- acceptable complexity and work economics;
- no known non-compensatory regression for the intended use.

## Kill / simplification rule

If a complex candidate does not materially outperform a smaller architecture or a simpler external workflow on representative work, the complexity is not justified. Preserve useful theory as Knowledge Capital, but do not keep it in the runtime or architectural kernel by inertia.
