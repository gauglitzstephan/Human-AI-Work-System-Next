# Δ4 Evidence Correction v0.1

**Status:** CORRECTION / PR #2 INVALID FOR MERGE  
**Date:** 2026-08-19  
**Scope:** `architecture/delta-04-adaptive-work-control` / PR #2  

## 1. Correction

The current Δ4 branch used an invalid historical comparison and must not be merged.

The specific error was treating the earlier `v0.3.4` whole-task/runtime acceptance as if it established a sufficiently complete pre-B.6 architecture baseline against which the later Professional Work / B.6 line could be evaluated as mostly redundant.

That inference is false.

## 2. Why the inference is invalid

### v0.3.4 acceptance was scoped

The historical whole-task result accepted v0.3.4 **within the tested suite**. It did not establish complete professional-work quality coverage, universal behavioral adequacy, or architectural sufficiency.

Later work explicitly discovered failure dimensions not adequately represented/evaluated by that acceptance boundary.

### The Quality Architecture was a material subsequent development

`Human–AI Work Quality Architecture Review v0.2` accepted a conceptual architecture direction with:

- Professional Excellence;
- Human–AI Collaboration + Human Agency;
- Governance;
- cross-cutting Assurance;
- Outcome Realization kept horizontal;
- Net Value / Proportionality cross-cutting.

It explicitly used failures such as S-Payment where:

```text
claim/source/technical/process QA PASS
+
recipient-level professional communication FAIL
```

as evidence that prior evaluation/quality framing was insufficient.

### The Architecture Falsification Audit further reopened weighting

The audit judged the system:

> direction basically right, materially misweighted

with under-modeling/under-evaluation of:

- expert cognition and tacit knowledge;
- professional taste / recipient judgment;
- sensemaking / situation awareness;
- cognitive-function allocation;
- reflective professional practice;
- comparative Human-only / AI-only / Human–AI performance;
- Human capability effects of delegation.

This means older runtime success cannot be treated as a complete control condition for later architecture.

### B.6 was downstream synthesis, not merely a redundant controller overlay

The Professional Work Spine B.6 candidate explicitly incorporated as conditional/cross-cutting mechanisms:

- Situation / Reality Model;
- Professional Performance Model;
- Reference + Reuse;
- Decision / Commitment events;
- Work Graph / Work Units;
- Professional Refinement / next-use maturity;
- Human–AI allocation;
- Integrity / Quality / Assurance;
- selective reopening / local recovery;
- Outcome Realization.

It also hardened claim-bound Qualification and introduced the Semantic Compiler as a prospective hypothesis within that richer Professional Work synthesis.

Therefore a valid Δ4 review cannot compare:

```text
old v0.3.4 success
vs
B.6 Semantic Compiler
```

as if everything except the Compiler were controlled.

## 3. Invalid claims on this branch

The following branch-level claims are **retracted**:

- that v0.3.4 whole-task success is evidence that most later B.6 work-control semantics were already behaviorally sufficient;
- that the recovered pre-B.6 evidence is enough to carry the conservative Δ4 closure decision;
- that the full Semantic Compiler should be demoted based on the A/B/C framing currently used in PR #2;
- that the proposed thin metapolicy is the only surviving incremental B.6 control contribution;
- that no further lineage reconstruction is required before Δ4 can be judged.

The external references on metareasoning, Robust Decision Making and real options may remain useful source material, but **their architectural placement inference on this branch is not qualified**.

## 4. What remains valid

The following higher-level bootstrap decisions from `main` are unaffected:

- Qualified Prior designs are closed-but-reopenable;
- architecture object types must remain distinct;
- no peer `Work Engine` layer is accepted by default;
- Δ1–Δ3 remain the provisional bootstrap dispositions recorded on `main`;
- Δ4 remains genuinely open;
- runtime effectiveness remains a separate evidence claim.

No Δ4 commit from PR #2 has been merged to `main`.

## 5. Correct Δ4 starting point

A corrected Δ4 must first recover the **actual mature predecessor state and development lineage**, especially:

```text
pre-v0.3.4 Core/runtime
→ v0.3.4 scoped whole-task acceptance
→ professional-quality failures / Work Product failures
→ Quality Architecture
→ Architecture Falsification Audit
→ Professional/Cognitive Work investigation
→ Professional Performance / Refinement / Maturity work
→ B-series / B.6 convergence
→ prospective B.6 canaries
→ Core v0.5 / Runtime v0.6.x integration and salience history
```

The valid question is then not:

> Did old Work Architecture already do most of B.6?

It is:

> Within the **mature qualified B.6/Core-v0.5 lineage**, what architectural responsibility is genuinely carried by adaptive work-control / Semantic Compiler semantics, what is carried by Professional Work/Performance/Qualification/Orchestration more generally, and which parts should survive into Next under the new parent architecture?

That is a lineage-preserving reconciliation problem, not an ablation against an earlier incomplete runtime.

## 6. Disposition

```text
PR #2 current Δ4 decision basis:     INVALID
ADR-0002 proposed closure:           RETRACTED
Delta-04 ablation design:            NOT AUTHORIZED AS CURRENT GATE
main bootstrap baseline:             UNAFFECTED
Δ4 status:                           OPEN
next action:                         RECOVER MATURE B.6 LINEAGE BEFORE JUDGMENT
```
