# ADR-0001 — Reconstruct without discarding qualified prior design

**Status:** ACCEPTED FOR BOOTSTRAP / LINEAGE-CORRECTED  
**Date:** 2026-08-19

## Context

The Human–AI architecture estate contains substantial accumulated knowledge across multiple repositories: accepted architecture baselines, reference work, runtime candidates, evaluations, failure analyses, counter-designs and implementation experience.

It also exhibits architecture churn and a recurring risk that constructs developed for different concerns or architecture object types become layered into one global model or compared as if they were equivalent.

A direct refactor of only the immediate predecessor would inherit accidental ontology. A blank-slate reconstruction would create the opposite failure: loss of qualified prior knowledge and rediscovery-by-renaming.

## Decision

Create `Human-AI-Work-System-Next` as a **lineage-aware reconstruction program**, not simply the next version of one predecessor and not a clean-room architecture exercise.

During bootstrap:

1. recover the relevant predecessor **lineage**, not only `Human-AI-Work-System`;
2. classify prior material by epistemic/design status, including raw evidence, candidates, Qualified Prior Designs, runtime evidence and counter-designs;
3. treat a sufficiently scoped, referenced, reviewed/falsified and human-accepted prior design as **closed-but-reopenable**, not open-by-default;
4. use external references differentially — to challenge, transfer or resolve genuine open questions, not to re-prove every qualified premise;
5. keep reference knowledge, raw internal evidence, architecture decisions, runtime evidence and evaluation artifacts distinguishable;
6. preserve architecture object types: responsibility layer ≠ view ≠ integrity/control contract ≠ work-control policy ≠ capability/method ≠ runtime profile;
7. do not migrate predecessor folders, names or runtime rules by default;
8. do not assume that `Work Engine`, DWM, Semantic Compiler, Work Graph, Realization or prior lifecycle constructs retain their previous **architectural placement** merely because the concepts existed;
9. equally, do not re-derive a qualified mechanism such as Work Units, state/authority distinctions or Work→Outcome semantics without an explicit reopen trigger;
10. require genuinely live architecture alternatives to compete with credible qualified priors and simpler counter-designs.

## Qualified-prior reopen rule

Reopen an accepted prior question only for a named trigger:

- changed System of Interest or intended claim;
- new external evidence materially conflicts with the prior;
- new real-use failure exposes an unhandled mechanism;
- a materially stronger or simpler rival preserves the required semantics;
- two Qualified Prior Designs conflict;
- implementation/runtime reality makes the prior infeasible for intended use;
- audit shows the prior was not actually qualified for the inherited claim.

Without a trigger, the default is:

```text
recover → map → provisionally retain / relocate
```

not:

```text
forget → rederive → rename
```

## Consequences

### Positive

- reduces both inheritance bias and blank-slate rediscovery;
- preserves prior work with its actual maturity and scope;
- creates explicit provenance and burden-of-proof rules for architecture change;
- makes external research decision-relevant rather than encyclopedic;
- allows previous concepts to survive, move level, change representation, merge or be rejected without losing lineage;
- supports a smaller runtime even when the reference architecture remains rich.

### Costs

- predecessor lineage must be recovered and typed before major new derivation;
- status and authority cannot be inferred from filename age or terminology;
- some older intermediate artifacts retain historically superseded `Next` instructions and therefore require a current-state pointer;
- architecture progress is measured by resolved genuine deltas, not by new model count.

## Revisit triggers

Revisit this decision if:

- lineage-aware reconstruction still repeatedly rediscovers accepted prior mechanisms;
- Qualified Prior status prevents justified change despite strong new evidence;
- the type system proves unable to reconcile the strongest predecessor models;
- a simpler external/reference architecture demonstrably subsumes the problem better;
- evaluation shows architecture-level work adds no material value over task-local methods and capable base models.
