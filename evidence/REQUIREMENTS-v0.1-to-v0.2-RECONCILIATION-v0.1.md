# Requirements v0.1 → v0.2 Reconciliation and Promotion Evidence v0.1

**Status:** PROMOTION EVIDENCE RECORD — PR #18 merge/readback and bounded post-merge authority reconciliation complete  
**Date:** 2026-08-24  
**Claim boundary:** bounded semantic reconciliation, de-bias review, Target-Architecture compatibility, exact-head assurance and repository-promotion readback for Requirements v0.2

## 1. Authoritative and qualified source basis

Repository sources inspected:

| Source | Path | Version / SHA | Use |
|---|---|---:|---|
| Prior Requirements baseline | `foundation/CONCERNS-AND-REQUIREMENTS-v0.1.md` | `3ce54f737ff5c3f8dfdbe7edb2fe92c99d6a6ffb` | prior controlling Requirement semantics / historical Qualified Prior |
| System of Interest | `foundation/SYSTEM-OF-INTEREST.md` | prior promotion-candidate source + post-merge reconciled main state | parent problem, scope and performance concerns |
| Architecture Principles | `architecture/ARCHITECTURE-PRINCIPLES-v0.1.md` | `76b95269d45490eeb7c9608df675ed4eea167b4e` | de-bias, proportionality and type-correctness challenge |
| Target Architecture | `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md` | `75d2669a3bf2d55258ad4f6e171ae55139e1d2c8` | compatibility and ownership check |
| Prior architecture decision | `decisions/ADR-0002-target-conceptual-baseline.md` | `6565fe47896168a43f054ebdb739e7f4d9b7c8b4` | prior Requirements/Architecture authority transition |
| Architecture method | `architecture/ARCHITECTURE-METHOD.md` | `49d9e2be213d05eece012f70a08288993da1ee18` | qualified-prior and reopen discipline |
| Pre-promotion program authority | `CURRENT.md` | `main@5e3c84309b3c59da4ba8bde7748c66eaa41d802f`; blob `e4f615b154e84352f36f13293a41d7f1f696a6d1` | active state and gate after PR #17 merge/readback |
| Human decisions | System Development conversation, 2026-08-24 | `ACCEPT` + bounded six-file write authorization + explicit PR #18 merge authorization | Requirements Design Basis acceptance, Candidate persistence/review and Promotion authority |
| Candidate branch | `reconcile/vnext-requirements-v0.2` | base `main@5e3c84309b3c59da4ba8bde7748c66eaa41d802f`; final reviewed head `e00fb7d2249e4bcd51f3ce50f32480edf039f1da` | exact Candidate persistence and review vehicle |
| Promotion merge | PR #18 | merge `b355ed63ad94d6456a6913cac079458238067921` | Requirements v0.2 repository Promotion |

Relevant internal evidence includes R20/R21 real-use/runtime records and the later observed high-latency/over-orchestration trigger. These records support Requirements formation and de-biasing; they do not by themselves promote the Requirement or reopen architecture.

## 2. Reconciliation method

The review preserves materially valid semantic obligations, not every prior wording or packaging choice.

Allowed dispositions:

```text
PRESERVE
STRENGTHEN
MERGE
RELOCATE
ADD
RETIRE
OPEN
```

A prior Requirement is not retained merely because it existed. A local failure does not become a global Requirement unless it exposes a material unowned semantic obligation.

Mechanisms such as Parent Rebind, Human-facing Control Return, Handoff Contracts, Skills or Subagent patterns remain outside the normative Requirements baseline unless their provider-neutral semantic obligation cannot be represented otherwise.

## 3. v0.1 → v0.2 treatment map

