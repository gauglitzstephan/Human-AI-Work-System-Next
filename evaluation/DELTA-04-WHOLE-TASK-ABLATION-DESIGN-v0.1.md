# Δ4 — Whole-Task Ablation Design v0.1

**Status:** EXECUTION-READY DESIGN / RUNS NOT YET AUTHORIZED  
**Date:** 2026-08-19  
**Parent:** `architecture/DELTA-04-FUNCTION-CASE-DISCRIMINATION-v0.1.md`  
**Purpose:** Determine whether the surviving thin Adaptive Work-Control metapolicy adds material whole-task value beyond the same qualified Work Architecture without that metapolicy.

This is **not** a micro-trigger test and does not compare architecture vocabulary recall.

---

# 1. Causal question

Primary comparison:

```text
A — SAME QUALIFIED WORK-ARCHITECTURE CONTROL

vs

B — A + THIN ADAPTIVE WORK-CONTROL METAPOLICY
```

Secondary complexity benchmark, only if needed:

```text
C — PAOS-STYLE MINIMAL CONDITIONAL ROUTING
```

The primary causal inference is A↔B because they share the same base and differ only by the Δ4 treatment.

C is not a matched ablation; it answers whether a much smaller operating contract reaches equivalent outcomes.

---

# 2. Shared evaluation rules

Use the same:
- model/version;
- surface/runtime class;
- tool availability;
- case prompt;
- evaluator rubric;
- context/source pack;
- randomness settings where controllable.

Each case starts in a fresh isolated context. Do not allow output from a prior condition/case to enter another run.

Record the exact environment actually used. Do not assume memory/instruction/tool isolation from product names alone.

Do not change either condition after an individual failure.

Evaluate the **whole task result**, not whether the model says `LEARN`, `ROBUSTIFY`, `STAGE`, `Semantic Compiler`, or any other architecture vocabulary.

---

# 3. Condition A — matched control

The following is the complete Δ4 control overlay. It is a compact projection of qualified Work Architecture for the functions material to this experiment.

```text
For material professional work, work from the intended outcome rather than wording alone. Use current authoritative reality and preserve valid existing work. Establish material requirements, professional method/reference, receiving context and success conditions. When the route is open, compare alternatives that differ in mechanism/bottleneck, including simpler/no-action where credible; investigate decision-flipping unknowns rather than exhaustive uncertainty. Decompose only when method, capability, dependency, interface, authority, assurance, transition or recovery differs materially. Allocate Human/AI/tool/workflow functions by effective capability and authority. Execute/integrate the actual Work Product, match assurance to the claim, reopen only affected dependencies after changed evidence, and close when additional work no longer has sufficient expected value or a real Human/external boundary is reached. Keep clear bounded work direct and do not expose process unless useful.
```

Condition A intentionally contains:
- decision-flipping unknowns;
- proportionality/net-value stopping;
- preservation/local reopen;
- route breadth;
- authority/assurance;
- simple-work collapse.

These are **not** credited to B.

---

# 4. Condition B — exact Δ4 treatment

Condition B = Condition A **plus only** this block:

```text
For consequential work where unresolved uncertainty or commitment structure can materially alter the next decision/state, use this metapolicy:

NEXT STATE — identify the exact legitimate decision/claim/state transition that matters next.

LEARN — acquire additional information only when an unresolved variable can materially change the route, is sufficiently learnable now, and expected decision improvement exceeds information-acquisition + delay + coordination cost. Otherwise do not research merely because uncertainty exists.

ROBUSTIFY — when future/external uncertainty is material but cannot or should not be resolved now, avoid false precision; stress-test only decision-relevant plausible states, expose vulnerabilities/breakpoints, and define useful signposts/adaptation triggers.

COMMIT — where commitment structure matters, compare WAIT / PILOT-TEST / STAGE / REVERSIBLE ACTION / INFORMATION-GENERATING ACTION / FULL COMMITMENT. Preserve flexibility only while expected learning/option value exceeds delay, coordination, lost-opportunity and flexibility cost.

STOP — stop additional cognition/flexibility when it can no longer change the decision enough to justify its cost; return the smallest useful next decision/action frontier.
```

Nothing else differs from A.

This tests the **thin metapolicy**, not the historical full Semantic Compiler bundle.

