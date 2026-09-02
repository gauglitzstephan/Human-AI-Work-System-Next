# E2E-04 / R20 — Native Work Skill Validation and Product-Semantics Reconciliation

**Date:** 2026-08-21  
**Status:** MATERIAL VALIDATION EVIDENCE — `material-work-entry v0.2` behaviorally supported on the tested ChatGPT Work surface; further synthetic testing of documented ChatGPT product semantics is not required.  
**Parent:** Human–AI Work System Runtime realization / R20 Entry-Admission repair.  
**Static Architecture:** KEEP CLOSED.  
**Promotion:** NONE. Skill remains an external ChatGPT Personal Skill / runtime candidate, not repository-promoted Runtime state.

## 1. Why this record exists

R20 originally localized a failure in Cold-Start Entry/Admission: ordinary ChatGPT behavior could move directly into preferred solution/story architecture before adequate professional Performance/Reference/Method Formation.

Global-CI-only repair candidates v0.6 and v0.7 both failed behaviorally. A local explicit Admission guard passed. A Two-Pass API gateway was prototyped as a different enforcement class, but live validation was later deferred because the Human preferred to exhaust simpler native ChatGPT mechanisms before adding API billing/infrastructure.

A Personal Skill, `material-work-entry`, was then formed and tested in ChatGPT Work.

During that work, some tests accidentally mixed two different questions:

1. **documented product semantics** — what ChatGPT Work, Chat, Projects, Memory and Personal Skills are designed to do;
2. **system-specific behavioral validity** — whether this custom Skill actually performs the required Entry/Admission behavior with acceptable routing/proportionality.

The Human correctly challenged the need to spend manual effort re-discovering documented ChatGPT functionality. This record therefore reconciles the product facts from current OpenAI documentation with the empirical Skill evidence and stops unnecessary synthetic product-feature testing.

## 2. Current documented ChatGPT product semantics

Official OpenAI documentation current on 2026-08-21 establishes the following.

### 2.1 ChatGPT Work

OpenAI describes ChatGPT Work as the ChatGPT agent for longer, more demanding work. In the desktop app, Chat and Work are modes within ChatGPT; Chat and Work chats appear together under Recents. Cloud Work chats sync across web, mobile and desktop.

A Project can start either a Chat or a Work chat. When Work is started inside a Project, it uses the Project context.

Source:
- https://help.openai.com/de-de/articles/20001275-chatgpt-work-and-codex

### 2.2 Projects and context

Projects keep related chats, files and instructions together and have built-in memory/context. A Project may be configured with project-only or default memory. With project-only memory, outside conversations are excluded. With default memory, saved memories are used, chats can use other conversations in the same Project, and for non-Enterprise plans outside-project context may also be referenced depending on settings/plan.

The important runtime implication is:

```text
Project
= explicit persistent context boundary/carrier

Chat or Work inside the Project
= different work surfaces using that Project context
```

Source:
- https://help.openai.com/de-de/articles/10169521-projects-in-chatgpt

### 2.3 General Memory / chat-history reference

When enabled, ChatGPT Memory can use useful context from chats, files and connected apps. `Reference chat history` can bring relevant information from earlier conversations into later responses. This is selective contextual retrieval, not a guarantee that every prior chat detail becomes authoritative state.

Source:
- https://help.openai.com/de-de/articles/8590148-faq-zu-erinnerung
- https://help.openai.com/de-de/articles/11146739-wie-funktioniert-gespeicherte-erinnerungen-verwenden

### 2.4 Personal Skills

OpenAI documents Skills as reusable workflows that ChatGPT can automatically use when helpful after installation. The Plugin documentation specifically states that Personal Skills in **Work** are available on paid plans except Free and Go; invocation/availability may depend on plan, role, workspace settings and supported surface.

Therefore the Human's observed UI — manual Personal Skill selection in Work, not ordinary Chat — is consistent with current product documentation. A separate synthetic test was not required to establish that product boundary.

