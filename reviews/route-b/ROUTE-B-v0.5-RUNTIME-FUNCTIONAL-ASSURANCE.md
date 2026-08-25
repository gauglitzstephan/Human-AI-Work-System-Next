# Route B v0.5 — Runtime Implementation Functional Assurance

## Verdict

**INSTALLATION BLOCK REMAINS UNTIL THIS REPAIR IS PROMOTED.**

**STATIC FUNCTIONAL COMPLETENESS AFTER REPAIR: PASS WITH RUNTIME-ONLY UNCERTAINTY.**

The prior `STATIC CARRIER-FIDELITY PASS` remains valid only for its stated semantic/packaging scope. This review reopens the merged Runtime Candidate because that prior assurance did not establish functional completeness or actual runtime behavior.

No Source or Target-Architecture reopen trigger was found.

## Review scope

Evaluate the complete composition:

- Global Custom Instructions;
- System Development Project Instructions;
- `work-formation` Skill and resources;
- method discovery/realization;
- Native Primary ownership and Subagent composition;
- activation/selection and progressive disclosure;
- known Route-B failure modes;
- Chat/Work and Project/non-Project paths;
- actual installability.

## External provider facts used

Dated 2026-08-25:

- OpenAI Projects documentation: Project Instructions apply only within the Project and override Global Custom Instructions.
- OpenAI Skills documentation: installed Skills can be used automatically when helpful; Skills may include instructions, examples, supporting resources and code.
- OpenAI Skills documentation: Personal Skills must be added separately on desktop and web/mobile and do not automatically synchronize across those surfaces.
- OpenAI Work documentation: Chat is the conversational surface; Work is designed for longer multi-step work and finished deliverables.

These are provider facts, not Route-B authority. Recheck only when a material platform/surface delta invalidates them.

## Findings

### F1 — Adapter acceptance was incompletely realized

**Original merged implementation: FAIL. Repaired on this branch.**

The accepted Adapter Definition requires explicit path identities, one semantic owner per responsibility, surface-specific Skill identity handling, mixed-runtime prevention and dated platform-fact lifecycle. The merged candidate lacked an implementation manifest covering these responsibilities.

Repair:

- `realization/runtime/route-b/v0.5-chatgpt-runtime/RUNTIME-IMPLEMENTATION-MANIFEST.yaml`

This does not create a runtime precedence engine or registry; it records the exact Candidate composition and unresolved installation state.

### F2 — Skill activation metadata was too abstract for robust selection

**Original merged implementation: FUNCTIONAL RISK / NOT ADEQUATELY ASSURED. Repaired statically; runtime behavior remains unverified.**

The previous description used mainly system-internal terms (`claim`, `transition`, `Work Basis`). Skills are selected for relevance before their full instructions/resources are applied, so activation metadata must map reliably to real user/work situations without making all complex work a trigger.

Repair:

- revised `work-formation/SKILL.md` description with concrete positive/negative relevance;
- explicit positive triggers in the Skill;
- `references/ACTIVATION-BOUNDARY-EXAMPLES-v0.5.md` for ambiguous boundaries and re-entry calibration.

Runtime activation precision/recall cannot be truthfully established without installed representative tests.

### F3 — Progressive disclosure lacked explicit resource-loading rules

**Original merged implementation: PARTIAL. Repaired.**

The Skill had two correct canonical references but no explicit rule for when to load which resource. That left a risk of either overloading context or failing to load method semantics when needed.

Repair in `SKILL.md`:

- Formation Method: always on substantive Formation activation;
- activation examples: only for ambiguous activation/re-entry/Probe boundaries;
- Core Work Functions/Method Contract: only when function/method eligibility is materially unresolved;
- Sparse Work Basis schema: only when a structured return materially helps handoff/continuity/verification.

### F4 — Structured Formation return had no reusable machine-readable resource

**Original merged implementation: GAP, not Source defect. Repaired.**

The canonical Formation source defines a Sparse Work Basis but the Skill package did not expose it as a directly reusable resource.

Repair:

- `references/SPARSE-WORK-BASIS-SCHEMA-v0.5.yaml`

The schema is explicitly optional and cannot become a mandatory form/process artifact.

### F5 — No executable script is required by the current mechanism

**KEEP / NO REPAIR.**

