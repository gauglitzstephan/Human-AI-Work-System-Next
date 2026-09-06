# Information Capital Architecture Decision — Candidate — 2026-09-06

**Status:** CANDIDATE DECISION RECORD — not merged, not promoted, not installed as product runtime.  
**Branch:** `candidate/human-state-infrastructure-v0-1`  
**Decision object:** whether and how persistent State / Evidence / Knowledge / Artifact handling should become part of the Human–AI Work System.

## 1. Decision boundary

This record does **not** decide a new universal AI operating system. It decides the smallest candidate architecture needed to prevent durable Human/work information from disappearing into chats, research runs, transient model context or unqualified memory while preserving native ChatGPT/Work ownership of ordinary reasoning and execution.

The controlling current repository remains `main` until explicit Human acceptance and promotion. The Human-reported active Global CI is recorded separately and remains the product-runtime reference until another payload is actually installed and read back.

## 2. Problem supported by observed work

Repeated genuine work has shown several distinct persistence failures:

- qualified decisions and constraints are lost or reconstructed inconsistently across chats/runs;
- research sources and evidence are difficult to recover as a coherent basis for later work;
- durable syntheses, hypotheses, frameworks and models remain buried in conversations instead of becoming reusable knowledge;
- produced artifacts can exist without a reliable current/candidate/approved/released identity or quality state;
- the Human repeatedly reconstructs already-developed context and detects AI-resolvable state divergence;
- storing something in chat history, memory, a branch or a file does not by itself establish current authority or retrievability.

These are not one failure class. A state-only solution is insufficient because Evidence, Knowledge and Artifact continuity have different semantics and quality/authority rules.

## 3. Architecture decision candidate

Adopt, for genuine-use validation, the following **logical** architecture:

```text
Human judgment / authority
          │
          ▼
Native ChatGPT / Projects / Work / Codex / tools
          │
          ▼
Context assembly for current work
          │
          ▼
Information Capital control plane
  ├─ State
  ├─ Evidence
  ├─ Knowledge
  └─ Artifacts
          │
          ▼
Native systems of record / source locations
Drive · GitHub · Notion · Web · Gmail · other domain systems
```

### Candidate physical implementation

Use one structured Notion database, `Information Capital Registry v0.2`, as the current catalog/control-plane adapter.

It has four semantic `Kind`s:

- `state`
- `evidence`
- `knowledge`
- `artifact`

and free-text `Scope` / `Topic` fields rather than a closed domain taxonomy.

The registry does **not** require every source or artifact body to live in Notion. It records enough identity, meaning, provenance, lifecycle, authority, quality and location data to recover and use the object. The native source/artifact may remain in Drive, GitHub, Web, another app, or a future store.

### New-topic rule

A new Human topic does not require schema, enum, project or database creation.

1. Treat the input as working context.
2. Search for materially related persisted capital when work is consequential enough to benefit.
3. If nothing relevant exists, proceed normally.
4. Create a new scope/topic only when durable material actually emerges.

Example: `tax/2025` can arise from durable tax work without prior system administration.

### Scale rule

Do not persist every chat turn, web page, tool call or transient thought.

Prefer promoted objects at useful granularity, for example:

- one Research/Evidence Pack representing a bounded research run;
- individual Evidence objects only for especially authoritative or decision-critical sources;
- one durable investment-thesis Knowledge object rather than dozens of intermediate observations;
- one Artifact catalog entry per reusable work-product version/state, not every drafting turn.

## 4. Responsibility trace

| Requirement | Owner / mechanism | Candidate realization |
|---|---|---|
| Preserve what currently applies | durable State semantics | `Kind=state` with subtype/lifecycle/authority |
| Preserve source-bound support | Evidence semantics | `Kind=evidence` + source/location/provenance |
| Preserve reusable understanding | Knowledge semantics | `Kind=knowledge` + confidence/authority/relations |
| Preserve produced work-product identity | Artifact semantics | `Kind=artifact` + version/status/quality/location |
| Avoid Human reconstruction | runtime retrieval | CI/context-assembly behavior + connected registry read |
| Avoid chat-only durable outputs | runtime capture | authorized write after material durable output emerges |
| Keep source systems legitimate | systems of record | registry references rather than universal copying |
| Protect Human authority | authority rules | no AI inference → Human commitment/decision/release without basis |
| Scale to new topics | open scope/topic model | no closed domain enum or per-topic schema |
| Avoid information explosion | promotion/granularity policy | packs, durable syntheses, material-state threshold |
| Detect semantic regression | real-use evaluation | bounded genuine-work cases and Human corrections as evidence |

