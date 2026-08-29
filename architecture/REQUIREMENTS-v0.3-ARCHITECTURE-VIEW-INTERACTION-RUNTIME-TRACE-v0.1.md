# Requirements v0.3 — Architecture / View / Interaction / Runtime Trace v0.1

**Status:** CURRENT NON-NORMATIVE COMPANION on authoritative `main`; CANDIDATE on any branch or PR until separately authorized merge and authoritative `main` readback  
**Date:** 2026-08-29  
**Recovered analysis basis:** authoritative `main` at `2693ac4427cf5f4406ca1e42212a6530a1028a90`  
**Controlling Requirements:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md`, blob `70f76ca5d3a7f5f562924e00894cc81e75c77c3c`  
**Historical Requirements lineage:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md`, blob `fc9cafa9d88a0180a3ba280e1e8ea6d2f6bb2f63`  
**Controlling architecture at recovery:** `architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md`, blob `75d2669a3bf2d55258ad4f6e171ae55139e1d2c8`; this package changes status/navigation metadata only, not the conceptual body  
**View basis:** `architecture/LAYER-VIEW-WORKCONTROL-RUNTIME-CORRESPONDENCE-v0.1.md`, blob `c046d9eb5f92d6c4bed391ef5a44df8271d8ddb9`  
**Claim boundary:** semantic lineage, responsibility ownership, architecture-description View coverage, conceptual mechanism, repository-source Runtime realization, bounded evidence status and repair disposition. This Candidate does not change Requirements semantics or conceptual Target-Architecture commitments/body and does not reopen Target Architecture; it changes only the companion trace and status/navigation metadata. It does not establish installed identity, behavioral conformance, professional outcome or value.

## 1. Purpose and use

This trace answers, for every controlling Requirements v0.3 semantic unit:

```text
v0.3 semantic
→ v0.2 lineage
→ owning Responsibility
→ relevant Architecture View(s)
→ accepted architecture invariant/mechanism
→ current Runtime source realization
→ evidence/status
→ lowest justified repair disposition
```

It additionally retains separate activation or salience rows for:

- the three v0.2 Conditional Requirements absorbed into v0.3 Core Requirements;
- the relational semantics of v0.2 IR-05;
- Comparative Human Value and the anti-max-autonomy middle position from v0.2 CR-07;
- the possible additional-gate reading of CR-15's phrase `admitted work`;
- all controlling v0.3 Central non-equivalences; and
- the one v0.2 Central non-equivalence without an explicit v0.3 successor.

This document is a navigation and conformance companion. It is not:

- a new Requirements source;
- an architecture baseline or amendment;
- a ninth View;
- a new interaction component, state object or controller;
- a mandatory runtime checklist or visible lifecycle; or
- evidence that every Requirement must become explicit on every episode.

A row activates operationally only when its semantic can materially change the current work or claim.

## 2. Codes

### Responsibilities

| Code | Responsibility |
|---|---|
| `S` | Strategic |
| `O` | Operating |
| `W` | Work |
| `E` | Execution |
| `L` | Learning / Change |

An entry such as `W + affected owner` means that Work Responsibility integrates the episode while legitimate wider ownership remains with the relevant `S`, `O`, `E` or `L` owner.

### Views

| Code | View |
|---|---|
| `V1` | Mission & Outcome |
| `V2` | Work Process |
| `V3` | Information & State |
| `V4` | Capability & Resource |
| `V5` | Interaction & Authority |
| `V6` | Quality & Assurance |
| `V7` | Governance & Learning |
| `V8` | Execution Context & Integration |

Views are architecture-description lenses, not system components or mandatory runtime activations.

### Architecture mechanisms and invariants

| Code | Accepted mechanism/invariant |
|---|---|
| `RESP` | distinct Strategic / Operating / Work / Execution / Learning responsibilities |
| `DTS` | Distributed Typed State |
| `AWS` | Adaptive Work-Selection Contract |
| `WRK` | Work Responsibility's intended-use transformation |
| `EXE` | Execution Responsibility's concrete execution/read/write/recovery role |
| `RSI` | Reality & State Integrity |
| `CAAI` | Capability, Authority & Agency Integrity |
| `PQCI` | Professional Quality & Claim Integrity |
| `VRCI` | Value, Realization & Change Integrity |
| `COND` | conditional mechanism activated by a material trigger |
| `RB` | Runtime / implementation boundary and semantic-preservation rule |

