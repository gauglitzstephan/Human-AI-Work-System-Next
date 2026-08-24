# ChatGPT-native Episode Runtime Kernel v0.1

**Status:** PROTOTYPE / CANDIDATE — not installed, deployed, promoted, or production-authorized.  
**Runtime mode:** ChatGPT-native; no OpenAI API, Agents SDK, or external orchestration host.  
**Effects:** disabled inside every governed episode.

## Purpose

Realize the existing HAWS runtime contracts across native ChatGPT carriers far enough to test the missing operational loop:

```text
controlling state rebind
→ episode admission
→ bounded Chat/Work/Codex handoff
→ provider return
→ parent rebind
→ claim-bound qualification
→ control return
```

The package does not add a Target-Architecture owner. It compiles the existing canonical semantics into:

- a concise native operating kernel;
- exact Episode, Provider Return, and Qualification packet schemas;
- a deterministic local validator runnable in Work or Codex;
- negative-control fixtures derived from the observed application failure class.

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