| v0.1 Requirement | Prior normative core | v0.2 location | Treatment | Reason |
|---|---|---|---|---|
| CR-01 | outcome/need before proposed means | CR-01 | PRESERVE | still universally material at the semantic level |
| CR-02 | claim-relative boundary and scale | CR-02 + IR-05 | STRENGTHEN | adds local-contribution integrity without importing a Parent/Rebind mechanism |
| CR-03 | reality, provenance, freshness, epistemic distinctions | CR-03 | PRESERVE | no material semantic change |
| CR-04 | actual state before consequential change | CR-04 | PRESERVE | retains proportional non-archaeological recovery |
| CR-05 | intended-use professional sufficiency and qualified reuse | CR-05 | STRENGTHEN | professional floor, Domain Method and reuse basis made more explicit |
| CR-06 | comparative Human–AI composition | CR-06 + CR-07 | STRENGTHEN | separates comparative allocation from Human agency/attention economics |
| CR-07 | Human agency, legitimate contribution, shared-state legibility | CR-07 | STRENGTHEN | adds attention/interruption/correction burden and AI-resolvable ownership |
| CR-08 | capability/access/authority/status integrity | CR-08 | STRENGTHEN | preserves decision/commitment/authorization/execution distinctions |
| CR-09 | Working State ≠ authority ≠ reusable knowledge | CR-09 + CCR-02 | STRENGTHEN | adds Continuity-first persistence semantics |
| CR-10 | minimum sufficient work, preservation and transition integrity | IR-04 + CR-10 | STRENGTHEN | makes non-compensatory floors and Whole-System Economics explicit |
| CR-11 | exact-claim, failure-detecting Assurance | CR-11 | STRENGTHEN | adds Domain/use-relative evaluation and avoids generic metric substitution |
| CR-12 | production → transition → use → outcome/value | CR-12 | PRESERVE | no material semantic change |
| CR-13 | Runtime/implementation fidelity and semantic preservation | CR-13 | STRENGTHEN | adds provider/surface isolation, portability and bounded diagnosability |
| CCR-01 | open framing/search integrity | CCR-01 | STRENGTHEN | explicitly covers professional Exploration readiness |
| CCR-02 | persistent/divergent state | CCR-02 | STRENGTHEN | Continuity Floor precedes shallow-carrier choice |
| CCR-03 | consequential risk/control | CCR-03 | PRESERVE | remains conditional and risk-proportionate |
| CCR-04 | Recipient/use-dependent maturity | CCR-04 | PRESERVE | transformation remains distinct from QA |
| CCR-05 | future uncertainty/commitment | CCR-05 | STRENGTHEN | adds explicit Information Value and staged/reversible alternatives |
| CCR-06 | competing initiatives/resources | CCR-06 | PRESERVE | remains a conditional strategic-resource concern |
| CCR-07 | Human capability formation/preservation | CCR-07 | PRESERVE | remains conditional rather than ceremonial |
| — | evidence-bound learning/change not explicit as one Requirement | CR-14 | ADD | makes local learning ≠ global mutation explicit while retaining narrow repair |

### Resulting claim

The bounded semantic crosswalk found no materially still-valid V0.1 obligation left without an owner in v0.2.

This is not a claim of eternal completeness or word-for-word lineage identity.

## 4. R01–R30 formation-candidate normalization

The earlier R01–R30 Candidate was a useful formation artifact but mixed Core, Conditional, interpretation, economics and Runtime concerns.

| R01–R30 Candidate | Normalized treatment |
|---|---|
| R01 | CR-01 |
| R02 | CR-02 |
| R03 Strategic/Portfolio | CCR-06 |
| R04 | CR-03 |
| R05 | CR-04 |
| R06 + R07 | CR-05 |
| R08 | CR-01 + CR-10 |
| R09 Exploration | CCR-01 |
| R10 Information Value | CR-10 + CCR-05 |
| R11 Decision/Commitment | CR-08 + CCR-05 |
| R12 | CR-06 |
| R13 + R14 | CR-07 |
| R15 | CR-08 |
| R16 Native Leverage | CR-06 + CR-13 |
| R17 | CR-13 |
| R18 | CR-08 |
| R19 Risk | CCR-03 |
| R20 | CR-09 |
| R21 Persistence | CR-09 + CCR-02 |
| R22 Orchestration | CR-06 + CR-10 + IR-05 |
| R23 | CR-10 |
| R24 + R25 | CR-11 |
| R26 | CR-12 |
| R27 | CR-10 |
| R28 Observability | CR-11 + CR-13 |
| R29 + R30 | CR-14 |

Disposition:

```text
R01–R30 semantic content     RETAINED where justified
R01–R30 packaging            SUPERSEDED by normalized v0.2
R01–R30 separate authority   NONE
```

## 5. Known-failure coverage without failure overfit

| Known failure / risk | Requirement coverage | Deliberately solution-open |
|---|---|---|
| Premature Solutioning | CR-01, CR-05, CCR-01 | Admission/Formation mechanism |
| Wrong evidence slice / wrong SoI | CR-02–04 | Retrieval and Context architecture |
| Professional Method not activated | CR-05, CR-13 | Method/Skill routing |
| Professional Exploration treated as trivial | CCR-01 | Work Mission representation |
| False Human Gate / avoidable Human burden | CR-07, CR-08, CR-10 | Interaction policy |
| Parent drift / child self-promotion | CR-02, IR-05, CR-08, CR-10 | Rebind and Control-Return mechanism |
| State divergence / memory-as-authority | CR-09, CCR-02 | carrier and reconciliation design |
| Over-orchestration / serial review chains | CR-06, CR-10 | Agent topology and coordination design |
| Context bloat | CR-10, CR-13 | progressive Context mechanism |
| Assurance explosion | CR-10, CR-11 | assurance composition |
| Architecture says it, Runtime does not | CR-13 | concrete Runtime realization |
| Local failure becomes global patch | CR-14 | change/promotion process |
| Speed optimization drops required work | IR-04, CR-05, CR-10 | Runtime activation/calibration |
| Provider/product lock-in | CR-13 | adapter and portability realization |

