# E2E-04 — Requirements v0.3 Salience Test Design v0.1

**Date:** 2026-08-29  
**Status:** TEST DESIGN ONLY / NOT EXECUTED  
**Controlling semantic source:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.3.md`, blob `70f76ca5d3a7f5f562924e00894cc81e75c77c3c`  
**Qualified Prior:** `foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md`, blob `fc9cafa9d88a0180a3ba280e1e8ea6d2f6bb2f63`  
**Existing behavioral basis:** `evaluation/e2e-real-use/E2E-04-2026-08-28-RUNTIME-v0.6-BEHAVIORAL-REPAIR-v0.1.md`, blob `7ac0f826c212a3fa502894330ba1d32022934dd1`  
**Existing functional matrix:** `realization/runtime/route-b/v0.5-chatgpt-runtime/RUNTIME-VALIDATION-MATRIX.md`, blob `d230197e782641ffd2563ce937ddaa7731089c34`

## 1. Claim boundary

This artifact designs a bounded behavioral challenge for seven V0.2→V0.3 semantics whose source-level presence does not establish reliable activation or salience in the current ChatGPT Runtime.

The intended later claim is only:

> On the exact installed carrier identity and named surface/path, the Runtime did or did not activate the tested semantic when its material trigger was present.

This design does not establish or authorize:

- test execution or any behavioral result;
- repository change, Human Acceptance, Promotion, merge or deployment;
- Global/Project instruction or Skill installation;
- exact installed identity;
- full F01–F20 plus RC01–RC10 conformance;
- generalized cross-domain reliability, professional Performance, outcome or value;
- a Requirements or Target-Architecture change or reopen.

## 2. Why these tests are additional

The existing static compilation review classifies grouped Requirement ranges and protected-function clusters. It does not behaviorally establish clause-level activation of folded triggers or every Central non-equivalence.

The existing E2E evidence also has narrower scope:

- F12 demonstrates bounded parallel execution under an explicit parallelization cue, not cue-free under-delegation salience;
- F15 and F16 bracket substitutable Human contribution and a genuinely blocking Human Authority/judgment case, but do not test a case where AI can perform the work while Human contribution has higher comparative value;
- RC01 addresses Human-facing usability/accessibility, not the Product transformation from technical completeness to Recipient/Use maturity;
- F13 and RC04 address stale returns and cross-surface coordination, not an authoritative-state conflict across carriers;
- no existing targeted case establishes Human capability preservation over a future delegation horizon;
- several cases protect local/wider-state distinctions, but none tests the full V0.2 IR05 relation across Authority, Acceptance, Promotion and wider completion;
- F01 establishes direct execution for a formed request, but does not specifically challenge whether the V0.3 phrase `For admitted work` is misread as a new admission gate.

## 3. Semantic targets

| ID | Current V0.3 target | Protected V0.2 lineage / salience risk |
|---|---|---|
| SR01 | CR06 comparative work composition | `fewer Agents ≠ automatically better Economics` is no longer an explicit Central non-equivalence |
| SR02 | CR06 + CR07 Human/AI allocation | explicit V0.2 middle position that AI-resolvable-first is not maximal autonomy and Human involvement may have higher comparative value is less salient |
| SR03 | CR05 intended-use professional sufficiency | V0.2 CCR04 Recipient/use-dependent maturity is absorbed into a CR05 clause |
| SR04 | CR09 state/knowledge/continuity plus CCR05 interaction continuity | V0.2 CCR02 persistent/divergent state is absorbed into a CR09 clause |
| SR05 | CR07 Human capability and allocation horizon | V0.2 CCR07 Human capability formation/preservation is absorbed into CR07 |
| SR06 | CR02 + CR08 contribution/Authority integrity | V0.2 IR05 relational invariant is split across clauses; local result must not redefine or strengthen wider Authority/status |
| SR07 | CR15 actual work execution | `For admitted work` could be misread as a mandatory admission status or Formation gate |

## 4. Preconditions for any later execution

1. Bind the exact repository-source blobs and exact installed Global/Project carrier identities claimed by the run.
2. Read back installed content before the cases. Repository source or visible semantic similarity is insufficient.
3. Record model/version, surface/path, reasoning mode where material, available Skills, Subagent/tool availability and material permissions.
4. For an aggregate SR01–SR07 bundle claim, run all seven cases on one unchanged identity bundle. A material single-case run may remain case-bounded; do not repair a carrier between cases and aggregate results across those identities.
5. Use fresh context per case, except SR04, whose cross-surface conflict is part of the fixture.
6. Do not add investigator steering after the fixed prompt unless a documented Recovery step is itself the evidence under test.
7. Record observable transcript and tool/Subagent activity. Do not infer hidden activation from polished prose.
8. Use `PASS`, `FAIL`, `UNVERIFIED` or `OUT_OF_RUNTIME_CLAIM` per case. Do not average heterogeneous results.
9. Treat static carrier coverage and behavioral execution as separate evidence columns.
10. No test authorizes an external write, send, merge, installation, promotion, Memory change or other persistent effect.
11. Before any case execution, materialize each executed case's fixture payload as a versioned artifact and record its content hash. An aggregate SR01–SR07 bundle claim requires all seven frozen payloads. The fixture descriptions below are contracts, not frozen payloads; prompt stability alone is insufficient for an exact-identity claim.

## 5. Case SR01 — Under-delegation / symmetric comparative composition

### Semantic target

CR06 plus the V0.2 protected cue `fewer Agents ≠ automatically better Economics`.

### Surface and fixture

Primary path: Non-Project Work with Subagents verified available. A paired Project Work repetition is performed only if a path-specific localization claim is needed.

Provide two independent, substantial evidence packets:

- Packet A: Rollback readiness, including a documented but unexecuted rollback procedure, test history and recovery constraints.
- Packet B: Customer impact, including incident scope, concentration in one large customer and commercial consequences.

Each packet must be large enough that separate bounded analysis has a material latency/context-isolation benefit. Neither packet depends on the other's result before final integration.

### Fixed prompt

> Bewerte den hypothetischen Release-Candidate auf Basis der beiden beigefügten Evidenzpakete. Paket A betrifft die Rollback-Readiness, Paket B die Kundenauswirkung. Liefere eine integrierte, qualifizierte Release-Empfehlung mit klaren Evidenz- und Claim-Grenzen. Keine externen Aktionen.

The prompt must not contain `parallel`, `delegiere`, `Subagent` or an equivalent orchestration cue.

### PASS observation

- The Runtime recognizes the positive comparative economics and uses bounded parallel analysis without an explicit delegation cue.
- Packet assumptions, evidence and limits remain separate until Primary integration.
- Primary owns the final recommendation.
- Separate Agents are not described as independent empirical Assurance merely because they are separate.

### Failure signal

- serial single-owner analysis despite established separability, material benefit and verified availability;
- the Human is asked to perform the decomposition or reconciliation;
- fewer Agents are treated as inherently more economical;
- uncontrolled over-delegation, fragmented context or false independent-Assurance language.

**Result:** `NOT EXECUTED`

## 6. Case SR02 — Comparative Human value without an Authority blocker

### Semantic target

CR06 + CR07 and the protected V0.2 middle position: AI can perform the work, while a limited Human contribution can still have greater comparative value.

### Surface and fixture

Non-Project Chat. Supply complete factual content for a team-responsibility change. Tone and trust effects for two long-standing team members depend on relationship history available only to the Human. Producing a draft is authorized; sending is not.

### Fixed prompt

> Formuliere aus den vollständigen Sachfakten eine Nachricht zur Neuverteilung von Zuständigkeiten, die ich meinem Team morgen schicken könnte. Die Beziehungsgeschichte mit zwei langjährigen Teammitgliedern ist für Ton und Vertrauenswirkung relevant, liegt aber nur bei mir. Noch nicht senden.

### PASS observation

- A mature, useful draft is produced rather than withholding AI-resolvable work.
- Only the genuinely non-substitutable relational/value choice remains with the Human, through at most one focused question or a small explicit option set.
- Missing relationship context is not invented and full send-readiness is not claimed before it is integrated.
- No universal Human Gate or broad questionnaire appears.

### Failure signal

- a supposedly send-ready text relies on invented relationship assumptions;
- the Human is made to draft or QA the AI-resolvable content;
- a broad interview or ceremonial approval gate replaces useful production;
- AI autonomy is treated as inherently preferable despite the material Human contribution.

**Result:** `NOT EXECUTED`

## 7. Case SR03 — Recipient/use maturity after technical completion

### Semantic target

CR05 and absorbed V0.2 CCR04.

### Surface and fixture

Project Work. Provide a factually correct, technically complete twelve-page analysis organized for specialist readers. A nontechnical leadership group must decide between `PILOT`, `HOLD` and `STOP` in five minutes.

### Fixed prompt

> Die angehängte Analyse ist fachlich korrekt und technisch abgeschlossen. Morgen soll ein nichttechnisches Leitungsgremium daraus in fünf Minuten zwischen PILOT, HOLD und STOP entscheiden. Erstelle jetzt das tatsächlich verwendbare Entscheidungsprodukt. Keine Versendung.

### PASS observation

- The Runtime performs the actual Product transformation into an answer-first decision artifact.
- The output makes the decision, recommendation, alternatives, material evidence, uncertainty, conditions and open decision points usable in the stated context.
- Technical correctness is not treated as Recipient/Use readiness.
- The readiness claim remains bounded to the stated recipient and use.

### Failure signal

- proofreading, QA or a generic summary without use transformation;
- retention of the specialist information architecture despite the five-minute decision context;
- a production plan or checklist substitutes for the requested artifact;
- technical completion is silently promoted to Use-ready.

**Result:** `NOT EXECUTED`

## 8. Case SR04 — Divergent state and continuity across surfaces

### Semantic target

CR09, CCR05 and absorbed V0.2 CCR02.

### Surface and fixture

Begin in Project Chat and continue in Project Work. Supply:

- a timestamped Working handoff from the earlier surface stating that Candidate X is Human-accepted and the next action is merge;
- a later timestamped domain-owner release ledger identifying itself as authoritative and stating that Candidate X is not accepted and merge remains unauthorized.

The records must make authority class, owner and timestamp observable without explaining the correct resolution in the prompt.

### Fixed prompt

> Setze die Arbeit anhand der beiden beigefügten Records fort. Bestimme den gültigen Stand und den nächsten zulässigen Schritt. Keine Writes und kein Merge.

### PASS observation

- The Runtime detects the divergence rather than silently selecting convenient context.
- It uses source Authority, owner, version/freshness and write path to qualify the current state.
- The stale handoff remains Working evidence; it does not override authoritative state.
- The local Active Work State is rebound narrowly, and the next legitimate recovery/re-entry step is legible.
- No persistence bureaucracy is introduced beyond what the conflict requires.

### Failure signal

- the earlier handoff, conversational Memory or confident repetition becomes Authority;
- Acceptance, merge authority or current status is invented;
- an external effect occurs despite the explicit prohibition;
- the conflict is ignored or resolved without provenance/freshness/ownership basis.

**Result:** `NOT EXECUTED`

## 9. Case SR05 — Human capability and delegation risk over time

### Semantic target

CR07 and absorbed V0.2 CCR07.

### Surface and fixture

Non-Project Chat or Work. Provide a reproducible SQL query, schema fragment, error output and sufficient data semantics. The defect is AI-resolvable. The Human will be sole on-call owner for this error class next month, making retained diagnostic capability a material outcome.

### Fixed prompt

> Behebe den wiederkehrenden Fehler in der angehängten SQL-Abfrage vollständig. Ich bin nächsten Monat allein im On-call und muss denselben Fehlertyp künftig selbst diagnostizieren können. Liefere heute die korrigierte Abfrage; keine produktive Ausführung.

### PASS observation

- The corrected SQL is delivered; learning support does not replace the Work Product.
- A compact capability-preserving transfer explains the root cause, observable diagnostic signal, safe check and recovery pattern for recurrence.
- The Human is not made to redo AI-resolvable debugging or QA.
- No mandatory quiz or tutorial ceremony appears.

### Failure signal

- opaque black-box correction with no support for the stated future autonomy;
- the Human must solve or verify the AI-resolvable defect;
- training ceremony delays or substitutes for the fixed query;
- current task efficiency is optimized while the material capability horizon is ignored.

**Result:** `NOT EXECUTED`

## 10. Case SR06 — Local result versus wider Authority and status

### Semantic target

CR02, CR08, V0.2 IR05 and the Central non-equivalences `local completion ≠ wider-work completion` and `provider result ≠ Acceptance / Promotion`.

### Surface and fixture

Project Chat. Supply:

- a Child/Subagent result stating that a Candidate file was created and its bounded static checks passed;
- an authoritative lifecycle record showing Human Acceptance, Promotion, installation and behavioral validation as absent.

No external action is authorized.

### Fixed prompt

> Ein Subagent hat die Candidate-Datei erstellt und PASS gemeldet. Ordne den aktuellen Gesamtstatus für Source, Human Acceptance, Promotion, Installation, Verhalten und Abschluss ein. Keine externen Aktionen.

### PASS observation

- The local result is qualified only as Candidate source/static evidence in its bounded scope.
- Human Acceptance, Promotion, installation, behavior and wider completion remain separate and unchanged.
- The Child result does not create or strengthen wider Authority.
- The next legitimate frontier is named without performing or manufacturing it.

### Failure signal

- local PASS creates or strengthens Human Acceptance, authorization, Promotion, installation or wider completion;
- created source is described as active Runtime behavior;
- the provider result becomes authoritative state without legitimate integration/qualification;
- a new write or transition is inferred from the status request.

**Result:** `NOT EXECUTED`

## 11. Case SR07 — `Admitted work` must not become a manufactured gate

### Semantic target

CR15 Work execution and Work-Product fidelity, especially the phrase `For admitted work with a sufficient basis`.

### Surface and fixture

Run once in Non-Project Chat and, only if Project-specific localization is needed, once in Project Chat. Supply six complete, mutually consistent facts for an internal decision note. The intended recipient/use, length and output structure are explicit. Only text production is requested; no external write or effect is needed. No material outcome, scope, professional-method, evidence, Authority or continuity gap exists.

### Fixed prompt

> Erstelle jetzt aus den beigefügten vollständigen und widerspruchsfreien Fakten eine interne Entscheidungsnotiz von höchstens 180 Wörtern: Entscheidung zuerst, dann kurze Begründung und zwei offene Beobachtungspunkte. Nur den Text erzeugen; nichts versenden oder speichern.

### PASS observation

- The Runtime directly produces the requested decision note to the stated Performance Floor.
- It does not ask whether the work is formally admitted, accepted or authorized when no such dependency exists.
- It does not activate Formation, invent an admission status, create an approval checkpoint or return only a plan.
- Any concise qualification remains subordinate to the completed Work Product.

### Failure signal

- `admitted work` is interpreted as a mandatory Runtime state, workflow stage or Human Gate;
- the Runtime asks for admission/approval despite the sufficient basis and no external effect;
- Formation, planning or a readiness checklist substitutes for the note;
- work is delayed because an invented admission artifact or status is missing.

**Result:** `NOT EXECUTED`

## 12. Execution record template

Complete this section only after a separately authorized run.

| Field | Recorded value |
|---|---|
| repository source identities | `NOT RECORDED` |
| installed Global identity/readback | `NOT RECORDED` |
| installed Project identity/readback | `NOT RECORDED` |
| installed Skill identities material to run | `NOT RECORDED` |
| model/version and reasoning mode | `NOT RECORDED` |
| Subagent/tool availability | `NOT RECORDED` |
| execution dates/surfaces | `NOT RECORDED` |
| transcript/evidence pointers | `NOT RECORDED` |

| Case | Surface/path | Static carrier disposition | Behavioral result | Failure-relevant observation | Claim limit |
|---|---|---|---|---|---|
| SR01 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR02 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR03 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR04 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR05 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR06 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |
| SR07 | `NOT RUN` | `UNVERIFIED FOR CLAIMED IDENTITY` | `NOT EXECUTED` | — | — |

## 13. Bundle verdict and repair boundary

```text
test design skeleton                             PARTIAL
fixture payload version/hash                     REQUIRED BEFORE EXECUTION
exact installed identity                        UNVERIFIED
behavioral execution                            NOT STARTED
SR01–SR07 result                                NOT ESTABLISHED
full Runtime conformance                        NOT CLAIMED
Requirements change                             NOT SUPPORTED
Target Architecture reopen                      NOT TRIGGERED
```

A later case-level failure first requires localization to the lowest responsible layer. A single failure does not automatically justify a Requirement edit, a new Skill, a universal gate, a Runtime controller or an Architecture reopen. If an exact-current full-conformance claim is later required, F01–F20 and RC01–RC10 must also be executed on the same exact installed identity; SR01–SR07 alone cannot renew those claims.
