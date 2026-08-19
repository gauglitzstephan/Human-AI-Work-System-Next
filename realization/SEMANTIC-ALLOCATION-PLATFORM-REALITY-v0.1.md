# Semantic Allocation & Platform Reality Map v0.1

**Status:** REALIZATION R1 CANDIDATE — semantic allocation / platform-reality mapping only  
**Date:** 2026-08-19  
**Conceptual baseline:** Target Architecture Baseline v0.2  
**Authority boundary:** This file does not authorize runtime instructions, Skills/plugins, Project restructuring, state migration, automation, deployment or external actions.

## 1. Question

Given the accepted conceptual baseline, where should each material semantic obligation live in actual operation so that:

1. authoritative reality remains authoritative;
2. Humans retain legitimate purpose/judgment/authority;
3. Runtime behavior receives enough control to perform useful work;
4. professional/domain knowledge stays local where appropriate;
5. platform-specific capabilities do not become architecture invariants;
6. implementation remains smaller than the conceptual architecture without losing material semantics?

The goal is **allocation**, not implementation.

---

# 2. Realization owner classes

Use only these owner classes for R1 mapping. They are allocation categories, not new architecture layers.

```text
H — HUMAN / LEGITIMATE EXTERNAL OWNER
    purpose, values, acceptance, material commitment, external authority,
    authentic authorship/judgment where non-substitutable

O — OPERATING STATE / POLICY / CAPABILITY
    persistent domain state, reusable capabilities, accepted operating patterns,
    long-lived ownership, capacity, lifecycle, reporting

R — RUNTIME CONTEXT / CONTROL
    active instruction/control semantics, work selection, context composition,
    capability/runtime preflight, interaction/coordination

W — WORK-LOCAL METHOD / CONTEXT
    task/domain professional method, references, requirements, temporary model,
    decomposition, recipient/use criteria, local uncertainty treatment

T — TOOL / APP / TECHNICAL ENFORCEMENT
    authoritative retrieval/write, deterministic checks, computation, execution,
    permissions, transactions, version/state inspection

A — ASSURANCE / OBSERVABILITY
    verification, challenge, representative-use validation, readback,
    monitoring/outcome observation, runtime trace/evidence

L — LATENT / NO PERSISTENT REALIZATION
    semantic obligation exists but no standing artifact/mechanism is justified
    until a material trigger occurs
```

A requirement may require more than one owner. `owner` here means the smallest legitimate realization locus, not exclusive responsibility.

---

# 3. Current ChatGPT/OpenAI platform reality — implementation evidence, not architecture

Official OpenAI product documentation reviewed 2026-08-19 establishes the following current implementation facts. Availability remains plan/workspace/role/region/surface dependent and must be observed in the actual account before relying on a capability.

## P1 — Chat

Current role: fast conversational assistance, search, brainstorming and everyday help.

Realization implication:
- strong default for direct/open/high-interaction work;
- conversation is working context, not automatically authoritative operational state;
- a successful response does not establish persistence, external execution or outcome.

Source: OpenAI Help Center — `ChatGPT Work and Codex`.

## P2 — Work

Current role: longer multi-step work and finished deliverables; can research/analyze, work across connected apps/files, and create documents/spreadsheets/presentations/reports/Sites where supported. Humans can review progress, answer questions, redirect work and approve important actions.

Work can use Project context. Cloud Work chats synchronize across supported ChatGPT surfaces; local desktop work has separate locality constraints.

Realization implication:
- candidate execution surface for longer bounded Work;
- does not become authoritative state merely because it runs longer;
- action/permission and connected-data semantics remain capability/context dependent.

Sources: OpenAI Help Center — `ChatGPT Work and Codex`; `Creating and editing documents, spreadsheets, and presentations with ChatGPT Work`; ChatGPT Release Notes 2026-07-09.

## P3 — Projects

Projects group chats, files and project instructions for longer-running work. Project instructions apply within the Project and override global Custom Instructions. Project memory can create stronger context boundaries; project-only memory limits context to the project.

Realization implication:
- strong candidate **Context Home / working-context carrier** when a domain needs continuity;
- Project content remains context/source material, not automatically authoritative truth;
- Project instructions are runtime configuration, not architecture authority;
- project creation is unnecessary for ordinary bounded work.

Source: OpenAI Help Center — `Projects in ChatGPT`.

## P4 — Memory / chat history

