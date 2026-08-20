# E2E Capability / Method / Provider / Surface Map v0.1

**Status:** CANDIDATE — concrete deployment mapping; no external installation.  
**Date:** 2026-08-20  
**Parent:** `realization/E2E-RUNTIME-DEPLOYMENT-MODEL-CANDIDATE-v0.1.md`.

## 1. Purpose

Prevent the repeated semantic collapse of:

```text
Work Function
≠ Method
≠ Capability Provider
≠ Surface / Environment
≠ Control Operator
≠ State / Knowledge Carrier
```

The Orchestrator starts from the **next legitimate transition**, not from a favorite tool or surface.

## 2. Generic Work Functions

These functions are project-independent. They are activated only when the current frontier requires them.

| Work Function | Core question | Typical method classes | Typical providers | Typical surfaces | Relevant controls |
|---|---|---|---|---|---|
| Admit / Frame | What work is actually in scope and worth admitting? | framing, scope/boundary, stakeholder/context analysis | ChatGPT, Human | Chat | Parent continuity, authority, stop/no-action |
| Formation | What is the real situation/need/value/outcome/requirements/solution mechanism? | Value-Focused Thinking, JTBD, systems/stakeholder framing, causal/mechanism modeling | ChatGPT, Human, web/apps for evidence | Chat by default; Work if analysis is long | Decision readiness, Commitment boundary |
| Information Acquisition / Evidence Work | What evidence can materially change the frontier? | source appraisal, search strategy, triangulation, market/literature research, measurement, experiment design | ChatGPT web, Work, apps/connectors, Human expert, deterministic tools | Chat for bounded/interative; Work for sustained research | Information Value, provenance, Handoff/Return |
| Decision | Which peer option/commitment is best-supported for the outcome? | Decision Quality, MCDA, scenario/robustness, real options/staging, trade-off analysis | ChatGPT + Human where judgment/authority material | Chat by default | Commitment Design, Human Gate, decision authority |
| Work / Realization Formation | What Work Product, method, units, providers, interfaces, assurance and transition are needed? | work design, architecture/design method, implementation planning, dependency/interface design | ChatGPT, Work, Codex, Human | Chat/Work | Work-Basis, Authorization, Handoff |
| Execution / Integration | Perform the authorized transformation and integrate child results | domain implementation method, coding, writing, analysis, data processing, artifact creation | Work, Codex, ChatGPT, tools/apps, Human/specialist | Work/Codex/tools; Chat for bounded work | Authorization, Handoff/Return, parent integration |
| Refinement / Maturity | What product transformation is needed for the next recipient/use context? | artifact/craft, usability, editing, presentation/design, recipient-fit method | ChatGPT, Work, specialist, deterministic checks | Chat/Work/artifact tool | No Human as default AI-resolvable QA |
| Assurance / Qualification | What exact claim is supported and can material failure be detected? | deterministic verification, source reconciliation, adversarial/independent review, recipient test, representative-use validation | tools, ChatGPT, Work, Human/specialist, real users | depends on detection need | claim scope, independence, PASS/FAIL/UNVERIFIED |
| Transition / Use | How does the Work Product enter the receiving context and become usable? | deployment, handoff, adoption, communication/training, rollout, recovery | Work, Codex, apps/tools, Human/owner | target system / Work / Chat | Authorization, Handoff, receiving readiness, rollback |
| Observation / Evaluation | What evidence of use/performance/mechanism/outcome matters? | measurement, monitoring, outcome evaluation, causal/evidence analysis | apps/data, Human owner, ChatGPT/Work | external systems + Chat/Work | observation horizon, attribution limits |
| Learning / Change / Closure | What changes, stays, reopens, waits or stops? | RCA, impact analysis, retrospective, change analysis | ChatGPT, Human, Work | Chat by default | Promotion, selective reopen, close/handoff/retire |

## 3. Method taxonomy

A Method is reusable professional know-how for performing a Work Function well. The same Work Function may use different methods by domain and claim.

### 3.1 Formation / framing methods

Examples:

- Value-Focused Thinking;
- Jobs-to-be-Done;
- stakeholder analysis;
- systems framing;
- causal/mechanism modeling;
- requirement elicitation/performance modeling.

### 3.2 Information / evidence methods

Examples:

- source appraisal;
- search/research strategy;
- triangulation;
- evidence synthesis;
- interview/elicitation;
- measurement/experiment design;
- market/competitive research.

### 3.3 Decision / uncertainty methods

Examples:

- Decision Quality;
- peer-option comparison / MCDA;
- Information Value;
- probabilistic forecast where legitimate;
- scenario/stress testing;
- real-options / staged commitment;
- robustness/regret analysis.

### 3.4 Domain / substantive methods

Examples:

- systems architecture / software engineering;
- financial modeling;
- strategy / market analysis;
- recruiting/application strategy;
- process design;
- legal/technical/professional standards where applicable.

### 3.5 Artifact / craft methods

Examples:

- CV / cover-letter craft;
- executive presentation design;
- professional document structure;
- UX/interface craft;
- code/documentation craft;
- recipient-facing editing.

### 3.6 Assurance / evaluation methods

Examples:

- deterministic constraint verification;
- requirements traceability;
- adversarial challenge;
- independent review;
- recipient/usability review;
- representative-use validation;
- outcome/benefit evaluation.

