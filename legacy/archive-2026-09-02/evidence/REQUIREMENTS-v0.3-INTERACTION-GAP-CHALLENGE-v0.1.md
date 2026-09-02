# Requirements v0.3 Interaction Gap Challenge v0.1

**Status:** CANDIDATE EVIDENCE — bounded Requirements challenge and repair basis; no Promotion or architecture change by itself  
**Date:** 2026-08-28  
**Reviewed object:** pre-repair `foundation/CONCERNS-AND-REQUIREMENTS-v0.3-CANDIDATE.md`, blob `90244af829d223f1de2f2969738178aa35a721cb`  
**Current authority:** `main/CURRENT.md`; Requirements v0.2 remains controlling and Target Architecture v0.2 remains closed  
**Repair branch:** `candidate/requirements-v0.3-interaction-repair-v0.1`

## 1. Claim boundary

This challenge asks whether identified Human–AI interaction gaps are already normatively sufficient, under-specified, only realization gaps, or genuinely new solution-neutral Requirements.

It does not evaluate a particular UI, prescribe a Chat/Work/Codex allocation, establish Runtime conformance, accept Requirements v0.3, reopen Target Architecture v0.2 or authorize Promotion.

## 2. Disposition rules

| Disposition | Test |
|---|---|
| `ALREADY_SUFFICIENTLY_COVERED` | The normative obligation and material failure mode are sufficiently derivable from the Candidate. |
| `UNDER_SPECIFIED` | A legitimate Requirement owner exists, but a material interaction failure could pass the current wording. |
| `REALIZATION_ONLY` | Requirements are sufficient; the remaining gap is a UI, Runtime, contract, carrier or evaluation problem. |
| `NEW_REQUIREMENT` | A material provider-neutral obligation is absent and cannot be derived without stretching existing Requirements. |

Classification is by primary defect. A realization mechanism may still be needed for an under-specified or new Requirement.

## 3. Internal and external evidence basis

Internal basis:

- controlling Requirements v0.2 and the pre-repair v0.3 Candidate;
- accepted Target Architecture v0.2 and the existing v0.3 compatibility review;
- `realization/E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md`;
- `realization/E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md`;
- current Route-B v0.6 Runtime carriers and observed state, coordination, meta-work and Human-reconstruction failures.

Qualified external challenge basis:

- Microsoft HAX Design Library: capability and limit communication, correction, dismissal, explanation, feedback, global controls and change notification — https://www.microsoft.com/en-us/haxtoolkit/library/
- Google PAIR, Mental Models: capability/limit understanding and calibrated expectations — https://pair.withgoogle.com/chapter/mental-models/
- Google PAIR, Explainability and Trust: reliance calibration and action-relevant explanations — https://pair.withgoogle.com/chapter/explainability-trust/
- Google PAIR, Feedback and Control: understandable feedback effects, control and fallback — https://pair.withgoogle.com/chapter/feedback-controls/
- Google PAIR, Errors and Graceful Failure: paths forward, takeover and re-entry — https://pair.withgoogle.com/chapter/errors-failing/
- NIST AI RMF, Human-AI Interaction: roles, oversight, presentation effects, bias and empowered Human challenge — https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/
- ISO 9241-11 and ISO 9241-210: intended-use usability and human-centred quality — https://www.iso.org/standard/63500.html and https://www.iso.org/standard/77520.html
- W3C WCAG: perceivable, operable, understandable and robust accessibility — https://www.w3.org/WAI/standards-guidelines/wcag/

These references support concern and failure-mode validity. They do not by themselves establish the exact internal Requirement wording.

## 4. Gap classification