### Runtime references

- `B§n` — `PROFESSIONAL-WORK-BASELINE.md`, section `n`
- `T§n` — `RUNTIME-TOPOLOGY.md`, section `n`
- `G/P` — current Global and System-Development Project instruction carriers
- `AE` — bounded `adaptive-exploration` Skill
- `DA` — bounded `decision-analysis` Skill

Exact current repository-source blobs:

| Runtime source | Blob |
|---|---|
| Professional Work Baseline | `e25f22f77b9665b4dca2531ea8d03b3cd53cbb7f` |
| Runtime Topology | `f1f104d032e297483ef1c0cfa0d9ea089a01076b` |
| Global Custom Instructions | `8fc25d99f3ffa66abe917e4a256a4701c929cffa` |
| System-Development Project Instructions | `e8ddb7b4db27804667500beb41b206c5a5adfeff` |

### Evidence/status

| Code | Meaning |
|---|---|
| `A` | architecture owner/mechanism and View representation established |
| `E` | semantic is embedded in the exact current repository source |
| `D` | semantic is delegated and bound at repository-source level |
| `BP` | bounded behavior evidence exists on a predecessor or PR37 installed identity |
| `U` | exact-current installation, behavior, generalized use or outcome remains unverified |

`A/E` is not behavioral proof. All rows inherit `U` for exact-current installed behavior and generalized outcome unless explicitly narrowed.

Current behavioral evidence is bounded:

- 25 cases passed on the immediately preceding installed Runtime;
- F12, F17, F20, RC06 and RC08 passed 5/5 on the PR37 installed carrier identity;
- the exact current PR38 Global and Project source blobs have no installed-content readback or exact behavioral run;
- no fresh exact-current 30/30 or generalized cross-domain conformance is claimed.

## 3. Interpretation Rules trace

| ID | v0.3 semantic unit | v0.2 lineage | Owner | Views | Architecture mechanism | Runtime realization | Evidence/status | Repair disposition |
|---|---|---|---|---|---|---|---|---|
| IR-01 | Semantically rich; operationally explicit only when material | IR-01 preserved | `S/O/W/E/L`, activation selected by `W` | V2, V5, V6, V8 | AWS; latent complexity | B§3, B§7; T§2, T§10; G/P | A/E; RC09 predecessor PASS; exact-current U | `KEEP`; retain as trace and anti-bloat regression unit |
| IR-02 | Materiality and sufficiency are relative to the next legitimate frontier | merge of v0.2 IR-02 + IR-03 | `W + affected owner` | V1, V2, V3, V5, V6 | AWS + DTS + PQCI | B§3–4, B§6–7; T§2, T§4, T§10; G/P | A/E; exact-current U | `KEEP` |
| IR-03 | Professional/reality/authority/continuity/assurance floors precede economy | v0.2 IR-04 preserved/renumbered | `W + affected owner` | V3, V4, V5, V6, V8 | AWS + RSI + CAAI + PQCI | B§4, B§7, B§11; T§2, T§10–11; G/P | A/E; exact-current U | `KEEP`; include explicitly in regression manifest |

## 4. Core Requirements trace