## 5. Maturity model

This maturity model is descriptive and used only to set the intended target for this Human; it is not a universal industry standard.

### M0 — Ephemeral Chat

- work exists mainly in individual conversations;
- little reliable cross-session continuity;
- Human reconstruction is normal.

### M1 — Native Workspace Continuity

- Projects, files, Memory, apps and native context provide useful continuity;
- persistence remains mostly implicit/probabilistic;
- authority/current-state distinction is weak.

### M2 — Persistent Information Capital

- durable State/Evidence/Knowledge/Artifact objects exist outside transient context;
- context is selectively reassembled from those objects;
- new durable outputs are captured with low Human maintenance;
- authority, lifecycle and artifact quality are explicit where material.

### M3 — Agentic Professional Work

- substantial work can be delegated with relevant context automatically assembled;
- Work/Codex/agents can create and update persistent capital as part of execution;
- Human review is concentrated on material judgment, acceptance, commitment and release;
- cross-session continuation requires little Human reconstruction.

### M4 — Durable Operational Automation

- long-running processes have reliable checkpoints/resume/monitoring;
- recurring agents/actions maintain state and information capital over time;
- observability, evaluation and permission boundaries are systematic.

### M5 — AI-native Organization

- multiple agentic roles/processes operate across business systems with institutional memory, identity, governance and evaluation loops.

## 6. Target maturity decision

**Target now: solid M2 with native paths into M3.**

Do not build M4/M5 infrastructure unless genuine work produces a specific unmet requirement that current ChatGPT/Work/plugins/automations cannot satisfy proportionately.

This means the near-term success claim is deliberately limited:

> The Human can start ordinary material work in ChatGPT without manually reconstructing durable prior State/Evidence/Knowledge/Artifacts, and durable outputs that matter to later work are persistently captured with low Human maintenance and correct authority/quality semantics.

## 7. Runtime candidate

The runtime behavior under evaluation is conceptually:

```text
RESOLVE current work context
        ↓
RETRIEVE relevant persisted capital when materially useful
        ↓
WORK using native ChatGPT / Work / tools
        ↓
ROUTE durable outputs by semantic kind
        ↓
CAPTURE only material durable objects
        ↓
READ BACK material writes where needed for the persistence claim
```

This is a responsibility model, not a mandatory visible lifecycle. Routine/simple chats should not incur registry ceremony.

The Candidate Global CI in:

`rebaseline/GLOBAL-CUSTOM-INSTRUCTIONS-INFORMATION-CAPITAL-CANDIDATE-2026-09-06.md`

is a proposed compact runtime carrier under the current 5,000-character product constraint. Its semantic equivalence to the Human-reported active CI is **not proven** by word-count fit. Installation, activation and behavioral conformance remain separate claims.

## 8. Genuine-use validation matrix

Use real work when these cases naturally recur. Do not manufacture tasks merely to tick boxes. Each case tests only the claims that matter to a concrete architecture decision.

| Real work case | Existing capital expected | Durable output likely | What success would support | Material failure signal |
|---|---|---|---|---|
| **Career — continue Mercedes** | pursuit decision; application standards; candidate evidence; current artifacts | revised CV/letter, new decision or open question | case continuation without Human reconstruction; correct authority/quality state | asks Human to restate known case; misses/contradicts active decision; treats working draft as approved |
| **Career — new opportunity** | reusable candidate evidence/standards, but no case state | new case scope, employer evidence, fit synthesis, pursue/defer decision | new topic/case forms without schema work; reusable capital transfers correctly | creates needless taxonomy/admin; imports irrelevant old case state; fails to persist material new case outputs |
| **Spatzennest — continue logo** | authoritative visual baseline decision; prior artifact/reference locations | new logo candidate/version; design decision | creative work starts from correct approved baseline without resurfacing obsolete reference | researches/uses wrong old logo; loses protected visual decisions; candidate not cataloged |
| **Investing — research a stock** | portfolio-strategy state; investment standards if any | evidence pack, thesis/risk knowledge, decision/open question, memo | research becomes reusable evidence/knowledge rather than chat-only prose | every URL becomes object; thesis/evidence collapse; AI recommendation silently becomes Human decision |
| **New domain — tax 2025** | perhaps global authority/working standards only | new scope, evidence refs, qualified tax knowledge/open questions/artifact | new domain arises organically without schema/project setup | cannot represent new topic without schema change; creates premature taxonomy; misses durable outputs |
| **Research-heavy strategy work** | prior strategy decisions/knowledge/artifacts | bounded research pack, updated synthesis/model, strategy artifact | source mass is compressed into useful durable capital with traceability | source sprawl; research disappears after chat; model/framework exists only as prose in conversation |
| **Correction mid-work** | active relevant capital | corrected/superseded state or artifact version | correction propagates to dependent current objects without rewriting unrelated history | old wrong state remains active; history silently overwritten; Human repeats correction later |
| **Chat → Work transition** | qualified State/Evidence/Knowledge/Artifacts for work object | finished Work artifact + new capital changes | Work receives enough context without rediscovery and returns durable results correctly classified | handoff omits protected state/evidence; Work recreates prior analysis; returned artifact/state not persisted |

