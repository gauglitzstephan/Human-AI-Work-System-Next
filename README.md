# Human–AI Work System Next

A requirements-led Human–AI work system for preserving context, choosing fit-for-purpose methods, executing real work, and improving from evidence without collapsing architecture, runtime behavior, and outcomes into one claim.

## Authority

Start with [`CURRENT.md`](CURRENT.md) on authoritative `main`. It declares the promoted state and the next valid transitions.

The controlling system basis is:

- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md)
- [`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md)

The current non-normative cross-level companion is [`architecture/REQUIREMENTS-v0.3-ARCHITECTURE-VIEW-INTERACTION-RUNTIME-TRACE-v0.1.md`](architecture/REQUIREMENTS-v0.3-ARCHITECTURE-VIEW-INTERACTION-RUNTIME-TRACE-v0.1.md). It relates Requirements v0.3 to the closed architecture’s responsibilities, inherited descriptive Views, interaction semantics, Runtime-source carriers and bounded evidence. It neither changes architecture nor establishes installed or behavioral Runtime state.

The current non-normative ChatGPT-Native Realization companion is [`realization/CHATGPT-NATIVE-OPERATIONALIZATION-MAP-v0.1.md`](realization/CHATGPT-NATIVE-OPERATIONALIZATION-MAP-v0.1.md). It maps N01–N40 to documented product capabilities, surfaces, access/activation evidence, Instruction Semantics and hard boundaries at a dated cutoff. It is not a Requirement, Architecture source, Runtime carrier, installed-state record or claim of behavioral reliability, professional fitness, outcome or value.

The current non-normative [Deployment & Surface Realization Design v0.1](realization/DEPLOYMENT-AND-SURFACE-REALIZATION-DESIGN-v0.1.md) compiles protected Runtime semantics into surface-independent Pre-Execution, provider selection, recovery, method activation, Execution/re-entry and deployment/readback boundaries. Its [carrier recompilation regression record](reviews/QUALIFIED-ORCHESTRATION-v0.2-CARRIER-RECOMPILATION-SEMANTIC-REGRESSION-v0.1.md) binds the exact repository-source payloads. Neither artifact is a new semantic owner or installed/behavioral claim.

Human Acceptance and repository Promotion of Requirements v0.3 were separately authorized on 2026-08-28 and are recorded in [`decisions/ADR-0004-requirements-baseline-v0.3.md`](decisions/ADR-0004-requirements-baseline-v0.3.md) and PR #34. [Requirements v0.2](foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md) remains immutable historical Qualified Prior evidence.

Human Acceptance for the repaired Runtime-v0.6 compilation source was granted on 2026-08-28 for semantic source head `7beaf27194de5726ae7b8659fded9d2f11ab280f`. After successful PR #35 merge and authoritative `main` readback, Runtime v0.6 is compiled against Requirements v0.3 at repository-source level. The [compilation and semantic-regression evidence](reviews/RUNTIME-v0.6-REQUIREMENTS-v0.3-COMPILATION-SEMANTIC-REGRESSION-v0.1.md) binds the exact source claim. Repository promotion does not establish installed-carrier identity, installed Skill identity, behavioral Runtime conformance, outcome effectiveness or deployment. The architecture remains closed unless a documented reopening trigger occurs.

PR #37 promotes a bounded behavioral-regression repair for strategic-resource completeness and binding `work-formation` activation. The Global and Project carrier blobs plus the canonical `work-formation` files were installed and read back before Promotion; the five failed or unverified obligations then passed targeted tests. The [behavioral repair evidence](evaluation/e2e-real-use/E2E-04-2026-08-28-RUNTIME-v0.6-BEHAVIORAL-REPAIR-v0.1.md) preserves the exact identities and limits: the 25 predecessor PASS cases were not rerun on the exact candidate, so this is not a fresh 30/30 or generalized Runtime-reliability claim. Target Architecture v0.2 remains closed.

PR #38 later promoted the bounded repository-source realization of the Professional Sufficiency & Method Activation Contract. Its Global `8fc25d99f3ffa66abe917e4a256a4701c929cffa` and Project `e8ddb7b4db27804667500beb41b206c5a5adfeff` blobs are the immediate protected pre-QOC prior, not current repository source. The last installed-carrier readback still identifies the earlier PR #37 blobs.

On 2026-08-30 the Human repository owner accepted IC-QOC-v0.1 at exact semantic Candidate head `47cfebea529660671c3a12fe2a20246b33c76c42`. The [QOC static regression review](reviews/QUALIFIED-ORCHESTRATION-v0.2-RUNTIME-COMPILATION-SEMANTIC-REGRESSION-v0.1.md) records the accepted blobs and bounded Static Source Regression PASS. Separate authorization produced status-reconciled head `af752f0c9583b223d84aa40a03b4e8f79bd17bfc`; PR #43 merged it into authoritative `main` as `fa536d914eede2ba005b5a3b1297c22110a7f34f`. That Promotion established Global `3f7a65c5f3fe667762c252d0f6cdf974f21759bc` and Project `3077c0c8504f7bcf95914018dd0bf56daf407b8c` as the immediate QOC predecessor carrier identities. PWB §3A and Topology §2A remain the accepted semantic/allocation loci.

The current downstream carrier recompilation leaves those owners and all protected upstream state unchanged while replacing only the compiled repository-source payloads: Global `2ab3fb01b31293eff529d2623cac5869829bf195` and Project `4615d61277575fe73fc43d39be7d52d183e5980a`. The Project embeds the complete Global kernel byte-identically and adds its System-Development overlay. Repository Promotion establishes neither exact installed identity nor session load, activation, behavioral conformance, professional fitness, Performance, outcome or value.

## Repository map

| Area | Purpose |
|---|---|
| `foundation/` | controlling concerns, requirements, and System of Interest |
| `architecture/` | accepted target architecture, non-normative correspondence/trace artifacts, and architecture guardrails |
| `decisions/` | accepted and historical Architecture Decision Records |
| `skills/` | canonical source for reusable skill packages plus portfolio registry |
| `.codex-plugin/plugin.json` | installable skills-only plugin view over the canonical `skills/` directory |
| `.agents/skills/` | repository-local Codex discovery links to the canonical packages |
| `realization/runtime/route-b/v0.6-chatgpt-runtime/` | native ChatGPT runtime instruction carriers and topology; not a second skill source |
| `realization/CHATGPT-NATIVE-OPERATIONALIZATION-MAP-v0.1.md` | current non-normative product-capability/surface operationalization companion; selected by `CURRENT.md` |
| `realization/DEPLOYMENT-AND-SURFACE-REALIZATION-DESIGN-v0.1.md` | current non-normative carrier/surface/deployment design; no semantic ownership or installed-state claim |
| `methods/` | historical or supporting method artifacts; active skill methods live with their skill package |
| `evaluation/` | case cards, real-use evidence, test designs, and results |
| `reviews/` | bounded source and promotion reviews |

## Native runtime model

Native ChatGPT owns the work episode: understanding the request, planning, tool use, production, integration, and communication. Reusable skills are selectively invoked professional methods, not a mandatory universal pipeline.

The active portfolio is indexed in [`skills/REGISTRY.md`](skills/REGISTRY.md). Its boundaries are intentional:

- materially open frame, opportunity, route, concept, or direction → `adaptive-exploration`
- blocking missing basis → `work-formation`
- missing or uncertain evidence → `research-evidence`
- bounded material choice → `decision-analysis`
- identifiable existing work product → `evaluate-work-product`
- work on this system or a comparable existing system → `system-development`
- ordinary planning, production, integration, and execution → native ChatGPT or a narrower domain method

Skill source identity, Personal Skill installation, runtime activation, runtime fitness, and outcome quality are separate claims and require separate evidence.

The source/deployment lifecycle is defined in [`skills/DEPLOYMENT-CONTRACT.md`](skills/DEPLOYMENT-CONTRACT.md). The repository does not use automatic two-way synchronization: runtime observations can justify a bounded source repair, but only the authorized repository path can promote it; installed copies change only through a separate install/update and readback transition.

## Change discipline

Repository changes move through explicit candidate, review, merge, and `main` readback transitions. A branch, pull request, installed copy, or successful isolated test is not promoted authority merely because it exists.