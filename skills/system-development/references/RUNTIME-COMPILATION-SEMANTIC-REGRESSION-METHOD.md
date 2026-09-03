# Runtime Compilation / Semantic Regression Method v0.2

**Status:** scoped internal System-Development method; repository promotion and installed identity are tracked separately in `CURRENT.md` and `skills/REGISTRY.md`.  
**Use when:** compiling architecture/runtime semantics into actual instructions, Project policy, Handoff contracts, tool/provider mappings or other deployment carriers.

## Method objective

Prove that a target-specific Runtime view preserves all material semantics through actual carrier constraints and bound mechanisms rather than lexical presence alone.

## Procedure

1. Fix the **canonical semantic source version**, exact target claim and target carrier/runtime context. Add the immediate qualified prior and a version-bound differential/lineage only when the claim concerns change, supersession or equivalence and those prior semantics could materially affect the target claim. Current-source-only compilation does not require a legacy inventory.
2. Record actual carrier facts: precedence, availability, field/size limits, context access, provider/tool bindings, permissions and write paths. Unknown facts remain `UNVERIFIED`.
3. For each semantic unit in the coverage inventory classify:
   - `EMBEDDED`;
   - `DELEGATED + BOUND`;
   - `EXTERNAL MECHANISM + VERIFIED`;
   - `UNVERIFIED`;
   - `NOT APPLICABLE`.
4. Require type integrity:
   `Work Function ≠ Control Operator ≠ Method ≠ Provider ≠ Surface ≠ State Carrier ≠ Boundary Contract`.
5. For delegated semantics prove the target is discoverable/accessed at the activation point; a referenced file alone is not a mechanism.
6. Verify mechanism chains where material:
   - Method need→source→fit→application→assurance;
   - Decision→Commitment→Work Basis→Authorization→Handoff→Return;
   - candidate→assurance/authority→Promotion/write→readback;
   - Human Gate→WAIT→re-entry.
7. Build and disposition a **claim-bounded semantic-obligation inventory** for the exact source and target claim fixed in step 1.
   - Include every material obligation on which the target claim depends.
   - When the source defines an enumerated normative scheme such as Interpretation Rules, Core Requirements or Conditional Requirements, or when the target claim is whole-carrier equivalence, disposition every applicable unit individually.
   - Include retired/absorbed triggers, relational invariants, historical protected functions or predecessor controls only when the fixed lineage identifies them as protected or the change/equivalence claim depends on them.
   - Record the rationale for excluded non-material classes; grouped disposition is allowed only when it cannot hide a material obligation.

   Each included unit requires its source/lineage locus, target mechanism or carrier locus, classification, static evidence, behavioral obligation where applicable, evidence identity/scope and claim limit. Clause-level embedding does not by itself establish activation of a folded trigger. Keep static source disposition and behavioral execution evidence separate. Do not recreate a legacy-complete inventory for a reduced current system when the bound claim does not depend on it.
8. Check envelope/count/hash for exact installable text.
9. Read back the actual deployed carrier before claiming installation/conformance.

## PASS rules

- **Static source coverage PASS** requires a complete inventory for the bound target claim, no omitted material obligation and no material `UNVERIFIED` unit on which that claim depends.
- **Installed-identity PASS** additionally requires envelope/hash checks and readback of the exact deployed carrier.
- **Behavioral-conformance PASS** additionally requires failure-capable execution evidence on the exact installed identity, claimed surface/path and relevant activation condition.

`EMBEDDED` is a source disposition, not behavioral evidence. A narrower PASS does not promote any wider installation, behavior, Performance, outcome or value claim.

## Failure modes

- `label = mechanism`;
- independently authored Global/Project policy forks;
- compression silently deleting relationship semantics;
- claim-bounded coverage used as a spot check that hides a material Interpretation Rule, non-equivalence, absorbed trigger or relational invariant;
- assuming Project/Skill/tool limits or availability;
- treating repository persistence as external installation;
- using a method/provider because it exists rather than because the frontier requires it.