| ID | v0.3 semantic unit | v0.2 lineage | Owner | Views | Architecture mechanism | Runtime realization | Evidence/status | Repair disposition |
|---|---|---|---|---|---|---|---|---|
| CR-01 | Outcome/need before proposed means | CR-01 preserved | S + W | V1, V2 | RESP + AWS | B§3; T§2; G/P | A/E; U | `KEEP` |
| CR-02 | Claim-relative scope and local-contribution integrity | CR-02 strengthened with part of IR-05 | W + affected wider owner | V1, V3, V5, V6 | RESP + DTS + CAAI + PQCI | B§3, B§11; T§2, T§7, T§10; G/P | A/E; U | `TRACE` IR-05 separately; targeted relational wording/salience check |
| CR-03 | Reality and epistemic integrity | CR-03 preserved | W + E | V3, V6, V8 | DTS + RSI + PQCI | B§6; T§3, T§7, T§11; G/P | A/E; U | `KEEP` |
| CR-04 | Recover actual state before consequential change | CR-04 preserved | W + E + affected owner | V2, V3, V6, V8 | AWS + DTS + RSI | B§3, B§6; T§2–4; G/P | A/E; U | `KEEP` |
| CR-05 | Intended-use professional sufficiency, qualified reuse, recipient transformation and material usability/accessibility | CR-05 strengthened; absorbs v0.2 CCR-04; later interaction repair | W | V1, V2, V4, V5, V6 | WRK + PQCI + VRCI | B§4–5, B§9, B§11, B§13; T§6, T§11; G/P | A/E; RC01 predecessor PASS; exact-current U | `TRACE` absorbed trigger separately; targeted genuine-use usability/recipient test |
| CR-06 | Comparative Human/AI/tool/process composition | CR-06 preserved | W + O/E where persistent or executed | V2, V4, V5, V6, V8 | RESP + AWS + CAAI + VRCI | B§2, B§7–8, B§12; T§5, T§8; G/P | A/E; F12 targeted Project PASS; under-composition/global behavior U | `SALIENCE TEST`; retain historical “fewer Agents” guard |
| CR-07 | Human agency, attention, capability, reliance calibration and legitimate contribution | CR-07 strengthened; absorbs v0.2 CCR-07; later interaction repair | W; S/O/L where horizon or authority requires | V1, V4, V5, V6, V7 | CAAI + VRCI | B§8–9; T§6, T§11; G/P | A/E; RC02–03 predecessor PASS; exact-current U | `TRACE` absorbed capability trigger and Comparative Human Value guard; test reliance calibration |
| CR-08 | Capability/status/Authority and transition-type integrity | CR-08 strengthened with part of IR-05 | W/E + legitimate affected owner | V3, V5, V6, V7, V8 | DTS + CAAI + RB | B§3, B§9–11; T§6–7, T§10–11; G/P | A/E; U | `TRACE` IR-05 separately; wording check only if behavior exposes loss |
| CR-09 | State/knowledge/continuity integrity, including divergence handling | CR-09 strengthened; absorbs v0.2 CCR-02 | O/W/E/L according to state type | V3, V5, V7, V8 | DTS + RSI + VRCI | B§3, B§6, B§10; T§3, T§6–7, T§9–10; G/P | A/E; cross-surface predecessor evidence only; exact-current U | `TRACE` absorbed trigger; targeted divergence/recovery test |
| CR-10 | Minimum sufficient work, Whole-System Economics and legitimate closure | CR-10 strengthened with closure | W; S/O when strategic resources are material | V1, V2, V4, V6 | AWS + PQCI + VRCI | B§7; T§2, T§10; G/P | A/E; RC09 predecessor PASS; U | `KEEP` |
| CR-11 | Claim-matched professional assurance | CR-11 preserved | W + E | V3, V5, V6, V8 | PQCI + RB | B§5, B§11; T§11; G/P | A/E; exact-current U | `METHOD REPAIR`: regression manifest must cover IRs, non-equivalences and protected lineage, not only CR/CCR |
| CR-12 | Work Product → transition/use/outcome/value integrity | CR-12 preserved | W + O/L where use/outcome persists | V1, V2, V3, V6, V7 | RESP + DTS + VRCI | B§13; T§10–11; G/P | A/E; exact-current U | `KEEP`; causal-claim salience remains claim-specific |
| CR-13 | Actual Runtime/provider/implementation fidelity | CR-13 preserved | E + O | V3, V4, V5, V6, V8 | EXE + DTS + RB + PQCI | B§6, B§11; T§3, T§5, T§7, T§11; Project carrier | A/E; exact current UI carrier identity U | `READBACK`: verify exact installed identity before conformance reliance |
| CR-14 | Evidence-bound learning/change plus feedback/adaptation control | CR-14 preserved and interaction-strengthened | L + legitimate affected owner | V3, V5, V6, V7, V8 | RESP + DTS + VRCI | B§10 + Learning Rule; T§6–7, T§11; G/P | A/E; RC06 targeted PASS on PR37 installed carrier; exact-current U | `KEEP`; rerun only if current carriers are deployed/relied upon |
| CR-15 | Execute the actual transformation and finish the required Work Product | new in v0.3 | W + E | V2, V6, V8 | WRK + EXE + AWS + PQCI | B§5, B§11, B§13; T§10; G/P | A/E; exact-current U | `KEEP`; retain separate `admitted work` gate-ambiguity guard |

## 5. Conditional Requirements trace

