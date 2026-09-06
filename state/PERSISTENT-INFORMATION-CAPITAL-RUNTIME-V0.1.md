# Persistent Information Capital Runtime v0.1

**Status:** CANDIDATE
**Purpose:** operationalize capture and retrieval across State, Evidence, Knowledge and Artifact stores so durable outputs do not remain only in Chat/Work context.

## 1. Existence rule

A category is not durable information capital merely because it is named, discussed or generated. It counts as capital only when the material object is actually persisted in an identified store with enough metadata to retrieve, qualify and maintain it.

The four operational stores are:

1. **Human State Registry** — what currently applies: decisions, constraints, preferences, standards, commitments, authority and open/resolved questions.
2. **Evidence Registry** — source-bound material: documents, webpages, datasets, research sources, observations and other evidence references.
3. **Knowledge Library** — qualified syntheses: findings, hypotheses, models, frameworks, principles and learnings.
4. **Artifact Registry** — produced work products: CVs, strategies, analyses, memos, logos, specifications, presentations, documents and other reusable deliverables.

Sources and artifacts may remain physically stored in their legitimate native systems. The registries must preserve stable identity/location, provenance, scope, status and relevant cross-references.

## 2. Runtime contract

For material work, the AI should perform these transformations when the relevant connected stores are available:

### Before consequential work — RETRIEVE

Retrieve only the relevant persisted objects needed for the current work:

- current authoritative State;
- material Evidence already acquired;
- reusable Knowledge already qualified;
- current/relevant Artifacts and their quality/authority state.

Do not ask the Human to reconstruct accessible persisted state. Do not dump entire registries into context.

### During work — ROUTE

When durable material is produced, classify it by what it *is*, not by where it appeared:

- fact/source/observation/research source -> Evidence Registry;
- durable synthesis/model/hypothesis/framework/learning -> Knowledge Library;
- decision/constraint/preference/standard/commitment/authority/open question -> Human State Registry;
- produced reusable work product -> Artifact Registry.

One episode may create several objects across different stores.

### At material transition or close — CAPTURE

Persist all durable objects whose future loss would materially degrade continuity, judgment, quality, reuse or auditability.

Do not persist routine conversation, transient brainstorming, duplicated source material or low-value intermediate text by default.

### After capture — READBACK

When a material persistent write occurs, read back or otherwise verify the written object where the surface permits it. Never claim persistence when the write did not occur or could not be verified sufficiently for the claim.

## 3. Authority and quality

- Human-explicit decisions, commitments, constraints, acceptance and release keep Human authority.
- AI-generated or AI-synthesized Knowledge is not automatically Human-adopted.
- An Artifact's existence does not imply fitness for use. Track working/candidate/approved/released and quality state separately.
- Evidence storage does not make a claim true; preserve provenance and source authority.
- State, Knowledge, Evidence and Artifact references can point to each other but must not collapse their semantic types.

## 4. Current v0.1 implementation

Operational registries currently exist in Notion as:

- `Human State Registry v0.1`
- `Evidence Registry v0.1`
- `Knowledge Library v0.1`
- `Artifact Registry v0.1`

The logical runtime remains store-independent. Notion is the current implementation adapter, not a permanent architectural invariant.

## 5. Daily-use target

The Human should normally continue working in natural language. Registry maintenance is an AI responsibility when connected read/write capability is available and authority permits the write.

The Human should be interrupted only for material authority, ambiguity, acceptance, commitment or release decisions that cannot be inferred legitimately.

If manual filing, tagging or duplicate entry becomes normal Human work, the implementation fails its intended operating model and must be repaired or reduced.

## 6. Validation

Do not promote this runtime merely because the registries exist. Genuine use must demonstrate:

- relevant state/evidence/knowledge/artifacts are retrieved without Human reconstruction;
- durable outputs are actually captured rather than left in Chat/Work;
- retrieval noise stays low;
- artifact authority/quality is not confused;
- Human maintenance burden remains low;
- cross-session continuation and reuse materially improve.

Observed failures must be localized to capture, classification, storage, retrieval, authority, quality or surface/tool availability rather than answered with new architecture by default.
