# Qualified Requirement Regression and Runtime Evidence — 2026-09-06

**Status:** CANDIDATE evidence and decision record.  
**Decision owner:** Human repository owner.  
**Decision:** Which current ChatGPT-native operating realization should carry the qualified Human–AI Work requirements, and which repository changes are justified?  
**Intended outcome:** A usable operating system that removes repeated Human reconstruction/orchestration without restoring obsolete custom runtime machinery.  
**Decision level:** Product/carrier operating realization, not selection of one universal surface.

## 1. Bound evidence state

| Evidence object | Exact state | Authority/claim |
|---|---|---|
| Current repository | `gauglitzstephan/Human-AI-Work-System-Next`, `main@9d195dd2270557c901c47147ed2411bd51ad6e59` | Authoritative base for this Candidate |
| Qualified prior repository | `gauglitzstephan/Human-AI-Work-System`, archived `main@8bcfb68e15c10dff520b451741f7696936cf5b8e` | Qualified prior evidence, not current authority |
| Current Global CI R3 | repository payload SHA-256 `e5de13b5989590959829ae12207f1269f691603d3c4f99568b4f68101be20985` | Human-reported installed/live; exact installed-field identity, per-turn activation, conformance and effectiveness not independently read back |
| Personal Skills | Three current packages usable in Work in this Human's setup | Does not establish ordinary Chat availability/activation |
| Repository plugin package | Prior installation attempt unsuccessful | Not an available dependency or proposed solution |
| Chat→Work transition | No universally reliable automatic context-preserving conversion established | Portable compiled handoff is required as a qualified fallback |
| Current episode | Work surface, skills, web, files, GitHub and interactive steering are available in this run | Proves this episode only, not every plan/surface/account |

The archived repository was richer but not therefore current; the reduced repository is current but not therefore complete. Recovery was semantic: explicit requirements, architecture invariants, accepted transformations, runtime contracts, method packages, preservation reviews, and Genuine-Use failure evidence were all included.

## 2. September 2026 OpenAI product reality

Only first-party product sources are used for product facts. Documentation establishes documented behavior; it does not establish this Human's account/surface availability or professional effectiveness.