## 6. Adversarial de-bias review

| Bias challenge | Finding |
|---|---|
| Control/Governance overfit | PASS — no Parent Rebind, Control Return, Human Gate, Handoff or Promotion mechanism promoted into Requirements |
| Recent-failure overfit | PASS — recent failures are covered through general semantics rather than one Requirement per incident |
| Simplicity bias | PASS — Professional/Reality/Authority/Continuity/Assurance floors cannot be traded away for speed |
| Legacy-preservation bias | PASS — dispositions allow Merge, Relocate, Add or Retire rather than preservation by default |
| Provider/ChatGPT bias | PASS — no named provider/product topology is normative |
| Single-/Multi-Agent ideology | PASS — comparative composition remains task-relative |
| Metrics bias | PASS — no universal time, token, Agent-count or generic-quality target |
| Materiality escape hatch | PASS at Requirement level — IR-02/IR-03 prevent unsupported sufficiency while retaining implicit simple work |
| Artifactization bias | PASS — the durable package is limited to one baseline, one evidence record and one ADR plus necessary authority/navigation updates |

## 7. Target Architecture v0.2 compatibility

The accepted Target Architecture has three structural commitments:

```text
distinct responsibilities
distributed typed state
adaptive work selection
```

plus cross-cutting Reality/State, Capability/Authority/Agency, Professional Quality/Claim, and Value/Realization/Change invariants.

### Core mapping

| v0.2 Requirement | Target Architecture owner |
|---|---|
| CR-01 | Work Responsibility + Adaptive Work-Selection inputs |
| CR-02 | claim-relative boundary + responsibility/authority boundaries + preservation |
| CR-03 | Reality & State Integrity invariant + current-reality input |
| CR-04 | current reality/preserved state/evidence-qualified reuse |
| CR-05 | Work Responsibility + professional performance input + Professional Quality invariant |
| CR-06 | Responsibility ≠ Actor + effective capability/economics inputs + adaptive route selection |
| CR-07 | Capability/Authority/Agency invariant + Human contribution/economics inputs |
| CR-08 | typed state + Capability/Authority/Agency invariant |
| CR-09 | Distributed Typed State |
| CR-10 | Adaptive Work Selection + resource/coordination/delay/opportunity-cost inputs |
| CR-11 | Work Responsibility + Professional Quality/Claim Integrity invariant |
| CR-12 | Work Responsibility transition/use + Value/Realization invariant |
| CR-13 | Execution Responsibility + actual Runtime conditions + semantic-preservation obligation |
| CR-14 | Learning/Change Responsibility + bounded change through legitimate owners |

### Conditional mapping

| v0.2 Conditional Requirement | Target Architecture owner |
|---|---|
| CCR-01 | open framing/search conditional mechanism |
| CCR-02 | Distributed Typed State + persistent/divergent-state conditional mechanism |
| CCR-03 | consequence/risk inputs + consequential-risk conditional mechanism |
| CCR-04 | Recipient/use-dependent refinement conditional mechanism |
| CCR-05 | uncertainty/commitment section + future-uncertainty conditional mechanism |
| CCR-06 | Strategic/Operating Responsibility + competing-initiative conditional mechanism |
| CCR-07 | Human capability formation/preservation conditional mechanism |

### Compatibility finding

```text
unowned v0.2 Requirement                  NONE FOUND
architecture contradiction               NONE FOUND
new mandatory architecture object        NONE REQUIRED
Target Architecture semantic change      NONE REQUIRED
architecture reopen trigger              NOT ESTABLISHED
```

Target Architecture v0.2 remains accepted and closed. The exact-head compatibility review passed before PR #18 merge; the Requirements promotion introduced no architecture semantic change.

This is a bounded compatibility finding, not a new architecture-acceptance claim.

## 8. Promotion assurance

### Static content checks

- exactly 5 Interpretation Rules;
- exactly 14 Core Requirements;
- exactly 7 Conditional Requirements;
- unique IDs;
- all v0.1 CR/CCR items treated in the crosswalk;
- all v0.2 Requirements mapped to Target Architecture;
- no named ChatGPT/Work/Codex/Skill/Project/Subagent topology in normative obligations;
- no mandatory lifecycle, visible workflow, artifact, Gate or persistent state introduced;
- no Runtime/behavioral/outcome claim promoted;
- no unresolved conflict between Quality Floors and Economy;
- `materiality` and `sufficiency` interpretation rules present;
- local contribution does not self-promote wider state.

