# End-to-End Human–AI Work Architecture Candidate v0.1

**Status:** CANDIDATE — static / architectural completeness candidate; not accepted baseline, runtime deployment, or behavioral claim.  
**Date:** 2026-08-20  
**Scope:** general professional Human–AI work from incomplete real-world input to the correct outcome / learning / closure boundary.  
**Requirements basis:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` (CR-01–13, CCR-01–07).  
**Accepted parent baseline:** `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`.  
**Historical evidence basis:** qualified prior architecture/runtime/evaluation material from `Human-AI-Work-System`, `human-ai-work-architecture`, and this repository.

## 1. Claim and boundary

This candidate makes one bounded claim:

> The architecture contains an owner/mechanism for every material transformation and control relation currently required by CR-01–13, CCR-01–07, and the reviewed historical real-use failure families, with no currently identified unowned material transformation.

This is **not** a claim that the system works behaviorally.

Not established by this document:

- runtime implementation completeness;
- behavioral reliability;
- cross-surface enforcement effectiveness;
- professional quality across domains;
- Quality-in-Use;
- real-world outcome effectiveness;
- causal/value superiority.

These require representative End-to-End Real-Use Validation.

## 2. Two bounded repairs incorporated before closure

### 2.1 Commitment ≠ Promotion / State Transition

`Commitment` remains a decision/optionality semantic:

```text
WAIT
PILOT / TEST
STAGED COMMITMENT
REVERSIBLE ACTION
FULL COMMITMENT
```

`Promotion / State Transition` is the generic control operation that changes the semantic status or controlling effect of state.

```text
WORKING / CANDIDATE STATE
        ↓
transition conditions
+ applicable assurance
+ legitimate decision / acceptance / authority
        ↓
PROMOTE / TRANSITION
        ↓
new legitimate semantic state
        ↓
persistent write if required
        ↓
READBACK / RECONCILE
```

The target state is type-specific: e.g. selected, accepted, authorized, controlling, released, deployed, or authoritative for a defined state domain. It is not generically `authoritative`.

Preserve:

```text
proposal
≠ recommendation
≠ decision
≠ acceptance
≠ commitment
≠ authorization
≠ implementation
≠ authoritative state write
```

### 2.2 Orchestrator is cross-cutting over the whole Work Architecture

The Orchestrator / Semantic Compiler is not a post-commit Realization component and not a mandatory runtime agent/module.

It operates across the entire work system:

```text
current controlling parent / intended outcome
+ current state / contemplated transition
+ requirements / Performance Model
+ blockers / dependencies
+ authority
+ capabilities / runtime reality
+ consequence / reversibility
+ uncertainty / horizon
        ↓
ORCHESTRATOR / SEMANTIC COMPILER
        ↓
minimum sufficient admissible work frontier
```

It may select framing, retrieval, formation, research, Human contribution, solution work, work formation, execution, assurance, transition, observation, change work, waiting, stopping, or no-action.

This preserves the existing ownership in the qualified prior `core/orchestration-model.md` and Parent-Work Continuity amendment without reifying Orchestration as an additional stage, room, agent, store, or surface.

## 3. Human-readable End-to-End Work projection

The projection below describes materially distinct transformation types. It is adaptive, recursive, proportional, and may collapse for bounded work. It is **not a mandatory stage machine**.

```text
                STRATEGIC / OPERATING CONTEXT
                            │
                            ▼
                    REALITY / TRIGGER
                            │
                            ▼
                       ADMIT + FRAME
                            │
                            ▼
╔════════════════════════════════════════════════╗
║              FORMATION WORKSPACE               ║
║                                                ║
║ Situation / Current Reality                    ║
║ Need / Problem / Opportunity                   ║
║ Value / Purpose                                ║
║ Goal / Intended Outcome                        ║
║ Requirements / Performance / Success           ║
║ Professional / Reference Intelligence          ║
║ Evidence / Futures / Uncertainty               ║
║ Solution / Mechanism Space                     ║
║ Outcome Mechanism / Realization Hypothesis     ║
║ Feasibility / Capability / Cost / Risk         ║
║ Consequences / Trade-offs                      ║
║ Decision / Recommendation                      ║
╚══════════════════════╤═════════════════════════╝
                       │
                       ▼
             DECISION-READY CANDIDATE
                       │
             DECIDE + COMMIT AS NEEDED
                       │
            STATE TRANSITION / PROMOTION
                       │
                       ▼
                SELECTED WORK BASIS
                       │
                       ▼