| Product fact | First-party evidence | Operating implication |
|---|---|---|
| The public Model Spec describes intended behavior and OpenAI explicitly says production models do not yet fully reflect it. | [Model Spec 2026-08-18](https://model-spec.openai.com/2026-08-18.html) | Model defaults such as truth-seeking, robust intent inference, uncertainty, and side-effect caution are helpful but cannot be the sole carrier or acceptance proof. |
| Instruction authority is Root → System → Developer → User → Guideline; later same-level instructions prevail; assistant/tool/quoted or untrusted content has no authority by default. Long conversations may be truncated toward recent/relevant content. | [Model Spec chain of command](https://model-spec.openai.com/2026-08-18.html#follow-all-applicable-instructions) | Repository text and user prompts operate inside higher product constraints; accessible transcript does not guarantee active context; external content must not silently instruct the agent. |
| Custom Instructions apply across chats when enabled; current limits are 1,500 characters for Free/Go and 5,000 for Plus/Pro/Enterprise/Business/Education. The article contains both immediate-application and future-conversation wording, so exact existing-chat behavior should be tested. | [Custom Instructions Help](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt) | R3 fits the documented paid limit but installation identity and behavior require separate readback/probes. Do not infer universal surface behavior. |
| Project Instructions apply only within their Project and override Global Custom Instructions. | [Projects in ChatGPT Help](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | A Project-specific instruction overlay can suppress R3. A compact Project cooperation kernel is a real carrier requirement. |
| Projects group chats, files, sources and instructions; chats can be moved when eligible and then inherit Project context. Project Sources may include saved responses and supported app links. | [Projects in ChatGPT Help](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | Projects are useful scoped context hubs, not guaranteed full-state or authority mechanisms. Curate source status and freshness. |
| Projects can use default or project-only memory. With project-only memory, chats are isolated to the Project and ChatGPT Work is not available. Shared Projects become project-only. | [Projects memory and Work boundary](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | “Work inside Project” is configuration-dependent. Choose privacy/isolation versus Work deliberately; use separate Work plus portable return when needed. |
| ChatGPT Learn says the same eligible Project may contain Chat and Work chats and recommends a Project when work continues, produces multiple outputs, or depends on recurring sources; self-contained work may start without one. | [Projects and chats](https://learn.chatgpt.com/docs/projects) | This reconciles with Help only conditionally: Project Work is available in eligible non-project-only configurations/surfaces, not universally. Projects are not required for professional work. |
| Memory is a continuously updated synthesis from chats, files and connected apps; its visible summary does not contain everything; users can inspect sources, correct or delete memory. | [Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq) | Memory reduces repetition for personalization but is not controlled exact state, authority, or an audit log. |
| Chat accepts natural language and does not require a perfect first prompt; it supports back-and-forth, web search, files, drafting, comparison and task clarification. | [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) | Natural opening and formative research can remain in ordinary Chat. No mandatory formation form or hundred-page prompt. |
| Work is intended for clear, reviewable outcomes and can plan, gather context, research, use tools/apps/files/code, create artifacts, run longer tasks, and be steered. It is a good fit for multiple sources/tools/steps, meaningful duration, reusable outputs, or repetition/monitoring. | [Get started with Work](https://learn.chatgpt.com/docs/get-started-with-work), [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) | Work is a substantial execution environment, not merely a downstream stage. Direct Work entry is valid when its Work Object is sufficiently clear. |
| Cloud Work can continue after the desktop app closes and across web/mobile; local Work can use local files/apps/browser when enabled. Features vary by plan, platform, region, rollout and workspace settings. | [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) | Select environment from source/tool need and verify actual access. Never generalize one Work episode. |
| Long-running Work supports in-chat steering and status; `/goal` and `/plan` exist only on supported surfaces. Separate chats can run independently, but concurrent writers to the same source should be avoided. | [Long-running work](https://learn.chatgpt.com/docs/long-running-work) | Preserve interactive correction and source-write isolation; do not make slash commands architectural dependencies. |
| A Skill is a reusable focused workflow with instructions/resources, selected by task match or explicit mention; Skills reduce repeated prompts. | [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins) | A Skill is justified by differentiated reusable method and usable deployment—not by every logical function. Installation/selection/load/application remain separate. |
| As of 2026-07-09 the directory is presented as Plugins; plugins may package Skills and apps, while apps supply external data/actions. App availability varies by plan, region, workspace, role, model and interface; write actions/approvals are app-specific. | [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) | The failed repository plugin installation cannot be assumed solved by documentation. Prefer already available apps/capabilities; verify exact action and permission. |
| Deep research creates a reviewable plan, can use web/files/eligible apps, can be steered/interrupted, and returns cited downloadable reports. App support and usage vary; deep research uses read actions, not app writes. | [Deep research in ChatGPT](https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt) | Use it for sustained multi-source synthesis when plan/source control adds value; keep Chat search for formative/urgent work; validate claims professionally. |
| Web search is first-party across documented surfaces; web results are untrusted input. | [Web search](https://learn.chatgpt.com/docs/web-search) | Search in Chat is legitimate; citations are evidence links, not authority or method validation. |
| Browser is available in ChatGPT web/desktop, uses a separate profile unless an extension supplies an existing session, and page content is untrusted. | [Browser](https://learn.chatgpt.com/docs/browser) | Use for research/website interaction after structured access; verify authentication, sensitive sharing and resulting state. |
| Computer Use is a Work/Codex desktop capability in supported regions requiring plugin/OS/app permissions; OpenAI recommends a dedicated plugin/MCP integration when available. | [Computer Use](https://learn.chatgpt.com/docs/computer-use) | Treat GUI operation as a scoped fallback, not universal access; preserve approvals, verification and recovery. |
| Eligible apps can trigger Work tasks on supported events; permissions remain bounded and approval-requiring actions pause. Work also supports scheduled recurring updates. | [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt), [Get started with Work](https://learn.chatgpt.com/docs/get-started-with-work) | Automations are sensors/actors with explicit source, trigger, permissions, reconciliation and stop—not memory or authority. |

## 3. Qualified prior regression

### Interpretation rules and Core/Conditional Requirements

| Prior ID | Current disposition | Current owner/carrier | Regression finding |
|---|---|---|---|
| IR-01 | Transformed/preserved | CJS-12; OB; R3 | Rich semantics remain; universal artifacts/stages were removed. |
| IR-02 | Preserved | CJS-01/12; NWT | Materiality/sufficiency remain frontier-relative. |
| IR-03 | Preserved | CJS-06/12/14; R3 | Non-compensatory floors still precede economy. |
| CR-01 | Preserved | CJS-01/02; R3 | Outcome before means; Candidate makes goal discovery explicit. |
| CR-02 | Preserved | CJS-01/02/11; NWT | Claim-relative scope/contribution and child→parent integration remain. |
| CR-03 | Preserved | CJS-10; R3 | Reality/epistemic integrity remains high-salience. |
| CR-04 | Preserved | CJS-08; R3 | Actual-state recovery remains; case effectiveness is partial. |
| CR-05 | Preserved | CJS-04/06/14; Skills/providers | Intended-use professional sufficiency, reuse and recipient transformation remain; runtime provider selection is not automatically sufficient. |
| CR-06 | Transformed/preserved | OB; NWT; native Work | Comparative work composition remains without a custom orchestrator. |
| CR-07 | Preserved | CJS-07/09/13; R3 | Human agency, attention, capability, legibility, correction and anti-persona theater remain. |
| CR-08 | Preserved | CJS-07/10/11; deployment contracts | Capability/status/authority and proposal→outcome type integrity remain. |
| CR-09 | Preserved | CJS-08/10/15; OB; Project Current candidate | Working/authoritative/reusable state distinction remains; sparse Project carrier closes a practical gap. |
| CR-10 | Preserved | CJS-12; OB | Minimum sufficient work, economics and legitimate closure remain. |
| CR-11 | Preserved | CJS-14; evaluate-work-product; narrower assurance | Failure-mode matching and conditional independence remain. |
| CR-12 | Preserved | CJS-11; NWT; realization semantics | Product→receiving context→transition→use→mechanism→outcome→value remains. |
| CR-13 | Preserved | CJS-10; NWT; system-development | Runtime/provider fidelity, portability and diagnosability remain; product preflight is strengthened. |
| CR-14 | Preserved | CJS-15; SL/GU | Evidence-bound learning and scoped feedback remain. |
| CR-15 | Preserved | CJS-11; OB | Actual transformation remains mandatory; meta-work does not substitute. |
| CCR-01 | Preserved | CJS-02/03/05; R3 | Open framing/exploration and problem–solution co-evolution remain. |
| CCR-02 | Preserved | CJS-07/10/12; PD controls | Consequential risk/recoverability remain. |
| CCR-03 | Preserved | CJS-12; decision-analysis | Future uncertainty, information value, staging/wait/commitment remain. |
| CCR-04 | Preserved | CJS-01/12; operating economics | Competing initiatives/resources remain without a portfolio subsystem. |
| CCR-05 | Preserved | CJS-08/09; NWT; Work steering | Common ground/status/correction/re-entry/contestability remain without mandatory dashboard. |

### Requirements transformed across older versions

| Earlier requirement-bearing semantic | v0.3/current disposition | Finding |
|---|---|---|
| Persistent/divergent state control | Absorbed into CR-09, CJS-08/10, sparse Project/external-state contract | Preserved; central store/DWM not required. |
| Recipient/use maturity | Absorbed into CR-05/12, CJS-06/11/14 | Preserved; product-refinement loop remains conditional. |
| Human capability formation | Absorbed into CR-07 and CJS-13 | Preserved; not forced when task completion dominates. |
| Parent continuity and promotion readback | CJS-08/11, NWT, system-development methods | Preserved; Candidate strengthens Work return/re-entry. |
| Protected Salience P1 complete product/success | CJS-06/11; R3; Work return | Source-preserved; runtime failures mean behavior is not established. |
| P2 mechanism breadth / resolve–deepen | CJS-03/05/12; R3 | Preserved without Adaptive Exploration Skill. |
| P3 next-use maturity | CJS-06/11/14; operating realization | Preserved; artifact-specific method still required. |
| P4 Human not default QA | CJS-07/14; R3 | Preserved but historically failed; requires genuine-use validation. |

### Historical mechanisms

| Mechanism/representation | Disposition | Semantic residue that remains |
|---|---|---|
| Runtime Semantic Compiler | Obsolete as runtime subsystem | Native adaptive selection/composition; AI-compiled Work brief; semantic regression at change time |
| Dynamic Work Model | Obsolete as central mandatory object | Sparse shared/current state, situation/use/requirements/reality/authority lenses when material |
| Work Graph | Obsolete as universal representation | Dependencies, parallelism, loops, integration and stop/escalation in proportionate Work Architecture |
| Controller / Work Engine | Obsolete | Native Chat interaction plus native Work execution within protected boundaries; no permanent Chat control role |
| Universal lifecycle/stage machine | Obsolete | Latent revisitable transformations and exact maturity claims |
| Universal QWS/Work Contract | Obsolete | Direct/Note/Brief/Pack NWT handoff when risk earns it |
| Persistence/assurance/independent reviewer by default | Obsolete | Risk/claim/failure-mode-triggered state and assurance |
| One Project per stage / room topology | Obsolete | One Project per persistent initiative where useful; separate chats per distinct outcome |

No semantic obligation was removed merely because its former mechanism was retired.

## 4. Terminology recovery

Search was performed across both exact repository snapshots and the current legacy archive. Absence means no exact repository occurrence was found; equivalent semantics are reported separately rather than back-filled as lineage.

| Requested term | Recovery result |
|---|---|
| `PIPS` | Exact term not located. Do not invent lineage. |
| standalone `PIP` | Exact term not located. Do not invent lineage. |
| similarly named concept | “Personal Information System” exists in Genuine-Use evidence; no `PIS/PIPS/PIP` acronym was established as a canonical concept. |
| `Joint Intelligence` | Located in current CJS/R3/NWT lineage and legacy qualification work; current meaning requires added AI contribution plus shared correction. |
| `Shared Intelligence` | Exact term not located. Common-ground/shared-state semantics exist under Joint Intelligence and interaction continuity. |
| `Added Intelligence` | Exact term not located. The obligation exists in CJS-03/R3 as hypotheses, evidence, alternatives, mechanisms, examples and counterpoints beyond paraphrase. |
| `Better Questions` | Exact canonical term not located. Question generation/discriminating-question semantics exist. |
| `Goal discovery` | Exact phrase not located. Outcome-before-means, need/purpose and competing-outcome semantics exist. |
| `Scope formation` | Exact phrase not located. Claim-relative scope/System of Interest/parent-child boundary semantics exist. |
| `Semantic Compiler` | Extensively located historically; explicitly retired as a runtime subsystem. Adaptive selection and handoff compilation survive as functions. |
| `Dynamic Work Model` | Extensively located historically; central mandatory object retired. Sparse qualified/shared state survives. |
| `Professional Performance Model` | Located in professional-cognition lineage; intentionally localized to task/domain method and Knowledge Capital rather than a global Core object. |
| `sparse` | Located in v0.3 interpretation rule “semantically rich, operationally sparse” and later state/architecture reasoning. |
| `progressive work state` | Exact phrase not located. Progressive context/retrieval/qualification semantics exist. |
| `parent continuity` | Located in core amendment, runtime regressions and current CJS/NWT equivalents. |
| `interaction frontier` | Located in historical interaction/runtime contracts; its selection function survives without a named subsystem. |
| `Knowledge Capital` | Located extensively in prior architecture/learning and preserved in current CJS as qualified reusable learning. |

## 5. Operating-realization comparison

### Decision constraints and non-compensatory floors

- Natural incomplete input must work.
- The Human must not become the recurring method selector, orchestrator, state rebuilder, or basic QA detector.
- Parent outcome, reality, professional method/quality, Human authority, state class, and claim integrity may not be traded away for prompt simplicity.
- The route must exist in current product reality; hypothetical plugin installation is excluded.
- Project and non-Project professional work must both remain valid.

Ratings are qualitative evidence judgments, not invented weights. `High` means structurally strong if available; `Mixed` means conditional; `Low` means a recurrent requirement gap.

| Candidate path | Interaction / formation | Sustained work / research / artifact | State / persistence | Human and prompt burden | Reliability / recovery | Verdict |
|---|---|---|---|---|---|---|
| A. Chat front door → Work for suitable frontiers | High for goal/question/scope/frame; risks Chat over-execution | High after qualified handoff | Mixed without native transfer; Project can help | Low early prompt burden; handoff can be substantial but AI-compiled | Good with portable brief/return; otherwise transition is fragile | Strong default for open situations, not universal |
| B. Direct Work entry for selected classes | Mixed if goal/frame open; high when bounded | High | Mixed; depends on Project/files/external state | Lowest duplicate-formation burden; brief still needs consequential boundaries | Good when Work Object is clear; risk of silent reinterpretation otherwise | Valid and necessary, not universal |
| C. Hybrid by interaction/capability/state need | High if selection is accurate | High | High with explicit state class | Low if AI selects; high if Human must route manually | Strong but needs simple observable selection rule | Best functional basis |
| D. Project-centric professional work | High continuity for recurring initiatives | High only in eligible configuration; project-only memory disables Work | High for context, not authority | Low repetition; ongoing curation burden | Strong recovery if Project Current is maintained; retrieval/config risks | Strongest rival for long-running initiatives, not universal |
| E. Non-Project work with explicit checkpoint/handoff | High for ad hoc work | High through direct/portable Work | Adequate when checkpoints are risk-triggered | Low setup; occasional mechanical copy | Portable and recoverable; no automatic cross-chat state guarantee | Required complement; professional and legitimate |
| F. Adaptive native portfolio: natural entry anywhere, Chat for interaction, Work direct or by handoff, Project only when continuity earns it, external authority, explicit return | High | High | High when state is deliberately classified | Lowest recurring Human orchestration; prompt/brief burden appears only when earned | Best recovery because every unavailable native route has a semantics-preserving fallback | **Recommended Candidate** |

### Recommendation

Adopt **Path F**, with Path C as its allocation logic. It is not a new controller: the AI applies a small decision rule based on dominant unresolved need, execution lift, continuity risk, and actual availability. Path A is the usual opening for materially open situations; Path B is preferred when a substantial Work Object is already bounded; Path D is invoked by persistent-initiative conditions; Path E preserves professional non-Project work and supplies fallback portability.

**Strongest rival:** Path D, Project-centric work. It becomes preferable as the local default when an initiative will continue, produce multiple outputs, reuse the same sources/decisions, and the Project's instruction/memory/Work configuration is compatible. Switch away when Project maintenance/retrieval ambiguity exceeds continuity value, project-only memory blocks needed Work, or authoritative state belongs primarily in an external workflow.

**No-action alternative:** keep current architecture unchanged. It is rejected because product precedence makes R3 non-universal inside Projects and the current NWT does not explicitly operationalize the known lack of a universal automatic Chat→Work transfer/return loop.

## 6. Skill portfolio requalification

| Skill/method | Differentiated reusable method | Requirement/failure class | Native or narrower alternative | Surface/deployment evidence | Burden effect | Decision |
|---|---|---|---|---|---|---|
| `decision-analysis` | Bounded decision object/owner/level; viable no-action/delay/stage/test; objectives/constraints; uncertainty/robustness; reversibility/option value; rival/switch condition; no fabricated precision | RM-032–040; premature commitment, wrong level, fake scoring | Native Chat is enough for bounded advice; narrower quantitative/domain method may be better | Source active; usable in this Human's Work; ordinary Chat activation unverified | Reduces method prompt when properly activated | Retain unchanged |
| `evaluate-work-product` | Exact object/intended use/reliance claim; object frozen during evaluation; claim/failure-mode-capable evidence; professional/recipient fit; no repair/authorization/outcome inflation | RM-041–046, RM-073–076; polish-as-fitness, wrong object, correlated review | Narrow professional evaluator first; native self-check only for ordinary defects | Source active; usable in Work; ordinary Chat activation unverified | Reduces review-prompt burden; misuse as generic reviewer would add ceremony | Retain unchanged |
| `system-development` | Exact-state recovery, requirement/architecture method, RCA, semantic regression, repository/product promotion/readback, genuine-use validation | RM-052, RM-061, RM-073, RM-079–083; architecture drift and false runtime claims | Native coding alone lacks the qualified system lineage; narrower repo tools execute writes | Active and used in this Candidate | Reduces recovery/reconstruction; bounded to this system | Retain unchanged |
| former `work-formation` | Minimum missing basis and READY/WEAKER/WAIT/HANDOFF/STOP/NO_ACTION termination | RM-001/002/005/009/023/067 | Native interaction + R3 + NWT already carry it | Demoted; no need to test deployment | Separate invocation would duplicate formation and raise ceremony | Do not revive |
| former `adaptive-exploration` | Mechanism-distinct alternatives, counterhypotheses and probes in open spaces | RM-010/011/019/022/032/033 | Native Joint Intelligence; narrower design/ideation provider where useful | Demoted | Generic activation increases selection burden; method semantics already carried | Do not revive |
| former `research-evidence` | Cross-domain evidence/provenance/freshness/counterevidence/information-value method | RM-023–028 | Native search/deep research and narrower domain evidence providers are now better execution routes | Demoted; current product offers dedicated research modes | Generic router adds little differentiation | Do not revive |

No new `goal-discovery`, `better-questions`, `work-architecture`, `project-state`, or generic professional-excellence Skill is justified. These are native interaction functions, sparse carriers, or domain-specific methods. A new Skill would be reconsidered only after recurrent failure plus a differentiated method plus a usable target-surface deployment path.

## 7. External challenge

| Field/source | Incremental challenge | Existing requirement coverage | New requirement? |
|---|---|---|---|
| Mixed initiative — [Horvitz, CHI 1999](https://dl.acm.org/doi/10.1145/302979.303030) | Couple automation and direct manipulation; initiative must reflect uncertainty, expected value and cost | CR-06/07/10; CCR-05; CJS-07/09/12 | No; strengthens allocation/steering test. |
| Human–AI interaction — [Amershi et al., CHI 2019](https://dl.acm.org/doi/10.1145/3290605.3300233) | Set expectations, make context-aware help timely, support correction/dismissal, disclose change over time | CR-07/08/14; CCR-05; CJS-07/09/10/15 | No; strengthens observability and feedback controls. |
| Human–AI synergy meta-analysis — [Vaccaro, Almaatouq & Malone 2024](https://www.nature.com/articles/s41562-024-02024-1) | Human–AI combinations improved on Humans on average but underperformed the better of Human or AI alone on average; task type and relative capability matter | CR-06/10; CJS-07/12; explicit user requirement that Joint Intelligence beat reformatted Human input and isolated AI | No; makes strongest-solo/provider comparison an assurance benchmark. |
| Trust/reliance — [Lee & See 2004](https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392) | Trust should be calibrated to actual capability, context and performance, not generalized from labels | CR-08/11/13; CJS-07/10/14 | No; reinforces capability-chain and claim-specific reliance. |
| Grounding/common ground — [Clark & Brennan 1991](https://collablab.northwestern.edu/CollabolabDistro/nucmc/ClarkAndBrennan-GroundingInCommunication-1991.pdf) | Common ground requires evidence of understanding and varies with communication medium/cost | CCR-05; CJS-08/09; parent continuity | No; supports sparse checkpoints and explicit correction/return. |
| Distributed/joint cognition — [Hutchins, *Cognition in the Wild*](https://books.google.com/books/about/Cognition_in_the_Wild.html?id=CGIaNc3F1MgC), [Hollnagel & Woods](https://www.routledge.com/Joint-Cognitive-Systems-Foundations-of-Cognitive-Systems-Engineering/Hollnagel-Woods/p/book/9780367864200) | Unit of analysis includes people, artifacts and practices; local agent quality is not whole-system performance | SOI; CR-02/06/07/09/12; CJS-01/07/08/11 | No; validates system boundary and state-carrier distinctions. |
| Intelligence augmentation — [Engelbart 1962](https://www.dougengelbart.org/pubs/papers/scanned/Doug_Engelbart-AugmentingHumanIntellect.pdf) | Capability arises from Human, tools, language, methods and training as a system; Human comprehension/capability matters | CR-07; CJS-13; cognitive/work allocation | No; already covers Human capability and method/tool composition. |
| Problem structuring — [OR Society overview](https://www.theorsociety.com/) and Mingers/Rosenhead lineage | Messy problems require models and facilitated negotiation rather than assuming goals/problems are uncontested | CCR-01/05; CJS-01/02/03; goal/scope/frame requirements | No; narrower professional method may be selected when stakeholder complexity earns it. |
| Professional expertise/reflective practice — Schön and expert-performance lineage; [Ericsson 2008](https://pubmed.ncbi.nlm.nih.gov/18778378/) | Experience or fluent rules alone do not prove observed expert performance; knowing-in-action and feedback matter | CR-05/07/11; CJS-06/13/14; COG/Q and genuine-use evidence | No; reinforces qualified field method, tacit input and performance evidence. |
| Provenance — [W3C PROV](https://www.w3.org/TR/prov-overview/) | Entity/activity/agent provenance supports assessments of quality, reliability and trustworthiness | CR-03/09/13; CJS-08/10/14 | No; existing requirement already includes source/transformation/write trace. |
| Organizational memory — [Ackerman 1998](https://joelchan.me/INST801-FA22%20Readings/Ackerman_1998_Augmenting%20organizational%20memory.pdf) | Capture has upstream cost; reuse needs retrievability, social/ownership context and downstream payoff | CR-09/10/14; CJS-08/12/15 | No; validates risk-triggered persistence and Knowledge Capital qualification. |
| Adaptive decisions — [Haasnoot et al. 2013](https://doi.org/10.1016/j.gloenvcha.2012.12.006) | Deep uncertainty favors pathways, sequencing, adaptation triggers and path-dependency analysis | CCR-03/04; CJS-12; decision-analysis | No; already carried by WAIT/TEST/STAGED/switch/stop/expand semantics. |
| AI/system reliability — [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework), [GAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Map context/risks, measure/validate, manage and monitor; provenance, testing and incident disclosure matter | CR-03/08/11/13/14; CCR-02; CJS-10/14/15 | No; reinforces claim-bound assurance, risk and outcome observation. |

**External-challenge verdict:** no materially independent requirement is missing. The strongest apparent additions—best-solo comparison, grounding costs, calibrated reliance, provenance, and adaptive pathways—are already entailed by qualified current/prior requirements. They are made explicit as operating/assurance tests rather than added as fashionable architecture.

## 8. Candidate change decision

### Implemented in this Candidate

1. `baseline/HUMAN-AI-WORK-OPERATING-REALIZATION.md`: complete Human-facing adaptive operating system, cognitive model, runtime influence map, product/carrier realization, state contract, modes and prompt/return contracts.
2. `inventory/REQUIREMENT-MASTER-2026-09-06.md`: exhaustive lineage-backed inventory with required status, roles, methods, state, carriers, effectiveness and repair.
3. `baseline/PROJECT-INSTRUCTIONS-CANDIDATE.md`: compact Project cooperation carrier justified by instruction precedence.
4. `baseline/PROJECT-CURRENT-TEMPLATE.md`: optional sparse working-state source for persistent Projects.
5. `baseline/NATIVE-WORK-TRANSITION.md`: product-configuration preflight, explicit portable handoff and parent reintegration.
6. `CURRENT.md`/`README.md`: entry-point reconciliation and corrected R3 product-state wording.

### Deliberately unchanged

- Canonical Joint-Work Semantics: requirement semantics were complete enough; no new canonical requirement survived external challenge.
- R3 payload: no behavioral evidence justifies recompilation; Project precedence is solved at the Project carrier.
- Three active Skill packages and registry: no method gap plus usable deployment path justifies change.
- Demoted Skills and retired runtime mechanisms: not revived.
- External ChatGPT product settings, Project Instructions, Memory, plugins/apps, Skills, automations, and authoritative domain stores: repository Candidate does not authorize or perform these changes.

### Acceptance and switching conditions

Accept the Candidate if semantic regression/readback pass and the Human accepts the product/carrier operating decision. After promotion, the next evidence is genuine use, specifically:

- one new Project behavioral probe after installing the exact Project payload;
- one portable Chat→Work→parent reintegration case;
- one direct-Work professional case;
- continued artifact-specific professional QA against known failure classes.

Switch or repair the realization only if evidence shows a material requirement failure, product change, recurrent orchestration burden, or a narrower method/provider that materially outperforms the current allocation. Do not open another architecture cycle merely because behavior remains probabilistic.

