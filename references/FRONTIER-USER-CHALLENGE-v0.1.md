# Frontier User Challenge v0.1

**Status:** WORKING STRESS TEST / NOT AN EMPIRICAL USER-PERCENTILE STUDY  
**Date:** 2026-08-19  
**Purpose:** Challenge the Reference Map and eventual architecture against the operating patterns that a highly capable contemporary AI-work user can plausibly exploit today.

---

## 1. Epistemic boundary

The phrase **“top 1% user”** is used here as a design challenge, not as a measured population claim.

We currently do not have a representative dataset proving which behaviors characterize the literal top one percent of ChatGPT users.

The valid question is:

> Given the strongest currently available work surfaces and the known failure modes of Human–AI work, what would a high-leverage user do differently from one-off prompt usage, and what architectural concerns does that expose?

Product features are mutable implementation evidence. They do not define the general Human–AI Work System.

---

## 2. Current product reality used for the challenge

Primary current OpenAI product references checked:

- ChatGPT Projects / project memory;
- Apps in ChatGPT;
- Deep Research;
- Skills in ChatGPT / OpenAI Academy Skills;
- ChatGPT Workspace Agents;
- Scheduled Tasks;
- ChatGPT Work / Codex and Codex repository workflows.

Relevant official sources include:

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/11487775-apps-in-chatgpt
- https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt
- https://help.openai.com/en/articles/20001066
- https://openai.com/academy/skills/
- https://openai.com/academy/workspace-agents/
- https://help.openai.com/en/articles/20001143
- https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex

These sources establish capability availability and intended product patterns, not general effectiveness.

---

# 3. Frontier-use hypotheses

## H1 — Architect context, not only prompts

A high-leverage user is likely to treat context as a designed resource:

- use bounded Projects/workspaces for coherent long-running domains;
- select which files, apps and sources are admissible;
- isolate contexts where cross-contamination is costly;
- retrieve rather than repeatedly paste large context;
- distinguish current inference context from durable state and reusable knowledge.

**Architecture challenge**
The system must explain context selection, scope, authority, freshness and cross-context handoff. A better prompt is insufficient.

**Reference pressure**
R4, R9, R14, R15.

---

## H2 — Connect to reality instead of narrating reality manually

Apps and connected sources allow AI work to search current external systems and, depending on permissions, take actions.

A high-leverage user is likely to prefer:

```text
authoritative/current source access
>
copy/pasted recollection
```

where the cost/risk is justified.

**Architecture challenge**
Reality access creates new state, permission, provenance, privacy and action-boundary problems. `access` must remain distinct from `authority` and `verified capability`.

**Reference pressure**
R9, R12, R13, R14, R15.

---

## H3 — Use source-scoped research as a controlled epistemic operation

Deep Research can use selected websites, uploaded files and connected apps, propose a research plan, expose progress, accept mid-course correction and return source-linked reports.

A high-leverage user is likely to use this selectively for questions where source quality, coverage and traceability materially matter.

**Architecture challenge**
Research should be represented as a capability with source-scope, evidence and stopping semantics—not as a universal preliminary phase.

**Reference pressure**
R7, R9, R12, R14.

---

## H4 — Turn repeated successful methods into reusable capabilities

Skills explicitly productize repeatable ways of working through instructions, examples, code and resources.

A high-leverage user is likely to move from:

```text
repeat prompt
→ stable method
→ reusable Skill / capability
→ evaluation
→ maintenance / retirement
```

rather than keeping successful work trapped in chat history.

**Architecture challenge**
The system needs a capability lifecycle: discovery, definition, invocation conditions, dependencies, evaluator, evidence, versioning, promotion, degradation and retirement.

A Skill is one possible realization of that lifecycle, not the lifecycle itself.

**Reference pressure**
R6, R9, R12, R14, R15.

---

## H5 — Use agents only for repeatable bounded work that has earned automation

Workspace Agents are positioned around repeatable workflows, connected systems, consistent outputs and real-world constraints.

A high-leverage user is likely to distinguish:

```text
one-off reasoning
repeatable method
repeatable workflow
delegated agentic workflow
```

instead of turning every complex task into an agent.

**Architecture challenge**
The Work System must determine when autonomy, repeatability, permissions, evaluator quality and recovery justify an agentic realization.

**Reference pressure**
R4, R10, R12, R13, R14, R15.

---

## H6 — Make changing-world work proactive rather than repeatedly reactive

Scheduled Tasks can perform recurring work and monitoring across time, including notifying only when meaningful change occurs.

A high-leverage user is likely to externalize suitable monitoring, follow-up and periodic synthesis rather than relying on memory or manual re-querying.

**Architecture challenge**
Longitudinal work creates trigger, freshness, prior-run state, termination, notification, cost and stale-assumption problems.

Product-specific discontinuities matter: for example, current Scheduled Tasks created in a Project cannot rely on that Project’s files.

**Reference pressure**
R7, R9, R13, R14, R15.

---

## H7 — Use repositories/versioned artifacts for work that must survive the conversation

Codex and repo-backed workflows make versioned technical work, diffs, tests and review first-class.

A high-leverage user is likely to move durable engineering/configuration work out of prose-only chat into versioned artifacts when traceability, rollback or reuse matter.

**Architecture challenge**
Chat is an interaction surface, not automatically the authoritative state or durable artifact system.

