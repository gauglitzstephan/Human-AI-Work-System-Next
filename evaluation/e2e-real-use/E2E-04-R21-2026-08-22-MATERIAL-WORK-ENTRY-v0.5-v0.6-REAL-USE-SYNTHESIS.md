# E2E-04 R21 — material-work-entry v0.5/v0.6 Real-Use Reconciliation

**Date:** 2026-08-22  
**Status:** RECONCILIATION EVIDENCE / CANDIDATE — NO REPAIR, PROMOTION OR ARCHITECTURE CHANGE  
**Branch:** `reconcile/r21-material-work-entry-v0.6-real-use`  
**System of Interest:** Native ChatGPT work formation, bounded persistence and handoff behavior around the external Personal Skill `material-work-entry`

## 1. Purpose and authority boundary

This record reconciles three genuine-use cases after the R20 native Work-Skill validation:

1. wedding dessert / cake concept formation;
2. Nissan Pulsar versus electric-car decision;
3. personal information-system discovery and bootstrap.

It records observed behavior, version boundaries, evaluator corrections and the remaining qualification frontier. It does **not**:

- repair the Skill;
- change Target Architecture;
- promote any Runtime, Canonical or Skill state;
- merge this branch;
- turn all three cases into v0.6 proof;
- treat a conversation excerpt as the complete evidence universe.

The controlling repository state remains `main/CURRENT.md` until a separately authorized promotion and merge.

## 2. Evidence and version ledger

| Case | Runtime marker observed | Material frontier reached | Qualification |
|---|---|---|---|
| Wedding dessert | `material-work-entry v0.5-candidate` | Taste-led concept selection and vendor-ready direction | PASS within concept-formation frontier |
| Electric-car decision | `material-work-entry v0.5-candidate` | WAIT decision with triggers and review timing | PARTIAL: decision closure passed; assurance basis incomplete |
| Personal information system | initial v0.5 behavior, then `material-work-entry v0.6-candidate` | Cross-surface boundary discovery and controlling Current bootstrap | v0.5 failure localized; v0.6 boundary/bootstrap PASS; provider-return loop still open |

The three cases are not a homogeneous v0.6 promotion wave. The first two are retained as v0.5 legacy evidence. Only the personal information-system case directly exercises the v0.6 additions.

## 3. Case findings

### 3.1 Wedding dessert — bounded concept formation

Observed progression:

- the original category “wedding cake” was challenged rather than blindly optimized;
- Human taste changed the direction away from cream-heavy conventional cakes;
- season, place, guest count and desired ritual were progressively bound;
- the result converged on a fine, fresh pear–almond–vanilla tart concept;
- the output closed as a usable confectioner briefing while leaving recipe engineering, sizing, transport and holding stability to the vendor.

Qualified result:

```text
Problem reframing                         PASS
Human taste contribution                 PASS
Proportional exploration                 PASS
Concept closure                          PASS
Vendor technical feasibility             UNVERIFIED
Actual ordered/served outcome             UNVERIFIED
Persistence requirement                  NOT EARNED before vendor handoff
```

Lesson: an exploratory phase can and should have a strategy and an explicit stopping condition. “Exploration” is not unstructured conversation; here it was a bounded search over concept class, taste, seasonality, ritual and feasibility.

### 3.2 Electric-car decision — WAIT is a legitimate closure

Observed progression:

- the current reliable paid-off car was compared with financing a newer electric car;
- Human-supplied income information materially changed the funding assessment;
- the result closed with a WAIT decision, repair/change triggers and a review window.

Qualified result:

```text
Decision disposition                     PASS — WAIT
Trigger-based closure                    PASS
Human factual contribution               PASS
Current-evidence assurance                PARTIAL
Resale / savings / financing basis        NOT FULLY TRACEABLE
Funding-program interpretation            REQUIRES authoritative-current verification
Future monitoring/persistence             WEAK in v0.5 run
```

The v0.5 run cannot be used to prove or disprove the later v0.6 persistence trigger. The useful lesson is narrower: “do nothing now” can be a completed professional decision when its assumptions, triggers and review point are explicit.

### 3.3 Personal information system — system boundary and bootstrap

Initial v0.5 failure:

- the reachable Google Drive slice was initially treated too readily as the whole work object;
- a Windows inventory was dispatched before a durable Parent state existed;
- the Human correctly widened the System of Interest to Windows, local projects, Git repositories, GitHub, Drive, paper, communications, devices and other potentially forgotten surfaces.

v0.6 response:

- System-Boundary Discovery prevented the reachable evidence slice from silently becoming the whole system;
- a controlling `PERSONAL_INFORMATION_SYSTEM_CURRENT.md` was instantiated before the cross-surface provider return;
- that Current records Parent/outcome, system boundary, evidence slice, provisional structure, authority/protected actions, frontier, expected return and re-entry/update logic;
- the Windows scan remains read-only and suspended until/through the bootstrap boundary.

Qualified result:

```text
Reachable-slice ≠ whole-system correction PASS
Minimal Parent-state bootstrap             PASS
Cross-surface handoff contract             PASS at dispatch boundary
Windows provider return                    PENDING
Return → Parent rebind                      UNVERIFIED
Current update after return                UNVERIFIED
Actual information-system migration        NOT STARTED
```

## 4. Evaluator correction

