# ChatGPT-native Episode Runtime Kernel v0.1

**Status:** PROTOTYPE / CANDIDATE — not installed, deployed, promoted, or production-authorized.  
**Runtime mode:** ChatGPT-native; no OpenAI API, Agents SDK, or external orchestration host.  
**Effects:** disabled inside every governed episode.

## Purpose

Realize the existing HAWS runtime contracts across native ChatGPT carriers far enough to test the missing operational loop:

```text
controlling state rebind
→ episode admission
→ bounded native Chat/Work/Codex/subagent dispatch
→ provider return
→ parent rebind
→ separate claim-bound qualification when material
→ control return
```

The package does not add a Target-Architecture owner. It compiles the existing canonical semantics into:

- a concise native operating kernel;
- exact Episode, Provider Return, and Qualification packet schemas;
- a deterministic local validator runnable in Work or Codex;
- negative-control fixtures derived from the observed application failure class.

The active `material-work-entry` Candidate compiles the native dispatch rule and detailed executor/reviewer packet fields. This repository package remains the development/evidence Candidate; it does not install or promote that Skill.

## Files

```text
NATIVE-EPISODE-KERNEL-CANDIDATE-v0.1.md  native carrier and control rules
episode.schema.json                     admission packet
provider_return.schema.json             bounded provider return
qualification.schema.json               separate qualification packet
validate_packets.py                     deterministic fail-closed validator
runtime_cases.json                      negative-control fixtures
run_evals.py                            offline regression harness
```

## Offline validation

Requires Python 3.10+ and no external packages or credentials.

```bash
python prototypes/native-episode-runtime-kernel/run_evals.py
```

Validate individual packets:

```bash
python prototypes/native-episode-runtime-kernel/validate_packets.py episode episode.json
python prototypes/native-episode-runtime-kernel/validate_packets.py return episode.json provider_return.json
python prototypes/native-episode-runtime-kernel/validate_packets.py qualification episode.json provider_return.json qualification.json
```

## Claim boundary

A validator `PASS` establishes only that the supplied packet satisfies the encoded structural and cross-field invariants. It does not establish:

- that ChatGPT invoked this kernel in a real episode;
- that a provider followed the packet;
- that native tools were mechanically withheld;
- professional domain quality;
- parent completion, acceptance, promotion, deployment, use, or outcome.

Until native behavioral validation succeeds, tool isolation and automatic activation remain **UNVERIFIED**. Real effectful work remains blocked.

## Native pilot evidence

The 2026-08-24 effect-disabled pilot used two real native subagent threads sequentially:

```text
controller admission
→ execution subagent Return
→ GitHub Parent readback/rebind
→ different review subagent
→ reviewer FAIL and child-claim demotion
```

This establishes one observed control trace. It does not establish repeated implicit activation, universal surface availability, mechanical per-child tool isolation, domain fitness, or production readiness. See `evaluation/e2e-real-use/E2E-04-2026-08-24-NATIVE-SUBAGENT-RUNTIME-PILOT.md`.
