# Predecessor Lineage & Reuse Audit v0.1

**Status:** PROCESS CORRECTION / QUALIFIED PRIOR INVENTORY  
**Date:** 2026-08-19  
**Purpose:** Prevent the reconstruction program from rediscovering, renaming, or re-proving design questions that prior repositories already developed, grounded, tested, accepted, rejected, or deliberately simplified.

---

# 1. Executive finding

The reconstruction program initially treated the immediate predecessor repository as the main internal architecture corpus and treated predecessor architecture generally as `evidence` that should not silently define the new system.

That was necessary but insufficient.

The user's GitHub estate contains a **lineage of materially different Human–AI system experiments**, including accepted architecture baselines, minimal-kernel counter-designs, persistence/governance systems, operating-model architectures, runtime experiments, and reconstruction programs.

Therefore:

> **Accepted prior design is not truth, but it is also not an unstructured evidence fragment.**

A prior design that has:

- explicit scope and claim boundary;
- external reference basis;
- recorded alternatives or failure analysis;
- review/falsification evidence;
- explicit human acceptance;

must enter the reconstruction as a **Qualified Prior Design Baseline**.

Its closed questions should not be reopened from first principles unless a named reopen trigger exists.

---

# 2. Corrected epistemic statuses

Internal material now needs at least five distinct statuses.

```text
I0 — RAW INTERNAL EVIDENCE
     work traces, observations, failures, user corrections

I1 — DESIGN HYPOTHESIS / CANDIDATE
     proposed architecture or mechanism without accepted closure

I2 — QUALIFIED PRIOR DESIGN
     reference-grounded and reviewed design with bounded acceptance

I3 — IMPLEMENTATION / RUNTIME EVIDENCE
     behavior, platform, state, deployment, integration, canary evidence

I4 — SUPERSEDED / REJECTED / COUNTER-DESIGN
     historically valuable negative evidence or simpler rival
```

`I2` does not equal universal validity. It changes the **burden of proof for reopening**.

---

# 3. High-signal repository lineage

This is a first-pass lineage, not a complete repository history.

## L1 — `Persistence-System`

**Role:** persistence / canonical-artifact / governance experiment.  
**Observed design:** GitHub-first canonical artifact store; Conversation → Extraction → Decision Readiness → Human Gate → Canonical Artifact → Registry → Review.  
**Value:** provenance, persistence-gate and external-write distinctions; explicit governance store.  
**Known limitation / later counter-design:** later work rejected GitHub-first and registry-by-default assumptions for ordinary work.

**Disposition:** `I4 SUPERSEDED / COUNTER-DESIGN`, with reusable persistence/governance mechanisms.

---

## L2 — `personal-ai-workspace-system`

**Role:** bounded persistence correction.  
**Observed accepted boundary:**

```text
Working Artifact ≠ Persisted Asset ≠ Executed Output
```

It explicitly blocks GitHub-first, registry, YAML, extractor, memory-update, execution and automation by default.

**Value:** strong negative architecture evidence against persistence/registry inflation; separates useful session output from durable promotion and external effect.

**Disposition:** `I2 QUALIFIED PRIOR DESIGN` for persistence boundary semantics within its stated manual-store scope.

---

## L3 — `PAW` — Personal AI Workbench

**Role:** governed workbench / repository operating model.  
**Observed design:** Chat as workbench, GitHub as source of truth/review, explicit Candidate → Review → Promotion → Merge flow, Core / Runtime / Workflows / Governance / ADR / Handovers split.

**Value:** separation of planning/review, patching, diff review and Human merge authority.

**Disposition:** `I2/I3` depending on artifact: qualified governance design plus implementation/workbench evidence.

---

## L4 — `PAOS` — Personal AI Minimum Kernel

**Role:** deliberate simplification / native-surface counter-architecture.  
**Observed design:** smallest sufficient structure; global chat default entry; Context Home, Execution Surface, Return Surface; selective handover; Project admission threshold; explicit rejection of universal formal Work Object / WOLC for ordinary work.

Important counter-evidence:

> Ordinary chat, research, document, or coding work does not require a formal Work Object.

**Value:** strong anti-overengineering prior; real alternative to universal work-object formalization; native-surface routing and project/context semantics.

**Disposition:** `I2 QUALIFIED PRIOR DESIGN / COUNTER-DESIGN` for minimal-kernel and surface-routing questions.