| ID | v0.3 semantic unit | v0.2 lineage | Owner | Views | Architecture mechanism | Runtime realization | Evidence/status | Repair disposition |
|---|---|---|---|---|---|---|---|---|
| CCR-01 | Open framing/exploration integrity | v0.2 CCR-01 preserved | W + S where strategic framing is material | V1, V2, V3, V6 | COND + AWS + WRK | B§3–4, B§12; T§8; AE | A/D; generalized activation/fitness U | `KEEP` |
| CCR-02 | Consequential risk and recoverability | v0.2 CCR-03 preserved/renumbered | legitimate affected owner + E/L | V3, V5, V6, V7, V8 | COND + CAAI + PQCI + VRCI + RB | B§10–11; T§6–7, T§11; G/P | A/E; RC07 predecessor PASS; exact-current U | `KEEP` |
| CCR-03 | Future uncertainty, information value and commitment | v0.2 CCR-05 preserved/renumbered | S/W/O | V1, V2, V3, V4, V5, V6 | COND + AWS + DTS + VRCI | B§3, B§6–7; T§2, T§4, T§8; DA where bounded | A/E+D; exact-current U | `KEEP` |
| CCR-04 | Competing initiatives and strategic resources | v0.2 CCR-06 preserved/renumbered | S + O; W may recommend only | V1, V2, V4, V5, V7 | COND + RESP + AWS + VRCI | B§10; T§6; G/P | A/E; F17/RC08 targeted PASS on PR37 installed carrier; exact-current U | `KEEP`; no Strategic-Authority transfer |
| CCR-05 | Human–AI interaction and coordination integrity | new conditional family assembled from v0.2 interaction ingredients and external gap challenge | W + E; O/L where continuity or adaptation persists | V2, V3, V5, V6, V7, V8 | COND + DTS + AWS + CAAI + VRCI + RB | B§9–10; T§6, T§10–11; G/P | A/E; RC04–05/09–10 predecessor PASS; exact-current U | `INTEGRATED TRACE + TARGETED REAL-USE`; no new interaction subsystem |

## 6. Protected activation, relation and salience rows

These rows are deliberately retained even where they are no longer independent v0.3 IDs. Their purpose is to prevent clause-level activation or salience loss when a compiler marks the containing Core Requirement as covered.

| Guard ID | Protected semantic / v0.2 source | Current v0.3 locus | Owner / Views | Runtime realization | Evidence/status | Disposition |
|---|---|---|---|---|---|---|
| AT-01 | v0.2 CCR-02 — Persistent/divergent state | conditional clause inside CR-09 | O/W/E/L; V3, V5, V7, V8 | B§3, B§6, B§10; T§3, T§6–7, T§9–10; G/P | source E; exact-current divergence/recovery behavior U | Keep as independent activation/regression row |
| AT-02 | v0.2 CCR-04 — Recipient/use-dependent maturity | product-transformation clause inside CR-05 | W; V1, V2, V5, V6 | B§4–5, B§9, B§11, B§13; T§6, T§11; G/P | source E; RC01 predecessor only | Keep as independent recipient/use-readiness row |
| AT-03 | v0.2 CCR-07 — Human capability formation/preservation | capability-effect clause inside CR-07 | W plus S/O/L where horizon is material; V1, V4, V5, V6, V7 | B§8–9; T§6, T§11; G/P | source E; dedicated comparative-allocation behavior U | Keep as independent allocation-horizon row |
| HL-IR05 | Local output shall not redefine or strengthen wider scope, outcome, state, Authority, Acceptance, Completion or Promotion | CR-02 + CR-08 | W + wider legitimate owner; V1, V3, V5, V6, V7, V8 | B§3, B§11; T§2, T§7, T§10–11; G/P | most semantics E; dedicated relational behavior U | Preserve as historical protected relation; see §7.1 |
| HL-CHV | v0.2 CR-07 — `AI-resolvable first` is not maximal autonomy; Human involvement is legitimate where comparative value is higher | distributed across CR-06 + CR-07 | W; S/O/L when horizon/outcome is material; V1, V4, V5, V6, V7 | B§8–9; T§5–6, T§8, T§11; G/P | broad composition and Human-contribution semantics E; dedicated middle-position behavior U | Preserve as Comparative Human Value / anti-max-autonomy guard; see §7.2 |
| HL-CR15-GATE | CR-15 phrase `For admitted work with a sufficient basis` must delimit legitimate execution, not create a new stage or admission gate | CR-15 + IR-02 + CR-10; architecture Work-Selection Contract uses `admitted or triggered work` | W + E; V1, V2, V5, V6, V8 | B§3, B§7, B§13; T§2, T§10; G/P | anti-meta-work and direct-execution semantics E; dedicated ambiguity behavior U | Preserve as interpretation guard; see §7.3 |