---

# 5. Condition C — secondary minimum-complexity benchmark

Use only if A↔B leaves a material live question or if B appears beneficial enough to justify comparison with a smaller rival.

```text
Keep clear bounded work direct. For material work establish the actual purpose/output, load only relevant context/evidence, choose the smallest adequate method/tool/capability, execute within the authorized boundary, separate technical checks from substantive quality and Human acceptance, and close/continue/repair based on the actual result. Create persistent state or additional structure only when it has clear future value. Human retains material judgment, commitments, external-action authority and final acceptance.
```

C is deliberately sparse. Do not infer that missing explicit language means the capable model cannot reason about uncertainty.

---

# 6. Test portfolio

Use four cases in Stage 1: one non-activation guard plus three true Δ4 discriminators. This is intentionally much smaller than prior broad suites.

## D4-WT-01 — Direct bounded guard

### Prompt

> Übersetze ins Deutsche: “The meeting starts at eight.”

### Expected behavior
Correct direct translation. No decision analysis, uncertainty discussion, process narration or new questions.

### Δ4 purpose
B must remain latent.

### Critical regression
Any visible or material metapolicy/process activation that worsens the simple result.

---

## D4-WT-02 — Learnable uncertainty with positive information value

### Prompt

> Ich betreibe ein kleines B2B-Datenprodukt und muss entscheiden, ob ich jetzt ca. 8.000 € und sechs Wochen in eine neue vertikale Version investiere. Fachlich können wir sie bauen. Das größte offene Risiko ist nicht die Technik, sondern ob die Zielkunden für genau diesen Workflow wirklich zahlen. Ich habe 12 passende bestehende Kontakte. Für rund 300 € und drei Arbeitstage könnte ich fünf strukturierte Kaufinterviews plus einen konkreten Pre-Sale-Test durchführen; das Ergebnis würde direkt beeinflussen, ob und für welches Segment wir bauen. Die Vollentwicklung wäre größtenteils versunkener Aufwand. Es gibt in den nächsten zwei Wochen keinen relevanten First-Mover- oder Deadline-Vorteil. Entscheide, was wir jetzt tun sollten, und führe die Entscheidung so weit wie sinnvoll aus — ich will keinen allgemeinen Research-Plan.

### Evaluator truth / decision structure
- one material unknown can flip the route;
- it is cheaply and quickly learnable;
- full commitment is largely sunk;
- delay cost is low relative to learning value.

### Strong target behavior
- recommend a bounded information-generating step rather than full build or broad market research;
- specify the minimum evidence/decision rule needed from the pre-sale/interview step;
- avoid researching unrelated uncertainties;
- make clear what happens after positive/negative/mixed signal;
- stop at an actionable frontier.

### B-specific dimensions
- explicit learnability/cost tradeoff;
- selective evidence acquisition;
- information-generating commitment;
- stopping/frontier precision.

### Critical failure
- full build without addressing the cheap decision-flipping test;
- extensive generic research instead of the available high-value evidence;
- endless deferral despite the bounded test being sufficient to move the decision.

---

## D4-WT-03 — Deep uncertainty / robustness rather than fake forecast

### Prompt

> Wir müssen für ein kleines B2B-Softwareprodukt jetzt eine Integrationsarchitektur wählen. Eine externe Branchen-Schnittstelle bzw. regulatorische Spezifikation könnte sich in den nächsten 6–18 Monaten deutlich ändern, aber es gibt aktuell keine belastbare Wahrscheinlichkeitsverteilung und Experten widersprechen sich. Variante A kostet jetzt 10.000 € und ist stark auf die heutige Spezifikation optimiert; bei einem größeren Wechsel wären ungefähr 50.000 € Migration plus mehrere Wochen Unterbrechung realistisch. Variante B kostet jetzt 14.000 €, nutzt einen Adapter-/Abstraktionslayer und wäre bei einem Wechsel voraussichtlich für etwa 8.000 € anpassbar, hat aber heute etwas mehr Entwicklungs- und Wartungsaufwand. Wir müssen diese Woche eine Architekturentscheidung treffen. Sag mir, welche Route wir wählen sollten und welche Unsicherheit wir sinnvollerweise noch behandeln — ohne so zu tun, als könnten wir die Zukunft exakt prognostizieren.

