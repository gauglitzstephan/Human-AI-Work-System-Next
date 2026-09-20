# Bestehender Stand — 20.09.2026

## Prüfumfang und Autorität

Der Auftrag ist Entwicklung eines Kandidaten, nicht dessen Aktivierung. Geprüft wurden der bereitgestellte Work Contract, die zugänglichen Library-Artefakte, der aktuelle persönliche Skill-Checkout und die einschlägigen privaten Repositories. `evidence/baseline-manifest.json` hält Pfade, Größen und SHA-256 der lokal gesicherten Quellen fest. Die folgenden Aussagen unterscheiden aktuellen Quellstand, historischen Audit und tatsächlich beobachtete Nutzung.

| Quelle | Feststellung | Belastbarkeit / Konsequenz |
|---|---|---|
| `intent_v1.md` | Universaltemplate mit umfangreichen Metadaten und etwa 17 Inhaltsbereichen; umfasst Outcome, Evidenz, Alternativen und Unknowns, aber auch Requirements Elasticity, Delegation, Holdouts, Telemetrie und Downstream-Verknüpfung. | Quellartefakt tatsächlich gelesen. Semantik erhalten, nicht als Pflichtformular übernehmen. |
| `intent_v1(1).md`, aktueller persönlicher Capture-Fall | Rund 30 KB, unterscheidet Erfassen, Wiederfinden und verlässliches Zurückkommen; hält Lösungswahl offen. Keine dokumentierte finale Akzeptanz. | Echtes Arbeitsartefakt; Länge und offene Stellen beobachtbar. Daraus folgt kein gemessener UX-Misserfolg und keine bewiesene Ursache. |
| Framing-v0.1.4-Audit und Audit Evidence, aktualisiert 18.09.2026 | Abschließendes Urteil **A—KEEP**; ursprünglicher AC4-Trace nachgereicht. Frühere Assurance-Lücke ist kein nachgewiesener Architekturfehler. | Historischer Snapshot mit Quellhashes und Auszügen. Vollständiger aktuell aktivierter Framing-Quellstand in dieser Runtime nicht verfügbar; keine Gleichsetzung mit heutiger Installation. |
| Intent Formation Runtime v2 reference | Reicher Inquiry State, Trennung von Ziel/Outcome/Mittel, vier Autoritätsebenen, lokale Präferenzarbeit, Revisions- und Kontinuitätsregeln. | Explizit isolierter Referenzkandidat für Project Chat; Paket enthält keine ausgeführten Verhaltensnachweise. Nicht als produktiv bewährt darstellen. |
| Human-AI-Work-System-Next: README, CURRENT, skills/REGISTRY und Baum | Aktuelle kanonische Unterstützung auf decision-analysis, evaluate-work-product, system-development reduziert; alte Work Formation archiviert. | Repository-Autorität ist nicht Beleg für installierten Runtime-Stand. Keine Rückpromotion archivierter Formation durch diesen Auftrag. |
| Persönlicher Skill-Checkout | Anwendungen, capital-curator und prepare-chatgpt-prompts sichtbar; Framing nicht im zugänglichen Checkout. Fremde unversionierte Änderungen vorhanden. | Nicht verändert. Fehlende lokale Sichtbarkeit beweist keine generelle Deinstallation. |
| Work-Foundation; AI-Native-Operating-System; AI-native-Operating-Model | Kontext/Architekturvorarbeiten gesichtet, keine neuere kanonische Intent-Formation-Implementierung nachgewiesen. | Keine pauschale Vollständigkeitsbehauptung über alle privaten Speicher. |

## Funktionen, die erhalten werden müssen

