# Evidence Map v0.2

**Status:** WORKING INVENTORY / LINEAGE-CORRECTED  
**Purpose:** Define how prior work becomes usable evidence or qualified inherited design without silently becoming the new architecture and without forcing repeated rediscovery.

---

## 1. Evidence principle

The reconstruction has substantial prior work available. That is an asset only if provenance, status and **design maturity** are preserved.

The prior corpus is not one homogeneous evidence bucket.

Keep distinct:

```text
raw observation
≠ design hypothesis
≠ qualified prior design
≠ implementation/runtime evidence
≠ accepted architecture
≠ external validation
```

A predecessor concept is not a requirement merely because it was carefully developed. Equally, an accepted reference-grounded and falsified predecessor design is not reset to zero merely because a new repository was created.

---

# 2. Internal evidence / design status classes

## I0 — Raw internal evidence

Examples:
- real work traces;
- user corrections;
- failures / near misses;
- output or transition defects;
- implementation incidents;
- observed successful patterns.

Use: causal/mechanism hypotheses and representative eval fixtures.

## I1 — Design hypothesis / candidate

Examples:
- candidate architecture;
- unaccepted HAPS/PAWS/AMM family claim;
- proposed lifecycle or semantic object;
- conceptual synthesis without accepted closure.

Use: compare alternatives; do not inherit as default.

## I2 — Qualified Prior Design

A bounded prior design with sufficiently explicit:
- scope / System of Interest;
- reference/rationale basis;
- alternatives/failure analysis;
- review/falsification;
- human acceptance;
- limitations / reopen conditions.

Use: **closed-but-reopenable prior**. Recover and map first. Reopen only with an explicit trigger.

## I3 — Implementation / runtime evidence

Examples:
- installed or runnable mechanisms;
- canary evidence;
- platform/access behavior;
- runtime regressions;
- state/recovery incidents;
- performance and cost observations.

Use: test whether conceptual semantics survive realization and ordinary use.

## I4 — Superseded / rejected / counter-design

Examples:
- GitHub-first persistence later rejected;
- heavy registry designs replaced by bounded manual storage;
- deliberately thin PAOS alternatives;
- failed or retired runtime architectures.

Use: negative evidence and architecture alternatives. Do not discard merely because superseded.

---

# 3. Primary internal sources

## E1 — Predecessor architecture lineage

**Sources include at least:**

- `AI-native-Operating-Model`;
- `human-ai-work-architecture`;
- `Human-AI-Work-System`;
- `PAOS`;
- `Personal-AI-Operating-Model`;
- `personal-ai-workspace-system`;
- `Persistence-System`;
- `PAW`;
- additional relevant repos discovered through lineage audit.

Potential evidence/design:
- accepted architecture versions and rationale;
- architecture audits / falsification;
- simplified counter-designs;
- runtime and integration variants;
- persistence/state/governance experiments;
- reference work already performed;
- rejected or superseded designs;
- commit history revealing churn, repair and convergence.

**Use:** classify each material artifact as I0–I4 before synthesis. Do not treat the immediate predecessor as the whole lineage.

See `PREDECESSOR-LINEAGE-REUSE-AUDIT-v0.1.md`.

## E2 — Real Human–AI work traces

Potential evidence:
- unusually strong work;
- intent misunderstanding;
- unnecessary questioning/work;
- premature artifact production;
- process/architecture overactivation;
- state-loss/conflict;
- displaced Human judgment/learning;
- cases where AI correctly completed work without needless relay to the Human.

Use: reconstruct episodes and causal hypotheses. User dissatisfaction/preference alone is not proof of a universal mechanism.

## E3 — Real implemented workflows and projects

Potential evidence:
- files, repositories, external apps, automation, persistent state;
- Human/AI/tool handoffs;
- operational failures/retries/recovery/resource limits;
- produced artifacts that failed transition/use;
- successful preservation/repair of existing assets.

Use: test conceptual semantics against real state, authority and implementation constraints.

## E4 — Existing evaluations and benchmarks

Potential evidence:
- representative fixtures;
- baseline comparisons;
- model/runtime comparisons;
- regression tests;
- evaluator disagreement;
- micro-test vs whole-task failures;
- architecture scenario evaluations and acceptance records.

Use: preserve with provenance, scope and construct validity.

## E5 — Human corrections and design decisions