**Reference pressure**
R9, R12, R14, R15.

---

## H8 — Treat memory as a continuity mechanism, not a canonical ledger

Current ChatGPT memory and project memory improve continuity and relevance, but product documentation also treats freshness, correctness, scoping and long-term synthesis as active problems.

A high-leverage user is likely to use memory for:

- preferences;
- recurring context;
- continuity;

while keeping consequential authoritative state in a source that can be inspected, updated and reconciled explicitly.

**Architecture challenge**
The Work System needs different semantics for personalization memory, working context, durable knowledge and authoritative state.

**Reference pressure**
R9, R12, R15.

---

## H9 — Build explicit contracts across product surfaces

Projects, apps, tasks, memory, Skills, agents, Codex and external applications offer powerful but non-identical context and permission models.

A high-leverage user is unlikely to assume:

```text
same account
⇒ same context
⇒ same state
⇒ same permissions
⇒ same authority
```

**Architecture challenge**
Cross-surface handoffs need explicit state, identity, provenance, permission and completion semantics when material.

**Reference pressure**
R9, R13, R15.

---

## H10 — Separate proposal, execution and authorization

Connected work surfaces can move from analysis into write actions or external effects.

A high-leverage user is likely to increase AI initiative while preserving explicit approval or permission boundaries for consequential effects.

**Architecture challenge**
The system must distinguish capability, access, proposal rights, execution permissions, legitimate authority, acceptance and responsibility.

**Reference pressure**
R4, R10, R13, R14, R15.

---

## H11 — Evaluate reusable work, not just inspect plausible outputs

Skills and agents become valuable only if their repeated behavior is sufficiently reliable for the use case.

A high-leverage user is likely to use:

- representative fixtures;
- baselines;
- adversarial cases;
- traces;
- outcome-linked measures;
- regression checks;
- explicit failure/recovery evidence;

for reusable or consequential workflows.

**Architecture challenge**
Evaluation must be attached to the claim and use case, not to architecture elegance or a one-time successful demo.

**Reference pressure**
R6, R12, R13, R14, R15.

---

## H12 — Manage human attention and maintenance as scarce system resources

More AI surfaces create more opportunities to configure, review, reconcile, monitor and maintain.

A high-leverage user should therefore optimize not only AI throughput but also:

- attention cost;
- review fatigue;
- coordination burden;
- maintenance surface;
- interruption cost;
- rework;
- subscription/compute cost;
- future migration cost.

**Architecture challenge**
A sophisticated AI system that produces more administrative work for the human may have negative net value.

**Reference pressure**
R3, R5, R7, R10, R11, R15.

---

## H13 — Preserve multiple cognitive modes instead of forcing one universal workflow

Current product surfaces increasingly support distinct modes for quick conversation, research, artifact work, repo execution, reusable skills and autonomous/repeatable workflows.

A high-leverage user is likely to route work according to the required cognitive/production function rather than force all work through one visible process.

**Architecture challenge**
The general system should support mode/capability selection while allowing trivial work to collapse to trivial execution.

**Reference pressure**
R2, R3, R4, R7, R14.

---

## H14 — Harvest durable learning without promoting everything into memory

A high-leverage user is likely to distinguish at least:

```text
useful conversation
repeatable method
validated capability
reference knowledge
current authoritative state
asset
```

and preserve only what has future value exceeding lifecycle cost.

**Architecture challenge**
Learning/persistence needs promotion criteria and destinations rather than indiscriminate storage.

**Reference pressure**
R6, R9, R10, R11, R12.

---

# 4. What this challenge adds to the Reference Map

The current frontier-use challenge does **not** justify an architecture made of `Projects + Apps + Skills + Agents + Tasks + Codex`.

It does establish that the Reference Map must be capable of studying:

1. context boundaries and progressive retrieval;
2. external reality and action interfaces;
3. capability packaging and lifecycle;
4. longitudinal/proactive work;
5. cross-surface state and handoff;
6. permission/authority separation;
7. evaluation and observability;
8. maintenance / human operating economics;
9. multiple work modes;
10. durable learning and promotion.

These are represented in Reference Map v0.2 through R6, R9, R10, R12–R15 and Coverage Lenses L4, L5, L7–L10, L13 and L14.

---

# 5. Counter-challenge: what a frontier user should *not* do

The same product capability landscape creates predictable traps.

A high-leverage operating model should resist:

- placing every preference, method and fact into global instructions;
- converting every recurring thought into an automation;
- building agents before the task/evaluator is stable;
- treating memory as a database;
- treating project context as an immutable source of truth;
- assuming tool access means authority;
- adding multiple agents merely to simulate independent review;
- storing every useful answer instead of selecting durable knowledge;
- using Deep Research when a simple lookup suffices;
- copying platform architecture into the general Human–AI Work System;
- maximizing automation at the expense of human learning, judgment or optionality;
- letting maintenance complexity grow faster than realized work value.

---

# 6. Current disposition

**Frontier-user challenge:** MATERIAL INPUT TO REFERENCE COVERAGE  
**Evidence strength:** PRODUCT-REALITY + DESIGN INFERENCE, NOT POPULATION EVIDENCE  
**Architecture authority:** NONE  
**Use:** stress-test Reference Map, later requirements and realization alternatives.

Re-run this challenge when the AI-work capability landscape changes materially.