1. **Current Working Model vor Konvergenz:** Problemverständnis, Gegenhypothesen und nächste erkenntnisreiche Intervention bilden; nicht nur ein Dokument ausfüllen.
2. **Epistemische Trennung:** Quellenaussage, Beobachtung, Interpretation, Annahme, unbekannte Tatsache und menschliche Entscheidung haben verschiedene Autorität.
3. **Menschliche Erfahrung und Werte:** Zugänglichen Kontext zuerst erschließen; Erleben, Taste und Wertkonflikte nicht aus allgemeinen Modellen erfinden.
4. **Lokale Reparatur:** Korrektur invalidiert abhängige Schlussfolgerungen und den betroffenen Artefaktteil, nicht sämtliche gültige Arbeit.
5. **Proportionale Untersuchung:** Die nächste Intervention muss materiell etwas ändern können; keine künstliche Unsicherheit bei klaren kleinen Aufgaben.
6. **Unabhängige Stop-Ausgänge:** Qualifizieren, untersuchen, menschliches Judgment, zurückstellen und beenden sind echte Ergebnisse. Bereits investierter Aufwand begründet kein Weiterarbeiten.
7. **Qualifizierte Arbeit ist nicht automatisch lösungsreif:** Formation-Readiness, menschliche Akzeptanz und Ausführungsbefugnis bleiben getrennt.

Diese Funktionen haben positive fachliche Begründung und teilweise historische Auditbelege. Für die Übertragung auf den neuen Kandidaten werden neue Läufe benötigt; die Auditbewertung wird nicht übertragen.

## Ändern, begrenzen oder nicht übernehmen

| Mechanismus | Bewertung | Behandlung im Kandidaten |
|---|---|---|
| Vollständiges intent/v1 für jeden Fall | Artefaktzwang, keine notwendige fachliche Invariante | Gemeinsame Semantik mit kurzer und erweiterter Lesefläche; optionale Inhalte nur materialitätsbezogen. |
| „Präferenzen dürfen bei besserer Evidenz überstimmt werden“ | Gefährliche Autoritätsmehrdeutigkeit | AI darf faktische Grundlage challengen; Wertentscheidung bleibt beim Menschen, auch bei gegenteiliger AI-Empfehlung. |
| Vollständige Metrik-/Holdout-/Telemetrie-/Recovery-Verträge | Teils nützlich, teils bereits Specification/Delivery | Beabsichtigte Wirkung und erkennbare Wirkung behalten; Messinstrumentierung und Feature-Abnahme downstream parken. |
| Breites allgemeines Framing | Anderer, weiter gültiger Aufgabenbereich | Unverändert lassen. Kein Ersatz durch einen engeren Intent-Skill. Pro Auftrag genau ein Formation-Verantwortlicher. |
| Fester großer Inquiry State v2 | Schutz gegen Gedächtnisverlust, aber potenzieller Pflegeaufwand | Nur entscheidungsrelevante State-Elemente persistieren; gesicherte Erkenntnisse, Revisionsgrund, offene Frage und Fortsetzung. |
| Pauschales Verbot jeder realen Lösungsalternative vor Abschluss | Verhindert frühe Architekturwahl, kann aber Reuse-Prüfung verhindern | Existenz und mögliche Bedarfserfüllung prüfen; keine Auswahl oder Gestaltung einer Lösung daraus ableiten. |
| Bisherige UX-/Wirksamkeitsannahmen | Teilweise plausibel, aber nicht durch kontrollierte Nutzertests belegt | Neue Verhaltensproben und aufgabenbezogene Artefaktprüfung; keine behauptete Human-UX-Validierung. |

## Beobachtung vs Hypothese

**Beobachtet:** großer realer intent/v1-Arbeitsstand, zahlreiche nachgelagerte Felder im Template, abschließendes KEEP im Framing-Audit, fehlende Verhaltensläufe im v2-Referenzpaket. **Nicht nachgewiesen:** dass v0.1.4 generell zu viele Fragen stellt, dass der Nutzer das lange Artefakt nicht versteht, dass neue Modularität von sich aus besser funktioniert oder dass ein Skill harte Runtime-Gates erzwingt.

Die Baseline-Evaluation nutzt deshalb das tatsächlich vorhandene intent/v1-Template und den v2-Carrier in klar benannten Bedingungen. Sie simuliert nicht den unbekannten vollständigen aktiven Framing-Skill. Eine Ablösung von Framing wäre ohne diese Quelle und neue Vergleichsevidenz unzulässig.
