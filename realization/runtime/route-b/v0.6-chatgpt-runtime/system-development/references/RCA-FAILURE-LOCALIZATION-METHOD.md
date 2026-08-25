# System Failure Localization Method v0.2

**Status:** scoped internal diagnostic method.  
**Use when:** observed behavior, artifact quality, runtime control, state continuity or outcome evidence in this system contradicts the expected claim.

This is not a universal causal root-cause-analysis methodology. Use an appropriate external/domain RCA method when the claim requires broader causal diagnosis.

## Objective

Locate the lowest responsible failure mechanism before changing broader architecture, policy or controls.

## Method

1. **State the failed claim and observed counterevidence.** Keep object/version/environment explicit.
2. **Recover the actual runtime/state involved.** Inspect effective instructions, provider/surface, authoritative state, method/tool used and relevant authority boundary rather than reconstructing from memory.
3. **Find the first material divergence.** Identify where expected state/behavior first differs from observed state/behavior.
4. **Classify the responsible layer provisionally:**
   - frame/requirement;
   - authoritative-state recovery;
   - formation/sufficiency;
   - professional method/source/application;
   - provider/tool/capability;
   - surface/environment;
   - handoff/context/return integration;
   - authority/commitment/promotion control;
   - execution/integration;
   - artifact/craft/refinement;
   - assurance;
   - transition/use/outcome;
   - architecture only if lower layers cannot represent or own the failure.
5. **Test plausible competing causes** when they would change the repair. Do not stop at the first coherent story.
6. **Preserve unaffected qualified state.** Define the smallest repair capable of fixing or detecting the responsible mechanism.
7. **Recheck the affected claim and material regressions.** Do not launch a new system redesign by default.
8. **Escalate only on evidence.** Architecture reopen requires a named failure that cannot be represented or repaired cleanly at lower layers.

## Output

- failed claim + evidence;
- first divergence point;
- most supported responsible mechanism/layer;
- material competing causes still open or ruled out;
- bounded repair;
- exact claim to recheck;
- broader reopen implication only if genuinely established.

## Failure modes

- symptom relabeled as root cause;
- Global/Project instructions changed for a domain-method or craft defect;
- process/agents added to compensate for a provider/tool problem;
- Human blamed for detecting an AI-resolvable defect;
- architecture reopened before runtime/method/state recovery;
- internal layer taxonomy mistaken for a general causal RCA method.