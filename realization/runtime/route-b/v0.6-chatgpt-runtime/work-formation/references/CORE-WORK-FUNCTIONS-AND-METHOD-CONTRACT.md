# Route B Core Work Functions and Method Discovery Contract v0.3

## Source identity

- Source kind: `PROVIDER-NEUTRAL CORE METHOD LAYER`
- Candidate package: `route-b-runtime-candidate-v0.5`
- Status: `NON-INSTALLED SOURCE`
- Operational owner: Native Primary

This source defines professional Work-Function and method-discovery semantics. It is not an episode controller, stage model, domain method, provider-selection engine or installable Skill.

## Responsibility boundary

The Core Method Layer owns:

- the provider-neutral vocabulary of composable Work Functions;
- Information/Evidence as a cross-cutting capability;
- discovery and qualification of eligible Professional Methods;
- the distinction between function, method, provider and surface.

It does not own:

- universal integrity invariants, which remain with the Kernel;
- Work-Basis Formation, which remains with the Formation Method;
- professional/domain execution, which remains with Domain Methods;
- planning, composition, Tools, delegation, waiting or synthesis, which remain with the Native Primary;
- decision, commitment, authority, external effect or promotion operators.

## Core Work Functions

Work Functions describe the professional transformation required for a Claim or intended use. They may be used alone or composed. They are not stages and have no mandatory order.

### Explore

Expand and structure a consequentially relevant possibility space before premature commitment. Produce qualified questions, hypotheses, probes, options, frames or search directions with a stopping rule appropriate to decision value.

Exploration outputs remain provisional. Exploration may narrow or falsify routes, examples or solution sketches, but does not promote a Probe into a Candidate. Candidate eligibility requires the relevant professional Performance Floor, Method basis and Evidence/comparison basis.

### Research

Acquire and synthesize qualified evidence that is not already adequately available. Use an explicit evidence strategy, source qualification, provenance/freshness control and bounded uncertainty.

### Analyze

Transform evidence or data into supported descriptions, relationships, estimates, comparisons or implications. Preserve definitions, assumptions, uncertainty and inferential limits.

### Diagnose

Explain an observed problem, failure, difference or change through evidence-bound causes, mechanisms and failure modes. Separate symptoms, contributing conditions, root causes and unresolved alternatives.

### Decide

Compare eligible routes against requirements, intended use, trade-offs, uncertainty, reversibility and consequence to support a legitimate decision. A decision does not itself create commitment, authorization or execution.

### Design

Specify a solution, system, service, artifact or operating mechanism capable of meeting the formed requirements and performance floor. Preserve feasibility, interfaces, constraints and outcome mechanism.

### Create

Produce a new artifact, representation, narrative, model or other Work Product to a defined quality and intended-use standard. Creation alone does not establish transition, use or outcome.

### Assure

Evaluate a bounded Claim or Work Product against explicit requirements using a method capable of detecting material failures. Distinguish self-review, verification, independent challenge, recipient validation, transition readiness and in-use evidence.

### Translate

Transform meaning, representation or form for a different recipient, domain, language, medium, environment or intended use while preserving required semantics and professional quality.

### Implement

Instantiate an authorized change in a real receiving environment. Respect effect and write authority, dependencies, rollback and readback. Implementation is not automatically verified behavior, adoption or outcome.

### Serve

Deliver or operate a continuing recipient-facing capability, decision service or professional function. Preserve service level, responsibility, feedback, continuity and use conditions appropriate to the intended value.

### Learn

Integrate new evidence into beliefs, models, methods or operating state. Reopen only dependent claims. A method, Runtime or promoted-state change remains a separately controlled act.

## Supporting functions and dispositions

### Retrieve / Inspect

Obtain and examine existing state, sources, artifacts, environments or prior work without claiming broader coverage than observed.

### Observe

Collect evidence across a relevant time or event horizon when current observation is insufficient and intervention is not yet warranted.

### Wait

Hold the transition because an external dependency, authority, event or observation horizon controls the next legitimate change.

### Close

End the bounded Work Unit because its requested and supported frontier is complete. Parent Outcome completion is a separate claim.

### Stop

End work because continuation is unjustified, unsafe, unauthorized, uneconomic or incapable of supporting the intended Claim.

### No Action

Deliberately preserve the current state because intervention has insufficient value, evidence, authority or advantage over the baseline.

## Composition semantics

- A Work Unit may require one Work Function or several.
- Multiple functions may be sequential only when their transformations genuinely depend on one another.
- Independent functions may be parallelized when integration and effect boundaries permit.
- A function may recur when new evidence reopens its dependent Claim.
- Supporting functions may appear wherever needed; they are not lower maturity levels.
- `Wait`, `Close`, `Stop` and `No Action` are legitimate dispositions, not process failures.

Do not infer a universal sequence such as Explore→Research→Analyze→Decide→Design→Implement. Use only the functions needed for the actual Claim and intended use.

## Information / Evidence capability

Information/Evidence is foundational and cross-cutting. It supports every Work Function to the depth required by consequence, uncertainty, reversibility and intended use.

It covers every Work Function to the depth required by consequence, uncertainty, reversibility and intended use.

### Retrieval and inspection

Locate and inspect relevant existing evidence, state, artifacts and environments. Distinguish observed coverage from the complete System of Interest.

