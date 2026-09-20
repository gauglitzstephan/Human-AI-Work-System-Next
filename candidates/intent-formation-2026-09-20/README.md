# AI-Native Intent Formation — Kandidat vom 20.09.2026

**Kandidat vorbereitet und geprüft; nicht installiert, nicht gemergt.** Bestehendes Framing bleibt unverändert. Gebaut wurde `form-intent`: ein dedizierter Einstieg mit optionalen Methoden, getrenntem Working State und lesbarem Intent. Er endet vor Specification und Planning.

Der finale Kern enthält eine verhaltensgeprüfte Reparatur für unbestimmte Problemschilderungen. Ein früher Abschlussfehler und ein erfolgloser erster Reparaturversuch bleiben nachvollziehbar. Kein vollständiger Human-UX-Nachweis: der Ownability-Test nutzt einen AI-Reviewer; eine reale menschliche Abnahme steht aus.

## Einstieg zur Entscheidung

- [Evaluation mit allen 26 Testklassen](tests/Intent_Formation_Evaluation.md)
- [Abnahmekriterien und Evidenzgrenzen](tests/Acceptance_Crosswalk.md)
- [Erhalt, Migration und Kompatibilität](handover/Migration_and_Compatibility.md)
- [Installation nach separater Freigabe](handover/Installation.md) und [Rollback](handover/Rollback.md)

## Installierbares Paket

Nur der Ordner `skills/form-intent` gehört zum Skill: `SKILL.md`, `agents/openai.yaml`, vier Referenzen (`selection.md`, `inquiry.md`, `state-and-artifact.md`, `boundary.md`) und zwei optionale Assets (`intent-short.md`, `intent-expanded.md`). Keine weiteren Laufzeitabhängigkeiten oder Hintergrunddienste. Der Test-Router ist ausschließlich eine Vergleichsvariante.

## Research und Analysis

- [Intent_Formation_Reference_Map.md](research/Intent_Formation_Reference_Map.md)
- [Intent_Formation_Research_Synthesis.md](research/Intent_Formation_Research_Synthesis.md)
- [Intent_Spec_Boundary.md](research/Intent_Spec_Boundary.md)
- [Existing_System_Assessment.md](research/Existing_System_Assessment.md)

## Design

- [Intent_Formation_Target_Design.md](design/Intent_Formation_Target_Design.md)
- [Intent_Domain_Model.md](design/Intent_Domain_Model.md)
- [Intent_Template_Strategy.md](design/Intent_Template_Strategy.md)
- [Intent_Formation_Quality_Model.md](design/Intent_Formation_Quality_Model.md)
- [Intent_Formation_Human_AI_UX_Model.md](design/Intent_Formation_Human_AI_UX_Model.md)
- [Intent_Artifact_Information_Architecture.md](design/Intent_Artifact_Information_Architecture.md)
- [Intent_Ownability_Model.md](design/Intent_Ownability_Model.md)
- [Upstream_Selection_and_Entry_Gate_Design.md](design/Upstream_Selection_and_Entry_Gate_Design.md)
- [Intent_Formation_Skill_Reference_Architecture.md](design/Intent_Formation_Skill_Reference_Architecture.md)
- [Intent_Engineering_Terminology_Assessment.md](design/Intent_Engineering_Terminology_Assessment.md)
- [Intent_Risk_Boundary_Temporal_Model.md](design/Intent_Risk_Boundary_Temporal_Model.md)

## Verification

- [Testplan](tests/Intent_Formation_Test_Plan.md), [Inputs](tests/inputs.json), [Laufmanifest](evidence/run-manifest.json)
- [Failure Modes und Known Limitations](tests/Failure_Modes_and_Known_Limitations.md)
- [Unabhängige Review](tests/runs/review/independent-review.md)
- [Gezielte Reparaturen](evidence/Repair_Record.md), [Proxies](evidence/proxy-metrics.json)
- [Artefakt-Reader-Test](tests/runs/D10/reader-response.md)
- Beispiele: [finaler persönlicher Intent](tests/runs/R21/intent.md), [nichttechnische Entscheidung](tests/runs/D03/intent.md), [kleine Korrektur](tests/runs/R24/intent.md), [DGUV-Arbeitsstand mit Blockern](tests/runs/D02/intent.md), [Stop nach Reuse-Evidenz](tests/runs/D08/intent.md)

Alle Szenario-Folgeantworten einschließlich Akzeptanz sind synthetische Fixtures, keine persönlichen Entscheidungen des Auftraggebers. Rohantworten enthalten ihre ursprünglichen lokalen Links; die relativen Indexlinks oben öffnen die gesicherten Artefakte. Dateihashes stehen im Release-Manifest.
