# Architecture Method v0.2

**Status:** BOOTSTRAP METHOD / LINEAGE-CORRECTED

## Purpose

Define how references, qualified prior designs and internal evidence become architecture without collapsing different architectural dimensions into one hierarchy or repeatedly rediscovering already-developed mechanisms.

## Core rule

> Architecture is derived from qualified concerns and requirements; it is not assembled by collecting attractive concepts or by forgetting prior qualified design work.

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
- **Runtime realization:** concrete models, instructions, skills, tools, code, state, and interfaces.
- **Evaluation / assurance:** evidence used to judge architecture or runtime claims.
- **Qualified Prior Design:** a prior bounded architecture/design decision with explicit scope, reference basis, review/falsification and human acceptance sufficient to change the burden of proof for reopening.

---

## 2. Derivation and reconciliation flow

The reconstruction is **not clean-room discovery**. It is lineage-aware reconstruction.

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

If no material reopen trigger exists for an accepted prior design, the default operation is **recover and provisionally retain**, not re-derive.

---

## 3. Qualified Prior Design rule

A prior design may be treated as a `Qualified Prior` when its evidence package is adequate for the claimed scope, normally including:

1. explicit System of Interest / purpose / claim boundary;
2. identifiable reference or rationale basis;
3. explicit alternatives, failures or trade-offs considered;
4. review, pressure test, falsification or other architecture-evaluation record;
5. human acceptance / canonical or bounded accepted status;
6. known limitations and reopen conditions.

A Qualified Prior is **not external truth** and does not automatically transfer to a changed SoI. It creates a **burden-of-proof asymmetry**:

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

Every reopened question should record the trigger and the exact prior claim being challenged.

---

## 4. Reference-to-architecture rule

A construct found in a standard, paper, framework, or production system is not promoted directly. For each candidate:

1. identify the concern it addresses;
2. understand the proposed mechanism;
3. record evidence and scope;
4. test transferability to our operating context;
5. identify competing or simpler mechanisms;
6. check whether a qualified predecessor already resolved the same problem and why;
7. decide whether it belongs in architecture, a capability, a method, runtime, evaluation, or knowledge only;
8. require enough benefit to justify the complexity it introduces.

Reference research should preferentially discriminate **open conflicts or reopen triggers**, not re-establish every already-supported premise.

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

---

## 6. Viewpoint discipline

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

---

## 7. Alternative-first rule

Before a material architectural commitment, compare credible alternatives where they exist.

But do not manufacture a new alternative space when prior work already compared and accepted alternatives. First recover the prior comparison and ask whether a reopen trigger exists.

Examples of genuine live alternatives may include:

- broad sociotechnical SoI vs nested engineered SoI for a specific claim;
- distinct Work Engine subsystem vs distributed work-control policy;
- global persistent state vs domain-owned authoritative state plus derived working context;
- one adaptive model vs orchestrated specialized agents;
- global invariants vs capability-local methods;
- explicit workflow states vs latent adaptive control;
- accepted whole-system operating architecture vs a demonstrably simpler counter-design.

Compare alternatives on performance, complexity, transferability, observability, failure containment, maintainability, runtime feasibility and evidence status.

---

## 8. Promotion and lineage states

Architecture-candidate progression:

`DISCOVERED → FRAMED → SUPPORTED → CANDIDATE → TESTED → ACCEPTED → RETIRED/SUPERSEDED`

Lineage disposition for inherited design:

`RETAIN | RETAIN-WITH-BOUNDARY | REFINE | RELOCATE | MERGE | SUPERSEDE | REJECT | OPEN-CONFLICT`

`SUPPORTED` is not `TESTED`; `TESTED` is not universal validity; `ACCEPTED` is not permanent truth.

---

## 9. Complexity budget

Every construct creates vocabulary, implementation, context, evaluation, interaction and maintenance cost. It should justify itself by preventing a material failure class, enabling a material capability, reducing downstream complexity through a real invariant, improving transfer, enabling necessary assurance, or materially improving work economics / human agency.

Re-derivation itself also has a cost. Reopening an accepted question without new decision value is **architecture process waste**.

If a mechanism can remain reference knowledge, a bridge reference, a conditional capability, an operating-model configuration or a qualified inherited design rather than new global architecture, that remains a live alternative.

---

## 10. Work Engine status

`Work Engine` remains a **candidate abstraction**, not an accepted subsystem.

However, the predecessor lineage already contains mature work-control constructs, especially:

- Work Architecture / Work Units / Work Graph in `AI-native-Operating-Model`;
- Work Object / Work Product / Working State / Work Episode semantics in `human-ai-work-architecture`;
- Semantic Compiler / Minimum Sufficient Work in `Human-AI-Work-System`;
- a deliberate counter-design in `PAOS` that rejects universal formal Work Objects for ordinary work.

Therefore the Work Engine question must now be framed as a **reconciliation/selection problem among qualified priors**, not as blank-slate invention.

The remaining candidate function to explain is approximately:

> select and coordinate the minimum sufficient next work for a bounded work episode, while respecting parent purpose, current authoritative state, professional method, capability, evidence, authority and resource constraints.

The open question is whether existing predecessor mechanisms already solve this adequately and, if not, what exact incremental role the term `Work Engine` adds.

---

## 11. Current architecture freeze gate

Do not freeze a new conceptual architecture until:

- the SoI boundary is adequate for the intended claims;
- predecessor lineage and qualified priors have been recovered;
- every materially reopened prior question has an explicit trigger;
- major concerns have reference coverage;
- raw internal evidence has usable provenance;
- qualified prior designs have explicit dispositions;
- cross-view integration is coherent;
- genuinely live alternatives were compared;
- the performance model can discriminate the remaining alternatives;
- material uncertainties plus evaluation plans are explicit.

The reconstruction succeeds not when it produces the newest architecture, but when it identifies **which prior knowledge still deserves to survive and exactly where new evidence requires change**.