### Research

Acquire missing external or connected evidence using a source and search strategy proportionate to the Claim.

### Source qualification

Assess authority, provenance, freshness, scope, independence, completeness, conflicts and methodological fitness.

### Current-state reconstruction

Reconstruct the best-supported present state from authoritative records, direct readback, evidence slices and unresolved conflicts. Do not silently replace current evidence with historical records.

### Evidence synthesis

Integrate converging, complementary and conflicting evidence without erasing provenance or transferring authority.

### Uncertainty management

Represent material unknowns, assumptions, sensitivity, alternative explanations and evidence limits. Learn more only when expected decision value exceeds information and delay cost; otherwise use robust, reversible or bounded choices.

Information/Evidence is not a mandatory preliminary phase. Direct work may use adequate available evidence; additional retrieval, research or observation is justified only when it can materially change the supported frontier.

## Method Discovery and Composition Contract

### Eligibility function

```text
Work Function
+ Intended Use
+ Performance Floor
+ Domain
+ Evidence Need
→ eligible Professional Method(s)
```

### Inputs

#### Work Function

The professional transformation or composable transformation set required for the next supported Claim or transition.

#### Intended Use

The receiving actor, context, decision, action, transition or service condition the Work Product must support.

#### Performance Floor

The non-compensatory properties the method and output must satisfy, such as accuracy, completeness, explanatory adequacy, usability, robustness, traceability, independence or effect safety.

#### Domain

The professional, organizational, technical, regulatory, cultural or operational context that determines valid concepts, methods, constraints and evidence.

#### Evidence Need

The evidence type, provenance, freshness, coverage, uncertainty and assurance required to support the Claim and intended use.

### Output

The contract returns one or more eligible Professional Methods with:

- method identity or method class;
- provenance and qualification basis;
- fit to function, intended use, performance floor, domain and evidence need;
- required inputs, capabilities and dependencies;
- material limitations and uncertainty;
- assurance implications;
- alternatives when no single method is adequate.

The output is an eligibility set, not an operational plan or provider assignment.

## Method qualification

A Professional Method is eligible only when its provenance and fit are adequate for the claimed property. Qualification may be established through accepted professional standards, authoritative methodology, validated organizational practice, qualified domain expertise or a transparent bounded method whose limitations are retained.

When no adequate method is available:

- lower the readiness or Claim;
- retrieve or research an adequate method when the information value justifies it;
- externalize to a qualified specialist or Human; or
- use a bounded provisional method with explicit limitations when consequence and reversibility permit.

Do not fabricate professional confidence or treat plausible model behavior as method qualification.

## Just-in-time method and reference scope

Use an already adequate method basis directly. When additional method or reference material is needed, retrieve or load only the slice required to qualify and execute the bounded claim. Preserve provenance, scope, version or freshness where material, limitations and the owning professional source.

A method or reference source may qualify work but does not acquire Kernel, Formation, operational, acceptance or action Authority ownership. Do not require a complete method registry or gateway lookup for straightforward work.

Operating/Learning may retire, simplify or replace a persistent method pointer when its provider assumptions, professional basis or expected benefit expires, overlaps or no longer supports the claimed property. This is a change decision at the owning layer, not a mandatory inventory or per-episode retirement ceremony.

## Native composition after eligibility

The Native Primary chooses the actual realization after eligible methods exist. It may compose:

- direct execution;
- Tools;
- Domain Skills;
- one native Subagent;
- multiple native Subagents;
- independent reviewer agents;
- specialist or recipient Humans.

Selection uses expected effectiveness, verifiability, specialization, independence, parallelism, context isolation, consequence, authority, learning, integration cost, attention, latency and token cost.

When composition can materially affect Human learning, skill formation, retained judgment, future autonomy or dependency risk over the relevant horizon, include those as intended outcomes or constraints. Do not infer a default requirement for Human execution or ownership.

Work Function ≠ Professional Method ≠ provider ≠ surface. A method may have multiple providers; a provider may execute multiple methods; a surface is only the execution environment.

## Relationship to Formation

Formation may identify or resolve the Work Function, intended use, performance floor, domain, evidence need or eligible method class only when their absence materially changes the next frontier.

Formation terminates once these are sufficient for the Native Primary. It must not execute, sequence or orchestrate the Professional Method.

## Relationship to assurance

Assure is both a Core Work Function and a property-specific professional responsibility. The assurance method must be capable of detecting the relevant failure and must match the bounded Claim, object, version, environment and intended use.

Independent challenge is conditional on material correlated-error risk. It is not mandatory for every method or Work Product.

## Prohibitions

The Core Method Layer must not:

- become a Work-Function stage machine;
- require a mandatory method pipeline;
- create a universal controller choreography;
- duplicate native planning, Tool routing, delegation, waiting or synthesis;
- mandate Primary self-execution or Subagent use;
- mandate Spawn→Return→Rebind→Reviewer flows;
- turn Information/Evidence into unconditional research;
- silently promote an exploratory Probe, route, example or solution sketch into a Candidate;
- execute Domain Methods;
- claim decision, commitment, authorization, transition, use, outcome or promotion;
- become a full method/reference registry, mandatory gateway or standing retirement ceremony.
