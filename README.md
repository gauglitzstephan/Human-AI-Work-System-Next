# Human–AI Work System Next

A requirements-led Human–AI work system for preserving context, choosing fit-for-purpose methods, executing real work, and improving from evidence without collapsing architecture, runtime behavior, and outcomes into one claim.

## Authority

Start with [`CURRENT.md`](CURRENT.md). It declares the current promoted state and the next valid transitions.

The controlling system basis is:

- [`foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md`](foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md)
- [`architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`](architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md)

The architecture is closed unless a documented reopening trigger occurs. Runtime repairs and new skill realizations do not reopen it by default.

## Repository map

| Area | Purpose |
|---|---|
| `foundation/` | controlling concerns, requirements, and System of Interest |
| `architecture/` | target architecture, decisions, traceability, and guardrails |
| `skills/` | canonical source for reusable skill packages plus portfolio registry |
| `realization/runtime/route-b/v0.6-chatgpt-runtime/` | native ChatGPT runtime instruction carriers and topology; not a second skill source |
| `methods/` | historical or supporting method artifacts; active skill methods live with their skill package |
| `evaluation/` | case cards, real-use evidence, test designs, and results |
| `reviews/` | bounded source and promotion reviews |
| `archive/` | superseded artifacts retained for history where needed |

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

## Change discipline

Repository changes move through explicit candidate, review, merge, and `main` readback transitions. A branch, pull request, installed copy, or successful isolated test is not promoted authority merely because it exists.
