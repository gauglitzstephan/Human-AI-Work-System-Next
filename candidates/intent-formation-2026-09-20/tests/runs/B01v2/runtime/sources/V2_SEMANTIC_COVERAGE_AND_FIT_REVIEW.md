# V2 Semantic Coverage & Fit Review

**Evaluated products:**

- `INTENT_FORMATION_WORKER_SEMANTIC_CONTRACT_v2.md`
- `INQUIRY_STATE_SCHEMA_v2.md`

**Bound intended use:** canonical semantic source for building a testable reference carrier and extending the adversarial dialogue pack.  
**Not evaluated here:** behavioral performance, installed Project conformance, outcome improvement or deterministic persistence.

## 1. Evaluation basis

The authoritative basis is:

1. `intent-outcome-clarification-architecture-v1.md` and `INQUIRY_STATE_SCHEMA_v1.md` for preserved structural obligations;
2. `intent-formation-orientation-architecture-reopening-brief-v0.1.md` for the accepted Formation & Orientation architecture;
3. `intent-formation-worker-requirements-completeness-audit-v0.1.md` for R1–R8 and the freeze criteria;
4. `goal-vision-alignment-requirements-addendum-v0.1.md` for Intent Architecture and Outcome Logic;
5. the explicit user constraints and adoptions represented in those sources.

Evaluation operations: source-coverage trace, type-integrity review, legal-transition review, boundary challenge and schema parse check.

## 2. Claim-bounded semantic-obligation inventory

| ID | Material obligation | V2 mechanism / locus | Disposition | Claim limit |
|---|---|---|---|---|
| O01 | Single-worker topology | Contract §§2, 4, 15 | `EMBEDDED` | logical architecture only |
| O02 | Evidence distinct from current interpretation | Contract §§2, 4; Schema `evidence_ledger` | `EMBEDDED` | persistence not guaranteed |
| O03 | Versioned defeasible state | Schema `formation_case`, `revision_log` | `EMBEDDED` | atomicity not claimed |
| O04 | Provenance, confidence, contradiction, rejection and supersession | `ClaimSemantics`, invariants 1, 6, 7 | `EMBEDDED` | calibration not claimed |
| O05 | User/external/AI/joint authority separation | Contract §5; `authority_plane` | `EMBEDDED` | runtime adherence untested |
| O06 | Understanding ≠ grounding ≠ adoption ≠ commitment | Contract §5; `ClaimSemantics`; transition table | `EMBEDDED` | grounding remains qualitative |
| O07 | Intent can be formed, not only extracted | Contract §1; Taste, Frame and Advice views | `EMBEDDED` | quality effect untested |
| O08 | Local, scoped Taste and substantive-fit criteria | Contract §6.4; Schema `taste_and_quality` | `EMBEDDED` | no global personality inference |
| O09 | User Agency with material challenge and guidance | Contract §§5, 6.2, 9.4 | `EMBEDDED` | no autonomous normative authority |
| O10 | Clearly labelled provisional recommendation | Contract §§6.8, 9.4; `advisory_assessments` | `EMBEDDED` | advisory calibration untested |
| O11 | Advice does not become intent without adoption | Contract §§2, 5, 9.4; invariants 2–5 | `EMBEDDED` | behavioral leakage untested |
| O12 | Parent Outcome stable but revisable | Contract §8; `parent_control`; legal transitions | `EMBEDDED` | trigger recognition untested |
| O13 | Parent Outcome as role in Outcome Network | Contract §6.3; Schema `intent_architecture` | `EMBEDDED` | no exhaustive goal graph |
| O14 | Purpose/Vision/Outcome/Means/Output/Signal separation | Contract §6.3; typed nodes; invariant 9 | `EMBEDDED` | Vision explicitly optional |
| O15 | End-to-end contribution logic | `contribution_hypotheses`; Alignment Gate | `EMBEDDED` | causal proof not claimed |
| O16 | Vertical, causal, horizontal, temporal, proxy and authority alignment | Contract §9.5; `alignment_view` | `EMBEDDED` | material subset only |
| O17 | Stop unproductive abstraction | Contract §9.5 | `EMBEDDED` | qualitative materiality judgment |
| O18 | General Contribution Contract for every substantive candidate | Contract §§6.10, 9.1; `candidate_moves[].contribution_contract` | `EMBEDDED` | policy execution untested |
| O19 | Formative structural/causal analysis allowed | Contribution Contract with `FORM`/`ORIENT` | `EMBEDDED` | option trade-off analysis blocked |
| O20 | Formative Orientation Research narrowly allowed | Contract §9.2; typed unknowns and research control | `EMBEDDED` | actual source quality untested |
| O21 | Downstream solution research deferred | Contract §§6.10, 9.2; research resolvability | `EMBEDDED` | relies on gate adherence |
| O22 | Diagnostic option/feasibility probes quarantined | Contract §9.3; `diagnostic_only`; invariant 10 | `EMBEDDED` | no candidate ranking allowed |
| O23 | Assumptions, constraints, signposts and controllability | Contract §6.6; Schema `assumptions_and_constraints` | `EMBEDDED` | no formal causal inference |
| O24 | Stakes, reversibility and urgency parameterize depth | Contract §6.1; `reliance_context` | `EMBEDDED` | no numerical risk engine |
| O25 | Decision rights and affected parties | Contract §6.2; `actors_and_authority` | `EMBEDDED` | specialist ethics review not replaced |
| O26 | Claim-specific evidence/advice fitness | Contract §§6.7–6.8; source-fitness metadata | `EMBEDDED` | verification depends on sources |
| O27 | One highest-value next intervention | Contract §10; `policy_control` | `EMBEDDED` | optimality/calibration not claimed |
| O28 | At most one substantive question by default | Contract §10.3 | `EMBEDDED` | bounded elicit–provide–elicit allowed |
| O29 | Context compilation excludes stale/rejected noise | Contract §13; minimal compiled view | `EMBEDDED` | retrieval reliability untested |
| O30 | Sufficiency relative to named intended use | Contract §9.6; Schema `sufficiency` | `EMBEDDED` | behavioral threshold untested |
| O31 | Typed Intent Contract handoff | Contract §11; Schema `intent_contract` | `EMBEDDED` | downstream receipt untested |
| O32 | Controlled re-entry without wholesale reset | Contract §12; invariant 13 | `EMBEDDED` | cross-chat behavior untested |
| O33 | Honest mapping to ChatGPT Project constraints | Contract §15 | `EMBEDDED` | current product facts need carrier-stage verification |
| O34 | Architecture reopen only on material structural evidence | Contract §16 | `EMBEDDED` | user/system authority still governs reopening |