## 7. Protected differential interpretation

### 7.1 IR-05 differential

The v0.3 split preserves:

- invalid transfer across scope/state/capability/Authority/outcome boundaries in CR-02;
- local completion not redefining wider outcome/state/Completion in CR-02; and
- local/provider result not creating wider Acceptance, Authorization, Completion or Promotion in CR-08.

The exact v0.2 phrase that a local contribution shall not by itself **redefine or strengthen** wider controlling Authority or Acceptance has no equally direct single-clause successor. The broad integrity mechanism remains present, but the relational cue is weaker.

**Disposition:** `MOSTLY PRESERVED / SALIENCE AND WORDING CHECK`. Do not edit Requirements now. Test a bounded case in which a technically successful local result appears to strengthen wider Authority or Acceptance. Repair the lowest layer that fails.

### 7.2 Comparative Human Value / anti-max-autonomy differential

v0.2 CR-07 stated explicitly:

```text
AI-resolvable first
≠ maximize autonomy

Human involvement remains legitimate
when its comparative value is higher
```

v0.3 preserves the ingredients but distributes them:

- CR-06 requires comparative allocation by actual capability, Authority, Whole-System Economics and context;
- CR-07 protects Human-specific judgment, context, expertise, authorship, learning, Acceptance, responsibility, Authority, Commitment and longer-horizon capability effects;
- the Runtime protects non-substitutable Human contribution and avoids AI-resolvable Human burden.

The explicit middle position is less salient: a compiler or runtime may correctly avoid ceremonial Human gates yet still over-generalize toward maximal autonomy.

**Disposition:** `SEMANTICALLY PRESERVED / ACTIVATION SALIENCE UNVERIFIED`. Retain this guard and test a case where AI can produce a plausible result but Human contribution has higher total value without being an Authority gate. Repair carrier salience before Requirements wording unless the normative distinction itself proves inadequate.

### 7.3 CR-15 `admitted work` gate ambiguity

Target Architecture v0.2 uses `admitted or triggered work` only to delimit the scope of Adaptive Work Selection. It does not define an admission subsystem or mandatory pre-execution stage. CR-15 likewise requires execution once a sufficient basis exists and expressly prohibits manufactured process or gates.

The phrase can nevertheless be misread in isolation as requiring an additional admission decision before work may proceed.

**Disposition:** `CORE INTENT PRESERVED / INTERPRETATION AMBIGUITY UNVERIFIED`. Retain this guard and test whether the Runtime performs already-qualified work directly. A failure should first be repaired through trace or compact carrier wording; change CR-15 only if the ambiguity remains materially normative.

## 8. Central non-equivalence trace