╔════════════════════════════════════════════════╗
║          WORK / REALIZATION FORMATION          ║
║                                                ║
║ Work Product(s) / next-use target              ║
║ Professional + craft method                    ║
║ Work Units / dependencies / interfaces         ║
║ Human / AI / tool / workflow allocation        ║
║ State / environment / capability / authority   ║
║ Integration route                              ║
║ Assurance / validation design                  ║
║ Transition / observation / recovery design     ║
╚══════════════════════╤═════════════════════════╝
                       │
                       ▼
               EXECUTE + INTEGRATE
                       │
                       ▼
             CANDIDATE WORK PRODUCT
                       │
             ┌─────────┴─────────┐
             │                   │
      REFINE / MATURE*       ASSURE / QUALIFY
             │            verify / challenge /
             └──────────→  validate as applicable
                               │
                               ▼
                       READINESS STATE
                               │
                  ACCEPT / AUTHORIZE /
                  PROMOTE AS REQUIRED
                               │
                               ▼
                    TRANSITION / ACTIVATE*
                               │
                               ▼
                        USE / OPERATE*
                               │
                               ▼
                         OBSERVE EVIDENCE
                               │
                               ▼
                 OUTCOME / VALUE EVALUATION*
                               │
                               ▼
                             LEARN
                               │
                               ▼
                     CHANGE CANDIDATE
                               │
                      DECIDE / PROMOTE
                               │
                               ▼
             KEEP / REPAIR / ADAPT / REOPEN /
                  WAIT / HANDOFF / RETIRE
                               │
                               ▼
                      CLOSE / CONTINUE
```

`*` = conditional.

## 4. Formation Workspace contract

Formation is a bounded cognitive workspace, not a linear pipeline.

It must be able to iterate among:

```text
Frame ↔ Situation / Reality
  ↕
Need ↔ Value / Purpose ↔ Goal / Intended Outcome
  ↕
Requirements / Performance / Success
  ↕
Evidence / Futures / Uncertainty
  ↕
Professional / Reference Intelligence
  ↕
Solutions / Mechanisms / Outcome Mechanism
  ↕
Feasibility / Capability / Cost / Risk
  ↕