| Gap candidate | Existing Candidate trace | Disposition | Reason |
|---|---|---|---|
| Ongoing Human–AI coordination quality: observable, understandable, predictable, controllable and resumable collaboration | CR-07/08/09/13 cover ingredients | `NEW_REQUIREMENT` | No existing Requirement treats the ongoing coordination relation itself as a conditional Performance object. Each ingredient could appear locally conformant while initiative, common state and continuation remain unusable. |
| Mental-model and reliance calibration | CR-07 responsible reliance and legibility; CR-08 capability/status; CR-13 actual Runtime conditions | `UNDER_SPECIFIED` | Relevant capability, limits, uncertainty, initiative and effects can remain misleading without clearly violating the current text. |
| Correction, stopping, graceful recovery and re-entry | CR-07 correctable/stoppable; CR-09 recovery semantics; CR-13 reconstructability; CCR-02 recovery | `ALREADY_SUFFICIENTLY_COVERED` | The general normative obligation exists. Undo, cancel, manual fallback, retry and re-entry flows are realization/evaluation choices. |
| Interaction Economics | CR-10 explicitly includes attention, interruption, correction, review, latency, coordination and observability | `ALREADY_SUFFICIENTLY_COVERED` | A further Requirement would duplicate the existing Whole-System Economics obligation. |
| Feedback and adaptation integrity | CR-14 evidence-bound learning and controlled change | `UNDER_SPECIFIED` | The Human-facing scope, effect, timing, persistence, inspectability and reset/correction semantics of feedback or adaptation are not sufficiently explicit. |
| Intended-use usability and accessibility | CR-05 intended-use Professional Performance Floor | `UNDER_SPECIFIED` | CR-05 can own the concern, but Human-facing use could avoid explicit usability/accessibility activation. No separate Requirement family is needed. |
| Cross-surface handoff and common ground | CR-02/08/09/13 | `REALIZATION_ONLY` | Scope, status, divergent state and Runtime fidelity are normatively covered; handoff and return contracts are realization mechanisms. |
| Human-facing progress, initiative, gate and next-action visibility | CR-07 legibility; CR-08 status; CR-10 closure and attention | `REALIZATION_ONLY` | Progress panels, activity logs, gate cards and Control Return are carriers, not Requirements. |
| Installed Runtime/source identity and change transparency | CR-13 Runtime fidelity; CR-14 controlled change | `REALIZATION_ONLY` | Deployment readback and installed-carrier identity are concrete realization claims. |
| Multi-Human/stakeholder contestability | CR-07 agency; CR-08 Authority; CCR-02 Rights/Fairness | `UNDER_SPECIFIED` | Existing owners are legitimate, but disagreement and challenge are not sufficiently activated when several responsible or materially affected Humans are involved. |
| Anthropomorphic or relational miscalibration | CR-07 responsible reliance, capability and autonomy; CCR-02 consequential risk | `UNDER_SPECIFIED` | Presentation could materially misrepresent capability, Authority, accountability or relationship without a clear failure condition. |

## 5. Repair disposition

The smallest coherent repair is:

1. add one conditional Requirement, `CCR-05 — Human–AI interaction and coordination integrity`;
2. strengthen CR-05 only for intended-use usability/accessibility where Human-facing interaction is material;
3. strengthen CR-07 only for reliance calibration and materially misleading presentation;
4. strengthen CR-14 only for Human-facing feedback/adaptation scope and control;
5. retain UI elements, surface allocation, handoff schemas, Runtime identity/readback and concrete controls at realization/evaluation level.

Resulting normative packaging:

```text
v0.2 controlling:        5 Interpretation + 14 Core + 7 Conditional = 26
v0.3 pre-repair:         3 Interpretation + 15 Core + 4 Conditional = 22
v0.3 repaired Candidate: 3 Interpretation + 15 Core + 5 Conditional = 23
```

The repair restores a missing interaction obligation without returning to the wider v0.2 element count or introducing a universal interaction lifecycle.

## 6. Anti-bloat and semantic-preservation checks

- No dashboard, fixed stage model, controller, Agent, state store or product surface becomes mandatory.
- Interaction state is surfaced only where it can materially change judgment, reliance, action, Authority or Continuity.
- The Human is not required to reconstruct AI-accessible hidden state or perform AI-resolvable QA.
- Generic correction/recovery and Interaction Economics remain with existing Requirements rather than being duplicated.
- Provider-specific Chat/Work/Codex behavior remains realization evidence, not general Work-System semantics.

## 7. Supported claim and non-claims

> The pre-repair v0.3 Candidate has one genuine conditional Human–AI coordination Requirement gap and several localized under-specifications. One new CCR plus bounded strengthening of CR-05, CR-07 and CR-14 is the smallest supported Requirements repair.

This record does not establish Requirements acceptance or Promotion, Runtime conformance, empirical cross-domain completeness, UI quality, architecture optimality or outcome effectiveness.