---

## L5 — `Personal-AI-Operating-Model`

**Role:** governed reference-reconstruction repository for HAPS / PAWS / AMM and Human–AI integration architecture.  
**Status in its README:** architecture not accepted; runtime not validated.  
**Value:** explicit Work Object implementation, source pipeline, provenance-bearing claim extraction, HAPS/PAWS/AMM boundary reconstruction, family admission discipline.

**Disposition:** primarily `I1 DESIGN / RESEARCH CANDIDATE` plus `I3` tooling/source-pipeline evidence.

---

## L6 — `human-ai-work-architecture`

**Role:** mature reference-grounded Human–AI Work Architecture line.  
**Canonical state on 2026-08-14:** Architecture Baseline v1.3.1 accepted.

Material accepted semantics include:

- Work Object / Work Product / Working State distinctions;
- Work Product staging and transition integrity;
- Internal Gate ≠ Human Gate;
- Publication / audience integrity;
- Professional Method Resolver;
- eight architecture views;
- Execution Context, Control/Instruction Stack, State/Context Stack;
- Workflow Package vs Professional Method;
- Capability Provider vs Capability Binding/access;
- Domain Adapter vs Runtime Adapter;
- Subject vs Evaluator Execution Context;
- claim-relative effective capability/access.

The repository also explicitly suspended mechanically continuing low-discrimination synthetic tests and shifted toward existing evidence and real future work.

**Disposition:** `I2 QUALIFIED PRIOR DESIGN BASELINE` with `I3` evaluation/runtime evidence.

Reopen only when later evidence, changed scope or a materially stronger rival invalidates a specific accepted decision.

---

## L7 — `AI-native-Operating-Model`

**Role:** whole operating-model architecture integrating strategy, persistent organization, work, execution and learning.  
**Date / accepted state:** Foundation v0.2 accepted on 2026-08-17 after external grounding, seven-scenario architecture falsification/fit exercise and bounded repairs.

### Accepted system shape

```text
1. Strategic Architecture
2. Operating Architecture
3. Work Architecture
4. Execution Architecture
5. Learning Architecture

Cross-cutting:
Reality & Provenance
Authority / Governance / Security
Assurance & Risk
Performance / Economics / Value
Knowledge / Configuration / Change
```

### Accepted Work Architecture already includes

- Need / Problem / Opportunity → Outcome → Work Object → Transformation → Receiving Context → Work Product → Success Conditions;
- authoritative reality and professional-method resolution;
- Work Graph;
- **Work Units** when method/capability/dependency/output/authority/assurance/transition/recovery differs materially;
- Human / AI / Human+AI / specialist-tool / validated workflow / existing-process allocation;
- Working State vs Authoritative State vs Knowledge Capital;
- Capability vs Access vs Authority;
- assurance ladder;
- Work Product → Receiving Context → Transition → Use/Action → Mechanism → Outcome → Benefit/Value;
- institutionalization boundary between reusable Work pattern and authoritative Operating pattern.

### Validation result

Seven scenario classes found no missing foundational layer/control plane. Two recurring ambiguities were repaired:

1. Operating ↔ Work ownership when a Work pattern becomes a persistent organizational process;
2. Learning proposes/routes change while authoritative mutation remains with the affected owner/domain.

The validation explicitly supported process proportionality and rejected creation of unnecessary new foundation parameters without incremental value.

**Disposition:** **highest-priority `I2 QUALIFIED PRIOR DESIGN BASELINE` for whole-system / Work-Architecture questions currently discovered.**

This baseline must be compared against — not silently rediscovered by — the Next reconstruction.

---

## L8 — `Human-AI-Work-System`

**Role:** later professional-work Core + runtime / Semantic Compiler line.  
**Current state on 2026-08-19:** integrated Core v0.5 candidate + B.6 Professional Work + Semantic Compiler + runtime v0.6.2; real-use canary evidence; repository explicitly states it is no longer in standalone architecture-exploration mode.

Material mechanisms:

- input ≠ requirement;
- Working State ≠ authoritative state ≠ Knowledge Capital;
- state-domain / authoritative-record / reconciliation semantics;
- Dynamic Work Model and Work Graph;
- claim-bound Qualification;
- Realization Model;
- next-state Semantic Compiler / Minimum Sufficient Work;
- Information Value;
- Prospective Robustness;
- Commitment Design;
- Human–AI allocation;
- salience/coverage regression evidence.