| ID | Controlling or protected guard | v0.2 lineage | Requirement / owner / Views | Architecture and Runtime realization | Status / disposition |
|---|---|---|---|---|---|
| NE-01 | `user request ≠ complete specification` | preserved | CR-01; S/W; V1,V2 | RESP+AWS; B§3, T§2, G/P | E; keep |
| NE-02 | `current focus ≠ controlling system` | preserved | CR-02; W+wider owner; V1,V3,V5,V8 | RESP+DTS; B§3, T§2, T§7, G/P | E; keep |
| NE-03 | `local completion ≠ wider-work completion` | preserved; IR-05 lineage | CR-02/08; W+wider owner; V1,V3,V5,V6 | RESP+DTS+CAAI+PQCI; B§3, T§2, T§10, G/P | E; retain HL-IR05 check |
| NE-04 | `provider result ≠ Acceptance / Promotion` | preserved | CR-08/13; W/E+wider owner; V3,V5,V6,V8 | CAAI+RB; B§3, B§11, T§7, T§10, G/P | E; keep |
| NE-05 | `professional method ≠ provider capability` | preserved | CR-05/13; W/E; V4,V6,V8 | PQCI+RB; B§4, B§11–12, T§8, G/P | E; keep |
| NE-06 | `capability ≠ access ≠ Authority` | preserved | CR-08; legitimate owner+W/E; V4,V5,V8 | CAAI+DTS; B§9–10, T§6–7, G/P | E; keep |
| NE-07 | `supporting/meta work ≠ required Work Product` | new | CR-15; W/E; V2,V6,V8 | WRK+EXE; B§13, T§10, G/P | E; keep |
| NE-08 | `more context ≠ better context` | preserved | CR-03/10; W/E; V3,V4,V6,V8 | RSI+AWS; B§3, B§6–7, T§3–4, G/P | E; keep |
| NE-09 | `more process ≠ more quality` | preserved | CR-05/10/15; W; V2,V6 | PQCI+AWS; B§1, B§7, B§13, G/P | E; keep |
| NE-10 | `more research ≠ better decision` | preserved | CR-10/CCR-03; W; V2,V3,V4,V6 | AWS+VRCI; B§6–7, T§4, G/P | E; keep |
| NE-11 | `more Agents ≠ better orchestration` | preserved | CR-06/10; W/O/E; V2,V4,V6,V8 | AWS+CAAI+VRCI; B§2, B§7–8, T§5, T§8, G/P | E; F12 Project PASS; keep and pair with HNE-01 |
| NE-12 | `more Human gates ≠ more Human agency` | preserved | CR-07/08; W+legitimate owner; V5,V6 | CAAI; B§8–9, T§6, T§11, G/P | E; keep and pair with HL-CHV |
| NE-13 | `minimum work ≠ prerequisite omission` | preserved | IR-03/CR-10; W; V2,V6 | AWS+PQCI; B§7, T§2, T§10, G/P | E; keep |
| NE-14 | `stored / retrieved state ≠ Authority` | preserved | CR-09; O/W/E/L; V3,V5,V7,V8 | DTS+RSI; B§3, B§6, T§3, T§7, T§9, G/P | E; keep |
| NE-15 | `QA passed ≠ professionally good` | preserved | CR-05/11; W/E; V5,V6,V8 | PQCI; B§5, B§11, T§11, G/P | E; keep |
| NE-16 | `artifact produced ≠ Use-ready` | preserved | CR-05/12; W; V1,V2,V6 | WRK+PQCI+VRCI; B§5, B§13, T§10, G/P | E; keep |
| NE-17 | `delivery ≠ outcome` | preserved | CR-12; W/O/L; V1,V2,V6,V7 | VRCI; B§13, T§10–11, G/P | E; keep |
| NE-18 | `outcome ≠ causal effect` | preserved | CR-12; S/W/L; V1,V3,V6,V7 | VRCI+RSI+PQCI; B§6, B§11, B§13 | E by combined claim/evidence semantics; causal-claim behavior remains U |
| NE-19 | `local learning ≠ global rule` | preserved | CR-14; L+affected owner; V3,V5,V7,V8 | VRCI+DTS; B§10+Learning Rule, T§6–7, G/P | E; RC06 targeted predecessor PASS |
| NE-20 | `closure ≠ manufactured next frontier` | new | CR-10/15; W/E; V1,V2,V6 | AWS+WRK; B§7, B§13, T§10, G/P | E; keep and pair with HL-CR15-GATE |
| HNE-01 | `fewer Agents ≠ automatically better Economics` | explicit in v0.2; no explicit v0.3 successor | latent in CR-06; W/O/E; V2,V4,V6,V8 | AWS+VRCI; `no form is inherently optimal`; B§2, B§7–8, T§5, T§8; Project carrier has comparative surface selection, Global carrier only generic benefit/economics cue | Core meaning inferable, explicit symmetry absent; no dedicated under-composition behavior. `SALIENCE TEST`, then lowest-layer repair only |

## 9. Consolidated findings

### 9.1 Established

1. All 3 IRs, 15 CRs and 5 CCRs have plausible owners in the five accepted Responsibilities.
2. All can be represented through the inherited eight-view architecture-description scheme; no additional View is needed for this trace.
3. All have a conceptual mechanism in Target Architecture v0.2.
4. All current Requirements are source-represented in the exact current Professional Baseline / Topology / Global / Project source, with CCR-01 and part of CCR-03 legitimately delegated and bound.
5. The interaction repair is relationally owned across Work, Execution, Distributed Typed State, Adaptive Work Selection and existing integrity invariants. It does not require a new interaction component or universal state store.
6. No Target-Architecture reopen condition is established.

