# Human State Infrastructure v0.1

**Status:** CANDIDATE
**Role:** thin, model-independent durable Human/domain state layer for AI-native work. It is not a runtime controller, workflow engine, memory replacement, or universal knowledge-management system.

## 1. Purpose

Persist only qualified state whose loss, confusion, silent reinterpretation, or stale reuse would materially degrade future Human–AI work.

The layer exists to answer, with provenance and authority, questions such as:

- What currently applies?
- What has the Human actually decided?
- What evidence or source supports a claim?
- What constraints and standards govern this work?
- What is committed, open, resolved, superseded, or expired?
- What may the AI decide or do autonomously, and what remains Human/domain authority?

Native ChatGPT/Work owns reasoning, planning, tool choice, execution and ordinary adaptation. Projects and memory provide working continuity and convenience. Domain systems retain their own authoritative data. Human State Infrastructure preserves the small durable subset that should survive model, chat, project and provider changes.

The operational registry can be understood as a **State Library**: a typed, provenance-aware index of durable current and historical state. It is not the Human's entire Knowledge Capital. Source documents, research, models, artifacts and domain-native records remain in their legitimate systems; the State Library records what currently applies, what is authoritative, what was decided, what remains open, what has been resolved, and how those states relate to source material.

## 2. Core model

Use one generic `StateObject` with typed semantics rather than separate incompatible stores.

Required logical fields:

- `id` — stable identifier
- `type` — one of the permitted state types
- `statement` — atomic meaning
- `status` — lifecycle state
- `scope` — where the object applies
- `authority_owner` — legitimate owner of the state
- `assertion_mode` — how the state entered the system
- `provenance` — source/reference and time where applicable
- `validity` — effective/review timing where applicable
- `relations` — supports, based_on, supersedes, constrained_by, governed_by, resolves, related_to

Optional fields are added only where semantically needed, e.g. confidence for epistemic claims or sensitivity for access handling.

## 3. Permitted state types

1. `evidence` — source-bound observation or material supporting a claim.
2. `claim` — a proposition treated as qualified enough for current work, with evidence/provenance where material.
3. `decision` — a Human/domain-owned choice among alternatives or a selected direction.
4. `preference` — a defeasible Human preference; not a hard constraint.
5. `constraint` — a binding limit on options or execution.
6. `standard` — a durable quality, method, evidence or production requirement.
7. `commitment` — an undertaken obligation or promised action/state.
8. `authority` — who may decide, approve, release, act or change specific state.
9. `open_question` — a material unresolved uncertainty worth preserving because it can change later work.

Do not persist ordinary conversation, transient exploration, model reasoning, routine task detail, or artifacts merely because they exist.

## 4. Epistemic and authority separations

Do not collapse:

- evidence into claim;
- AI inference into Human assertion;
- preference into constraint;
- exploration into decision;
- recommendation into commitment;
- accessible context into authority;
- old state into current state.

`assertion_mode` should distinguish at least:

- `human_explicit`
- `human_observed`
- `source_extracted`
- `ai_inferred`
- `ai_generated`

AI-inferred state about the Human may be proposed but must not silently become Human-authoritative fact, preference, constraint, decision or authority.

## 5. Lifecycle

Minimum lifecycle:

- `proposed`
- `active`
- `resolved`
- `superseded`
- `expired`
- `rejected`

`resolved` means the object reached a legitimate terminal outcome without becoming false or being replaced. Typical examples are an answered open question, a fulfilled commitment, or a closed case whose history remains useful.

Never silently overwrite material history. A replacement should normally supersede the prior object and preserve the relation. Resolution should preserve the object and, where useful, relate it to the answer, outcome or successor state.

Retrieval defaults to active state plus any resolved state that is materially relevant to the current work; historical state is available when needed for audit, explanation, requalification or comparison.

## 6. Scope

Use a small hierarchy, not a large ontology:

`global -> domain -> project/case -> object`

Examples:

- global: external release remains Human authority;
- domain/career: CV claims must be evidence-bound;
- case/Mercedes: pursue MER00043GU;
- object/Mercedes-CV: current recipient-language requirement.

More specific valid state may override a general default only when the authority and relationship are legitimate and explicit.

## 7. Two core operations

### CAPTURE_STATE

Input: conversation, Work result, source or explicit Human instruction.

Output: zero or more candidate mutations:

- `CREATE`
- `UPDATE`
- `RESOLVE`
- `SUPERSEDE`
- `EXPIRE`
- `RELATE`

Persist only state that is likely to alter later work materially.

### GET_STATE

Input: current work intent plus resolvable domain/project/entity context.

Output: a compact authoritative State Packet containing only the state relevant to the present work, ranked primarily by scope proximity, authority, current status and task relevance; recency is secondary and only used where time matters.

The packet should normally include active decisions, relevant claims/evidence, constraints, standards, authority, commitments and blocking/open questions. It may include resolved state where prior outcomes materially inform current work. It should not dump the full store into context.

## 8. Human gates and autonomy

No extra confirmation is required when the Human has already made an explicit material statement and the system is merely recording it faithfully.

Human authority is required before an AI inference can:

- create a material Human decision;
- supersede a Human decision;
- add or materially loosen a constraint;
- expand AI authority;
- convert a recommendation into a Human commitment;
- authorize external release/action beyond already granted authority.

Evidence extraction, relationship suggestions, non-authoritative hypotheses and retrieval may be automated where provenance is retained and error is reversible.

## 9. Runtime allocation

- **ChatGPT Memory:** convenience and personalization; not sole authority.
- **Projects:** scoped working context and continuity; not sole authoritative state registry.
- **Chat / Work / Research / Codex:** reasoning and execution consumers/producers of candidate state events.
- **Human State Store / State Library:** durable typed authoritative state and its lifecycle.
- **Domain systems (Drive, Gmail, Calendar, GitHub, finance systems, web sources, etc.):** retain domain-native authoritative records and evidence.
- **Repository:** schema/policy/system-learning authority, not the operational database for all personal state.

## 10. v0.1 implementation hypothesis

Use a structured Notion database as the first operational registry because it supports typed properties, views and AI-accessible read/write actions in the current environment. Keep the logical schema store-independent so the registry can later move to another service or a native OpenAI state store without semantic redesign.

Do not migrate all historical chats or data. Seed only enough real state to test the loop on genuine work, initially across representative domains such as Career, Investing, Spatzennest and Marketing Strategy.

## 11. Success criteria

The implementation is justified only if genuine use materially improves one or more of:

- reconstruction burden;
- state-loss rate;
- false-authority errors;
- retrieval precision;
- Human maintenance effort;
- downstream decision/artifact quality;
- portability and recovery.

If maintenance burden or retrieval noise outweighs benefit, reduce or retire the mechanism rather than expanding architecture.

## 12. Non-goals

v0.1 does not introduce:

- a universal work lifecycle;
- a new agent/controller/router;
- mandatory state capture after every interaction;
- full personal knowledge management;
- a replacement for ChatGPT Memory or Projects;
- automatic authority escalation;
- a requirement that every domain use Notion;
- a graph database, embeddings layer or custom RAG stack unless genuine-use evidence later justifies one.