### Evaluator truth / decision structure
- uncertainty is material;
- probabilities are not credible enough for a precise expected-value forecast;
- options have materially different vulnerability / switching cost;
- action cannot simply wait for full resolution.

### Strong target behavior
- explicitly avoid fabricated probabilities/false forecast precision;
- compare vulnerability/regret/robustness of the two architectures;
- likely favor the modular route unless a concrete present constraint outweighs the resilience premium;
- identify only useful signposts (e.g. formal draft/publication/API deprecation/vendor implementation evidence) that would trigger adaptation;
- do not launch generic long-horizon forecasting work.

### B-specific dimensions
- uncertainty-mode fit: forecast vs robustness;
- vulnerability/breakpoint thinking;
- signpost/adaptation quality;
- decision despite unresolved uncertainty.

### Critical failure
- invent probability numbers and optimize on them as facts;
- say “wait for more information” when the decision cannot wait and no high-value resolution path exists;
- ignore the large asymmetry in future migration exposure.

---

## D4-WT-04 — Paired commitment calibration / anti-optionality

This case has two variants. Run each condition on **both variants** only if D4-WT-02 or D4-WT-03 suggests a material treatment effect; otherwise keep them as holdout confirmation.

### Variant A — flexibility should win

> Wir überlegen, ein neues internes AI-Workflow-System für einen wiederkehrenden Prozess aufzubauen. Die Vollautomatisierung kostet rund 25.000 € und drei Monate; der größte unbekannte Faktor ist, ob die Nutzer den neuen Ablauf tatsächlich annehmen und ob die Ausnahmen automatisierbar sind. Für 2.000 € und zwei Wochen können wir denselben Prozess als Human+AI-Pilot mit 20 realen Fällen fahren. Dieser Pilot liefert direkt Daten zu Nutzung, Ausnahmequote, Zeitersparnis und Fehlern; fast alle Pilot-Artefakte sind später wiederverwendbar. Es gibt keinen relevanten Markttermin. Wie weit sollten wir uns jetzt festlegen?

**Target:** stage/pilot first; define expand/stop/redesign evidence; do not confuse pilot with final automation readiness.

### Variant B — flexibility should lose

> Gleiche Grundentscheidung, aber diesmal gilt: Ein Pilot würde sechs Wochen dauern, die zentrale technische Unsicherheit erst nach echter Vollintegration auflösen und kaum wiederverwendbare Arbeit erzeugen. Ein bereits vertraglich zugesagter Kunde zahlt 18.000 € nur, wenn die produktive Integration in drei Wochen verfügbar ist; bei späterer Lieferung entfällt der Auftrag. Die Vollintegration kostet 12.000 €, nutzt weitgehend reversible Standardkomponenten und kann bei Nichterfolg mit etwa 2.000 € Rückbaukosten beendet werden. Die verbleibenden technischen Risiken sind bekannt und testbar während der Implementierung. Wie weit sollten wir uns jetzt festlegen?

**Target:** do not ritualistically pilot/wait; the information value of a separate pilot is low while delay has a large known cost. A bounded full/accelerated commitment with embedded checks/recovery may dominate.

### B-specific dimensions
- commitment-mode fit;
- anti-optionality discipline;
- learning value vs delay/lost-opportunity cost;
- distinction between action that learns and delay that only postpones.

### Critical failure
Same `pilot/stage` recommendation for both variants without engaging with the changed economics/information structure.

---

# 7. Why prior real cases are not rerun by default

Existing evidence already establishes useful regression behavior:

- Bergfreunde recovery: preservation/local reopen/readiness boundary;
- Bewerbung ledger: state/authority/local repair;
- Opportunity Search: current search + decision-flipping unknowns + research stopping;
- v0.3.4 whole-task suite: strong pre-Compiler work on directness, route challenge, actual-state repair and readiness calibration.

Rerunning these as if they were new compiler-specific tests would spend evaluation effort without sufficient discrimination.

The historical `adaptive-decision-quality-test-v0.1` is explicitly superseded and prohibits another context-poor micro-trigger/pre-commitment loop. Δ4 therefore uses **context-rich whole-task decisions** only.

---

# 8. Evaluation rubric

Score only dimensions material to the case using:

