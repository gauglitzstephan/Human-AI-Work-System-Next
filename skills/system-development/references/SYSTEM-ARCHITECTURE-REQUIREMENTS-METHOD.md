# System Requirements / Architecture Reasoning Method v0.4

**Status:** scoped internal System-Development method.  
**Use when:** this Human–AI Work System requires requirements clarification, architecture comparison/change, or conformance reasoning.

This method is not a universal substitute for formal systems-engineering, requirements-engineering or software-architecture standards. When the intended claim requires such a professional standard, retrieve and apply it explicitly.

## Objective

Produce the smallest requirements/architecture result sufficient for the current system claim. Preserve existing structure when it can adequately meet the need; ownership alone is not performance evidence.

## Method

1. **Bind the exact claim and boundary** — what decision, change or evaluation is required, for which system/object/version and intended outcome?
2. **Recover authoritative state** — current requirements, accepted architecture, decisions, runtime constraints, observed failures and existing valid structures.
3. **Separate need from proposed solution** — user wording, current artifact or proposed component is evidence of intent, not automatically the requirement.
4. **Form only material requirements/performance needs** — functional outcome, intended use, quality floors, authority/state/transition constraints and relevant failure modes.
5. **Trace responsibility/ownership** — each material requirement must have a legitimate owner/mechanism; do not turn every concern, distinction or view into a component, agent or store.
6. **Compare peer routes only when the choice is materially open** — preserve/repair/reuse/adapt/compose/build/no-action or narrower use at one decision level. Choose by required performance, recurrence, consequences, uncertainty and total cost including Human correction. A broader mechanism can be justified by inadequate performance despite existing ownership; no fixed escalation ladder or default controller follows.
7. **Check realization feasibility** — establish the actual runtime/provider/state/permission/carrier conditions needed for any implementation claim. State what the proposed mechanism actually does to detect or prevent the material failure and what observable result would support that claim. Distinguish semantic owner, active carrier, activation path and execution owner. “Native owns it” and “Skill available” do not close an unresolved execution or professional-validity gap. Check the relevant operation or retain that realization claim as unverified.
8. **Check relational integrity** — requirement → owner → mechanism → runtime claim, with evidence appropriate to each link. Detect unowned transformation, type collapse, authority contradiction and semantic loss.
9. **Stop at the required claim** — do not extend into implementation, promotion or additional architecture work unless the current task requires it.

## Output

Proportionately:

- current authoritative baseline;
- exact requirement/problem delta;
- candidate route or architecture delta;
- responsibility/mechanism trace where material;
- unresolved assumptions/dependencies;
- exact supported claim and any genuine reopen condition.

## Failure modes

- architecture-first invention;
- requirement = literal request or proposed means;
- static wording coverage mistaken for runtime realization;
- mixed-level alternatives compared as peers;
- logical distinctions reified as permanent architecture objects;
- implementation simplicity used to justify semantic loss;
- internal method presented as an external professional standard.