**Disposition:** `I1/I2/I3` mixed by artifact: candidate Core, previously accepted mechanisms, and strongest current real-use/runtime evidence.

---

## L9 — `Human-AI-Work-System-Next`

**Intended role after this audit:** **reconstruction / reconciliation / selection program**, not another architecture branch that restarts discovery.

Its primary job is now:

```text
recover lineage
→ normalize claims / scope / status
→ compare qualified priors
→ identify genuine conflicts / gaps
→ use external references + real evidence to discriminate
→ retain / refine / relocate / supersede / reject
→ only invent where prior designs and established references are insufficient
```

---

# 4. Immediate finding: Q1–Q3 partially rediscovered prior work

The current Next Stage-1 Cross-Reference Synthesis produced:

- nested SoIs;
- typed focal units;
- Strategy / Portfolio / Work / Operational control separation;
- a narrowed Work Engine around episode-level control.

These are not worthless, but they were presented too strongly as new derivation.

### Already-developed precedents

`AI-native-Operating-Model` already distinguishes:

```text
Strategic Architecture
Operating Architecture
Work Architecture
Execution Architecture
Learning Architecture
```

and its Work Architecture already defines Work Units, Work Graph, Work Product, state/authority and realization semantics.

`human-ai-work-architecture` already distinguishes Work Episode execution context, Work Object / Work Product / Working State, eight architecture views, Work Product transitions, capability/access/authority and runtime integration.

`PAOS` already provides a serious simpler counter-design that rejects universal formal Work Objects and uses bounded native-surface routing.

Therefore Q1–Q3 should be reclassified as:

> **REFERENCE RECONCILIATION / RECOVERY**, not novel architecture discovery.

Any genuinely new delta must be stated explicitly relative to these priors.

---

# 5. New reopen rule

A prior accepted decision enters the Next program as **closed-but-reopenable**, not open-by-default.

Reopen only when at least one trigger applies:

1. **Changed System of Interest / intended claim** — prior scope no longer matches.
2. **New external evidence** — materially invalidates or limits the prior mechanism.
3. **New real-use failure** — prior architecture cannot represent, prevent or repair a material failure.
4. **Stronger rival** — simpler or more effective architecture preserves required semantics with lower burden.
5. **Internal contradiction** — two accepted prior baselines make incompatible claims that matter now.
6. **Implementation impossibility / material platform change** — architecture cannot be realized for the intended use.
7. **Unqualified prior** — the supposed prior did not actually have sufficient source, review or acceptance basis.

Without a trigger:

```text
recover → map → retain provisionally
```

not:

```text
forget → re-derive → rename
```

---

# 6. Required reconciliation outcomes

For each major prior mechanism or architecture decision:

```text
PRIOR ID / source
Prior scope
Prior status
Reference basis
Validation / evidence basis
Decision / mechanism
Known counter-designs
Current external evidence delta
Current real-use delta
Reopen trigger? yes/no
Disposition:
  RETAIN
  RETAIN-WITH-BOUNDARY
  REFINE
  RELOCATE
  MERGE
  SUPERSEDE
  REJECT
  OPEN-CONFLICT
Novel delta, if any
```

---

# 7. Process correction / current gate

## STOP

Do **not** continue Q4–Q8 as if the research space were blank.

## NEXT

First construct a **Prior Architecture Reconciliation Matrix** centered on the highest-qualified baselines:

1. `AI-native-Operating-Model` Foundation v0.2;
2. `human-ai-work-architecture` v1.3.1;
3. `Human-AI-Work-System` current Core/B.6/runtime line;
4. `PAOS` as minimum-kernel counter-design;
5. `Personal-AI-Operating-Model` HAPS/PAWS/AMM research where it contains unresolved alternative semantics;
6. persistence/workspace repositories for state/promotion counterevidence.

Then run Cross-Reference Synthesis only on:

- **open conflicts** among these priors;
- **material gaps** not already resolved;
- **changed external evidence**;
- **new SoI requirements**;
- **real failures** that existing priors cannot explain.

The reconstruction goal is not to prove that the latest prior architecture was right. It is to avoid paying the intellectual cost of rediscovering it before finding out where it is wrong.