### 3.7 Transition / implementation methods

Examples:

- deployment/rollout;
- migration;
- training/briefing/adoption;
- rollback/recovery;
- change-management / receiving-context enablement.

## 4. Method carrier rules

A method must have an actual accessible carrier when it is needed.

Preferred order is contextual, not absolute:

| Carrier | Use when | Authority/status |
|---|---|---|
| Validated Skill/workflow | account supports it and reusable automation adds value | Method carrier, not global authority |
| Repository / Drive method pack | reusable across Projects or requires versioning/provenance | Knowledge/method source; may be authoritative for method definition if designated |
| Project source/file | method is project/domain-local | Project-local method source |
| External authoritative reference | standard/framework/reference must be current | evidence/reference; not instruction authority unless delegated |
| Task-local research | no adequate validated method pack exists | working method candidate until qualified |
| Human specialist | tacit expertise/judgment cannot be substituted | Human contribution/provider |

For ChatGPT Pro, do **not** require Personal Skills to exist. A repository/Drive/Project method library is the fallback.

## 5. Provider capability dimensions

Provider selection is evaluated against the actual Work Function + Method requirements.

```text
information/context access
reasoning / domain competence
artifact production ability
tool/environment access
verifiability / observability
consequence / reversibility
latency / cost / coordination burden
learning/authorship needs
authority / permissions
verified performance in similar use
```

Do not treat `AI`, `Work`, `Codex`, or a Skill as universally superior providers.

## 6. Surface defaults

### Chat

Default for:
- interactive control/rebind;
- Formation and Decision with Human interaction;
- bounded Information Acquisition;
- Human Gate / commitment / acceptance / promotion interaction;
- bounded execution/repair;
- Handoff preparation and Return reconciliation.

### Work

Default for:
- longer multi-step research/evidence work;
- sustained analysis;
- artifact creation;
- multi-step execution that can proceed inside a bounded Frontier Contract.

Work is a provider/environment **inside the frontier**, not the global controller.

### Codex

Default for repository/software engineering and technical implementation when it is the most effective environment.

### Apps/tools/external systems

Default for authoritative retrieval, deterministic compute/verification and external actions.

## 7. Control operators cross the whole map

These operators are not rows in the Work Function table because they govern transitions across functions/providers/surfaces.

### Commitment

```text
Decision-ready route
→ WAIT / PILOT / STAGED / REVERSIBLE / FULL COMMIT
→ Work Basis
```

### Authorization

```text
Work Basis + provider
→ exact allowed operation / write / transition
```

### Handoff

```text
responsibility/environment changes
→ Frontier Handoff Contract
→ receiving provider executes bounded frontier
→ Return Contract
→ parent rebind
```

### Promotion

```text
candidate state
→ assurance + legitimate decision/acceptance/authority
→ target status / write
→ readback / reconcile
```

### Human Gate

```text
required Human contribution blocks transition
→ mature decision object
→ WAIT / no blocked downstream execution
→ Human event
→ rebind frontier
```

## 8. System Development project mapping

### Generic functions likely to activate

All generic Work Functions remain available, but common System Development work often emphasizes:

- current-state recovery;
- Formation / architecture decision;
- Information Acquisition from repo/reference/product docs;
- Work/Realization Formation;
- execution through GitHub/Codex/tools;
- regression/assurance;
- Promotion/readback;
- real-use evaluation / learning.

### Project-local methods

Candidate reusable method packs:

```text
System Architecture / Requirements Method
Existing-System Recovery Method
RCA / Failure Localization Method
Runtime Compilation / Semantic Regression Method
Repository Promotion / Readback Method
Real-Use Validation Method
```

These method packs should be versioned/qualified separately from the Global Runtime kernel.

### Providers / carriers

```text
GitHub main/CURRENT.md   → controlling program state
GitHub repo              → architecture/runtime/evidence state by path/domain
Chat                     → interactive controller / Formation / Decision / reconciliation
Work                     → long research/analysis/artifact frontier
Codex                    → repository/software implementation frontier
web/apps/tools            → product reality/evidence/execution
Human                     → values/judgment/acceptance/authority where non-substitutable
```

## 9. Application / Career project mapping — later second Project

Same generic Work Functions, different project-local methods/state.

Candidate method packs:

```text
Role-Fit / Positioning Method
Job + Company Research Method
Recruiter / ATS Screening Method
Career Evidence Mapping Method
CV / Cover-Letter Craft Method
Interview / STAR Method
Recipient-Facing Application Assurance Method
```

Project state might include master CV, career evidence, target roles, job postings, application tracker, Human preferences/decisions and external feedback.

Learnings are classified before feeding back to System Development:

```text
domain-method defect
vs
controller/runtime defect
vs
provider/surface defect
vs
state/handoff defect
vs
architecture reopen trigger
```

## 10. Acceptance criterion

A Runtime mapping is not complete until a material frontier can answer, without type ambiguity:

```text
What Work Function is needed?
Which Method is required?
Where is that Method accessible?
What capability characteristics are required?
Which Provider actually satisfies them?
Which Surface/Environment should host it?
What Commitment/Authorization applies?
Does responsibility/environment change require Handoff?
What Return state is required?
What may be promoted, by whom, through what write path?
```
