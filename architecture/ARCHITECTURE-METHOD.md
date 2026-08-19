# Architecture Method v0.1

**Status:** BOOTSTRAP METHOD

## Purpose

Define how references and internal evidence become architecture without collapsing different architectural dimensions into one hierarchy.

## Core rule

> Architecture is derived from qualified concerns and requirements; it is not assembled by collecting attractive concepts.

## Keep these objects distinct

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
- **Runtime realization:** concrete models, instructions, skills, tools, code, state, and interfaces.
- **Evaluation / assurance:** evidence used to judge architecture or runtime claims.

## Derivation flow

```text
Problem / mission / operational context
        + stakeholder concerns
        + external references
        + internal evidence
                 ↓
       qualified needs / requirements
                 ↓
      mechanisms + credible alternatives
                 ↓
     conceptual architecture alternatives
                 ↓
       viewpoints and architecture views
                 ↓
          cross-view integration
                 ↓
         architecture decisions
                 ↓
       evaluation / falsification
                 ↓
          runtime realization
```

## Reference-to-architecture rule

A construct found in a standard, paper, framework, or production system is not promoted directly. For each candidate:

1. identify the concern it addresses;
2. understand the proposed mechanism;
3. record evidence and scope;
4. test transferability to our operating context;
5. identify competing or simpler mechanisms;
6. decide whether it belongs in architecture, a capability, a method, runtime, evaluation, or knowledge only;
7. require enough benefit to justify the complexity it introduces.

## Internal-evidence rule

A repeated success or failure also does not automatically become a global invariant. Reconstruct the episode, separate observation from interpretation, list competing explanations, check relevant reference knowledge, compare repairs at different levels, and promote only the narrowest supported mechanism.

## Viewpoint discipline

Do not force different dimensions into one tree. Candidate viewpoints may eventually include:

- context / boundary;
- functional / control;
- capability;
- information / knowledge / state;
- Human–AI responsibility / authority;
- workflow / temporal / lifecycle;
- assurance / trust;
- runtime / realization;
- economics / resource allocation.

This list is provisional. A viewpoint earns existence only if it addresses a material concern not adequately represented elsewhere.

A single entity may appear in several views without becoming several entities. Identity and semantics must survive cross-view integration.

## Alternative-first rule

Before a material architectural commitment, compare credible alternatives where they exist. Examples include:

- human inside the SoI vs human in the operational environment;
- distinct Work Engine subsystem vs distributed work-control policy;
- global persistent state vs domain-owned authoritative state plus derived working context;
- one adaptive model vs orchestrated specialized agents;
- global invariants vs capability-local methods;
- explicit workflow states vs latent adaptive control.

Compare alternatives on performance, complexity, transferability, observability, failure containment, maintainability, and runtime feasibility.

## Promotion states

`DISCOVERED → FRAMED → SUPPORTED → CANDIDATE → TESTED → ACCEPTED → RETIRED/SUPERSEDED`

`SUPPORTED` is not `TESTED`; `TESTED` is not universal validity.

## Complexity budget

Every construct creates vocabulary, implementation, context, evaluation, interaction, and maintenance cost. It should justify itself by preventing a material failure class, enabling a material capability, reducing downstream complexity through a real invariant, improving transfer, enabling necessary assurance, or materially improving work economics / human agency.

If a mechanism can remain reference knowledge or a conditional capability rather than global architecture, that remains a live alternative.

## Work Engine status

`Work Engine` is currently a **candidate abstraction**, not an accepted subsystem.

The provisional function to explain is:

> Select and coordinate the minimum sufficient next work given intent, current state, available capabilities, constraints, uncertainty, authority, and evidence requirements.

Reference work and evidence must determine whether this function is best represented as a subsystem, distributed control policies, a viewpoint, a runtime loop, or another construct.

## Architecture freeze gate

Do not freeze a conceptual architecture until the SoI boundary is adequate for the intended claims, major concerns have coverage, relevant reference families have been checked, internal evidence has usable provenance, cross-view integration is coherent, key alternatives were compared, critical constructs have mechanisms and placement, the performance model can discriminate alternatives, and material uncertainties plus evaluation plans are explicit.