- **2 — strong pass**
- **1 — partial**
- **0 — material fail**
- **N/A**

## Core outcome dimensions

1. **Decision / recommendation quality** — route is defensible given case facts.
2. **Information-selection quality** — seeks only information capable of changing the decision at justified cost.
3. **Uncertainty-mode fit** — learns, forecasts, robustifies or proceeds according to the actual uncertainty structure.
4. **Commitment calibration** — commitment depth matches reversibility, learning value, delay and downside.
5. **Frontier / stopping precision** — ends with the smallest next action/decision frontier rather than research or process sprawl.
6. **Evidence / uncertainty integrity** — no fabricated probabilities or unsupported readiness.
7. **Efficiency / proportionality** — no unnecessary questions, analysis, scenarios or framework narration.
8. **Directness regression** — simple work remains simple.

## Cost dimensions

Record separately:
- response length;
- tool/search calls if any;
- number of Human questions;
- visible process/architecture narration;
- treatment text length / semantic burden.

Do not compensate a critical decision failure with lower token use.

---

# 9. Blinding / run discipline

For A↔B:

1. freeze both condition overlays before first run;
2. assign opaque labels `X` and `Y` to condition outputs before substantive scoring where feasible;
3. run the same case prompt in fresh contexts;
4. retain complete first response and tool traces;
5. score outputs before revealing condition;
6. do not patch conditions mid-wave;
7. record model/surface/tool state exactly.

Because model variance exists, a single close pair is not evidence of equivalence or superiority.

---

# 10. Staged evidence budget

Avoid another large benchmark program.

## Stage 1 — minimum discrimination

Run:

```text
D4-WT-01: A + B
D4-WT-02: A + B
D4-WT-03: A + B
```

Total: **6 runs**.

### Stop immediately if

A and B are materially equivalent on WT-02/03 and B adds any noticeable directness/process cost.

Disposition then:

```text
explicit Δ4 metapolicy → REJECT / method-level knowledge only
```

### Continue only if

B shows a material decision-quality gain on at least one true discriminator without a directness/critical regression.

## Stage 2 — anti-optionality confirmation

Run both WT-04 variants under A and B.

Additional: **4 runs**.

Purpose: verify that B does not simply over-preserve flexibility.

## Stage 3 — minimum-complexity benchmark, conditional

Only if B still has positive evidence, compare C on the discriminating cases where B won.

Do not run C on every case by default.

---

# 11. Decision logic

## Outcome D4-0 — no incremental value

If A matches B on the discriminating cases or B mainly changes vocabulary/visible process:

```text
Semantic Compiler as architectural controller → REJECT
thin Adaptive Work-Control global policy     → REJECT
VoI / Robustness / Commitment                → retain as conditional methods / knowledge
```

## Outcome D4-1 — narrow policy value

If one specific policy family repeatedly changes decision quality:

```text
promote only that narrow conditional policy
not the full bundle
```

Example: if Prospective Robustness helps but Information Value/Commitment are redundant, keep robustness routing only where future-sensitive decisions require it.

## Outcome D4-2 — thin metapolicy earns existence

If B reproducibly improves multiple distinct discriminator families, survives the anti-optionality pair, and does not harm direct work:

```text
RETAIN THIN ADAPTIVE WORK-CONTROL METAPOLICY
inside Work Architecture
```

Still do **not** create a peer Work Engine layer.

Δ5 would then decide how/where the policy can be behaviorally activated under finite runtime salience.

## Outcome D4-3 — C matches B at much lower burden

If PAOS-style C matches B on the exact cases where B appeared useful:

```text
prefer minimal routing + conditional decision methods
```

The Semantic Compiler may remain explanatory Knowledge Capital, not active global architecture.

---

# 12. Evidence claim boundary

This experiment can establish only:

> whether the frozen thin Δ4 treatment improves the selected whole-task decision behaviors relative to the frozen matched control under the tested model/context conditions.

It cannot by itself establish:
- universal superiority;
- runtime deployment design;
- final Custom Instructions wording;
- effectiveness across all domains;
- final Work Engine architecture;
- long-term Quality-in-Use or outcome value.

No GitHub Actions/CI automation is required for this evaluation. Manual controlled runs are sufficient and preserve the current resource/complexity budget.