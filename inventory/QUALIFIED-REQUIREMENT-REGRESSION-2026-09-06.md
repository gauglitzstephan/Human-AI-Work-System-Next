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
| Personal Skills | Three base packages Human-reported usable in Work; two revised formation/exploration entries also available and read in this session | Does not establish ordinary Chat availability/activation |
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
| Work is intended for clear, reviewable outcomes and can plan, gather context, research, use tools/apps/files/code, create artifacts, run longer tasks, and be steered. It is a good fit for multiple sources/tools/steps, meaningful duration, reusable outputs, or repetition/monitoring. | [Get started with Work](https://learn.chatgpt.com/docs/get-started-with-work), [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt) | Work is a substantial execution environment, not merely a downstream stage. Direct Work entry is valid; its next contribution can be developing the goal/frame from unfinished input, with known boundaries preserved. |
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
| P2 mechanism breadth / resolve–deepen | CJS-03/05/12; R3 | Source-preserved; optional revised exploration now provides differentiated method support without becoming a mandatory stage. |
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
| `interaction frontier` | Exact contiguous phrase not located; “Interaction / Frontier” and the named E2E interaction-frontier contract are located. The function survives without a subsystem. |
| `Knowledge Capital` | Located extensively in prior architecture/learning and preserved in current CJS as qualified reusable learning. |

## 5. Operating-realization comparison

### Decision constraints and non-compensatory floors

- Natural incomplete input must work.
- The Human must not become the recurring method selector, orchestrator, state rebuilder, or basic QA detector.
- Parent outcome, reality, professional method/quality, Human authority, state class, and claim integrity may not be traded away for prompt simplicity.
- The route must exist in current product reality; hypothetical plugin installation is excluded.
- Project and non-Project professional work must both remain valid.

These are conditional operating policies at the same decision level. A–E vary entry/organization assumptions; F is the concrete realization of hybrid C, not an independent option that can be declared superior by definition. No comparative runtime experiment establishes a universal winner. Judgments below describe operational consequences supported by documentation, source analysis and Human evidence, not measured scores.

| Dimension | A: Chat front door → Work | B: direct Work | C/F: conditional hybrid | D: Project-centric | E: non-Project + checkpoint |
|---|---|---|---|---|---|
| Interaction quality | Convenient short exchanges | Interactive steering supported | Keep useful interaction where work occurs | Shared initiative context can help | Full interaction within current chat |
| Goal/question/scope discovery | Supported; risk of unnecessary preformation | Supported inside Work; outcome may be discovery | Neither surface monopolizes formation | Project context can inform or anchor framing | Recover just the relevant context |
| Professional cognition | Native reasoning plus available references | Can add methods and sustained inquiry | Pick adequate method for actual claim | Same need; Project is not a method | Same professional obligation |
| Research | Bounded Chat research; transfer sustained program when useful | Sustained inquiry with available sources/tools | Search/deep research/Work by method and control need | Context aids inquiry; access still conditional | Research possible without Project |
| Skill availability | Ordinary Chat Personal Skills unverified; Work usable here | Usable Work catalog; load/application separate | Prefer actual available provider | Work requires compatible Project configuration | Available in non-Project Work here |
| Tool availability | Varies by Chat and receiving Work | Actual Work tool set | Check the needed action, not directory membership | Project scope does not grant external permissions | Connected permissions still govern |
| State continuity | Cross-surface loss risk | Avoids entry handoff; long-context risk remains | Minimize unnecessary switches; explicit deltas | Shared context helps; retrieval not complete | One chat coherent; checkpoint on risk |
| Persistence | Parent chat plus optional source/record | Files/current record as needed | Correct store per state class | Curated source with external authority pointers | Versioned portable checkpoint or external record |
| Human burden | Low opening burden; avoid unnecessary formation work | Low entry burden; preserve real questions/authority | AI selects, prepares and reconciles | Initial settings and source curation where UI-only | Occasional mechanical save/attach |
| Prompt burden | AI compiles sufficient brief | Natural opening can suffice; sources/boundaries recovered | No repetition of legitimately recoverable information | Standing kernel + mutable source | Local context + reusable checkpoint |
| Handoff burden | Potentially material; justified only for lift | No initial transfer | Change environment only if benefit exceeds transfer cost subject to floors | Same Project does not prove conversion/full context | Portable self-contained brief and return |
| Reliability | Formation and transfer both probabilistic | Selection/formation/execution probabilistic | Bounded recovery mechanisms, not guarantee | Retrieval and configuration add failure modes | Explicit state aids recovery; manual transfer remains |
| Observability | Shared conversation then execution receipt | Progress/steering/actual artifact/checks | Report material state and supported claims | Cite source/version, expose conflicts | Checkpoint and source pointer make state inspectable |
| Correction | Propagate exact delta into Work if separate | Correct in same episode | Repair affected dependencies only | Update current source when correction is material | Update checkpoint before later handoff |
| Professional output | Requires field craft/assurance after formation | Requires same field craft/assurance | Select provider and checks capable of detecting failure | Context organization is no proof of quality | Professional work fully legitimate |
| Portability | AI-compiled brief/receipt | Work output/state export as needed | Preserve semantic content across actual available routes | Avoid Project-only assumptions in portable pack | Strong explicit portability, no automatic new-chat memory claim |
| Failure recovery | Rebind parent and handoff, do not re-ask all context | Recover current qualified checkpoint and tool state | Narrow fallback must preserve claim/authority | Reconcile stale or conflicting sources | Retrieve named checkpoint/external source |
| Product constraints | No universally reliable automatic Chat→Work conversion | Account/surface/permissions/credits | All actual constraints remain | Project-only memory currently excludes Work; instructions override global | No shared Project retrieval; Memory not an authority substitute |

**Recommendation:** use C, concretely specified as F in the playbook: natural entry in either Chat or Work; Work when its inquiry/method/tool/iteration capabilities help; Projects when continuing context earns their cost; non-Project work and portable state fully supported. A is useful when short conversational exchanges are currently the best contribution. B is useful even with unfinished goals when Work can investigate and form them. D is the strongest local alternative for a continuing initiative, not a universal default. E is a valid primary operating mode and a recovery complement.

**Switching conditions:** move from Chat when a sustained contribution earns Work; stay in Work when interaction or formation is needed there; adopt a Project when repeated source recovery/multi-output continuity costs exceed its setup/curation burden. Keep project-only isolation when required, using a limited external Work package if legitimate. Prefer a specialist/external workflow when professional validity or authoritative state requires it. Keep the current surface when a switch brings no material benefit.

**No-change alternative:** retaining source semantics alone leaves Project-carrier, practical persistence/return, direct-entry and contradictory Skill-verdict gaps. Bounded repair is justified; neither empirical universal superiority nor restoration of the old runtime is claimed.

## 6. Skill portfolio requalification

| Skill/method | Differentiated reusable method | Requirement/failure class | Native or narrower alternative | Surface/deployment evidence | Burden effect | Decision |
|---|---|---|---|---|---|---|
| `decision-analysis` | Bounded decision object/owner/level; viable no-action/delay/stage/test; objectives/constraints; uncertainty/robustness; reversibility/option value; rival/switch condition; no fabricated precision | RM-032–040; premature commitment, wrong level, fake scoring | Native Chat is enough for bounded advice; narrower quantitative/domain method may be better | Source active; usable in this Human's Work; ordinary Chat activation unverified | Reduces method prompt when properly activated | Retain unchanged |
| `evaluate-work-product` | Exact object/intended use/reliance claim; object frozen during evaluation; claim/failure-mode-capable evidence; professional/recipient fit; no repair/authorization/outcome inflation | RM-041–046, RM-073–076; polish-as-fitness, wrong object, correlated review | Narrow professional evaluator first; native self-check only for ordinary defects | Source active; usable in Work; ordinary Chat activation unverified | Reduces review-prompt burden; misuse as generic reviewer would add ceremony | Retain unchanged |
| `system-development` | Exact-state recovery, requirement/architecture method, RCA, semantic regression, repository/product promotion/readback, genuine-use validation | RM-052, RM-061, RM-073, RM-079–083; architecture drift and false runtime claims | Native coding alone lacks the qualified system lineage; narrower repo tools execute writes | Active and used in this Candidate | Reduces recovery/reconstruction; bounded to this system | Retain unchanged |
| revised `work-formation` v0.7 | Missing-premise tests for need/means, goal and decision level, causal relevance, actual constraints, next-use maturity, authority; resolve/contain only the material gap | RM-005–013, 023, 041, 067; premature optimization and local-proxy failures | Native capability may suffice; it does not establish professional sufficiency. Narrow domain framing can be better | Exact revised restoration source; entry available/read in current Work; two limited explicit tests in receipt | May reduce repeated Human premise repair; no mandatory invocation, questionnaire or Skill handoff | Integrate exact revised source; optional Work method; no product install |
| revised `adaptive-exploration` v0.2 | Mechanism-distinct frames, counterhypotheses and discriminating probes; scoped Human calibration | RM-010/011/019/022/032/033; cosmetic alternatives and premature convergence | Native Joint Intelligence or narrower domain design/strategy/scientific provider | Exact revised restoration source; entry available/read in current Work; limited explicit test | May reduce Human option orchestration; no option quota or mandatory sequence | Integrate exact revised source; optional Work method; no product install |
| former `research-evidence` | Claim-relative evidence need, specialized method choice, source appraisal, conflicts, provenance and stop rule | RM-023–028 | Native search/deep research is an execution environment; use a qualified narrower method when validity requires it | Demoted; no independent need for this generic wrapper established | Can duplicate routing; its evidence obligations must still be applied | Keep demoted; do not mistake research-product access for method sufficiency |

The earlier categorical redundancy verdict for formation/exploration is withdrawn. See the [exact later evidence and source reconciliation](RUNTIME-REALIZATION-RECONCILIATION-2026-09-06.md). No new `goal-discovery`, `better-questions`, `work-architecture`, `project-state` or generic excellence Skill is justified. These functions are realized through interaction, selected methods and legitimate state carriers. Method presence is not proof of activation or comparative effectiveness.

## 7. External challenge

The [reconciled external challenge](RUNTIME-REALIZATION-RECONCILIATION-2026-09-06.md#external-challenge-what-actually-changes-the-realization) records current primary sources, concrete failure classes, existing requirement relations, owners and whether a system change is needed. It covers mixed initiative, HCI, augmentation and team-performance counterevidence, problem structuring, adaptive decisions, provenance and assurance/realization.

No independent new top-level obligation was established within that targeted challenge. This is a scoped finding, not proof of universal completeness. The 2026 field experiment supplies material counterevidence against mandatory collaboration procedure; it does not establish that Skills are ineffective. The repaired realization protects selective methods, Human capability, continuity/assurance floors and actual source-write mechanics without adding a controller.

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
- Three base Skill packages: unchanged. Revised formation/exploration source and five-method discovery/registry are integrated from the exact qualified restoration Candidate.
- Research-evidence and retired runtime defaults: remain demoted/retired. Optional revised methods do not restore the old runtime.
- External ChatGPT product settings, Project Instructions, Memory, plugins/apps, Skills, automations, and authoritative domain stores: repository Candidate does not authorize or perform these changes.

### Acceptance and switching conditions

The exact Candidate is ready for Human source/operating acceptance after readback. No merge or product installation is performed. R3 requires no reinstall. Project Instructions are a prepared optional carrier for a relevant Project; source identity and the new source-recovery/access path should be checked after separately authorized installation where material. Existing five-method Work availability does not require reinstall simply because source integration occurred.

Use the playbook immediately with the actual available surfaces and known limits. Observe method selection, premise correction, output fitness or state recovery only when the evidence could change a real decision. Do not run a generic natural-entry/transition/long-running test campaign merely to rediscover stochastic activation. If a failure appears, repair the responsible carrier/method/state path and affected dependencies rather than beginning another architecture cycle.
