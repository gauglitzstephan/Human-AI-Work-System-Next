# Test Plan — 20.09.2026

## Methode

Reale Ausführung in frischen verfügbaren Agent-Kontexten, jeweils mit Skill und realistischem Raw Input. Keine Diagnosen, Sollantworten oder Bewertungsrubrik im Arbeitsauftrag. Isolierte Laufordner außerhalb des Kandidaten; keine Produktionsänderungen und keine Nachrichten an Dritte. Jeder Lauf darf zugängliche Werkzeuge für die Aufgabe nutzen. Antworten für Fortsetzungsfälle sind vorab definierte **synthetische Nutzer-Fixtures**, keine Aussagen oder Akzeptanz von Stephan. Der reale Capture-Input informiert D01; konkrete Episoden sind ausdrücklich Szenariodaten.

Feste Invarianten: keine ungefragte Spec/Plan/Implementierung; kein erfundenes Human Judgment oder Acceptance; keine verdeckte Umdeutung von Evidenz in Nutzerwerte; materiale Blocker nicht als erledigt deklarieren. Ergebnisqualität, Formation, Interaktion, Artefakt-UX und Downstream Utility getrennt bewerten, ohne Gesamtscore. Negative Beobachtungen bleiben erhalten; Änderungen am Kandidaten erhalten eine neue Revision und gezielte Wiederholungen.

## Fälle und Contract-Testklassen

| Fall | Aufgabe | Abdeckung |
|---|---|---|
| D01 | Persönliches Capture/Open-Items-Problem; konkrete Episode nach Rückfrage; Korrektur; Handoff | T01, T07, T11, T12, T13 |
| D02 | DGUV/BetrSichV-Produktidee; echte Quellenrecherche und Verantwortungsgrenzen | T02, T09, T10, T21, T22 |
| D03 | Nichtsoftware-Entscheidungsgrundlage mit Zeitfenster | T03, T23 |
| D04 | Vollständig beschriebener kleiner Defekt/Änderungswunsch | T04, T11, T22 (Vergleich niedriges Risiko) |
| D05 | Eng gefasster Team-Prozess mit zugänglichen Ursachenbelegen | T05, T09, T10, T21 |
| D06 | Ungebildete Präferenz mit echtem Zielkonflikt, anschließender Auswahl | T06, T24 |
| D07 | Gemischte Signale mit Verpflichtung, Duplikat, Risiko, Option und niedriger Priorität | T17, T18, T19, T20 |
| D08 | Nach intensiver Formation neue Evidenz für Reuse/Stop | T25, T19 |
| D09 | Intent-Auftrag mit mitgelieferten technischen Wünschen und Sog zum Plan | T08 |
| D10 | Frischer Leser erhält nur fertiges Intent; konkrete Such-/Korrektur-/Handoff-Aufgaben | T14, T15 (Proxy), T16 |
| A01/A02 | D07 und D04 mit eigenständigem Selection-Router und demselben Formation-Kern | T26 |

T12 wird zusätzlich durch Wiedereinstieg in einen Discovery-Stand (D02/D05) geprüft. D10 ist ein **AI-Reviewer-Proxy** für aufgabenbasierte Ownability. Ein menschlicher Reviewer wurde nicht erfunden; die Human-UX-Aussage bleibt begrenzt.

## Vergleichsbedingungen

- Candidate: tatsächliche aktuelle Skill-Dateien, Checksum/Commit dokumentiert.
- Raw baseline: gleicher Raw Input, direkter Auftrag zu `intent.md`, ohne zusätzlichen Formation-Skill.
- intent/v1 baseline: gleiches Input plus tatsächlich vorhandenes aktuelles Template; dessen Form nicht nachträglich zugunsten des Kandidaten verändern.
- Reference-near: v2-Runtime-Carrier auf dem Capture-Fall; keine Behauptung, damit den nicht verfügbaren vollständigen aktiven Framing-v0.1.4-Skill zu reproduzieren.
- Architekturvergleich: gleicher Input, verschiedene Einstiegsschicht, gemeinsamer Formation-Kern.

Mindestens Capture und klarer Änderungsfall in Raw/v1 vergleichen. Bereits vorhandene reale Artefakte ergänzen neue Laufbelege, ersetzen sie nicht.

## Beobachtung und Auswertung

Pro Lauf Input, geladene Bedingung, Agent-ID, Folgeinputs, Antworttext, gespeicherte Dateien und relevante Werkzeug-/Quellenbelege sichern. Zählen: gestellte Fragen, erkennbare redundante Fragen, vom Menschen verlangte Rekonstruktion zugänglicher Information, explizite Koordinationsschritte und Artefaktwörter. Zählungen sind Proxies ohne wissenschaftlich validierte Schwellenwerte. Latency/Tokenkosten sind ohne Telemetrie nicht behauptbar.

Qualitativ prüfen: fachlicher Beitrag gegenüber Raw Input, erhaltene Alternativen, Quellen-/Autoritätstrennung, letzte Korrektur in beiden Dateien, Status/Acceptance und begründete Stop-Entscheidung. Boundary-Prüfung ist semantisch, nicht nur Dateinamenprüfung. Artefaktprüfung nutzt Leseraufgaben: finde Zweck, Outcome, gesetzte Grenzen, eine AI-Deutung, offene Fakten/Judgments, Status und Reopen-Bedingung; ändere einen materiellen Punkt und benenne abhängige Stellen.

## Abbruch und Grenzen

Kein langwieriger nutzloser Testlauf; isolierte Ausgaben, keine externen Mutationen. Bei unzugänglicher Quelle den konkreten Befund dokumentieren. Automatische Skill-Auswahl, tatsächliche Installation, UI-Klickpfade, lange reale Zeitabstände und menschliche Empfindungen werden durch diese Läufe nicht bewiesen. Keine Installation ohne separaten Auftrag.
