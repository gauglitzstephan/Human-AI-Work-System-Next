# AI-Native Intent Formation — Kandidat R3 vom 20.09.2026

**Kandidat vorbereitet und geprüft; nicht installiert, nicht gemergt.** Bestehendes Framing bleibt unverändert. Gebaut wurde `form-intent`: ein dedizierter Einstieg mit optionalen Methoden, getrenntem Working State und lesbarem Intent. Er endet vor Specification und Planning.

R3 präzisiert die Qualifikation an der Grenze zur nachfolgenden Arbeit, unterscheidet Beobachtung, Deutung und gewünschte Wirkung und verbessert die Lesefläche. Acht neue Formation-/Fortsetzungsläufe und ein isolierter Leser-Test ergänzen die historische Evidenz. Die frühere pauschale Fertig-/Abnahmeaussage gilt nicht fort. Der originale R21-Status wurde anhand seiner tatsächlichen synthetischen Nachlieferung unabhängig als tragfähig beurteilt; daraus wird keine allgemeine Discovery-Fähigkeit abgeleitet. Menschliche Eignung und produktive Aktivierung bleiben gesondert.

## Einstieg zur Entscheidung

- [Aktuelle R3-Evaluation und Grenzen](tests/Intent_Formation_Evaluation.md)
- [Konkrete Änderungen und Ausgangsbefund](evidence/Repair_R3_Record.md)
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
- [R3-Prüfkriterien](tests/Qualification_Repair_R3.md), [R3-Laufmanifest](evidence/R3-run-manifest.json)
- [Unabhängiger R3-Review](tests/runs/review-r3/independent-review.md)
- [Historische Review](tests/runs/review/independent-review.md), [frühere Reparaturen](evidence/Repair_Record.md), [historische Proxies](evidence/proxy-metrics.json)
- [Neuer Artefakt-Leser-Test](tests/runs/Q38/reader-response.md)
- Neue Beispiele: [persönlicher Intent](tests/runs/Q31/intent.md), [Vereinsfall](tests/runs/Q32/intent.md), [Entscheidungsanalyse](tests/runs/Q33/intent.md), [kleine Korrektur](tests/runs/Q34/intent.md), [Korrektur nach neuer Evidenz](tests/runs/Q35H/intent.md), [DGUV-Arbeitsstand mit Blockern](tests/runs/Q36/intent.md), [Intent-/Spec-Grenze](tests/runs/Q37/intent.md)
- Erhaltene historische Fälle: [Original R21](tests/runs/R21/intent.md), [Stop nach Reuse-Evidenz](tests/runs/D08/intent.md); [historischer R2-Bewertungsstand](evidence/history/R2/Intent_Formation_Evaluation.md)

Alle Szenario-Folgeantworten einschließlich Akzeptanz sind synthetische Fixtures, keine persönlichen Entscheidungen des Auftraggebers. Rohantworten enthalten ihre ursprünglichen lokalen Links; die relativen Indexlinks oben öffnen die gesicherten Artefakte. Dateihashes stehen im Release-Manifest.
