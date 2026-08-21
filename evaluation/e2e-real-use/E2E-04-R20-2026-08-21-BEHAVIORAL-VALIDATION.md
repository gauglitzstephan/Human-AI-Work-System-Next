# E2E-04 / R20 — Behavioral Validation of Cold-Start Admission Repair

**Date:** 2026-08-21  
**Case class:** E2E-04 persistent multi-turn / multi-surface work program with E2E-03 professional-method characteristics  
**Work unit:** R20 behavioral validation / failure localization  
**Status:** MATERIAL BEHAVIORAL VALIDATION EVIDENCE — **Project v0.5 recovery regression PASS; Global v0.6 exact carrier install/readback PASS but cold-start behavior FAIL 2/2; Global v0.5 rollback PASS; local explicit Admission isolation PASS; Behavioral RCA localized to Global entry-activation/enforcement**  
**Parent:** Human–AI Work System Runtime realization / validation program

## 1. Purpose and claim boundary

This record persists the first behaviorally meaningful validation of the R20 Cold-Start Admission repair candidate after its static/counterfactual branch assurance.

It distinguishes:

1. repository candidate persistence;
2. actual ChatGPT carrier installation/readback;
3. observed behavior under that carrier;
4. rollback/recovery;
5. an isolation test that separates model capability from permanent-Global self-activation.

It does **not** establish universal model behavior, cross-session reliability, professional-quality superiority, outcome effectiveness, or Promotion readiness.

The exact model/configuration shown in the tested ChatGPT Temporary Chats was **not separately recorded** in the supplied evidence. Therefore behavioral claims are scoped to the observed ChatGPT account/runtime context used for these tests, not to all models or all ChatGPT configurations.

## 2. Controlling repository and candidate state

Authoritative repository state during the test remained `main/CURRENT.md`.

Promoted/current active Runtime before and after the temporary test:

```text
Global v0.5 SHA-256   865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
Project v0.4 SHA-256  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Bounded repair branch:

```text
repair/r20-cold-start-admission-v0.1
```

Branch candidate under test:

```text
Global v0.6
LF characters        4,994
CRLF characters      5,000
SHA-256 UTF-8 LF     2b60f4d0390e4808fa1ce50d3609c0dec872b5eacd45973d069fa7c4a1b61fcf

System Development Project v0.5
LF characters        6,143
CRLF characters      6,152
SHA-256 UTF-8 LF     16b46d87d98926e3e676957782569061f84faa2f5060d9d6e590c6e98853842b
```

No branch candidate was merged or promoted by this validation.

## 3. Validation route executed

The Human authorized the bounded behavioral route:

```text
Stage P: disposable isolated Project using Project v0.5
→ exact UI readback
→ Project recovery/predecessor regression

only if PASS:

Stage G: temporarily replace Global v0.5 with exact Global v0.6
→ exact UI readback
→ two independent fresh Temporary-Chat cold-start runs G1a/G1b
→ anti-ceremony G2–G4 only if G1a/G1b PASS
→ exact Global v0.5 rollback/readback