The Formation function is semantic judgment: determine claim-relative sufficiency, identify the material missing basis/method class, then terminate. No identified correctness property is improved by deterministic code at this layer. Adding a script merely to resemble other Skills would add mechanism and maintenance without a supported failure it solves.

If later evidence identifies a deterministic property (for example a package-validation or schema-validation need) that materially reduces failure, add code at that lowest responsible layer then.

### F6 — Professional method realization remains complete by design, not by embedding a universal library

**PASS STATIC; RUNTIME EXECUTION UNVERIFIED.**

The Core Method Contract defines:

`Work Function + Intended Use + Performance Floor + Domain + Evidence Need → eligible Professional Method(s)`

The Runtime resolution order remains:

1. already-qualified Domain Skill/Method Pack;
2. fit repository Method Registry pack;
3. other qualified Project/Drive/repository source;
4. current authoritative external method/standard;
5. transparent bounded task-local method with limitations;
6. qualified Human/specialist.

If none is adequate, readiness/claim is weakened or work waits/handoffs/stops. Generic model plausibility does not substitute for professional validity.

This is the intended quality mechanism; copying all domain methods into `work-formation` would be a Method-monolith failure.

### F7 — Native ChatGPT integration is topologically correct, behavior still unverified

**PASS STATIC / UNVERIFIED RUNTIME.**

- Native Primary remains planning/tool/Subagent/wait/integration/final-answer owner.
- Formation terminates before professional method execution.
- Global/Project carriers do not reproduce Spawn/Wait/Synthesis/permission orchestration.
- Project Instructions are a complete alternative Kernel carrier because they override Global inside the Project.
- Work is treated as a comparative execution surface, not a lifecycle stage.

Actual provider behavior after installation remains a runtime claim and must be tested.

### F8 — Known failure modes now have explicit runtime tests

**STATIC TESTABILITY: PASS; CLOSURE IN USE: UNVERIFIED.**

Added:

- `realization/runtime/route-b/v0.5-chatgpt-runtime/RUNTIME-VALIDATION-MATRIX.md`

It covers Hidden Formation Controller, Method Monolith, native-capability duplication, over-delegation, context fragmentation, stale-world integration, false independent assurance, Human capability/authority erosion, process-success/outcome-failure and control ratchet, plus immediate kill criteria.

### F9 — Cross-surface behavior cannot be certified before installation

**UNVERIFIED BY NATURE, NOT A STATIC DEFECT.**

Personal Skill installation/identity is surface-specific. Each of Non-Project Chat, Non-Project Work, Project Chat and Project Work is independently claimed only after exact Skill availability/install/readback and representative behavior on the target surface.

No silent Global-/Project-CI-only fallback is allowed for materially underformed work if the Formation Skill is unavailable.

### F10 — Actual installability is conditional, not yet executed

**INSTALLATION-DECISION READY AFTER REPAIR PROMOTION, subject to two direct target-UI facts at cutover.**

The repository package will be ready to attempt installation once this repair is merged. The remaining checks are not design work:

1. the target Project UI accepts the prepared Project Instructions payload;
2. the target surface allows installation/readback of the exact `work-formation` Skill package.

At cutover, prevent legacy `material-work-entry` and `work-formation` from being co-active on the same claimed path. Retain only the immediately replaced state needed for practical rollback; no historical reconstruction program is required.

A successful paste/upload is installation evidence only. Runtime behavior remains unverified until the validation matrix is exercised.

## Assurance by requested lens

| Lens | Result after repair |
|---|---|
| Functional completeness | PASS STATIC; runtime behavior unverified |
| Activation/selection | strengthened and statically coherent; requires runtime cases |
| Progressive disclosure | PASS STATIC |
| Professional-method realization | PASS STATIC; JIT execution unverified |
| Native ChatGPT integration | PASS STATIC topology; behavior unverified |
| Known-failure closure | test mechanisms present; real closure unverified |
| Cross-surface behavior | UNVERIFIED until surface-specific install/test |
| Actual installability | decision-ready after repair merge; two direct UI facts at cutover |

## Supported next state

After this repair is reviewed and merged:

> Route-B v0.5 Runtime Candidate is ready for a **bounded live installation attempt and runtime validation**, not Runtime Promotion.

No further pre-install Source/Architecture expansion is supported by current evidence.

## Disposition

**PROMOTION GATE — MERGE FUNCTIONAL-ASSURANCE REPAIR; THEN INSTALL/TEST.**