Saved memories and referenced chat history can inject useful personal/history context. Chat-history recall is selective rather than a complete record; saved memory persists until removed but remains personalization context rather than an authoritative domain database.

Realization implication:
- suitable for stable personal preferences/context when useful;
- unsuitable as authoritative operational/project state;
- retrieved memory must retain normal scope/freshness/authority discipline.

Source: OpenAI Help Center — `How does Reference saved memories work?`.

## P5 — Custom / Project Instructions

Custom Instructions apply broadly to ChatGPT conversations; Project Instructions apply only within their Project and override global Custom Instructions.

Realization implication:
- global instructions are scarce cross-context runtime-control capacity;
- Project instructions can specialize local behavior;
- neither should contain the full conceptual architecture;
- semantics delegated to an instruction surface require conformance/coverage review because compression can silently lose functions.

Sources: OpenAI Help Center — `Custom Instructions in ChatGPT`; `Projects in ChatGPT`.

## P6 — Plugins / Apps / Skills

Plugins are the current discovery/packaging mechanism for repeatable workflows across ChatGPT and Codex. A plugin may include Skills, Apps and App templates. Apps connect external data/actions. Actual availability depends on plan, workspace settings, role, supported surface, region and app capabilities. App-backed actions depend on configured permissions; consequential external actions may require confirmation.

Realization implication:
- Plugins/Skills are reusable capability packaging, not architecture state;
- Apps are capability/data/action bindings, not proof of authority or effectiveness;
- availability/access must be checked in the current execution context;
- external systems remain authoritative only for the state domains they legitimately own.

Sources: OpenAI Help Center — `Plugins in ChatGPT and Codex`; `Apps in ChatGPT`.

## P7 — Scheduled Tasks

Scheduled Tasks can run one-off/recurring work or condition checks and notifications. Their supported tools and context differ from ordinary interactive work; current documentation includes limitations such as Project-file access for tasks created in Projects.

Realization implication:
- suitable for recurrence/monitoring when an actual observation path exists;
- not a truth store;
- task execution context must be treated as a separate runtime context rather than assumed equivalent to the originating chat/project;
- no automation should be adopted until semantic/context coverage is demonstrated.

Source: OpenAI Help Center — `Scheduled Tasks in ChatGPT`.

## P8 — Codex

Codex is a distinct software-development/technical execution surface. Desktop Codex can work with repositories, folders, terminals and development tools; its history/context and availability differ from ordinary Chat/Work surfaces.

Realization implication:
- candidate execution environment when success depends on real files/repos/commands/tests;
- technical validation in Codex does not establish substantive acceptance/outcome;
- handoff/state/authority between Chat/Project and Codex must be explicit where material.

Source: OpenAI Help Center — `ChatGPT Work and Codex`.

---

# 4. Baseline requirement → smallest realization ownership

Legend: `P` primary, `S` supporting, `-` normally unnecessary.

| Requirement | H | O | R | W | T | A | L | Minimum realization interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| CR-01 Outcome before means | S | - | P | P | - | - | S | Work Selection/runtime must not treat raw wording as complete specification; no persistent artifact for simple work. |
| CR-02 Claim-relative scope | - | S | P | P | S | S | S | Resolve only enough boundary/context for the claim; runtime/app/context transfer requires evidence. |
| CR-03 Reality/epistemic integrity | - | S | P | P | P | S | - | Retrieve/inspect real state where material; classify evidence/inference locally; memory/chat is not truth. |
| CR-04 Current state before change | - | P | P | P | P | S | - | Existing-system work starts with sufficient authoritative-state recovery before replacement design. |
| CR-05 Professional sufficiency/reuse | S | S | S | P | S | P | - | Professional method/reference belongs primarily in work/domain-local assets; reuse requires transfer appraisal. |
| CR-06 Comparative composition | S | S | P | P | S | S | - | Runtime/work selection chooses available effective composition; no fixed Human/AI topology. |
| CR-07 Human agency/legibility | P | S | P | S | S | S | - | Human purpose/authority remains external; runtime must surface material state when Human judgment/action depends on it. |
| CR-08 Capability/access/authority | P | S | P | - | P | S | - | Runtime preflight distinguishes provider existence, access, permission, effectiveness and Human/external authority. |
| CR-09 State/knowledge integrity | S | P | S | S | P | S | - | Authoritative state remains in legitimate stores/domains; Projects/chats/memory are working/derived unless explicitly authoritative. |
| CR-10 Minimum sufficient work | - | S | P | P | S | S | S | Adaptive selection is active runtime logic; decomposition/persistence/assurance remain latent until value/quality/risk triggers. |
| CR-11 Detection-capable assurance | S | S | S | P | P | P | S | Assurance method chosen by claim/failure mode; deterministic/tool checks and genuinely different review/reality where needed. |
| CR-12 Realization/outcome integrity | P | P | S | P | P | P | S | Work must reach only supported boundary; receiving context/outcome owner often lies outside ChatGPT. |
| CR-13 Runtime/implementation fidelity | - | S | P | - | P | P | - | Maintain explicit conformance/allocation from baseline semantics to actual runtime/context; prevent unowned semantic loss. |

