# Architecture Method v0.3

**Status:** CLOSURE-SYNCED METHOD / POST-BASELINE REOPEN DISCIPLINE  
**Authority boundary:** `CURRENT.md` controls current repository development/operating state and next-work authority. This method governs architecture derivation/reopen discipline; it does not independently set the active program gate.

## Purpose

Define how references, qualified prior designs and internal evidence become architecture — and, after architecture acceptance, how architecture may be reopened without collapsing different architectural dimensions, rediscovering qualified prior mechanisms or confusing realization problems with architecture problems.

## Core rule

> Architecture is derived from qualified concerns and requirements; it is not assembled by collecting attractive concepts or by forgetting prior qualified design work.

After acceptance, architecture is **closed by default**. Runtime/operating/method failures are repaired at the narrowest supported level unless a named architecture reopen trigger is established.

---

## 1. Keep these objects distinct

- **System of Interest (SoI):** the entity being architected.
- **Operational environment:** external actors, systems, conditions, constraints, and interfaces.
- **Architecture:** fundamental concepts/properties of the SoI and their governing relationships.
- **Architecture description:** our representation of that architecture.
- **Concern:** a stakeholder-relevant matter the architecture must address.
- **Viewpoint:** conventions for constructing a view around particular concerns.
- **View:** a representation from one viewpoint.
- **Requirement / constraint:** a qualified need the system must satisfy.
- **Mechanism:** a causal or functional means that may satisfy one or more requirements.
- **Component / subsystem:** a structural realization decision, not a synonym for a capability or concern.
- **Capability:** an ability required or available, independent of its eventual realization.
- **Runtime realization:** concrete models, instructions, skills, tools, code, state, actors and interfaces.
- **Evaluation / assurance:** evidence used to judge architecture, realization or runtime claims.
- **Qualified Prior Design:** a prior bounded architecture/design decision with explicit scope, reference basis, review/falsification and human acceptance sufficient to change the burden of proof for reopening.

---

## 2. Derivation, realization and selective reopen flow

The repository is **not clean-room discovery**. It is lineage-aware reconstruction followed by evidence-grounded realization.

```text
Problem / mission / operational context
        + stakeholder concerns
        + external references
        + qualified prior designs
        + raw internal / real-use evidence
                 ↓
      prior-design reconciliation
      retain / refine / relocate /
      supersede / reject / open conflict
                 ↓
       qualified needs / requirements
                 ↓
      unresolved mechanisms + alternatives
                 ↓
     conceptual architecture alternatives
                 ↓
       cross-view / cross-concern integration
                 ↓
         architecture decision
                 ↓
       evaluation / falsification
                 ↓
     accepted conceptual architecture
                 ↓
       runtime / operating realization
                 ↓
 behavioral + implementation evaluation
                 ↓
 local repair / capability or operating promotion
                 ↓
 architecture reopen only if a named trigger exists
```

If no material reopen trigger exists for an accepted prior or the accepted Target Architecture, the default operation is **recover and preserve**, not re-derive.

---

## 3. Qualified Prior Design rule

A prior design may be treated as a `Qualified Prior` when its evidence package is adequate for the claimed scope, normally including:

1. explicit System of Interest / purpose / claim boundary;
2. identifiable reference or rationale basis;
3. explicit alternatives, failures or trade-offs considered;
4. review, pressure test, falsification or other architecture-evaluation record;
5. human acceptance / canonical or bounded accepted status;
6. known limitations and reopen conditions.

A Qualified Prior is **not external truth** and does not automatically transfer to a changed SoI. It creates a burden-of-proof asymmetry:

```text
accepted qualified prior
→ closed-but-reopenable

not

accepted qualified prior
→ forgotten and open-by-default
```

### Reopen triggers

Reopen a qualified prior only when at least one applies:

