# ADR-0004 — Requirements Baseline v0.3 Promotion Candidate

**Status:** PROPOSED — source formed for Human acceptance review; no Acceptance, Promotion or merge authorized by this record  
**Date:** 2026-08-28  
**Decision owner:** Human repository owner  
**Current authority:** ADR-0003 and Requirements v0.2 remain controlling until an explicit later decision, authorized merge and `main` readback

## Context

Requirements v0.2 was accepted and promoted through ADR-0003. It remains the current controlling solution-neutral Requirements baseline.

Subsequent professional-work and genuine-use evidence exposed two material semantics that had remained too implicit:

- actual Work execution / Work-Product fidelity and legitimate closure;
- Human–AI interaction and coordination integrity, including reliance calibration, Human-facing usability/accessibility and controlled feedback/adaptation.

The v0.3 Candidate preserves the valid v0.2 families, consolidates duplicated packaging, adds CR-15 Work execution / Work-Product fidelity and, after the bounded Interaction Gap Challenge, adds CCR-05 plus localized CR-05, CR-07 and CR-14 strengthening.

Qualified Candidate evidence includes:

- `evidence/REQUIREMENTS-v0.2-to-v0.3-RECONCILIATION-v0.1.md`;
- `evidence/REQUIREMENTS-v0.3-INTERACTION-GAP-CHALLENGE-v0.1.md`;
- `reviews/REQUIREMENTS-v0.3-TARGET-ARCHITECTURE-v0.2-COMPATIBILITY.md`;
- `reviews/REQUIREMENTS-v0.3-INTERACTION-REPAIR-TARGET-ARCHITECTURE-v0.2-ADDENDUM-v0.1.md`;
- `reviews/REQUIREMENTS-v0.3-RUNTIME-v0.6-SEMANTIC-TRACE-AND-PROMOTION-READINESS-v0.1.md`.

The Runtime trace establishes that promoted Route-B v0.6 source preserves most v0.3 semantics but is not fully compiled against the repaired Candidate. This does not invalidate the Requirements design; it requires an explicitly separate Runtime-Compilation repair and prevents any Runtime-conformance claim from being inferred from Requirements Promotion.

## Proposed decision

If the Human later accepts the mature promotion object and separately authorizes the final promotion write/merge, the proposed decision is to:

1. adopt `foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md` as the controlling solution-neutral Requirements baseline;
2. retain Requirements v0.2 immutably as historical Qualified Prior and supersede it only in the controlling role;
3. retain Target Architecture v0.2 as controlling and closed:
   - the base and interaction-repair compatibility reviews remain the current Requirements↔Architecture trace;
   - no architecture semantic change or reopen is accepted;
4. classify `foundation/CONCERNS-AND-REQUIREMENTS-v0.3-CANDIDATE.md` as promoted Candidate lineage rather than a second controlling source;
5. declare promoted Runtime v0.6 only partially compiled against Requirements v0.3 until a separate Runtime-Compilation PR, source readback, deployment update and installed-carrier readback establish narrower claims;
6. authorize no Runtime/UI installation, external action, architecture change or outcome claim through the Requirements decision itself.

## Proposed accepted baseline

```text
3 Interpretation Rules
15 Core Requirements
5 Conditional Requirements
central non-equivalences
```

The v0.3 packaging has 23 top-level normative elements versus 26 in v0.2. The reduction is consolidation, not removal of valid professional, reality, authority, continuity, assurance or conditional-risk semantics.

## Acceptance boundary

Acceptance would mean only:

> Requirements v0.3 is sufficiently coherent, solution-neutral, lineage-reconciled, externally challenged and compatible with Target Architecture v0.2 to serve as the next controlling Requirements Design Basis.

Acceptance would not establish:

- Runtime-v0.6 conformance to v0.3;
- installed Global or Project carrier identity;
- generalized Skill activation or fitness;
- Human–AI synergy, cross-domain completeness or outcome effectiveness;
- any UI, provider, Agent, Skill, state-store or workflow topology;
- a Target-Architecture reopen.

## Promotion dependencies

Before a merge decision, the promotion package must:

1. preserve exact v0.3 Candidate semantics in the proposed baseline;
2. contain the v0.2→v0.3 reconciliation, Interaction Gap Challenge and Runtime semantic trace;
3. retain a complete Requirements↔Architecture owner trace with no reopen trigger;
4. state the Runtime-v0.6 partial-compilation gap without treating it as a Requirements blocker;
5. repair action-bearing version/count references that would otherwise remain stale after Promotion;
6. present the exact final `CURRENT.md`, README/navigation and supersession state;
7. receive explicit Human Acceptance and separate merge authorization;
8. after merge, read back `main` and reconcile all material entry points.

## Current disposition

```text
semantic Candidate maturity       READY_FOR_HUMAN_ACCEPTANCE
Requirements Promotion            NOT AUTHORIZED
repository merge                  NOT AUTHORIZED
Target Architecture reopen        NOT TRIGGERED
Runtime v0.6 conformance           NOT ESTABLISHED
Runtime-Compilation repair         REQUIRED AS SEPARATE PACKAGE
UI/installed-carrier update        NOT AUTHORIZED
```

This ADR remains `PROPOSED` until the legitimate decision owner explicitly accepts the decision and authorizes the corresponding promotion path.