---

# 5. Conditional requirement allocation

| Conditional requirement | Primary activation locus | Smallest sufficient realization |
|---|---|---|
| CCR-01 Open framing/search | R + W | activate alternative framing/mechanism search only while route is materially open |
| CCR-02 Persistent/divergent state | O + T | identify authoritative store/owner/write path/reconciliation only for material state domains |
| CCR-03 Consequential risk/control | H + O + R + T + A | action-specific authority/permissions, protection and recovery proportional to consequence |
| CCR-04 Recipient/use maturity | W + A | local professional refinement plus recipient/use test; not global checklist |
| CCR-05 Future uncertainty/commitment | H + R + W | local information-value/robustness/staging decision only when future uncertainty can flip route/value |
| CCR-06 Competing initiatives/resources | H + O | persistent priority/capacity/portfolio decision outside local Work Selection authority |
| CCR-07 Human capability effect | H + O + W | activate only when learning/expertise/authorship/recovery capability has material future value |

---

# 6. What should be persistent vs latent

## Persist by default only when there is a legitimate persistent owner/value

### Human / stable personal context
Examples: stable preferences, protected values, recurring constraints where explicit memory is useful.

Carrier candidate: Saved Memory / Human-controlled profile.

Not suitable for: changing project state, live opportunity status, authoritative external facts.

### Domain / operational state
Examples: application state, accepted system configuration, canonical rules/processes, current artifact pointer, owner/authority, external reporting state.

Carrier candidate: legitimate external System of Record such as GitHub/Drive/Sheets/Docs/other connected system according to domain.

ChatGPT surfaces consume/derive this state; they do not become authoritative merely by discussing it.

### Reusable professional/solution knowledge
Examples: validated methods, patterns, Skills/workflows, exemplars and failure evidence.

Carrier candidate: evidence-qualified Knowledge Capital repository/library/plugin/Skill where recurring reuse justifies maintenance.

Reuse remains scope/transfer qualified.

## Latent by default

Do not persist merely because the conceptual architecture contains the semantic:
- Work Object;
- integrated DWM;
- Work Graph;
- explicit lifecycle stage;
- assurance ledger;
- uncertainty register;
- Human Gate record;
- realization model;
- Semantic Compiler state.

Material work may instantiate one or more temporarily or persistently when continuity, authority, dependency, risk, audit or reuse value justifies it.

---

# 7. Smallest plausible realization profile — candidate, not yet accepted

The current evidence supports a **thin-global / strong-context / authoritative-external-state** direction as the smallest plausible profile:

```text
GLOBAL CHATGPT RUNTIME KERNEL
  only semantics that must survive cross-domain ordinary work
  and cannot safely rely on each domain to rediscover them

        +

WORK / PROJECT-LOCAL CONTEXT
  actual domain state, requirements, professional method,
  references, work-specific constraints and current artifacts

        +

EXTERNAL AUTHORITATIVE STATE
  legitimate systems of record per state domain

        +

CONDITIONAL CAPABILITIES
  Work / Codex / Plugins-Apps / Skills / Tasks / tools
  selected only when the current work requires them

        +

CLAIM-BOUND ASSURANCE
  deterministic/tool/independent/recipient/reality evidence
  selected by failure mode and claim
```

This is a **direction for the next discrimination gate**, not permission to write global instructions or create Projects/Skills.

---

# 8. Candidate global-vs-local semantic placement

## Likely global runtime candidates

