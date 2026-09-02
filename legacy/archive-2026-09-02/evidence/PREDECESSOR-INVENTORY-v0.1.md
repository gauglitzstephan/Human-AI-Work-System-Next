# Predecessor Evidence Inventory v0.1

**Source repository:** `gauglitzstephan/Human-AI-Work-System`  
**Snapshot date:** 2026-08-19  
**Status:** FIRST-PASS INVENTORY — not yet a full harvest

## 1. Why this source matters

The predecessor repository is a high-value evidence corpus because it contains not only a current architecture but also historical versions, runtime candidates, falsification work, real-use canaries, references, and explicit uncertainty about what has or has not been behaviorally established.

It is also a potential source of inheritance bias. The inventory therefore records source material without granting its current ontology privileged status.

---

## 2. Repository-level observations

The predecessor root currently contains at least these major areas:

- `architecture/`
- `capabilities/`
- `core/`
- `decisions/`
- `evaluation/`
- `knowledge/`
- `project/`
- `references/`
- `runtime/`

The current README describes five repository layers — Core, Knowledge Capital, Capability/Product Reality, Runtime Deployment, and Evaluation/Learning — while also describing a current Core v0.5 candidate and a B.6 Professional Work projection.

**Harvest implication:** prior layer names and boundaries are evidence about design evolution, not a template for the new architecture.

---

## 3. Priority source set A — current integrated state

Read early because these documents define the latest predecessor belief state.

| Priority | Source | Harvest question |
|---|---|---|
| A1 | `README.md` | What does the predecessor currently claim, distinguish, and explicitly leave unproven? |
| A2 | `architecture/context-package-v0.4.md` | What is the latest integrated architecture map and how are concepts related? |
| A3 | `core/work-lifecycle.md` | Which lifecycle semantics are treated as domain-independent? |
| A4 | `core/dynamic-work-model.md` | What dimensions/views were required to represent work? |
| A5 | `core/work-graph.md` | What problem does graph structure solve and at what unit? |
| A6 | `core/orchestration-model.md` | How is work selection/control currently represented? |
| A7 | `core/realization-model.md` | How are artifact, transition, use, outcome, and value separated? |
| A8 | `runtime/global-ci-v0.6.2-salience-repaired-candidate.md` | Which semantics were compressed into the latest runtime, and what was lost/restored? |

---

## 4. Priority source set B — falsification and negative evidence

These are especially important because they challenge the predecessor rather than merely explain it.

| Priority | Source | Known relevance |
|---|---|---|
| B1 | `evaluation/architecture-falsification-audit-v0.1.md` | Explicitly treats repo as current belief rather than truth; identifies misweighting toward lifecycle/state/governance and under-modeling of expertise, cognition, taste, comparative Human–AI performance, and learning effects. |
| B2 | `evaluation/runtime-v0.6.1-historical-salience-regression-audit-v0.1.md` | Evidence that compilation/compression can lose behaviorally important older semantics. |
| B3 | `evaluation/runtime-v0.6.2-historical-salience-coverage-review-v0.1.md` | Evidence for restoration and remaining salience/coverage questions. |
| B4 | `evaluation/runtime-semantic-coverage-contract-v0.1.md` | Existing attempt to control function loss across runtime changes. |
| B5 | human-facing / room / coordination pilots under `evaluation/` | Evidence that structural separation and handoffs can add cost without independent review or better work. |

---

## 5. Priority source set C — behavioral and real-use evidence

The `evaluation/` directory contains real-use canaries and operational pilots in addition to synthetic tests. First-pass visible examples include:

- `bewerbung-2026-b6-canary-checkpoint-01.md`
- `bewerbung-2026-b6-canary-checkpoint-02.md`
- `bewerbung-2026-bergfreunde-recovery-canary-01.md`
- `bewerbung-2026-operational-ledger-pilot-m1.md`
- `behavioral-evaluation-v0.1.md`
- `adaptive-decision-quality-test-v0.1.md`
- `b6-system-snapshot-2026-08-19.md`

