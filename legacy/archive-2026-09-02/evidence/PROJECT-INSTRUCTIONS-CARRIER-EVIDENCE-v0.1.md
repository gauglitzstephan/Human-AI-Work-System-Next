# Project Instructions Carrier Evidence v0.1

**Status:** HUMAN-OBSERVED PRODUCT/UI EVIDENCE  
**Date:** 2026-08-20  
**Account/runtime context:** selected ChatGPT Pro account / `System Weiterentwicklung Projekt`  
**Source:** Human directly inspected the Project Instructions UI during Runtime deployment repair.

## Observed carrier fact

The Human reports that the Project Instructions field accepts up to:

```text
8,000 characters
```

This resolves the previously unverified numeric carrier constraint for the selected first Project/account context.

## Candidate fit

Current compiled Project payload:

- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.3.md`

Payload identity:

```text
LF characters:      4,231
CRLF characters:    4,239
SHA-256 UTF-8 LF:   6abeda584e19122aa0620a0009a13c8f62ce8876f33c916f95874a3b3a1422e4
Observed carrier:   8,000 characters
```

Therefore:

```text
Project v0.3 static carrier-size fit = PASS
```

No recompilation is justified merely because additional carrier capacity exists. The current payload already preserves the required canonical semantics and project-local bindings; unused capacity is not a defect.

## Evidence boundary

This establishes only the **observed numeric Project Instructions carrier capacity** for the selected account/Project context and the resulting size-fit claim.

It does **not** establish:

- that Project v0.3 has been saved/installed;
- exact post-save readback identity;
- Project-over-Global behavioral precedence in this concrete run;
- Work/Codex access to repository Method Packs;
- Handoff/Human-Gate enforcement behavior;
- professional or outcome quality.

Those remain installation/preflight/real-use claims.