### 9.2 Confirmed trace/salience repairs

1. The three absorbed v0.2 CCR triggers require separate activation rows.
2. v0.2 IR-05 requires a protected relational lineage row rather than only CR-level coverage.
3. Comparative Human Value / anti-max-autonomy requires a separate salience row because the current semantics are distributed across CR-06 and CR-07.
4. CR-15 `admitted work` requires an interpretation guard against a manufactured admission gate.
5. The compilation/regression manifest must enumerate:
   - Interpretation Rules;
   - Core Requirements;
   - Conditional Requirements;
   - all Central non-equivalences;
   - absorbed-trigger guards;
   - protected historical relations and salience guards; and
   - explicit retired guards whose semantic/salience remains under review.
6. The recovered repository/navigation baseline was stale in several places, and this Candidate repairs those entry points:
   - Target Architecture header still says `PROPOSED` and points to Requirements v0.1;
   - its embedded trace ends at CR-13 and seven old CCRs;
   - compatibility/addendum records retain Candidate-era statuses; and
   - `CURRENT.md` still contains pre-merge PR38 status/transition language despite main HEAD being the PR38 merge.

These are documentation/authority-navigation repairs, not conceptual architecture changes.

### 9.3 Residual hypotheses, not established defects

1. **Agent-composition symmetry:** explicit `fewer Agents ≠ automatically better Economics` salience is absent.
2. **Comparative Human Value:** the explicit middle position between ceremonial Human gates and maximal autonomy is less salient.
3. **IR-05 relation:** the direct `redefine or strengthen wider Authority/Acceptance` wording is weaker after relocation.
4. **Absorbed triggers:** whole-CR coverage may fail to activate recipient maturity, divergent state or Human capability horizon.
5. **CR-15 wording:** `admitted work` could be misread as an additional gate even though architecture and surrounding semantics reject that reading.
6. **Current Runtime claim:** exact current Global/Project installed identity and behavior remain unverified.

None currently justifies a Requirements or architecture change.

## 10. Repair disposition

### Repair now at documentation/trace level

1. Keep this file as the current non-normative companion on authoritative `main` and as Candidate elsewhere.
2. Add it to current navigation as the current Requirements ↔ Architecture ↔ Views ↔ Interaction ↔ Runtime trace.
3. Reconcile stale status and source pointers without rewriting the closed conceptual architecture body.
4. Amend the Runtime Compilation / Semantic Regression method so the fixed semantic manifest includes every category named in §9.2.

### Test only the residual salience hypotheses

Use bounded genuine episodes or failure-capable fixtures for:

- beneficial additional Agent/Subagent use where fewer actors would reduce whole-system performance or economics;
- AI-capable work where Human contribution has higher comparative value without constituting an Authority gate;
- a local technical success that appears to strengthen wider Authority or Acceptance;
- recipient/use transformation after technical completeness;
- divergent state across time or surfaces;
- Human capability/future-autonomy effects in allocation;
- `admitted work` being interpreted as a manufactured gate; and
- current cross-surface interaction after exact carrier deployment/readback.

### Repair only after a failure is established

Use the lowest responsible layer:

```text
trace/activation manifest
→ compact Runtime-carrier salience
→ interaction/realization contract
→ Requirements wording
→ architecture reopen only on a named accepted reopen trigger
```

Do not introduce a new architecture, View, controller, Interaction store, lifecycle, dashboard, mandatory narration or Human Gate from this trace.

## 11. Supported claim and non-claims

Supported:

> Using authoritative `main` `2693ac4427cf5f4406ca1e42212a6530a1028a90` as the recovered analysis basis, controlling Requirements v0.3 remain semantically owned by closed Target Architecture v0.2 and representable through the inherited eight-view architecture-description scheme; no additional View is needed for this trace. This Candidate changes only the integrated companion trace, regression scope and status/navigation metadata. Remaining semantic concerns are bounded activation, wording or salience hypotheses, not an established need for new architecture.

Not supported:

- that the v0.2→v0.3 transition was perfectly lossless in wording or activation salience;
- exact current installed Global/Project identity;
- exact-current Runtime behavioral conformance;
- generalized cross-domain professional effectiveness;
- Human–AI synergy, use, outcome or value;
- any Requirements-semantic or conceptual Target-Architecture commitment/body modification; or
- Architecture reopen.