Sources:
- https://help.openai.com/de-de/articles/20001066
- https://help.openai.com/de-de/articles/20001256-plugins-in-chatgpt-und-codex

## 3. Correction to prior test interpretation

A previous S6 normal-Chat run was used to explore whether `material-work-entry` might auto-activate in ordinary Chat even though the Skill selector was only visible in Work.

That experiment is no longer required as a product-semantics test. Current documentation already places Personal Skills in Work and makes supported-surface availability explicit.

The S6 result therefore must **not** be promoted into a stronger claim such as:

> normal Chat is an empirically falsified Skill runtime.

The correct bounded claim is:

> `material-work-entry` was validated on Work, the surface where the user's Personal Skill is actually exposed and where current OpenAI documentation explicitly supports Personal Skills. No additional ordinary-Chat Skill-enforcement claim is needed for the current native runtime candidate.

## 4. Skill candidate and bounded repairs

### v0.1

`material-work-entry v0.1` successfully activated manually in Work and detected fresh/material work, but a fresh street-lighting case still formed and then prematurely named a strongest architecture candidate.

Verdict:

```text
Invocation                         PASS
Fresh-work detection               PASS
Substantive Formation              PASS
Professional/reference basis       INSUFFICIENT
Probe→Candidate boundary            FAIL
```

### v0.2 repair

v0.2 changed only the Skill body, not the auto-routing description. It strengthened:

- professional Performance/Reference/Method formation before route qualification;
- explicit prohibition on ranking/preference during open Formation unless earned;
- probe→Candidate boundary;
- self-qualification caution.

The validation marker was changed to `[material-work-entry v0.2]`.

## 5. v0.2 behavioral evidence on Work

### S1-COLD — manual fresh Work / sewer-history Graphic Novel

Prompt: new Graphic Novel about the history of sewerage.

Observed:

- marker present;
- historical problem core formed;
- professional/historiographic quality criteria formed;
- references/evidence used;
- three story routes explicitly kept as unqualified probes;
- no story architecture selected;
- substantive next test defined.

Verdict: **PASS**.

### S2-WORK-AUTO — water-supply Graphic Novel

The old overlapping `discover-and-form-work` Skill was removed. In the next fresh Work run only `material-work-entry v0.2` was used automatically.

Observed:

- automatic Skill activation;
- substantive historical/reference Formation;
- three narrative models remained not selected;
- no premature strongest/preferred route.

Verdict:

```text
Auto activation in Work             PASS
Single-Skill attribution            PASS
Cold-start Formation                PASS
Probe integrity                     PASS
```

### DIRECT negative control — translation

Prompt: translate one supplied sentence.

Observed:

- no Skill activated;
- direct correct translation.

Verdict: **PASS — correct non-activation / proportional DIRECT behavior.**

### Explicit ideation control

A beer Graphic-Novel ideation run activated both the Skill and Memory, so causal attribution was confounded by existing beer-work context.

A fresh unseen mailbox-history ideation prompt was then used.

Observed:

- no Skill activated;
- five direct creative ideas;
- no Formation ceremony.

Verdict: **PASS — explicit exploration remains DIRECT when no material prior-work context is retrieved.**

### Changed-claim re-admission

Three-turn Work case:

1. ceramic-cup product description → direct;
2. shorten it → bound continuation/direct;
3. change into a complete premium brand positioning → Skill activated and Formation opened.

Observed on turn 3:

- prior product copy correctly demoted to a subordinate communication module;
- competitive/reference evidence added;
- strategic territories remained unqualified hypotheses;
- no route selected.

Verdict: **PASS — material changed claim re-admitted.**

### Nested professional child

Three-turn Work case:

1. shipping note for an existing notebook shop → direct;
2. translate note → direct;
3. additionally develop a professional loyalty program for the same shop → Skill activated and Formation opened.

Observed:

- professional/economic criteria before mechanics selection;
- four mechanisms remained unqualified probes;
- no loyalty mechanism selected.