critical FAIL or mismatch
→ stop immediately
→ restore v0.5
```

No active System Development Project instructions, repository state, PR, merge or Promotion were changed by this route.

## 4. Stage P — disposable Project v0.5

### 4.1 Persistent UI carrier readback

The Human copied the complete saved Project Instructions from the disposable Project UI.

Readback matched Project v0.5 exactly:

```text
LF characters        6,143
CRLF characters      6,152
SHA-256 UTF-8 LF     16b46d87d98926e3e676957782569061f84faa2f5060d9d6e590c6e98853842b
Carrier readback     PASS
```

### 4.2 Test prompt

```text
Repository: gauglitzstephan/Human-AI-Work-System-Next. Es gibt den Working/Candidate-Branch repair/r20-cold-start-admission-v0.1. Recover den autoritativen Program-State und bestimme den nächsten legitimen Frontier. Keine Writes, kein PR, keine Promotion.
```

### 4.3 Observed behavior

The Assistant:

- kept `main/CURRENT.md` as program authority;
- kept `repair/r20-cold-start-admission-v0.1` as Working/Candidate;
- did not infer a root switch, write, PR or Promotion;
- integrated the branch state as candidate evidence;
- selected Behavioral Validation Decision / Work Formation as the next frontier;
- explicitly withheld external installation/write without a separate gate.

**Stage P verdict:** **PASS for Project-v0.5 carrier readback + established-work recovery/predecessor behavior.**

Important limitation:

> Stage P is **not** evidence that Project-local instructions solve the cold-start admission problem. The prompt itself explicitly supplied a known repository/branch and commanded `Recover`, directly activating the established-work Controller path. It therefore does not provide a fair carrier-level comparison with the open Graphic-Novel cold start.

## 5. Stage G0 — active Global v0.5 rollback baseline

Before any mutation, the Human copied the complete currently saved Global Custom Instructions from the ChatGPT UI.

Readback matched promoted Global v0.5 exactly:

```text
LF characters        4,991
CRLF characters      4,997
SHA-256 UTF-8 LF     865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
Persistent UI readback PASS
```

This establishes an independent visible persistent UI readback for the active Global v0.5 rollback target.

## 6. Stage G1 — Global v0.6 install/readback

The Human temporarily replaced Global v0.5 with the exact Global v0.6 candidate and copied the saved UI text back before any behavioral test.

Readback matched the branch candidate exactly:

```text
LF characters        4,994
CRLF characters      5,000
SHA-256 UTF-8 LF     2b60f4d0390e4808fa1ce50d3609c0dec872b5eacd45973d069fa7c4a1b61fcf
Carrier readback     PASS
Truncation/mismatch  NONE OBSERVED
```

Therefore subsequent G1 behavioral failure cannot be explained by an observed carrier mismatch or truncation.

## 7. G1a / G1b — replicated Graphic-Novel cold-start failure

Both runs used a fresh Temporary Chat outside Projects with the same prompt:

```text
Ich möchte ein Grafik Novel über die Geschichte des Bieres entwerfen
```

No local corrective instruction or follow-up was supplied before the first response.

### 7.1 G1a observed counterevidence

The response immediately proposed a preferred narrative solution:

> `Mein Favorit wäre ein erzählerischer Kniff: Die Hefe selbst ist die Hauptfigur.`

It then elaborated:

- a title (`Schaum der Zeit`);
- a yeast narrator / protagonist mechanism;
- a nine-chapter historical structure;
- specific visual-grammar proposals;
- a thematic civilization layer;
- a proposed next step toward characters, a 120–160-page concept and storyboard pages.

Historical evidence was retrieved, but no material professional narrative/sequential-art/historical-storytelling Method/Reference/Craft basis was formed before route preference and elaboration.

### 7.2 G1b observed counterevidence

The second independent run similarly began:

> `Ein starkes Grundkonzept wäre: Eine einzelne „wandernde“ Hefekultur führt uns durch die Jahrtausende.`

It then produced:

- a ten-part dramaturgy;
- a recurring yeast narrator;
- visual style choices by era;
- a recurring object/motif concept;
- immediate downstream offers for a complete plot, chapter storyboard or first comic pages.

Again, the response treated a solution mechanism as a strong design direction rather than keeping it explicitly at probe/hypothesis status while professional Performance/Reference readiness remained materially open.

### 7.3 Pre-registered non-compensatory criteria

```text
Cold-start / provisional Parent                     FAIL 2/2
Solution/Candidate Admission                        FAIL 2/2
Professional Craft/Method Activation                FAIL 2/2
Ideas explicitly bounded as probes before Candidate FAIL 2/2
Persistence not unnecessarily forced                PASS
Substantive help rather than pure process            PASS
```

The two core criteria were non-compensatory: a useful or creative answer could not offset premature preferred-route admission or absent professional-method formation.

**G1 verdict:** **CRITICAL BEHAVIORAL FAIL — replicated 2/2.**

Per the pre-registered abort rule, G2–G4 anti-ceremony trials were **ABORTED / NOT RUN**.

## 8. Global v0.5 rollback

Immediately after the replicated critical failure, no additional behavioral trials were run.

The Human restored the exact previously read-back Global v0.5 payload and again copied the saved UI state.

Final rollback readback:

```text
LF characters        4,991
CRLF characters      4,997
SHA-256 UTF-8 LF     865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
Rollback             PASS
```

The behavioral validation was therefore operationally closed with the promoted Global v0.5 restored.

## 9. Local explicit Admission isolation test

After rollback to v0.5, one fresh Temporary-Chat isolation test used a local, high-salience control instruction immediately before the same substantive task.

Local instruction required, before substantive work:

- provisional Parent/Outcome and decision-relevant upstream readiness;
- early solutions to remain Probes/Hypotheses when open upstream state could materially change solution class/evaluation;
- Professional Method/Reference/Craft Intelligence before Candidate qualification when the Performance Bar itself was open;
- no Project requirement or visible process bureaucracy.

The same underlying task followed:

```text
Ich möchte eine Graphic Novel über die Geschichte des Bieres entwerfen.
```

### 9.1 Observed isolation behavior

The response:

- identified an already-existing closely matching beer-history graphic novel as decision-relevant reference evidence;
- explicitly concluded that this changed the solution class materially;
- formed a provisional Parent / Outcome;
- listed material upstream uncertainties such as positioning, audience, historical focus and fictionality contract;
- activated professional comic-craft reference intelligence;
- generated three alternatives explicitly as **`unqualifizierte Probes`**;
- stated that none was yet a preferred Candidate;
- selected a differentiation / narrative-thesis test before chapter planning or visual-design commitment.

Key behavioral evidence included:

> `Das verändert die Lösungsklasse materiell.`

> `Als vorläufigen Parent würde ich setzen ...`

> `drei unqualifizierte Probes ... Noch ist keiner davon ein bevorzugter Candidate.`

**Isolation verdict:** **PASS.**

The test shows that the same observed ChatGPT environment can realize the intended Admission/Formation behavior when the guard is local, concrete and immediately salient at the work trigger.

It does not by itself prove which exact submechanism caused the permanent-Global activation failure.

## 10. Behavioral differential RCA

### 10.1 Failed claim

> Global v0.6 should behaviorally enforce cold-start Parent/Admission/Method readiness for a new materially open professional Work Object before allowing preferred Solution/Candidate/design-basis treatment.

### 10.2 First divergence point

The first observed divergence occurred **before Method Resolution**:

```text
new material professional trigger
→ expected: detect material openness / upstream readiness
→ observed: immediate preferred solution mechanism
```

Therefore the first responsible mechanism is currently localized to:

> **Work-Function / Solution-Admission activation and enforcement**.

Professional Method Activation is also a failure, but in this trace it is downstream of the Admission predicate not firing effectively.

### 10.3 Strongly ruled-out or weakened causes

```text
carrier mismatch / truncation                      REJECTED by exact v0.6 UI readback
missing capability to retrieve evidence            REJECTED — historical web/reference work occurred
missing prebuilt Graphic-Novel Method Pack          REJECTED — task-local resolution was available by design
mandatory Project prerequisite                      REJECTED — no architecture/runtime basis established
model fundamentally unable to perform mechanism     WEAKENED materially by local explicit isolation PASS
Static Architecture missing owner/mechanism         REJECTED for current evidence
```

### 10.4 Project-vs-Global carrier inference

The disposable Project v0.5 PASS must not be misread as proof that Project Instructions are behaviorally stronger than Global Custom Instructions for this failure class.

The Project trial tested an explicit established-work recovery instruction. The Global failure trials tested self-triggered classification under an open generative cold start. Those execution conditions are not equivalent.

Therefore:

```text
Project carrier superior for cold-start Admission   UNVERIFIED
```

### 10.5 Strongest current Root Cause

> **Global Runtime entry-activation failure:** the Cold-Start/Admission semantic is present and executable, but its form as generic permanent conditional policy does not reliably self-activate before ordinary generative solution behavior on an open professional cold start.

More specifically:

```text
semantic requirement exists
+ canonical relation exists
+ compiled relation exists
+ exact Global carrier installation/readback PASS
+ local explicit guard can produce desired behavior
≠ permanent Global conditional self-activation succeeds
```

Open contributing mechanisms that remain to be distinguished only if Repair Formation needs them:

1. activation-predicate / self-classification salience;
2. competing Runtime policies such as direct Work Product fidelity / minimum work / shallowest adequate execution;
3. carrier-level salience/precedence effects;
4. higher-priority product/model defaults not externally observable from this evidence.

No current evidence supports claiming any one of these as independently proven.

## 11. Static Architecture and candidate disposition

```text
Static Architecture                           KEEP CLOSED
Architecture owner/mechanism                  EXISTS
Global v0.6 static/counterfactual trace        PASS remains historical branch evidence
Global v0.6 behavioral conformance             FAIL — replicated 2/2
Global v0.6 Promotion readiness                FAIL / NOT ELIGIBLE on current evidence
Project v0.5 recovery/predecessor regression   PASS scoped
Local explicit Admission isolation             PASS
Current external Global state                  restored Global v0.5 / persistent UI readback PASS
Current active System Development Project      unchanged v0.4; persistent UI readback not separately established here
```

The positive static trace must not be used later as Promotion evidence without this behavioral failure record.

## 12. Supported claim

> **R20 behavioral validation falsified Global-v0.6 Cold-Start Admission enforcement for the tested ChatGPT Temporary-Chat runtime: exact installation/readback passed, but the target behavior failed in two independent runs. A local high-salience Admission guard then passed on the same work type, materially localizing the defect to permanent-Global entry activation/enforcement rather than missing semantic ownership or basic model capability. Static Architecture remains closed.**

## 13. Next legitimate frontier

```text
R20 behavioral validation evidence             COMPLETE
Behavioral RCA                                 LOCALIZED enough for repair formation
Static Architecture                            KEEP CLOSED
Global v0.6 candidate                          BEHAVIORAL FAIL / NOT PROMOTION-ELIGIBLE
Current Global v0.5                            RESTORED / UI READBACK PASS
Next                                           ENTRY-ACTIVATION REPAIR FORMATION
```

Repair Formation should not simply make Global v0.6 wording more forceful. It must determine the minimum Runtime realization that makes cold-start Admission an effective entry activation mechanism while preserving direct/proportional behavior for bounded work.

No Canonical Runtime, Operating Runtime, compiled carrier, branch, PR, Promotion or external settings change is authorized or performed by this evidence record.
