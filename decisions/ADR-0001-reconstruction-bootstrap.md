# ADR-0001 — Reconstruct rather than directly refactor

**Status:** ACCEPTED FOR BOOTSTRAP  
**Date:** 2026-08-19

## Context

The predecessor `Human-AI-Work-System` contains substantial accumulated knowledge: architecture versions, runtime instructions, reference work, evaluations, failure analyses, and implementation experience.

It also exhibits architecture churn and a recurring risk that constructs developed for different concerns become layered into a single global model or runtime. Direct refactoring would therefore inherit both valuable knowledge and potentially accidental ontology.

The reconstruction needs to preserve knowledge without granting prior structure automatic authority.

## Decision

Create `Human-AI-Work-System-Next` as a **reconstruction program**, not as the next version of the predecessor architecture.

During bootstrap:

1. treat the predecessor repository as a primary evidence and knowledge source;
2. use state-of-the-art external references before major derivations;
3. establish the System of Interest, operational context, concerns, requirements, performance model, and architecture method before freezing a structural decomposition;
4. keep reference knowledge, internal evidence, architecture decisions, and evaluation artifacts distinguishable;
5. do not migrate predecessor folders, names, or runtime rules by default;
6. do not assume that `Work Engine`, `Capabilities`, `Environment`, DWM, Semantic Compiler, Work Graph, Realization, or prior lifecycle states retain their previous architectural status;
7. require architecture candidates to compete with credible alternatives and simpler baselines.

## Consequences

### Positive

- reduces inheritance bias;
- preserves prior work as knowledge capital;
- creates explicit provenance for architectural decisions;
- makes cross-disciplinary reference coverage part of the method;
- allows previous concepts to survive, move level, change form, or be rejected based on evidence;
- creates a path to a smaller empirically justified runtime if that is what the evidence supports.

### Costs

- some prior work must be re-qualified rather than copied;
- terminology may change;
- architecture progress initially appears slower because problem definition and reference synthesis precede structural freeze;
- duplicated historical material must be avoided through references rather than wholesale copying.

## Revisit triggers

Revisit this decision if:

- reconstruction loses material validated behavior from the predecessor with no compensating benefit;
- the new architecture method proves unable to integrate predecessor evidence efficiently;
- a reference architecture is found that demonstrably subsumes the problem better than a custom reconstruction;
- evaluation shows that architecture-level work adds no material value over task-local methods and capable base models.