An earlier evaluation incorrectly reported that no Current bootstrap had been created because the Human supplied only a text excerpt and not the link/file. Once `PERSONAL_INFORMATION_SYSTEM_CURRENT.md` was attached, its contents demonstrated that the required bootstrap existed.

Classification:

```text
Observed issue          evaluator evidence-slice error
Skill/runtime defect    NOT ESTABLISHED
Repair implication      NONE
Required correction     inspect available artifact before inferring absence
```

This is itself a system lesson: missing evidence in the evaluator’s current view is not evidence that the work product does not exist.

## 5. Cross-case lessons

### 5.1 Work control and professional method are different responsibilities

Entry/Formation control decides whether direct work is legitimate, what remains unknown, whether persistence is earned and where the next frontier lies. It does not replace domain method. Wedding aesthetics, automotive economics/funding law and personal information architecture each require their own professional method and evidence.

### 5.2 Human contribution is not synonymous with a Human gate

Human input is most valuable for taste, lived priorities, inaccessible facts, risk acceptance and authority-bearing decisions. The AI should acquire or research AI-resolvable context itself. A Human gate is justified only when a decision or missing input cannot legitimately be supplied by the AI.

### 5.3 Closure is typed, not singular

The cases demonstrate distinct legitimate endings:

- **concept closure:** a sufficiently specific direction and vendor brief;
- **decision closure:** WAIT with triggers and review time;
- **bootstrap closure:** a durable Parent state plus expected-return contract;
- **outcome closure:** external use or measured result, not yet present in these cases.

A formation run must declare which closure it reached and what remains outside the claim.

### 5.4 Persistence is risk-triggered, not complexity-triggered

A Project or Current file is not mandatory merely because an input is complex. Persistence is earned when work must survive time, chats, surfaces, provider returns or consequential state loss. The wedding concept did not require an immediate Project. The personal information-system investigation did require a minimal controlling state before a Windows handoff.

### 5.5 Repair the lowest responsible layer

Do not patch the Skill because:

- a v0.5 case predates a v0.6 mechanism;
- a domain assertion lacked enough authoritative evidence;
- an evaluator failed to inspect an attached Current;
- a provider return has not yet occurred;
- repository documentation lags the installed external candidate.

These are different failure classes and require different responses.

## 6. ChatGPT-native product reconciliation

Current official OpenAI documentation supports the following bounded operating model:

| Native construct | Supported role in this reconciliation | Unsupported overclaim |
|---|---|---|
| Chat | answers, explanations, brainstorming and bounded work | universal precursor stage to Work |
| Work | substantial work with multiple sources, tools, steps or deliverables | automatic guarantee of professional method or persistence |
| Project | conditional continuing context for related chats, files and instructions; can contain Chat and Work | mandatory container for every task or a professional method |
| Skill | focused reusable workflow selected explicitly or implicitly; test on realistic requests | universal availability/reliability across every surface and plan |
| Memory / chat history | selective contextual retrieval | authoritative Current, complete history or controlling state |
| Files / connectors / tools | bounded evidence or action providers | authority to act beyond granted permissions; proof of whole-system coverage |

There is no fixed product pipeline `Chat → Plan → Work → Project`. The legitimate route depends on the work’s outcome, evidence, continuity and authority needs. For persistent work, the useful invariant is state continuity across the chosen native surfaces, not ritual use of every surface.

Current official references consulted:

- https://learn.chatgpt.com/docs/get-started-with-work
- https://learn.chatgpt.com/docs/projects
- https://learn.chatgpt.com/docs/skills-and-plugins
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/plugins
- https://learn.chatgpt.com/docs/use-chatgpt
- https://learn.chatgpt.com/docs/customization/memories
- https://learn.chatgpt.com/blog/run-long-horizon-tasks-with-codex

The long-horizon Codex article is treated as a coding precedent for durable prompt/spec, plan, implementation/runbook, status and verification—not as a universal file stack for all ChatGPT work.

## 7. Repair and architecture decision

```text
Target Architecture                       KEEP CLOSED
Global Custom Instructions                NO NEW REPAIR
material-work-entry v0.6-candidate        KEEP CANDIDATE
Skill source/structure                    PREVIOUSLY VALIDATED
Repository/runtime reconciliation         REQUIRED and performed only on this branch
Skill repair                              NOT AUTHORIZED / NOT JUSTIFIED
Runtime promotion                         NOT AUTHORIZED
Merge / PR                                NOT AUTHORIZED
```

The evidence supports the two v0.6 additions as necessary and promising:

1. System-Boundary Discovery;
2. Persistence/Bootstrap Trigger.

It does not yet establish full v0.6 end-to-end reliability.

## 8. Remaining qualification frontier

Before any repair or promotion decision, obtain the smallest missing evidence:

1. **Provider-return/rebind:** complete the read-only Windows inventory, return it to the personal information-system Parent, verify rebind and update the Current.
2. **Consequential v0.6 decision:** run one real decision requiring current authoritative evidence and verify closure plus persistence/monitoring behavior.
3. **Negative control:** run one tiny bounded request under v0.6 that must remain direct and must not create a Project, Current or unnecessary Formation.

Success requires exact version attribution, artifact inspection before absence claims, claim-bounded evidence and no automatic promotion from a positive run.

## 9. Disposition

> **CONTINUE — provider-return/rebind qualification. KEEP architecture closed. Keep `material-work-entry v0.6-candidate` unpromoted. No repair is justified by the reconciled evidence.**

[material-work-entry v0.6-candidate]
