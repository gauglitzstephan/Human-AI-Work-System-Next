# Runtime Compilation / Semantic Regression Method v0.1

**Status:** CANDIDATE METHOD PACK  
**Use when:** compiling architecture/runtime semantics into actual instructions, Project policy, Handoff contracts, tool/provider mappings or other deployment carriers.

## Method objective

Prove that a target-specific Runtime view preserves all material semantics through actual carrier constraints and bound mechanisms rather than lexical presence alone.

## Procedure

1. Fix the **canonical semantic source version** and target carrier/runtime context.
2. Record actual carrier facts: precedence, availability, field/size limits, context access, provider/tool bindings, permissions and write paths. Unknown facts remain `UNVERIFIED`.
3. For each material semantic classify:
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
7. Regression-test all CR-01–13, CCR-01–07, historical protected functions and exact-live predecessor controls relevant to the claim.
8. Check envelope/count/hash for exact installable text.
9. Read back the actual deployed carrier before claiming installation/conformance.

## PASS rule

Deployment PASS requires **no material `UNVERIFIED` semantic that the claimed behavior depends on**. Static wording coverage is insufficient.

## Failure modes

- `label = mechanism`;
- independently authored Global/Project policy forks;
- compression silently deleting relationship semantics;
- assuming Project/Skill/tool limits or availability;
- treating repository persistence as external installation;
- using a method/provider because it exists rather than because the frontier requires it.
