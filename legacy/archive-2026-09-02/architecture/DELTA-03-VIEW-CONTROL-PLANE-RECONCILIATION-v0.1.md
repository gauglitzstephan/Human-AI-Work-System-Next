# Δ3 — View vs Control-Plane Reconciliation v0.1

**Status:** PROVISIONAL DISCRIMINATION / LINEAGE-AWARE  
**Question:** Can the accepted eight Architecture Views and five accepted cross-cutting Control Planes be simplified without losing material semantics, ownership, observability or change control?  
**Qualified priors:** `human-ai-work-architecture` v1.3.1 (8 Views) + `AI-native-Operating-Model` v0.2 (5 responsibility layers + 5 control planes).

---

# 1. Executive decision

## Do not choose `8 Views` versus `5 Control Planes`.

They are different architecture object types.

```text
Responsibility Layers
= where persistent architectural responsibility lives

Architecture Views
= how selected concerns are represented and inspected

Control Planes
= cross-layer integrity semantics that must remain coherent
```

The duplication problem comes from presenting all three as peer decompositions.

### Δ3 disposition

```text
Five responsibility layers                 RETAIN as leading parent responsibility model
Eight accepted views                       RETAIN as architecture-description/viewpoint set
Five “control planes”                      RETAIN semantics, RELOCATE representation
                                            → Cross-Cutting Integrity Contracts / Lenses
                                            → traced through relevant Views + Layers
```

No evidence currently justifies deleting one of the eight Views or adding a ninth.

No evidence currently justifies treating the five Control Planes as another structural hierarchy beside the Layers and Views.

The simplification is therefore **type correction and representation compression**, not semantic deletion.

---

# 2. Qualified prior sets

## 2.1 Responsibility architecture

From `AI-native-Operating-Model`:

```text
Strategic Architecture
Operating Architecture
Work Architecture
Execution Architecture
Learning Architecture
```

Question answered:

> **Which class of durable architectural responsibility owns this problem/change?**

---

## 2.2 Architecture-description Views

From `human-ai-work-architecture` v1.3:

```text
V1 Mission & Outcome
V2 Work Process
V3 Information & State
V4 Capability & Resource
V5 Interaction & Authority
V6 Quality & Assurance
V7 Governance & Learning
V8 Execution Context & Integration
```

Question answered:

> **Which concern-specific representation is needed to understand/evaluate the architecture?**

A View may cut through several responsibility layers.

---

## 2.3 Prior Control Planes

From `AI-native-Operating-Model`:

```text
CP1 Reality & Provenance
CP2 Authority, Governance & Security
CP3 Assurance & Risk
CP4 Performance, Economics & Value
CP5 Knowledge, Configuration & Change
```

Question answered:

> **Which semantics must remain consistent as work/architecture crosses responsibility boundaries?**

These are explicitly cross-cutting in the qualified prior and were never intended as a workflow.

---

# 3. Correspondence test

## CP1 — Reality & Provenance

Primary View carriers:
- V3 Information & State;
- V6 Quality & Assurance;
- V8 Execution Context & Integration.

Layer applicability:
- all five layers.

Unique role:
- common semantics/invariants for source, observation, inference, provenance, authoritative state and current reality.

**Decision:** retain as cross-cutting Integrity Contract, not separate structural plane.

---

## CP2 — Authority, Governance & Security

Primary View carriers:
- V5 Interaction & Authority;
- V7 Governance & Learning;
- V8 Execution Context & Integration.

Layer applicability:
- all five layers.

Unique role:
- preserve identity/capability/access/decision-right/authorization/accountability distinctions across conceptual and runtime boundaries.

**Decision:** retain as cross-cutting Integrity Contract.

---

## CP3 — Assurance & Risk

Primary View carriers:
- V6 Quality & Assurance;
- V5 Interaction & Authority where Human/independent assurance matters;
- V8 Execution Context for actual test/evaluator environment.

Layer applicability:
- Strategic claims, Operating capabilities, Work Products, Execution and Learning claims all require claim-relative assurance.

**Decision:** retain as cross-cutting Integrity Contract.

---

## CP4 — Performance, Economics & Value

Primary View carriers:
- V1 Mission & Outcome;
- V4 Capability & Resource;
- V6 Quality & Assurance;
- V7 Governance & Learning.

Layer applicability:
- all five layers, at different horizons.

Unique role:
- prevent local output/throughput/component metrics from breaking end-to-end value and resource economics.

**Decision:** retain as cross-cutting Integrity Contract.

---

## CP5 — Knowledge, Configuration & Change

Primary View carriers:
- V3 Information & State;
- V7 Governance & Learning;
- V8 Execution Context & Integration.

Layer applicability:
- strategy assumptions, Operating capabilities/patterns, Work methods/state, runtime configuration, Learning promotion.

Unique role:
- preserve ownership/status/version/supersession and change propagation across boundaries.

**Decision:** retain as cross-cutting Integrity Contract.

---

# 4. Why the eight Views are not reducible to the five integrity contracts

Each View contains material representation concerns that no Control Plane owns.

Examples:

