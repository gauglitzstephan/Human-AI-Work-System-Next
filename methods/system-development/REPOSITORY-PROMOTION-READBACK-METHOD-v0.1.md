# Repository Promotion / Readback Method v0.1

**Status:** CANDIDATE METHOD PACK  
**Use when:** a candidate repository change may alter accepted/controlling program state, runtime guidance, architecture, policy, decision or validation evidence.

## Method objective

Keep technical write capability distinct from legitimate semantic promotion and preserve parent/program continuity.

## Procedure

1. Recover the controlling baseline (`main/CURRENT.md` plus affected authoritative files/domains).
2. Define the exact candidate delta and target semantic/control status.
3. Identify dependencies, reopened claims and downstream implications.
4. Apply the assurance required for the target claim/status.
5. Identify legitimate decision/acceptance/promotion authority and exact authorized write path.
6. Keep branch/file/commit/PR state as Candidate unless explicitly promoted.
7. At Human/authority gate present a mature decision object: baseline, delta, evidence, risks, unresolved items and recommended promotion action.
8. On authorization, execute the exact write/merge only.
9. **READBACK** the resulting authoritative state from the target branch/path.
10. Reconcile the controlling parent state and record any material reopened work.

## Promotion contract

```text
baseline
+ delta
+ target status
+ assurance
+ dependencies
+ authority
+ write path
→ WRITE / MERGE
→ READBACK
→ RECONCILE
```

## Failure modes

- AI-generated branch/commit treated as accepted;
- PR creation treated as merge authorization;
- merge treated as external runtime installation;
- successful write treated as correct semantic status;
- `CURRENT.md` not read back after a material promotion;
- child branch state silently becoming the parent program root.