No material source obligation for the bound claim remains `UNVERIFIED` at the static semantic level.

## 3. Failure challenges performed

| Challenge | Examination | Result |
|---|---|---|
| Advice contamination | Trace unacknowledged `AI` advice toward user-owned Outcome | Blocked by separate advisory view, authority plane, invariants 2–5 and legal transition table |
| Parent volatility | Trace ordinary local correction toward Parent replacement | Blocked by `parent_control`, review triggers and owner-confirmation transition |
| Parent ossification | Introduce broken load-bearing assumption/context shock | Expressible through trigger references, `UNDER_REVIEW` and confirmed supersession |
| Research leakage | Classify a vendor/strategy search as orientation | Fails `purpose=ORIENT` and the orientation-output restriction; remains downstream |
| Question-only failure | Present an entrenched harmful assumption | Advice/Challenge Gate permits bounded directional intervention |
| Taste substitution | AI proposes polished quality criterion | Remains `AI/NOT_ADOPTED` until explicit adoption or reformulation |
| Output-as-outcome | User requests an artifact or optimizes a metric | Typed node plus vertical/forward/proxy checks prevent silent promotion |
| Local optimization | Current Outcome conflicts with sibling/longer horizon | `CONFLICTS_WITH`, horizontal and temporal alignment can represent the issue |
| Handoff reframing | Downstream worker discovers infeasibility | Recorded trigger requires `REENTER`; silent overwrite prohibited |
| Schema pseudo-completeness | All fields populated but live material frontier remains | `residual_formation_value` and intended-use gate still block readiness |

## 4. Defects found and repaired during review

1. **Candidate-level Contribution Contract:** the initial schema placed one contract at policy level, although every substantive candidate must be classifiable. It now lives under each `candidate_move`, with the selection referencing a `candidate_id`.
2. **Parent review traceability:** the initial schema had Parent lifecycle on nodes but no compact control object for triggers and candidate replacements. `parent_control` now owns that transition state.
3. **Evidence type ambiguity:** `EVIDENCE` as an Outcome Network node could be confused with the Evidence Ledger. Both artifacts now state that the node is an outcome indicator; the ledger carries state basis.
4. **AI-role cardinality:** permitted AI roles are now a list rather than an accidental single-choice field.
5. **Handoff lineage:** the Intent Contract now records its own version and the Formation State version from which it was derived.

Affected properties were reinspected after repair. No new static contradiction was found.

## 5. Deterministic checks

- All Markdown files are present and non-empty.
- All fenced YAML blocks parse successfully as YAML.
- No `TODO`, `TBD`, `FIXME` or placeholder marker remains.
- Contract and schema contain explicit loci for authority, grounding, Parent review, Contribution Contract, Orientation Research, Diagnostic Probe, Advice, Alignment, Sufficiency, Handoff and Re-entry.

## 6. Fitness disposition

**Static semantic-source claim: `FIT_FOR_STATED_USE_WITH_LIMITS`.**

The two V2 artifacts are fit to serve as the canonical semantic source for a reference runtime carrier and an expanded adversarial evaluation pack. Their structure covers the accepted requirements without adding a new agent, store or general decision layer.

The limit is material: static coverage does not establish behavioral gate adherence, Project installation, cross-chat persistence, intervention optimality or outcome improvement. Those claims require a carrier-bound semantic regression check and failure-capable dialogue executions.

## 7. Immediate implication

Freeze these artifacts as **V2 semantic candidate 2.0**. The next legitimate step is to derive an uncompressed reference carrier, extend the adversarial pack with paired gate cases, and test behavior before compressing the final Project Instructions.
