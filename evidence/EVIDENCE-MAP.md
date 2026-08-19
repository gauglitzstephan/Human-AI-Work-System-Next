# Evidence Map v0.1

**Status:** WORKING INVENTORY  
**Purpose:** Define how prior work becomes usable evidence without silently becoming the new architecture.

## 1. Evidence principle

The reconstruction has substantial prior work available. That is an asset only if provenance and epistemic status are preserved.

The evidence stream therefore distinguishes:

- what was actually observed;
- what was inferred from the observation;
- what design response was attempted;
- what changed afterward;
- whether the change was causally tested;
- what scope the result can legitimately support.

A predecessor concept is not a requirement merely because it was carefully developed.

---

## 2. Primary internal evidence sources

### E1 — Predecessor repository

**Source:** `gauglitzstephan/Human-AI-Work-System`

Potential evidence:
- architecture versions and rationale;
- architecture audits and falsification attempts;
- runtime / Custom Instruction variants;
- evaluation fixtures and outputs;
- failure taxonomies;
- reference work already performed;
- rejected or superseded designs;
- commit history revealing architecture churn and repair cycles.

**Use:** harvest claims, mechanisms, evidence, and unresolved conflicts. Do not migrate the directory structure or terminology by default.

### E2 — Real Human–AI work traces

Potential evidence:
- conversations where work succeeded unusually well;
- conversations where intent was misunderstood;
- unnecessary questioning or unnecessary work;
- premature artifact production;
- excessive process/architecture activation;
- state-loss or state-conflict episodes;
- situations where human judgment or learning was displaced;
- situations where AI correctly took on work that otherwise would have been delegated back to the human.

**Use:** reconstruct work episodes and causal hypotheses. Avoid treating user dissatisfaction or preference alone as proof of a general mechanism.

### E3 — Real implemented workflows and projects

Potential evidence:
- workflows using files, repositories, external applications, automation, or persistent state;
- handoffs between AI, deterministic tooling, and humans;
- operational failures, retries, recovery, and resource limits;
- artifacts that were produced but failed in transition or use;
- successful cases where existing assets were preserved and repaired.

**Use:** test whether conceptual distinctions survive contact with real state, authority, and implementation constraints.

### E4 — Existing evaluations and benchmarks

Potential evidence:
- representative task fixtures;
- baseline comparisons;
- model/runtime comparisons;
- regression tests;
- evaluator disagreement;
- failure cases where micro-tests passed but whole-task performance did not.

**Use:** preserve reusable fixtures and results only with sufficient provenance, versioning, and scope.

### E5 — Human corrections and design decisions

Potential evidence:
- repeated corrections of the same semantic failure;
- explicit acceptance or rejection of proposed mechanisms;
- decisions made under known constraints;
- later reversals that reveal missing assumptions or changed reality.

**Use:** distinguish `human preference`, `domain truth`, `design decision`, and `empirical evidence` rather than merging them.

---

## 3. Work-episode harvest schema

Each high-information episode should be reconstructed into a compact evidence object:

```text
Episode ID
Source / date / version
Work context
Initial user intent / requested outcome
Available state and constraints
What the Human–AI system actually did
Observed success / failure
Downstream result, if known
Human correction or intervention
Competing causal explanations
Candidate mechanism(s)
Evidence strength
Transferability / boundary conditions
Architecture relevance, if any
Candidate eval fixture? yes/no
```

## 4. Architecture-artifact harvest schema

For predecessor concepts, decisions, or documents:

```text
Artifact ID
Source path / commit / date
Problem it attempted to solve
Construct / mechanism proposed
Reference basis
Internal evidence basis
What changed behaviorally, if known
Known failure / conflict / supersession
Dependencies on other concepts
Current status:
  REUSE-AS-EVIDENCE
  REFERENCE-ONLY
  CANDIDATE-FOR-RETEST
  SUPERSEDED
  REJECTED
  UNKNOWN
```

## 5. Evidence strength

Use a simple explicit scale rather than rhetorical certainty:

- **E0 — assertion:** proposed without supporting observation or reference.
- **E1 — observed:** one or more real episodes are consistent with the claim.
- **E2 — triangulated:** multiple independent episodes or external references support the mechanism.
- **E3 — tested:** a comparison or targeted test discriminates the mechanism from meaningful alternatives.
- **E4 — replicated / robust:** performance persists across representative task classes, models/conditions, or repeated use sufficient for the claim.

Evidence strength never substitutes for scope. A strong result on one task class does not automatically generalize.

---

## 6. Harvest sequence — first pass

The first harvest should be deliberately bounded and information-dense:

1. predecessor repository: current core architecture, latest runtime, architecture falsification audits, reference/coverage audits, evaluation framework;
2. 15–30 high-information real work episodes spanning radically different task classes and scales;
3. 3–5 persistent/tool-rich workflows where state, authority, recovery, or transition actually mattered;
4. existing benchmark/evaluation assets that can be reused with provenance;
5. explicit predecessor concepts that were repeatedly added, removed, or repaired.

The purpose is **not completeness**. The purpose is to expose the strongest evidence, contradictions, and alternative explanations before conceptual architecture is frozen.

---

## 7. Anti-bias rules

- Do not harvest only spectacular failures; include strong success cases and cases where the base model was already sufficient.
- Do not treat repeated terminology as repeated independent evidence.
- Do not infer causality from a better response after a prompt change without an adequate comparison.
- Preserve negative evidence and cases where additional structure reduced quality or efficiency.
- Preserve temporal order so that later design vocabulary is not projected backward onto earlier observations.
- Do not convert every failure into a new global rule; first test whether an existing capability, local method, runtime implementation, or state defect explains it.

## 8. Output of the harvest

The harvest should produce three separate outputs:

1. **Evidence corpus** — reconstructed observations with provenance.
2. **Mechanism candidate register** — possible general mechanisms with evidence status and competing explanations.
3. **Eval fixture pool** — representative episodes that can discriminate architecture alternatives.

None of these is itself the architecture.