The predecessor README explicitly labels recent positive Quality-in-Use observations as useful evidence **but not a controlled benchmark**.

**Harvest implication:** preserve the episodes and their evidence strength; do not convert qualitative improvement reports into causal claims.

---

## 6. Priority source set D — architecture evolution

The predecessor contains multiple architecture and context-package generations, including:

- `architecture/context-package-v0.1.md`
- `architecture/context-package-v0.2.md`
- `architecture/context-package-v0.3.md`
- `architecture/context-package-v0.3.1.md`
- `architecture/context-package-v0.4.md`
- `architecture/human-ai-work-quality-architecture-proposal-v0.1.md`
- `architecture/human-ai-work-quality-architecture-proposal-v0.2.md`
- `architecture/human-ai-work-quality-architecture-proposal-v0.3.md`
- `architecture/end-to-end-reference-diff-v0.1.md`
- `architecture/b6-architecture-integration-candidate-v0.1.md`

**Harvest question:** which changes were driven by external reference discovery, which by observed failures, which by conceptual cleanup, and which have demonstrated behavioral consequences?

Do not read history only as progress. Look for reversals, recurring concepts under new names, and complexity that may have migrated between layers.

---

## 7. Priority source set E — runtime evolution as natural experiment

The runtime directory records a useful design sequence:

- `global-ci-v0.3.2.md`
- `global-ci-v0.3.3-solution-space-candidate.md`
- `global-ci-v0.3.4-consolidated-candidate.md`
- `global-ci-v0.3.5-work-object-product-repair-candidate.md`
- `global-ci-v0.3.6-coverage-preserved-candidate.md`
- `global-ci-v0.3.7-work-product-maturity-candidate.md`
- `global-ci-v0.4.0-architecture-aligned-candidate.md`
- `global-ci-v0.4.1-architecture-aligned-coverage-preserved-candidate.md`
- `global-ci-v0.4.2-decision-frame-integrity-candidate.md`
- `global-ci-v0.4.3-boundary-integrity-candidate.md`
- `global-ci-v0.5.0-recomposed-candidate.md`
- `global-ci-v0.5.1-grounded-recomposed-candidate.md`
- `global-ci-v0.6.0-b6-semantic-compiler-candidate.md`
- `global-ci-v0.6.1-uncertainty-aware-candidate.md`
- `global-ci-v0.6.2-salience-repaired-candidate.md`

The predecessor README identifies `v0.3.6` as the last accepted thin historical baseline and `v0.6.2` as the current integrated candidate.

**Harvest implication:** treat runtime history as a quasi-experimental sequence, but do not infer causality from version order. Recover the intended delta, test evidence, regressions, and user-visible effect for each material transition.

---

## 8. Initial predecessor hypotheses to re-test

These are **not carried forward as accepted architecture**:

1. professional work needs semantics beyond prompt/task completion;
2. current/authoritative state must be distinguished from working context and reusable knowledge;
3. input, requirement, decision, authorization, implementation, transition, use, outcome, and value require non-equivalent semantics where material;
4. preserving and repairing existing work often dominates regeneration;
5. assurance must be claim-bound and detection-capable;
6. Human–AI composition should be based on comparative capability and authority rather than collaboration ideology;
7. a next-state / minimum-sufficient-work control mechanism may provide a useful general work-selection abstraction;
8. global runtime salience is scarce and can be degraded by semantic accumulation;
9. architecture was likely misweighted toward governance/state relative to cognition, expertise, craft, and work performance;
10. visible process and multi-room/multi-agent structure can create coordination cost without better assurance.

Each hypothesis must be mapped to external references, internal episodes, alternatives, and a prospective architectural placement before promotion.

---

## 9. Next predecessor harvest unit

The next pass should extract a structured evidence matrix from the eight A-sources and five B-sources first. For each source capture:

`problem → reference basis → mechanism → architectural placement → evidence → counterevidence → dependencies → current confidence → candidate disposition`.

Only after that should the reconstruction decide which predecessor concepts deserve deeper re-testing.