### V2 Work Process
Contains Work formation, transformation, dependencies, Work Products, Work Units, transitions and closure.

No Control Plane supplies this work semantics.

### V4 Capability & Resource
Contains capability composition, method/resource fit and resource depth.

The Economics contract constrains it but does not replace it.

### V8 Execution Context & Integration
Contains concrete runtime binding: instruction stack, context stack, model/runtime, Workflow Packages, providers, access relationships and subject/evaluator contexts.

Security/Change contracts constrain V8 but do not replace the runtime-integration representation.

### V1 Mission & Outcome
Contains intended purpose, beneficiary, use and closure/outcome semantics.

Performance/Value constrains these claims but does not replace the Mission/Outcome representation.

**Finding:** collapsing eight Views to the five Control Planes would destroy material model kinds.

---

# 5. Why the five integrity contracts are not redundant with Views

A View shows one concern domain. A cross-cutting contract ensures semantic consistency **across** Views and Layers.

Example:

```text
V3 says what authoritative state means
V5 says who may change it
V6 says what evidence qualifies it
V8 says which runtime store/version actually exists
```

Without a shared Reality/Authority/Change contract, the same concepts can drift across Views.

Thus the control-plane semantics add value as **cross-view invariants**, even when no separate “plane” object is shown to a user.

---

# 6. Proposed representation

## 6.1 Parent architecture

```text
RESPONSIBILITY LAYERS
Strategic
Operating
Work
Execution
Learning
```

This answers ownership/architectural responsibility.

## 6.2 Architecture description

```text
VIEWS
Mission & Outcome
Work Process
Information & State
Capability & Resource
Interaction & Authority
Quality & Assurance
Governance & Learning
Execution Context & Integration
```

Activate/use only Views relevant to the architectural decision.

## 6.3 Cross-cutting integrity contracts

Rename/reframe the five Control Planes in the Next reconstruction as:

```text
IC1 Reality & Provenance Integrity
IC2 Authority / Governance / Security Integrity
IC3 Assurance & Risk Integrity
IC4 Performance / Economics / Value Integrity
IC5 Knowledge / Configuration / Change Integrity
```

This is a representation candidate, not a claim that prior terminology was incorrect.

The key difference is semantic:

> **Integrity Contracts constrain and trace across Layers/Views; they are not another decomposition of the system.**

---

# 7. Traceability contract

For a material architecture decision:

```text
Concern
→ owning Responsibility Layer(s)
→ required View(s)
→ applicable Integrity Contract(s)
→ architecture decision/mechanism
→ runtime realization where relevant
→ verification/evidence
```

Not every decision needs every View or Integrity Contract.

Example:

```text
“Can an AI agent archive incoming email automatically?”

Owning layers:
  Operating + Execution

Views:
  V2 Work Process
  V3 State
  V5 Authority
  V6 Assurance
  V8 Execution Context

Integrity contracts:
  IC1 Reality/Provenance
  IC2 Authority/Security
  IC3 Risk/Assurance
  IC4 Economics if recurring cost/burden matters
  IC5 Change/Config for persistent automation
```

The model remains rich while activation stays proportional.

---

# 8. Compression test

### Alternative A — Five Layers only

**Reject:** loses concern-specific representation and runtime/state/authority clarity.

### Alternative B — Eight Views only

**Reject as complete parent model:** Views describe but do not establish durable responsibility ownership cleanly enough across Strategy/Operating/Work/Execution/Learning.

### Alternative C — Five Layers + Eight Views + Five peer Control Planes

**Reject representation:** semantically valid but invites dimensional confusion and perceived architecture bloat.

### Alternative D — Five Layers + Eight Views + five cross-cutting Integrity Contracts

**Leading candidate.**

Preserves qualified semantics while making the type system explicit and reducing false hierarchy.

---

# 9. Falsifiers / reopen triggers

Reopen the eight-View set if:
- a recurring architecture decision cannot be represented without forcing unrelated concerns into one View;
- two Views repeatedly have identical models/owners and no distinct decision value;
- real runtime/architecture work shows a missing model kind.

Reopen the Integrity Contract representation if:
- the five contracts become generic slogans with no traceable effect;
- they cannot be checked across Views/Layers;
- an integrity concern is fully owned by one View/Layer with no cross-boundary role;
- the representation increases architecture ceremony in ordinary implementation work.

---

# 10. Δ3 result

| Question | Disposition |
|---|---|
| Five responsibility layers | **RETAIN leading parent model** |
| Eight Views | **RETAIN** |
| Five Control Plane semantics | **RETAIN** |
| Control Planes as peer architecture axis | **DO NOT RETAIN in Next representation** |
| Reframe as Integrity Contracts / Lenses | **PROMOTE as leading representation candidate** |
| Add/remove architecture View now | **NO** |

### Net effect

```text
semantic content retained
architecture type confusion reduced
no new layer
no new view
one axis demoted from decomposition → cross-cutting contract
```

Remaining genuine deltas:

- Δ4 Adaptive Work-Control / Semantic Compiler value;
- Δ5 Architecture→Runtime semantic compilation;
- Δ6 Knowledge Capital ownership/promotion.