## 9. Evaluation dimensions

For a material episode, evaluate only dimensions that can change the architecture decision:

1. **Retrieval correctness** — relevant durable capital was found; irrelevant material did not dominate.
2. **Continuity** — the Human did not have to reconstruct accessible qualified prior work.
3. **Semantic routing** — State, Evidence, Knowledge and Artifact were not collapsed into each other.
4. **Capture completeness** — durable outputs that matter to later work did not remain only in chat/Work.
5. **Authority integrity** — AI inference/recommendation did not become Human decision/commitment/approval/release without basis.
6. **Artifact integrity** — existence, version, quality state, Human acceptance and release remained distinguishable.
7. **Granularity / scale** — registry growth was useful rather than proportional to raw events/sources/tokens.
8. **Human burden** — no routine manual filing/tagging/reconstruction was required.
9. **Professional quality** — the persistence mechanism improved or at least did not degrade the actual work product.
10. **Proportionality** — retrieval/capture overhead earned its cost.

## 10. Merge gate

Do **not** merge this candidate merely because the schema and CI compile.

A merge recommendation requires bounded genuine-use evidence showing at minimum:

- successful retrieval and continuation in at least **two materially different existing domains/cases**;
- successful organic creation/capture in at least **one genuinely new topic/scope** without schema modification;
- at least **one research-heavy case** demonstrating useful evidence/knowledge granularity rather than source sprawl;
- at least **one produced Artifact** whose working/candidate/approved state is correctly represented;
- no observed material authority regression;
- no recurring need for Human manual registry maintenance;
- no material professional-quality regression attributable to the runtime hook;
- any CI semantic compression used for installation has survived relevant regression comparison against the Human-reported active CI.

These are decision gates, not statistical proof of universal reliability.

## 11. Repair / retire conditions

### REPAIR the candidate when

- the architecture is useful but a localized capture/retrieval/schema/CI/tool mechanism repeatedly fails;
- a material semantic type or lifecycle relation is missing;
- Notion proves operationally awkward while the logical model remains useful;
- registry granularity creates avoidable noise;
- runtime retrieval/capture is too inconsistent but could plausibly be improved at a lower layer.

### RETIRE or materially reduce the candidate when

- native ChatGPT/Projects/Memory reliably provide the needed durable semantics without external state burden;
- Human maintenance becomes routine;
- retrieval noise regularly harms work;
- the system captures lots of objects but does not materially improve continuity/reuse/quality;
- a simpler store-independent mechanism achieves the same result;
- future native OpenAI typed-state/context infrastructure makes the external control plane redundant.

## 12. Current decision state

**KEEP AS CANDIDATE / DO NOT MERGE YET.**

Protected current claims:

- `main` remains repository authority;
- the Human-reported active Global CI remains the current product-runtime reference until changed in-product;
- `Information Capital Registry v0.2` exists as a candidate physical adapter;
- the logical four-kind model and M2 target are candidates for genuine-use validation;
- the 4,970-character information-capital-aware CI is uninstalled/unvalidated unless the Human explicitly installs it;
- further architecture expansion is not justified before genuine-use evidence identifies a concrete gap.

## 13. Next legitimate transition

1. Human reviews this decision record and, if acceptable, may authorize installation of the information-capital-aware Global CI Candidate.
2. Continue normal real work.
3. On the first relevant genuine-use cases, record only material support/failure evidence against the matrix above.
4. After the merge gate is sufficiently informed, decide `KEEP / REPAIR / RETIRE / MERGE`.

Do not create another architecture version merely because a test has not yet occurred.