Consequences / Trade-offs / Decision
```

Key invariants:

- raw human input, stated goal, and proposed solution are evidence of intent, not automatically complete requirements or binding decisions;
- where an existing material system is being repaired/redesigned/extended, reconstruct enough current authoritative state, requirements, workflow, and observed failure evidence before replacement design;
- distinguish fundamental value/purpose from means objectives;
- bind comparisons to one decision question and compare peer options at the same scope/type; split parent/child choices when candidates are not peers;
- use qualified precedent/reuse before bespoke design when valuable;
- include simpler/no-action where materially relevant;
- model enough of the Outcome Mechanism / Realization Hypothesis before consequential solution commitment;
- establish enough realization feasibility, capability/environment fit, cost, dependencies, authority, transition, and risk before treating a route as decision-ready;
- use forecast where legitimately forecastable; otherwise use decision-relevant scenarios, robustness, signposts, or staged commitment without converting plausibility into probability.

### Formation output

A `Decision-Ready Candidate` contains, proportionately:

- Frame / scope / decision object;
- current reality and material assumptions/unknowns;
- Purpose / Intended Outcome;
- requirements / Performance Model / success conditions;
- professional/reference basis where material;
- candidate solution / route and relevant alternatives;
- Outcome Mechanism / Realization Hypothesis;
- feasibility / capability / cost / risk / uncertainty;
- recommendation / decision case;
- proposed commitment level;
- material reopen/signpost conditions.

## 5. Promotion / State-Transition control

A material promotion changes what downstream work may legitimately rely on.

Before promotion, establish enough of:

```text
source / controlling baseline
+ exact delta
+ semantic status being assigned
+ requirements / applicable assurance
+ material dependencies / downstream implications
+ legitimate decision / acceptance / authority
+ persistence/write path where required
```

After a material persistent promotion:

```text
WRITE → READBACK → RECONCILE CONTROLLING STATE
```

Technical write capability, reversibility, local AI confidence, file existence, a favorable self-review, or repository persistence do not grant promotion authority.

## 6. Work / Realization Formation contract

Input: selected/committed work basis with sufficient upstream state.

Transformation: determine how the selected route will actually be produced, integrated, assured, transitioned, observed, and recovered.

Where material:

- complete Work Product(s) and next-use target;
- substantive professional method;
- artifact/craft method;
- evidence/research needs;
- Work Units and dependencies;
- required capability by function;
- Human / AI / mixed / specialist / deterministic tool / workflow / existing-process allocation;
- actual accessible/effective capabilities and environments;
- state reads/writes and authoritative paths;
- authority / permissions;
- integration route;
- assurance route for exact claims;
- transition / receiving-context requirements;
- representative-use validation route;
- rollback / recovery / monitoring / retirement where material.

Key invariant:

```text
functional / coverage distinction
≠ Work Unit
≠ persistent module / agent / room / store boundary
```

Persistent boundaries must earn interface, duplication, synchronization, lifecycle, assurance, governance, or failure-isolation cost.

## 7. Execution + Integration contract

Execution performs authorized work through actual Humans, AI, tools, workflows, systems, or external actors.

Integration must reconcile child outputs into the controlling parent result.

```text
child Work Unit completed
≠ parent Work Product complete
```

Preserve actual runtime state, tool results, permissions, provenance, dependencies, and authoritative writes where material.

## 8. Next-use Maturity / Refinement

Activate when a coherent candidate Work Product can still differ materially from what the next recipient/use context needs.

```text
CURRENT WORK PRODUCT
→ NEXT RECEIVING CONTEXT / MATURITY CLAIM
→ material maturity delta
→ highest-value product transformation(s)
→ REFINE THE PRODUCT
→ re-assure affected claims
→ advance readiness or keep pending
```

Refinement changes the Work Product. Assurance evaluates a claim about it.

AI should resolve AI-resolvable completeness, surface-fit, craft, clarity, usability, deterministic constraint, and recipient-readiness defects before defaulting detection to the Human.

## 9. Assurance / Qualification

Assurance is claim-bound and may occur throughout the architecture.

Keep distinct where material:

```text
self-review
≠ deterministic verification
≠ professional / source challenge
≠ independent challenge
≠ recipient judgment
≠ intended-use validation
≠ operational / transition readiness
≠ robustness
≠ forecast accuracy / calibration
≠ Quality-in-Use
≠ outcome evidence
≠ causal attribution
```

A claim is no stronger than the evidence and detection capability that establish it.

Missing material coverage/evidence/capability/authority yields FAIL / UNVERIFIED / pending, not inferred PASS.

## 10. Transition / Use / Outcome contract

When success depends on real-world realization, preserve enough of:

```text
Work Product
→ receiving context
→ transition / activation
→ use / adoption / action
→ performance / fidelity
→ mechanism
→ intermediate outcomes
→ Intended Outcome
→ benefit / value
```

Production, integration, readiness, transition, use, observed outcome, causal effect, and realized value remain distinct.

Where outcome is delayed/external, establish enough of observer/owner, evidence source, horizon, signpost/decision threshold, and attribution limits.

## 11. Learning / Change / Closure

Learning does not automatically mutate Strategy, Operating state, Work methods, Runtime, or authoritative records.

```text
observation / outcome evidence
→ evaluation / learning
→ change candidate
→ legitimate decision / promotion
→ KEEP / REPAIR / ADAPT / REOPEN / WAIT / HANDOFF / RETIRE
```

Reopen only materially dependent state where safe; preserve unaffected qualified work.

Closure options include:

```text
CLOSE
CONTINUE
WAIT
HANDOFF
STOP / NO-ACTION
MONITOR / OBSERVE
```

Close at the strongest boundary actually supported by evidence and authority.

## 12. Work Control & Integrity Harness

The Harness is cross-cutting control infrastructure, not a stage and not by itself the Orchestrator.

It preserves/realizes, proportionately:

- Reality / evidence / epistemic status;
- typed state / provenance / freshness / lineage;
- authoritative record / owner / legitimate write path by state domain;
- parent/program continuity;
- decision / acceptance / commitment / authorization / promotion semantics;
- Human agency / legitimate contribution;
- professional method / reference / craft knowledge;
- Human–AI / capability / environment composition;
- claim-specific assurance;
- risk / consequence / reversibility / containment / rollback / recovery;
- economics / opportunity cost / information value / optionality;
- Knowledge Capital / reuse / promotion;
- actual runtime / instruction / tool / permission reality;
- transition control / enforcement where a material downstream step must actually be withheld;
- change / promotion / readback / selective reopen control.

### Mechanism requirement

A critical function is not considered realized merely because its policy appears in prose.

Examples:

```text
Human Gate policy
≠ effective wait / downstream-transition enforcement

professional method requirement
≠ method actually found / accessible / applied

state/promotion rule
≠ authorized write + readback + reconciliation