1. changed SoI or intended claim;
2. new external evidence materially conflicts with the prior;
3. new real-use failure exposes an unhandled mechanism;
4. a stronger/simpler rival preserves required semantics at lower burden or better performance;
5. two qualified priors conflict materially;
6. implementation/runtime reality makes the prior infeasible for intended use;
7. audit shows the prior was not actually qualified for the claim being inherited.

For Target Architecture v0.2, use its explicit accepted reopen conditions / ADR-0002 discipline. Every reopened architecture question should record the trigger and the exact accepted claim being challenged.

---

## 4. Reference-to-architecture rule

A construct found in a standard, paper, framework, or production system is not promoted directly. For each architecture candidate:

1. identify the concern it addresses;
2. understand the proposed mechanism;
3. record evidence and scope;
4. test transferability to our operating context;
5. identify competing or simpler mechanisms;
6. check whether a qualified predecessor or accepted baseline already resolves the same problem and why;
7. decide whether it belongs in architecture, a capability, a method, runtime/operating realization, evaluation, or knowledge only;
8. require enough benefit to justify the complexity it introduces.

After Target Architecture acceptance, reference research should preferentially discriminate:

- a named architecture reopen trigger;
- a material realization alternative;
- an implementation/evaluation uncertainty that can change the realization decision.

Do not reopen architecture merely because a new framework, product feature or vocabulary exists.

---

## 5. Internal-evidence rule

A repeated success or failure does not automatically become a global invariant. Reconstruct the episode, separate observation from interpretation, list competing explanations, check relevant reference knowledge, check prior design responses, compare repairs at different levels, and promote only the narrowest supported mechanism.

Internal material must preserve type:

```text
raw observation
≠ design hypothesis
≠ qualified prior design
≠ implementation/runtime evidence
≠ accepted architecture
≠ external validation
```

For post-acceptance failures, localize the first invalid transition or mechanism where possible:

```text
architecture requirement/semantic gap?
runtime / operating realization gap?
carrier / activation failure?
execution / permission / state failure?
professional-method / artifact-quality failure?
assurance / evaluation failure?
authority / promotion failure?
```

Only architecture-level evidence opens architecture-level work.

---

## 6. Viewpoint discipline

Do not force different dimensions into one tree. Useful architecture-description viewpoints may include:

- context / boundary;
- functional / control;
- capability;
- information / knowledge / state;
- Human–AI responsibility / authority;
- workflow / temporal / lifecycle;
- assurance / trust;
- runtime / realization;
- economics / resource allocation.

Target Architecture v0.2 does not require one mandatory final viewpoint set. A viewpoint earns use only if it addresses a material concern not adequately represented elsewhere.

A single entity may appear in several views without becoming several entities. Identity and semantics must survive cross-view integration.

---

## 7. Alternative-first rule

Before a material architectural commitment, compare credible alternatives where they exist.

But do not manufacture a new alternative space when prior work already compared and accepted alternatives. First recover the prior comparison and ask whether a reopen trigger exists.

Examples of alternatives that may be relevant at the appropriate level include:

- broad sociotechnical SoI vs narrower technical subsystem for a specific claim;
- distributed adaptive work-selection policy vs an explicit controller implementation;
- global persistent state vs domain-owned authoritative state plus derived working context;
- one adaptive model vs orchestrated specialized agents;
- global invariants vs capability-local methods;
- explicit workflow states vs latent/adaptive control;
- current incumbent realization vs a materially simpler or more reliable carrier configuration.

Compare alternatives on performance, complexity, transferability, observability, failure containment, maintainability, runtime feasibility, Human burden/agency, economics and evidence status.

---

## 8. Promotion and lineage states

Architecture-candidate progression:

`DISCOVERED → FRAMED → SUPPORTED → CANDIDATE → TESTED → ACCEPTED → RETIRED/SUPERSEDED`

Lineage disposition for inherited design:

