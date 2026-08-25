# Repository Promotion / Readback Method v0.1

**Status:** CANDIDATE METHOD PACK  
**Use when:** a candidate repository change may alter accepted/controlling program state, runtime guidance, architecture, policy, decision or validation evidence.

## Method objective

Keep technical write capability distinct from legitimate semantic promotion and preserve parent/program continuity across all material repository entry points.

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
11. **ENTRY-POINT HYGIENE SCAN:** when Promotion changes current program state, Runtime guidance, installable configuration or next-work authority, verify that all material action-bearing entry points agree with the promoted state. At minimum inspect where applicable:
    - root `CURRENT.md`;
    - root `README.md` / navigation;
    - current installation/deployment bundles or manifests;
    - registries/indexes that select active methods/configuration;
    - superseded executable-looking artifacts where a stale instruction could cause a wrong action.
12. For superseded action-bearing artifacts, ensure the current file is either unambiguously historical or carries an explicit **SUPERSEDED / DO NOT INSTALL / DO NOT EXECUTE** status. Preserve original provenance through repository history rather than leaving stale executable guidance active merely for lineage.
13. Re-read the repaired entry points after any hygiene write and confirm that one unambiguous current package/gate can be derived without chat history.

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
→ READBACK authoritative target
→ RECONCILE parent state
→ SCAN action-bearing entry points / supersession
→ REPAIR stale navigation or executable guidance if in authorized scope
→ READBACK / RECONCILE again
```

The hygiene scan is assurance for the promoted claim. It does **not** authorize unrelated cleanup, branch deletion, architecture change or new Runtime semantics.

## Minimum post-promotion claim

A successful repository Promotion may claim only what the readback supports. Where current-state guidance is distributed across multiple entry points, Promotion is not fully reconciled until controlling state, root navigation, current action-bearing package pointers and supersession safety are mutually coherent for the promoted scope.

## Failure modes

- AI-generated branch/commit treated as accepted;
- PR creation treated as merge authorization;
- merge treated as external runtime installation;
- successful write treated as correct semantic status;
- `CURRENT.md` not read back after a material promotion;
- `CURRENT.md` correct while root README/navigation still points to an older gate;
- superseded installation/deployment artifact still contains apparently executable instructions after its promotion precondition has become true;
- newest-looking version selected without controlling pointer;
- migration/history document silently overriding current state;
- child branch state silently becoming the parent program root;
- broad cleanup performed under the pretext of post-promotion hygiene.