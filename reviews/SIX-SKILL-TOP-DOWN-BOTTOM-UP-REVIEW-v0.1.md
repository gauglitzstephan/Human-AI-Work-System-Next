# Six-Skill Top-Down / Bottom-Up Review v0.1

## Evaluated claim

Whether the six canonical Skill packages on `main` form a coherent, technically realizable, context-efficient portfolio for ChatGPT and Codex, and what smallest repairs are required before a new deployment candidate is justified.

## Decision

**PASS — REPOSITORY PROMOTED WITH BOUNDED REPAIRS.**

The six responsibilities are coherent and collectively sufficient for the intended selective-method layer. No seventh controller, calibration, planning, execution, state, or assurance Skill is justified.

The current package semantics are preserved. The completed repairs cover discovery metadata, entrypoint compaction, stale method-status labels, and native packaging/discovery mechanics. PR #29 was merged to `main` as `15f3f3b0e72f33ea45d4800d1b520649ca119f59`.

Installation, implicit activation, runtime execution quality, and outcome quality remain separate and unverified for the repaired package until deployment/readback and genuine use.

## Current official runtime facts

Official OpenAI documentation establishes that:

- Skill selection starts from `name` and `description`; the full `SKILL.md` loads only after selection.
- Descriptions may be shortened under the initial Skill-list context budget, so positive triggers and essential exclusions must be front-loaded.
- Codex repository discovery uses `.agents/skills` and follows symbolic links.
- A plugin can package multiple related Skills by pointing its manifest to `./skills/`.
- Repository presence, plugin packaging, installation, and runtime behavior are distinct states.

Primary basis: https://learn.chatgpt.com/docs/build-skills and https://learn.chatgpt.com/docs/build-plugins

## Package dispositions

| Package | Top-down responsibility fit | Bottom-up/source issue | Disposition |
|---|---|---|---|
| `adaptive-exploration` | clean owner for CCR-01 open-space integrity | description over-explains routing | REPAIR description; KEEP method |
| `work-formation` | clean owner for materially blocking missing basis | description can be shorter and more trigger-first | REPAIR description; KEEP method |
| `research-evidence` | clean cross-domain evidence discipline and specialist-method router | description too long for its primary trigger | REPAIR description; KEEP method |
| `decision-analysis` | clean owner for bounded material choice | 1,024-character description risks truncating exclusions; `SKILL.md` duplicates the detailed reference | REPAIR description and compact entrypoint; KEEP method |
| `evaluate-work-product` | clean owner for existing-product fit-for-use evaluation | description and entrypoint duplicate method detail | REPAIR description and compact entrypoint; KEEP method |
| `system-development` | clean owner for this system's recovery, diagnosis, compilation, promotion, and genuine-use validation | description slightly broad; three active references still claim Candidate status | REPAIR description/status labels; KEEP methods |

No package is replaced or retired.

## Top-down semantic trace

| Requirements concern | Runtime owner/mechanism | Result |
|---|---|---|
| CR-01 outcome before means | Native Instructions; `work-formation` only when missing basis is material | PASS |
| CR-02 scope/contribution integrity | Native episode ownership plus claim-relative binding across Skills | PASS |
| CR-03 reality/epistemic integrity | Native Instructions; `research-evidence`; truth boundaries in other methods | PASS |
| CR-04 actual state before change | `system-development` recovery method; Formation only for a blocking gap | PASS |
| CR-05 professional sufficiency/reuse | every Skill routes to narrower qualified methods when needed | PASS |
| CR-06 comparative composition | Native ChatGPT, not a Skill controller | PASS |
| CR-07 Human agency/attention | Human-only contributions and no manufactured gates across methods | PASS |
| CR-08 capability/status/authority | Native Instructions plus explicit method boundaries | PASS |
| CR-09 state/knowledge/continuity | Native/Project Instructions and authoritative repository; no unnecessary Skill | PASS |
| CR-10 minimum sufficient work | proportional activation and stop rules across all six | PASS |
| CR-11 claim-matched assurance | `evaluate-work-product` for products; `system-development` for runtime; specialist methods where required | PASS |
| CR-12 transition/use/outcome integrity | Native Instructions and explicit non-claims across methods | PASS |
| CR-13 runtime/provider fidelity | `system-development` runtime-compilation method plus this packaging repair | PASS AT SOURCE / DEPLOYMENT UNVERIFIED |
| CR-14 evidence-bound learning/change | `system-development` real-use and promotion methods | PASS |
| CCR-01 open exploration | `adaptive-exploration` | PASS AT SOURCE |
| CCR-02 persistent/divergent state | authoritative repo plus Project/Runtime state rules; not a universal Skill | PASS |
| CCR-03 consequential risk/recoverability | Native authority/permissions and narrower domain methods | PASS |
| CCR-04 recipient/use maturity | `evaluate-work-product` plus responsible production method | PASS |
| CCR-05 uncertainty/information/commitment | `decision-analysis` and `research-evidence` | PASS |
| CCR-06 competing initiatives/resources | Strategic/Operating responsibility; no local Skill authority | PASS |
| CCR-07 Human capability preservation | Native Human-allocation rule; no ceremony Skill | PASS |

Architecture remains closed: the repair realizes existing semantics and adds no responsibility or mandatory lifecycle.

## Bottom-up compilation result

| Mechanism | Before | Candidate result |
|---|---|---|
| canonical source | `main/skills/` | preserved |
| installed identity for five existing Skills | exact normalized text match, including all references | preserved as evidence for predecessor versions; repaired versions require new deployment readback |
| `adaptive-exploration` installation | absent/unverified | unchanged until explicit deployment |
| description discovery economy | about 3,922 characters for six names/descriptions; several descriptions overlong | about 2,542 characters and trigger-first |
| progressive disclosure | Decision and Evaluation entrypoints duplicate detailed references | entrypoints compacted; detailed methods remain authoritative in references |
| Codex repo discovery | no `.agents/skills` view | symbolic links point to canonical packages without duplication |
| ChatGPT/Codex distribution | no plugin manifest | skills-only plugin manifest points to `./skills/` |
| two-way synchronization | no safe automatic mechanism | explicit controlled source→deploy→readback and evidence→repair→promotion contract |

## Static assurance

| Check | Result |
|---|---|
| canonical Skill Creator validation for all six packages | PASS |
| canonical Plugin Creator validation | PASS after adding the required `interface.defaultPrompt` metadata |
| description length and discovery economy | PASS — every description is 447 characters or fewer; aggregate name/description footprint reduced from about 3,922 to about 2,542 characters |
| progressive disclosure | PASS — Decision entrypoint reduced from 8,833 to 3,476 bytes; Evaluation entrypoint from 5,089 to 3,302 bytes; substantive methods remain in references |
| `SKILL.md` reference resolution | PASS |
| 24 portfolio activation/boundary cases | PASS at static semantic level |
| `.agents/skills` symbolic-link identity | PASS — six mode-`120000` Git entries; every target blob resolves to the intended canonical package path |
| candidate-branch readback | PASS — all 17 text artifacts match their created Git blob identities |
| post-merge `main` readback | PASS — PR #29 is merged; all 17 text artifacts retain their candidate blob identities on `main`, and the six mode-`120000` discovery links retain their validated targets |

## Claim boundary

A successful merge may establish only a coherent, validated repository and installable packaging candidate. It cannot establish that a ChatGPT or Codex surface has installed the repaired package, selects it implicitly, executes it correctly, improves genuine work, or produces value.