`RETAIN | RETAIN-WITH-BOUNDARY | REFINE | RELOCATE | MERGE | SUPERSEDE | REJECT | OPEN-CONFLICT`

`SUPPORTED` is not `TESTED`; `TESTED` is not universal validity; `ACCEPTED` is not permanent truth.

For realization work, keep separate:

```text
candidate carrier / mechanism
≠ implemented candidate
≠ verified realization
≠ accepted / promoted operating state
≠ behavioral effectiveness
```

Promotion authority remains with the legitimate owner/write path for the affected state domain.

---

## 9. Complexity budget

Every construct creates vocabulary, implementation, context, evaluation, interaction and maintenance cost. It should justify itself by preventing a material failure class, enabling a material capability, reducing downstream complexity through a real invariant, improving transfer, enabling necessary assurance, or materially improving work economics / Human agency.

Re-derivation itself also has a cost. Reopening an accepted question without new decision value is **architecture process waste**.

If a mechanism can remain reference knowledge, a conditional capability, a local working method, an operating configuration or a qualified inherited design rather than new global architecture, that remains the preferred lower-burden alternative when performance is equivalent.

Runtime realization is likewise not optimized for minimal artifact count or minimal instruction length in isolation; total-system performance and burden decide.

---

## 10. Work-control / `Work Engine` disposition after Target Architecture v0.2

The bootstrap phase treated `Work Engine` / Semantic Compiler placement as an open architecture delta.

Target Architecture v0.2 superseded that standing delta sequence and accepted a smaller semantic commitment:

> **Adaptive Work-Selection Contract** — for admitted/triggered work, select the minimum justified next work from current reality, intended outcome/claim, requirements, preserved state, dependencies, capability/authority/runtime reality, consequence, uncertainty and economics.

Therefore:

```text
Adaptive Work-Selection semantic obligation    ACCEPTED
peer `Work Engine` architecture subsystem      NOT REQUIRED / NOT ACCEPTED
Semantic Compiler label/implementation          CONDITIONAL REALIZATION OPTION
Work Graph / Work Units                         CONDITIONAL REPRESENTATION / MECHANISM
B.6 macro projection                           OPTIONAL HUMAN-READABLE PROJECTION
```

`Work Engine` is no longer a standing foundational architecture question. It reopens only if realization/evaluation evidence shows that the accepted semantic contract cannot be implemented, observed or preserved adequately without a distinct architectural object — which would require a valid architecture reopen trigger.

Working methods inside Work, including the currently active Solution Formation method, do not become architecture objects merely because they improve or structure runtime behavior. Their promotion burden remains at the method/realization/evaluation level unless evidence establishes an architecture-level gap.

---

## 11. Post-acceptance architecture gate

The pre-acceptance architecture-freeze gate is historical for Target Architecture v0.2 and is not the current repository development gate.

Post-acceptance rule:

> **Do not reopen foundational architecture while the observed problem can be represented and repaired within the accepted semantics at method, realization, runtime, operating or evaluation scope.**

Before any architecture reopen:

- name the exact accepted reopen trigger;
- identify the accepted claim/requirement that is insufficient, contradictory or unrealizable;
- recover the evidence and affected scope;
- show why a runtime/operating/method/capability repair is insufficient;
- compare credible architecture alternatives and simpler non-architecture repairs;
- define the claim-matched evaluation needed for promotion.

Otherwise the generic path is:

```text
accepted architecture
→ recover actual current reality / realization
→ preserve qualified state
→ identify the material problem or gap
→ select the smallest adequate method / realization / operating change
→ execute + readback / representative use
→ behavioral / implementation evaluation
→ promote, repair locally or reject
```

The **current concrete operating mode and next legitimate work** are defined only by `CURRENT.md`; do not infer them from historical `Next`, delta or gate sections in architecture artifacts.

The method succeeds not when it produces the newest architecture, but when it preserves qualified system knowledge, localizes failures correctly and changes only the level that evidence justifies.
