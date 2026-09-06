# Persistent Information Capital Runtime v0.2

**Status:** CANDIDATE
**Supersedes:** v0.1 as the current candidate implementation model.

## 1. Operational model

Use **one physical Information Capital Registry** with four semantic object kinds:

- `state`
- `evidence`
- `knowledge`
- `artifact`

The four kinds remain semantically distinct but are exposed as filtered views, not separate operational databases.

Current Notion adapter: `Information Capital Registry v0.2`.

The prior four v0.1 registries remain pilot/history only and are not the target runtime.

## 2. Why one registry

The runtime must not require schema work when a new topic appears and must not query four stores on every material turn.

A new topic, project, case, entity or question is represented through free-form `Scope` and `Topic`; it does not require a new enum, table, Project, folder or schema migration.

A topic does not become persisted merely because it is mentioned. It becomes durable when the first material object worth preserving is created.

## 3. New-topic behavior

For materially relevant user input:

1. infer the current work scope/topic/entity from the request and accessible context;
2. query the unified registry for matching current objects;
3. if a matching scope exists, reuse it and retrieve only relevant objects;
4. if no matching scope exists, continue as a new working context without creating administrative state;
5. when the work creates the first durable object, assign a stable scope and persist that object;
6. later objects reuse that scope unless evidence justifies a split or merge.

Do not force every conversation into an existing Career/Investing/etc. bucket. Those are useful scopes, not a closed ontology.

## 4. Retrieval

For material work, use one scoped retrieval against the registry.

Search order:

1. exact/near current object, case, entity or topic;
2. parent scope/domain where relevant;
3. global standards/authority only where applicable.

Return only the relevant subset of current objects plus materially useful resolved/history objects.

Do not scan or inject the full registry by default.

## 5. Capture and routing

Classify durable outputs by semantics:

- **state** — decisions, constraints, standards, authority, preferences, commitments, open/resolved questions, current claims whose future validity matters;
- **evidence** — source-bound material or a durable pointer to a source/evidence bundle;
- **knowledge** — qualified findings, hypotheses, models, frameworks, synthesis, principles or learnings;
- **artifact** — reusable produced work products and their location, version, authority and quality state.

Persist only when future loss would materially degrade continuity, judgment, quality, reuse or auditability.

## 6. Scale rule for evidence/research

Do not register every webpage, search result or transient datapoint.

Default research capture is an **Evidence/Research Pack**: one durable object pointing to the research output or source bundle and summarizing scope/provenance.

Promote an individual source to its own evidence object only when it is decision-critical, authoritative, contested, likely to be reused independently, or required for audit/verification.

This keeps the registry compact while preserving source traceability.

## 7. Artifact rule

Artifacts remain in the best native location (Drive, GitHub, Notion, generated file, etc.). The registry stores the durable pointer plus scope, version, status, authority and quality state.

Artifact existence does not imply approval or fitness for use.

## 8. Daily runtime

For material work:

`RESOLVE SCOPE -> RETRIEVE -> WORK -> ROUTE -> CAPTURE -> READBACK`

This is a behavioral contract, not a visible user ritual or custom controller.

The Human should normally work in natural language. Registry maintenance is an AI responsibility when tool access and authority permit it.

No write is required when no durable object changed.

## 9. Runtime carrier

The repository is specification/audit, not the trigger.

The product runtime needs a compact instruction in the installed Global Custom Instructions and, where Project Instructions override them, equivalent project-level semantics:

- retrieve relevant persisted information capital for material work;
- do not ask the Human to reconstruct accessible persisted objects;
- persist durable new objects to the unified registry when authority permits;
- verify material writes;
- never treat storage as authority.

## 10. Validation

Promote only if genuine use shows:

- new topics require no manual setup;
- material re-entry retrieves the correct prior objects;
- durable state/evidence/knowledge/artifacts are captured without Human filing work;
- research mass does not flood the registry;
- artifact authority/quality remains explicit;
- retrieval noise and maintenance burden remain low.

Localize failures to scope resolution, retrieval, classification, capture, storage, authority, quality, or product/tool availability before changing architecture.