### Repository-state checks

- PR #17 merged and read back on `main`;
- exact authorized PR #18 base was `main@5e3c84309b3c59da4ba8bde7748c66eaa41d802f`;
- Candidate branch was `reconcile/vnext-requirements-v0.2`;
- changed-file set matched the authorized six-file package;
- old v0.1 file remained unchanged and historically accessible;
- ADR-0002 remained unchanged;
- Target Architecture v0.2 remained unchanged;
- no files under `realization/`, Runtime, Skills or external systems changed;
- PR #18 was explicitly authorized and merged at `b355ed63ad94d6456a6913cac079458238067921`;
- post-merge `main` readback confirmed Requirements v0.2 presence and exposed only stale pre-merge status wording, repaired by bounded authority reconciliation.

### Promotion claim boundary

PR #18 merge + readback establishes only:

```text
Requirements v0.2        controlling repository Requirements baseline
Requirements v0.1        superseded as controlling / retained historical
ADR-0003                 active Requirements-transition decision
Target Architecture v0.2 retained / compatibility requalified / not reopened
Runtime Solution Formation next eligible frontier / not yet executed
```

It does not establish:

- Runtime or Skill change;
- architectural superiority;
- behavioral effectiveness;
- cross-domain empirical completeness;
- any solution topology;
- any Runtime Solution Formation result.

## 9. Exact-head integrity failure, bounded repair and re-review

The first persisted Candidate commit was:

```text
242a8bd574e46ab9d180ef68b3a369369c43f47a
```

A subsequent attempted `CURRENT.md` cleanup produced head:

```text
9ed57379afd3478fdc56a7fd4431ada9f74fed07
```

The exact-head challenge found that this second commit had replaced the entire repository `CURRENT.md` content with the literal local path:

```text
/mnt/data/req_work/CURRENT.corrected.md
```

Therefore:

```text
write action success              ≠ correct persisted state
intended repair                   ≠ verified repair
9ed57379... package integrity     FAIL
Requirements semantics           NOT IMPUGNED by this failure
Architecture compatibility       NOT IMPUGNED by this failure
```

The bounded repair first reset `reconcile/vnext-requirements-v0.2` to the last intact Candidate commit `242a8bd574e46ab9d180ef68b3a369369c43f47a`, removing the destructive commit from the active branch. The Evidence Record was then updated at `592dd0ea8564e4fbdad02023f4876b1f153277de`.

The new exact-head diff subsequently exposed four residual, unintended `CURRENT.md` deltas: one claim wording change, one typo and two formatting-only changes. These were repaired in two bounded `CURRENT.md` commits, ending at:

```text
7c208c961d22a81caca538c992366c2cb7561a97
```

The exact-head challenge at `7c208c961d22a81caca538c992366c2cb7561a97` found:

```text
CURRENT.md structural integrity              PASS
unintended post-R21 CURRENT regressions       NONE FOUND
changed-file scope                            EXACTLY SIX
branch relation to authorized base            AHEAD 4 / BEHIND 0
Requirements semantic candidate               PASS
Target Architecture compatibility             PASS within bounded static claim
authority/supersession semantics              PASS
Runtime / Skill / UI / solution change        NONE
```

The final Candidate head was `e00fb7d2249e4bcd51f3ce50f32480edf039f1da`. GitHub later reported it mergeable with no observed commit-status blockers before the Human merge authorization.

No Requirements, Architecture, Runtime, Skill, Project UI or solution semantics were changed by the repair itself.

## 10. Promotion and readback status

```text
semantic reconciliation                    PASS
de-bias review                             PASS
known-failure coverage                     PASS within current evidence
Target Architecture compatibility          PASS within bounded static claim
repository Candidate persistence           COMPLETE
prior exact-head challenge                  FAIL at 9ed57379afd3478fdc56a7fd4431ada9f74fed07
bounded CURRENT.md repair                   PASS through 7c208c961d22a81caca538c992366c2cb7561a97
final reviewed Candidate head               e00fb7d2249e4bcd51f3ce50f32480edf039f1da
PR #18 merge                               PASS / b355ed63ad94d6456a6913cac079458238067921
post-merge main readback                    PASS
Requirements v0.2 Promotion                COMPLETE
Requirements v0.1 controlling role         SUPERSEDED
Target Architecture v0.2                    ACCEPTED / CLOSED / NOT REOPENED
Runtime Solution Formation                  ELIGIBLE / NOT YET EXECUTED
```

---