Only cross-domain semantics with repeated catastrophic/expensive failure if absent:
- raw input/proposed means is not automatically the requirement/outcome;
- reality/provenance/authority distinctions;
- retrieve/inspect current state before consequential redesign where accessible;
- capability/access/authority are distinct;
- minimum sufficient work / avoid unnecessary Human/process burden;
- exact claim must not exceed evidence;
- material runtime-context differences must not be assumed away;
- local defect/evidence should not trigger global restart by default.

These are **candidate functions**, not wording.

## Prefer work/project/domain-local

- professional methods and quality bars;
- domain requirements/rules;
- reference/exemplar sets;
- explicit Work Graph/DWM representation;
- artifact/craft methods;
- realization models;
- domain-specific assurance;
- current case/project state;
- domain-specific Human roles/authority.

## Prefer external/technical enforcement

- authoritative read/write;
- deterministic constraints and calculations;
- file/repository changes and tests;
- permissions/identity/action confirmation;
- transaction/readback;
- scheduled observation when platform context supports it.

---

# 9. Key realization risks identified

## RISK-R1 — Global instruction inflation
Encoding the whole baseline globally would recreate the prior failure mode: architecture-as-static-overlay, high salience burden and semantic competition.

## RISK-R2 — Project-as-truth confusion
Projects improve continuity but can contain stale files, old chats and instructions. Project presence does not establish authoritative state.

## RISK-R3 — Memory-as-state confusion
Memory/chat history is useful personalization/context, but incomplete/selective recall makes it unsuitable as operational truth.

## RISK-R4 — Surface capability transfer
Work, Chat, Codex, Tasks and Plugins/Apps have different capabilities/context/access. A claim proven in one surface does not automatically transfer.

## RISK-R5 — Scheduled-task context loss
Tasks may not carry the same project files/context/tools as interactive work. Monitoring/automation must prove its actual observation path before it becomes an operating mechanism.

## RISK-R6 — Skill/plugin cargo-culting
Reusable packages can improve repeated work but can also freeze context-specific methods into global behavior. Promotion requires repeated transfer value and version/owner/retirement discipline.

## RISK-R7 — External write without state ownership
The existence of an App/tool write capability does not make ChatGPT the owner of the state or the decision authorizing mutation.

## RISK-R8 — Semantic compilation loss
Any thin runtime will omit most conceptual detail. The omission is acceptable only when omitted semantics are recoverable/latent/owned elsewhere and no material requirement becomes unowned.

---

# 10. R1 verdict

## Allocation coherence

`PASS as a mapping candidate.`

The accepted conceptual baseline does not require one universal runtime object. A plausible realization can keep:

- legitimate purpose/authority with Humans/external owners;
- persistent authoritative state in domain Systems of Record;
- only a thin cross-domain control kernel in the global runtime;
- professional method/state in work/project/domain context;
- technical actions/checks in tools/apps;
- assurance/observability claim-bound and conditional;
- most architecture semantics latent until material.

## Not yet established

This mapping does not establish:
- the exact global-runtime kernel wording/content;
- whether Custom Instructions, Work defaults, a Plugin/Skill or another mechanism is the correct carrier;
- Project topology/admission rules;
- a state-store migration;
- a general Skill/plugin architecture;
- automation/scheduling topology;
- behavioral equivalence to the accepted conceptual baseline.

---

# 11. Next gate

**REALIZATION R2 — Minimum Runtime / Operating Profile Discrimination.**

Compare the smallest plausible realization profiles, not instruction drafts:

```text
A — GLOBAL-KERNEL MINIMAL
    tiny cross-domain runtime invariants
    + domain/project/external state retrieved as needed

B — PROJECT-CENTRIC
    minimal global kernel
    + Projects as primary continuity/context carrier
    + external authoritative state

C — WORK/PLUGIN-ORCHESTRATED
    minimal global kernel
    + Work as long-task controller
    + Plugins/Skills/Apps as reusable capability packages
    + external authoritative state
```

These are not mutually exclusive products; R2 asks which responsibilities each profile should own by default and which should remain conditional.

Evaluate only:
- CR-01…CR-13 semantic coverage;
- ordinary-work burden;
- state/authority integrity;
- runtime-context fidelity;
- professional-method locality;
- portability/exit;
- observability/debuggability;
- failure containment;
- dependence on mutable product capability.

Do **not** write Custom Instructions, build Skills/plugins, create Project topology or schedule automations before R2 discriminates the minimum profile.
