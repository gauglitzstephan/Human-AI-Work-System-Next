# System Failure Localization Method v0.4

**Status:** scoped internal diagnostic method.  
**Use when:** observed behavior, artifact quality, runtime control, state continuity or outcome evidence in this system contradicts the expected claim.

This is not a universal causal root-cause-analysis methodology. Use an appropriate external/domain RCA method when the claim requires broader causal diagnosis.

## Objective

Localize supported causal contributions and choose the smallest sufficiently effective intervention. The first observed divergence, its causes and the best intervention location can differ.

## Method

1. **State the failed claim and observed counterevidence.** Keep object/version/environment explicit.
2. **Recover the actual runtime/state involved.** Inspect effective instructions, provider/surface, authoritative state, method/tool used and relevant authority boundary rather than reconstructing from memory.
3. **Find the first material divergence.** Identify where justified expected state/behavior first differs from observed state/behavior. For version claims, bind repository candidate, approved operating target, actual installed and loaded identities separately. A newer repository version alone does not establish a deployment obligation. An unknown approved target leaves that obligation unresolved; a false claim about the version used can still be corrected.
4. **Classify causal contributions provisionally; several can coexist:**
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
   - architecture when a material performance, coordination or structural gap remains; existing ownership or representability does not rule it out.
5. **Test plausible competing causes** when they would change the repair. For each live rival, name the observation expected if it were true and a check capable of discriminating it. Obtain accessible evidence and update the localization; do not stop at a coherent story or a list of untested causes. Distinguish a missing source operation, a different installed/loaded version, failed selection, and non-application of an available operation. These require different repairs. If internal causality is not observable, report the first supported divergence and retain the unresolved causal claim.
6. **Select an adequate intervention and preserve unaffected qualified state.** Compare only materially plausible routes: local correction, provider/method or execution-mechanism change, narrower use/claim, or architecture change. Judge required performance, recurrence, consequences, uncertainty, feasibility and total cost including Human correction. A detection measure must also lead to timely correction or containment. A local fix can be enough for a one-off omission; repeated failure under accessible valid instructions is evidence against merely repeating them. Combine repairs when independent or interacting contributions require it.
7. **Recheck the affected claim and material regressions.** Do not launch a new system redesign by default.
8. **Reopen only affected dependencies on evidence.** Architecture change requires a material unresolved need and a justified realization route; neither exhaust a fixed ladder of smaller changes nor assume a new controller is the answer. If adequacy remains uncertain, choose a discriminating check or bound use until the relevant claim is supported.

## Output

- failed claim + evidence;
- first divergence point;
- supported causal contributions, separated from the first observed divergence;
- material competing causes still open or ruled out;
- bounded intervention and why it is sufficient, including combined contributions when needed;
- exact claim to recheck;
- broader reopen implication only if genuinely established.

## Failure modes

- symptom relabeled as root cause;
- Global/Project instructions changed for a domain-method or craft defect;
- process/agents added without evidence of adequate effect or comparison with credible provider/tool remedies;
- Human blamed for detecting an AI-resolvable defect;
- architecture reopened before runtime/method/state recovery;
- internal layer taxonomy mistaken for a general causal RCA method.

## Discriminating example

A response omitted a required comparison. One hypothesis is that the source lacks it; another is that the active source differed; another is non-application. Read the expected source, recover the available installed/loaded identity and inspect the episode's actual comparison. If v2 is only a repository candidate and v1 remains approved, loading v1 is not an installation defect. If the approved target is unknown, keep that issue unresolved. If v2 is the approved operating target and actual v1 is loaded, a deployment divergence is supported; update only within the authorized path and read back the result. In all three cases correct a false claim that v2 was used. An exact v2 read plus an omitted required comparison supports non-application, without proving why the model omitted it or making reinstallation an adequate repair. A source file's existence alone distinguishes neither case. Recheck the affected claim and material regressions on the chosen intervention, without adding a global rule to cover every rival.
