# E2E-04 — Native Subagent Runtime Pilot

**Date:** 2026-08-24  
**Status:** EFFECT-DISABLED BEHAVIORAL EVIDENCE — control path observed; child claim failed/demoted; no Promotion.  
**Parent:** HAWS Operating/Runtime Realization reopen; static architecture closed.  
**Candidate:** `prototype/chatgpt-native-episode-runtime-kernel-v0.1`.  

## 1. Purpose and boundary

Test the missing ChatGPT-native responsibility loop with actual native subagent threads rather than a narrated handoff:

```text
Controller
→ bounded execution subagent
→ typed Provider Return
→ Parent readback/rebind
→ different assurance subagent
→ claim-scoped verdict
→ Control Return
```

Allowed operations were read, analyze, return, qualify, and readback. Application work, persistent target writes, external mutation, submission/release, merge, static-architecture change, Runtime Promotion, and parent-status claims were blocked.

## 2. Controlling state

```text
main / Parent commit        b0c402d296dd368206572e5a839cc236156205d2
Runtime Candidate branch   prototype/chatgpt-native-episode-runtime-kernel-v0.1
Static Architecture        CLOSED
Application production     STOPPED
Effects                    DISABLED
```

## 3. Execution handoff and Return

The controller spawned a real execution subagent in a separate agent thread with:

- exact Parent, commit, gate, and frontier;
- two authorized local contract sources;
- a bounded extraction transformation;
- `READ / ANALYZE / RETURN` only;
- an exact Return shape;
- blocked writes, network/connector calls, application work, parent-status claims, and Promotion.

The provider read only the bound files and returned before further work. It reported:

```text
operations       READ / ANALYZE / RETURN
writes           NONE
external actions NONE
parent status    NONE
Promotion        FALSE
claim            BOUNDED_RETURN_OBLIGATIONS_EXTRACTED
```

## 4. Parent readback and rebind

After Return, the controller reread the actual GitHub relation:

```text
main base         b0c402d296dd368206572e5a839cc236156205d2
Candidate branch  ahead 1 / behind 0
Parent drift      NONE observed
```

No child claim was treated as integrated before this readback.

## 5. Separate assurance

The controller then spawned a different assurance subagent with the rebound Parent version, exact provider claim, Return content, cited source ranges, and a read-only qualification task. The reviewer independently read the sources.

Verdict:

```text
BOUNDED_RETURN_OBLIGATIONS_EXTRACTED  FAIL
CORE_BOUNDED_RETURN_SEQUENCE_PARTIALLY_EXTRACTED  supported narrower claim
```

Material findings included omitted Return obligations for output/state delta, exact child-to-parent contribution, transition/use state and material-effect readback; omitted rejection conditions; incomplete Qualification duties; and an overbroad prohibition on all readiness claims rather than only parent readiness.

The controller did not average the outputs into PASS, did not let the producer repair and self-pass, and did not promote Parent or Runtime state.

## 6. Exact qualification

```text
actual native execution subagent dispatch             PASS
bounded provider context and operations                PASS observed
Provider Return before further work                    PASS observed
post-Return Parent readback/rebind                      PASS observed
different assurance subagent                           PASS observed
reviewer detects omissions and overclaim               PASS observed
failed child claim demoted / no dependent transition   PASS observed
effects / application / Promotion                      NONE

executor substantive child claim                       FAIL / DEMOTED
automatic Skill activation                             UNVERIFIED
repeated runtime reliability                           UNVERIFIED
mechanical per-child tool isolation                    UNVERIFIED
Work-surface cross-context transfer                     UNVERIFIED
domain or application production fitness               NOT ESTABLISHED
```

## 7. Runtime implication

The observed defect was not a missing Target-Architecture owner. The installed Entry Skill and Runtime Candidate required an executable native compilation rule:

```text
selected native provider
→ actual spawn, not handoff prose
→ bounded Return
→ Parent readback/rebind
→ different assurance provider when material
→ FAIL/UNVERIFIED demotes claim and blocks transition
```

This evidence justifies a bounded Candidate repair to `material-work-entry` and the native Episode Runtime Kernel. It does not authorize application production, main merge, Runtime Promotion, or static-architecture change.

## 8. v0.8 repair forward smoke

A second held-out, effect-disabled episode exercised the repaired Skill as an explicit controller-mediated route:

```text
Controller
→ bounded cross-source execution subagent
→ Provider Return: NATIVE_CONTROL_CHAIN_PARTIALLY_COHERENT
→ Parent readback
→ different assurance subagent
→ PASS for the exact partial-coherence claim
→ bounded source repair
→ fresh independent post-repair reviewer
→ PASS at static source-coherence scope
```

The first executor/reviewer pair detected, rather than concealed, remaining Candidate defects: `UNVERIFIED` did not carry an explicit demotion/block consequence in the native runtime reference, and the visible Kernel Return/Qualification summaries omitted material obligations. The controller repaired only those authorized Runtime-Candidate sources. A fresh reviewer then verified these exact properties:

- `FAIL` and `UNVERIFIED` both demote the exact claim and block every dependent transition;
- Provider Return exposes the material Skill/runtime-reference obligations;
- Qualification exposes evidence, findings, checks, failures, verdict, `UNVERIFIED` conditions, supported claim and limits, operations/effects, and no parent-status or Promotion claim;
- a selected `NATIVE_SUBAGENT` route requires an actual child thread and cannot silently downgrade to controller self-execution.

Rebound post-repair source identities were:

```text
Material Work Entry SKILL.md             15a4f79faef52fc57d85984e721ef3d0b052b6028f87a7dbae3ba2358aa05e8c
native-subagent-runtime.yaml             5377dc1380507204a9c478c1412d9f845acac6fcfd84f25e5c6c55a97d201745
Native Episode Kernel Candidate          c0bc8a87809a0c4f8c76d64eb855a8a149a14c140f1f5a7d386fba182c7930a0
```

The exact qualified claim is limited to closure of the identified visible coherence gaps at static source scope. It does not qualify automatic/implicit activation, repeated reliability, mechanical tool isolation, application fitness, installation of the repository Kernel, Runtime Promotion, or production.

## 9. Disposition

```text
NATIVE CONTROL PATH PILOT       COMPLETE
CHILD CLAIM                     FAIL / DEMOTED
V0.8 SOURCE-COHERENCE REPAIR    PASS AT EXACT STATIC SCOPE
SKILL/RUNTIME CANDIDATE REPAIR  AUTHORIZED SEPARATELY
MAIN MERGE / RUNTIME PROMOTION  BLOCKED
APPLICATION PRODUCTION          STOPPED
```