Verdict: **PASS — existing Parent + new professional Child is re-admitted.**

A wording issue (`new Work Object` instead of more precise child claim/object under the existing Parent) was observed but did not produce actual Parent drift in the tested work.

## 6. Qualified Work-surface mechanism matrix

```text
manual Skill invocation in Work                 PASS
fresh material cold-start Formation             PASS
automatic activation on material new work       PASS
single-Skill attribution                        PASS
professional/reference Formation                PASS
probe ≠ Candidate                               PASS
simple bounded transformation                   PASS / Skill stays inactive
explicit ideation                               PASS / Skill stays inactive in clean case
BOUND continuation                              PASS
material changed claim                          PASS / Skill re-activates
existing Parent + new professional Child        PASS / Skill re-activates
```

Supported narrow claim:

> **`material-work-entry v0.2` is behaviorally supported as an automatic native Entry/Admission controller on the tested ChatGPT Work surface.**

This does not establish universal reliability across all prompts, accounts, models or future product versions.

## 7. Memory / context implication

One Work ideation run showed both `material-work-entry` and Memory as sources and reused earlier beer-story state. This is consistent with documented ChatGPT Memory/chat-history behavior.

The architectural implication is not to disable Memory by default. Instead preserve the already-established type boundary:

```text
Memory / retrieved prior chat context
= contextual evidence
≠ automatically authoritative Parent/state/decision
```

Whether retrieved memory is sufficiently fresh/complete/authoritative remains claim-relative and must not be silently transferred into controlling state.

## 8. Native runtime candidate after product reconciliation

The simplest currently supported native composition is:

```text
GLOBAL CUSTOM INSTRUCTIONS
→ permanent invariants / authority / state / Human-agency rules

CHAT
→ ordinary conversation, bounded questions, quick direct work

WORK
→ longer/material professional work
→ Personal Skill routing
→ `material-work-entry v0.2`
→ DIRECT or FORMATION

PROJECT
→ persistent initiative/context carrier when continuity earns it
→ can host either Chat or Work using Project context

MEMORY / CHAT HISTORY
→ optional contextual retrieval according to user settings
→ evidence/context, not automatic authority

API TWO-PASS GATEWAY
→ deferred hard-enforcement option if native Work-Skill performance later proves insufficient or surface-independent automation is required
```

Custom GPT is likewise deferred because the Work+Skill path already provides a lower-complexity native Entry mechanism with positive behavioral evidence.

## 9. What no longer needs synthetic validation

Do **not** spend Human time re-testing documented product basics such as:

- whether Chat and Work are both ChatGPT modes and their chats appear together in Recents;
- whether Work inside a Project uses Project context;
- whether Project memory can preserve project chats/files/instructions;
- whether enabled Memory/chat history can provide relevant prior context;
- whether Personal Skills are a Work capability on the supported paid surface.

These are product facts to recover from current authoritative OpenAI documentation and only re-test if a concrete discrepancy/bug is observed.

## 10. What remains legitimately empirical

The remaining validation burden should be limited to system-specific claims that documentation cannot answer:

- whether `material-work-entry v0.2` continues to route correctly on **real** material work;
- whether it misses important re-admissions or overactivates in realistic use;
- whether Memory/Project context causes actual Parent/state/authority drift in representative work;
- whether Human gates are proportionate and AI-resolvable formation/assurance remains AI-owned;
- whether Work→Project transition is useful when persistence actually becomes material;
- whether the resulting work achieves professional intended-use quality.

## 11. Next legitimate frontier

**Native Work-Skill Real-Use Pilot.**

Use an actual new material Work Object rather than another synthetic fixture. Observe the Skill as part of ordinary use, repair only actual failures, and persist evidence at the next material evidence/promotion boundary.

No further Global-CI wording iteration, Custom-GPT build or API validation is required before that pilot.

**Disposition:** CONTINUE — NATIVE WORK-SKILL REAL-USE PILOT.