assurance label
≠ detection-capable assurance actually applied
```

## 13. Orchestrator / Semantic Compiler

The Orchestrator reads the controlling work state and Harness reality and selects the next legitimate frontier.

It must preserve Parent-Work Continuity:

```text
controlling parent Work Object / Intended Outcome
+ current parent state / gate
+ active child contribution
+ allowed operation / mutation authority
```

A child thread, local hypothesis, current chat topic, artifact, branch, or most-recent output must not silently become the root.

If parent/gate/contribution is materially unclear, recover/reconcile controlling state before local continuation.

Possible frontier outputs include:

- direct answer/work;
- framing/qualification;
- retrieval/research/measurement;
- professional/reference resolution;
- solution/decision work;
- work formation/decomposition;
- Human contribution / Gate;
- execution/tool action;
- product refinement;
- assurance/validation;
- transition/use work;
- observation/monitoring;
- change/repair;
- wait/stage/reversible action;
- stop/no-action/external handoff.

The Orchestrator is a logical policy/function. A concrete runtime may co-locate it with other functions; no separate agent/service is required by this architecture.

## 14. Human Gate semantics

A Human Gate exists only when a material transition cannot legitimately or effectively occur without Human-exclusive truth/context, values/judgment, expertise, authorship/learning, acceptance, responsibility, or authority.

A real Gate requires:

```text
blocked transition
+ exact Human contribution
+ mature decision object / evidence
+ why AI/retrieval/robust proceeding cannot substitute
+ effective wait / transition enforcement where needed
+ re-entry condition
```

Human review must not be the default first detector of AI-resolvable professional-quality defects.

## 15. Runtime-carrier boundary

Architecture function ≠ product surface.

Chat, Projects, Work, Skills, Apps/connectors, files, repositories, tools, Codex, automations, or future product surfaces may carry architecture functions if they provide the required information, capability, authority, persistence, assurance, or enforcement.

Do not hard-map logical architecture objects to current product features without runtime evidence.

For every material runtime claim distinguish:

```text
required function
≠ feature existence
≠ account availability
≠ access/binding
≠ effective capability
≠ authority
≠ verified performance
```

## 16. End-to-End transition contracts

| Transition | Input | Transformation | Output | Readiness condition | Next interface |
|---|---|---|---|---|---|
| Trigger → Formation | Raw reality/input | Admit, scope, frame | Admitted work frame | relevant work sufficiently framed | Formation |
| Formation → Decision | framed work | purpose/outcome/requirements/solution reasoning | decision-ready candidate | material alternatives/dependencies sufficiently treated | decision/commitment |
| Decision → Work basis | candidate | decide/commit + legitimate state transition | selected/committed work basis | status/authority/assumptions clear | Work Formation |
| Work Formation → Execution | selected basis | method/capability/dependency/orchestration design | executable work composition | inputs/capabilities/authority sufficient | Execution |
| Execution → Candidate Product | executable work | perform + integrate | coherent candidate Work Product | parent completeness checked | Refinement/Assurance |
| Candidate → Readiness | candidate product | refine where needed + assure exact claims | qualified readiness state | exact claim supported or FAIL/UNVERIFIED | acceptance/transition |
| Readiness → Transition | qualified result | acceptance/authorization/promotion where required | legitimately transitionable result | receiving context ready | Activation |
| Transition → Use | transitionable result | deploy/handoff/enable | operating/use state | access/ownership/dependencies satisfied | Use/Observation |
| Use → Outcome evidence | operating state | observe performance/mechanism | use/outcome evidence | evidence horizon/scope known | Evaluation |
| Evidence → Change | outcome evidence | evaluate/learn | change candidate | implications/dependencies known | legitimate decision |
| Change → Closure/Adaptation | change candidate | decide/promote/reopen | new controlled state | owner/authority/readback complete | Continue/Wait/Close |

## 17. Relationship to accepted Target Architecture v0.2

This candidate does not replace the three accepted structural commitments by default:

1. distinct Strategic / Operating / Work / Execution / Learning-Change responsibilities;
2. distributed typed state;
3. adaptive Work-Selection contract.

It is a **candidate end-to-end Work Architecture / human-readable transformation-and-control projection** that composes those commitments with qualified prior mechanisms recovered from historical evidence.

No new mandatory runtime layer, central state store, agent topology, stage machine, room topology, or product-surface mapping is claimed.

## 18. Static completeness claim

Subject to `reviews/E2E-STATIC-CLOSURE-REVIEW-v0.1.md`:

```text
CR-01–13                         PASS
CCR-01–07                        PASS / conditional-owned
Historical Failure Families      OWNED
Spine transition contracts       COMPLETE
Label-only critical mechanisms   NONE FOUND
Boundary reification             NONE REQUIRED
Unowned material transformation  NONE FOUND
```

Therefore:

> **STATIC / ARCHITECTURAL COMPLETENESS CANDIDATE — PASS within the defined scope and current evidence/reference horizon.**

Reopen the static architecture only for a named material trigger such as an unowned real-use transformation, a non-realizable required mechanism, a semantic contradiction, a materially simpler rival satisfying the same requirements, or a changed legitimate requirement/scope.