Potential evidence:
- repeated semantic corrections;
- explicit accept/reject decisions;
- known constraints;
- reversals revealing missing assumptions or changed reality.

Use: distinguish Human preference, domain truth, architecture authority, acceptance and empirical evidence.

---

# 4. Work-episode harvest schema

```text
Episode ID
Source / date / version
Work context
Initial Human intent / requested outcome
Available authoritative state / constraints
What the Human–AI system actually did
Observed success / failure
Downstream result, if known
Human correction / intervention
Competing causal explanations
Prior mechanism(s) already intended to handle this failure?
Candidate mechanism(s)
Evidence strength
Transferability / boundary conditions
Architecture relevance
Candidate eval fixture? yes/no
```

The added `Prior mechanism` field is mandatory for material architecture learning: do not invent a new mechanism before checking whether the failure is an implementation, salience, activation, state, or conformance defect in an existing one.

---

# 5. Architecture / prior-design harvest schema

```text
Artifact / Decision ID
Repository / source path / commit / date
System of Interest / scope
Prior status: I1 | I2 | I3 | I4
Problem / concern
Construct / mechanism / architecture decision
External reference basis
Internal evidence basis
Alternatives / counter-designs considered
Validation / falsification performed
Human acceptance / authority state
Known failure / conflict / supersession
Reopen conditions
Dependencies
Current external-evidence delta
Current real-use delta
Reopen trigger now? yes/no
Disposition:
  RETAIN
  RETAIN-WITH-BOUNDARY
  REFINE
  RELOCATE
  MERGE
  SUPERSEDE
  REJECT
  OPEN-CONFLICT
Novel delta, if any
```

---

# 6. Evidence strength

Use an explicit evidence scale for empirical claims:

- **E0 — assertion:** proposed without supporting observation or reference.
- **E1 — observed:** one or more real episodes are consistent with the claim.
- **E2 — triangulated:** multiple independent episodes or external references support the mechanism.
- **E3 — tested:** comparison or targeted test discriminates meaningful alternatives.
- **E4 — replicated / robust:** performance persists across representative task classes, models/conditions, or repeated use sufficient for the claim.

Do not confuse this empirical scale with design acceptance status. An architecture can be accepted as a bounded design decision while many real-world performance claims remain unvalidated.

---

# 7. Corrected harvest sequence

The old first-pass sequence started too late in the lineage.

Use this sequence instead:

1. **Lineage recovery** — inventory relevant prior repositories and canonical/accepted/candidate states.
2. **Qualified-prior reconciliation** — extract the highest-value accepted architecture decisions, scope, reference basis, validation and reopen conditions.
3. **Counter-design recovery** — preserve deliberately simpler, rejected or superseded alternatives such as PAOS and persistence corrections.
4. **Current real-use/runtime evidence** — map recent canaries, failures and state/platform observations against prior mechanisms.
5. **External delta research** — search only where evidence changed, prior sources were weak, or an open conflict remains.
6. **Representative episode/eval harvest** — use cases that can discriminate remaining alternatives rather than reproduce prior tests.

The purpose is not completeness. It is to expose **where prior knowledge is still valid and where the real unresolved decision frontier begins**.

---

# 8. Anti-bias / anti-rediscovery rules

- Do not harvest only spectacular failures; include strong success and base-model-sufficient cases.
- Do not treat repeated terminology as independent evidence.
- Do not infer causality from a better response after a prompt change without adequate comparison.
- Preserve negative evidence where added structure reduced quality/efficiency.
- Preserve temporal order.
- Do not convert every failure into a new global rule; check existing mechanism, implementation, state and activation first.
- **Do not re-derive a qualified accepted prior merely to make the new repo self-contained.** Summarize/link it and reopen only with cause.
- **Do not prefer the newest vocabulary.** Prefer the best-supported mechanism and clearest boundary.
- **Do not equate old with superseded.** Status must be established, not assumed from age.

---

# 9. Outputs of the lineage-aware harvest

1. **Prior Architecture Reconciliation Matrix** — accepted/candidate/counter-design lineage with current disposition.
2. **Evidence corpus** — reconstructed observations with provenance.
3. **Mechanism candidate/conflict register** — only genuinely unresolved mechanisms.
4. **Eval fixture pool** — representative episodes capable of discriminating live alternatives.

None is itself the new architecture.
