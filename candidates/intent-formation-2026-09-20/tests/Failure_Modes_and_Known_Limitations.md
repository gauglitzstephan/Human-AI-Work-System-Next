# Failure Modes and Known Limitations

Dies ist ein Verhaltenskatalog, keine Behauptung universeller Absicherung. Laufdateien unter `runs/`, getrennte unabhängige Review unter `runs/review/`. „Nicht beobachtet“ bedeutet nicht „unmöglich“.

| Failure Mode | Konkrete Probe / Befund |
|---|---|
| Paraphrase-only | D02 Quellenchallenge, D05 Ticketzeit vs Arbeitsverlust. Frühes D01 blieb zu nahe am groben Input; gezielte Reparatur R1/R2. |
| Interrogation / Fragebogen | D04/D03/D09 ohne Fragen; D06 eine zusammenhängende Wertfrage; kein Pflichtformular beobachtet. |
| Premature Solution Lock-in | D02 SaaS-Framing bleibt Vorschlag; D05 kein Chatbotbeschluss; D09 technische Ideen nicht zu Constraints aufgewertet. |
| Premature Specification | Kandidatenläufe ohne Feature-/Architekturentwurf; B01v1 erzeugt dagegen ungefragte Abnahme-/Governance-Inhalte. |
| Research Avoidance | D02 führt Primärquellenprüfung aus und benennt Zugangslücken. Nicht alle möglichen Domänen untersucht. |
| Research Overkill | Keine externe Recherche bei D04; D02 begrenzter rechtlicher Rahmen mit konkreter Konsequenz. Reale Zeitkosten nicht instrumentiert. |
| False Certainty | D05 Counts nicht Arbeitsverlust; D08 kein erfundener 20/20-Retest. D01/R01 zu endgültiges Qualification-Urteil beobachtet und repariert. |
| Context Amnesia | D02H nur aus State/Intent orientiert; D01H Fortsetzung aus Dateien, keine Nutzerrückrekonstruktion. |
| Context Overreach | D01H benennt ausdrücklich übernommene Quellen statt behaupteter Originalprüfung. Breite personalisierte Kontextsuche nicht umfassend getestet. |
| Human-Judgment Substitution | D06 offene Präferenz nicht erfunden; D07 Messepriorität offen. Synthetische Wertantworten, keine echte Präferenzmessung. |
| Infinite Discovery | D08 beendet Neubau nach neuer Evidenz; D04 direkte Konvergenz. Keine Monate dauernde reale Nutzung geprüft. |
| Template Filling | D04 151 Wörter, keine leeren Abschnitte. B01v1 knapp 3.000 Wörter trotz gleicher Raw-Information. |
| Intent Bloat | D03/D05 teils ausführlicher als nötig; D01H reiche Reparaturhistorie. Keine Behauptung optimaler Textlänge. |
| State Bloat | D01-State wiederholt Teile stabiler Bedeutung; im Test noch lesbar, aber künftiger Verdichtungspunkt. Keine eigene Datenbank aufgebaut. |
| Lossy Compression | D01H behält Zusage/Idee und alte vs neue Akzeptanz; D10 erkennt offene Punkte. Kein automatischer Vollständigkeitsbeweis. |
| Downstream Leakage | D09 semantisch geprüft, keine Requirements/Plan. Datei-Namenprüfung allein wäre unzureichend. |
| Failure to Stop | D08 respektiert explizit keine neue Formation; alle Kandidaten enden am Intent oder einem begründeten Blocker. |
| Reference Blindness | D02 ändert Problemverständnis aufgrund Primärquellen; Systemreferenzen vor Architektur ausgewertet. |
| Missed Opportunity | D02 Alternativen der Nachweis-/Organisationslücke, D07 Reuse und Optionsvermerk erhalten. Vollständigkeit des Opportunity-Raums nicht beweisbar. |
| False Constraint Acceptance | D09 bestehende Plattform tatsächliche menschliche Grenze, React/OCR nur Ideen. D02 automatische Fristen fachlich challenged. |
| Cognitive Overload | Kein belastbarer menschlicher Lastwert. Proxies zeigen Baseline-Formlast; komplexe Kandidaten teilweise lang. |
| Orientation Loss | D02H kann Stand/Entscheidung/Evidenzlücken selbst rekonstruieren; Antwort mit 432 Wörtern eher ausführlich. |
| Over-questioning | Kandidat klare Fälle null unnötige Fragen. A01 stellt zwei Messefragen mit unklarer Reihenfolge, D07 eine. |
| Opaque Autonomy | D05 Antwort formuliert vorgeschlagenen Whole-Problem-Rahmen bestimmter als Artefakt; Empfehlung im Chat künftig konsequent als solche lesen. |
| Ceremonial Approval | Candidate verlangt kein Freigaberitual für jede Formulierung. B01v1 fordert Accept trotz eigener Nichtblocker-Einschätzung. |
| Artifact Unscannability | D10 kann Aufgaben mit Fundstellen lösen; komplexe Dokumente länger. Keine gemessene menschliche Suchzeit. |
| Machine-first Artifact | Candidate natürliche Abschnitte mit kurzer Statuszeile; v1 umfangreiche YAML-/Tabellenstruktur. |
| Hidden Human-Judgment Substitution | R0 kleine AI-Leitplanken teils erst im State eindeutig zugeordnet. D06 Kontraste können dennoch ankern; explizite Zurückweisbarkeit mindert, eliminiert das nicht. |
| Poor Re-entry | D10 liest nur drei Intents, D02H nur State/Intent. Tatsächlicher zeitlicher Abstand simuliert durch frischen Kontext. |
| Acceptance conflation | B04v1 verwechselt Sachbeschluss mit Dokumentannahme; Kandidat D04/D01H trennt beides. |
| Status subject ambiguity | D08 `dropped` gilt laut sichtbarer Statuszeile nur dem Neubau; bloße Enum-Auswertung könnte dennoch den gültigen Zweck schließen. Status immer mit seinem Bezugsgegenstand lesen. |
| Historical-link drift | Frühere Antworten zeigen mit `intent.md` auf aktuellen Stand. Archivversionen sichern Inhalt, machen alte Links aber nicht automatisch unveränderlich. |

## Verbleibende Aussagegrenzen

1. Die Läufe sind instruktionsbasierte Agent-Ausführungen in der verfügbaren Work-Runtime. Keine Installation, keine implizite Skill-Discovery, kein UI-Nutzertest und keine produktive Downstream-Ausführung.
2. Thread-Kontexte waren frisch, das Dateisystem gemeinsam. Lesegrenzen waren instruierte Isolation, keine technische Sicherheitsbarriere. Keine beobachtete Nutzung anderer Testausgaben; vollständige native Tool-Traces wurden nicht exportiert.
3. Kleine Fallzahl, gleiche Modellfamilie, keine Randomisierung oder statistische Effektschätzung. Wortzahlen sind exakt reproduzierbare Proxies, keine gemessene kognitive Last. Ein Lauf pro Bedingung begründet keine allgemeine Architekturüberlegenheit.
4. T15 ist ein aufgabenbasierter AI-Reviewer-Proxy. Kein Mensch wurde als Reviewer ausgegeben. Menschliche Verständlichkeit, Präferenzwirkung und Owner-Akzeptanz bleiben zu bestätigen.
5. Die vollständige aktuell aktive Framing-v0.1.4-Implementierung war nicht verfügbar. Audit, gesicherte Ausschnitte und vorhandene Templates erlauben Erhaltsempfehlung, aber keinen vollständigen direkten A/B-Test dieses Skills.
6. Analysten-Terminologie und gesperrte Norm-/Verlagstexte bleiben begrenzte Quellenbereiche. Kein Standardkonsens, keine formale Compliance und keine individuelle Rechtsprüfung behauptet.
7. Der finale Skill wurde nach einem beobachteten Qualification-Defizit schmal geändert. Betroffene Fälle wurden neu geprüft; die gesamte ursprüngliche Suite wurde nicht unnötig wiederholt. Ergebnisse früherer Revisionen bleiben als solche gekennzeichnet.

Empfehlung: Kandidat zur fachlichen Abnahme bereitstellen, zunächst menschlichen Ownability-Review an den konkreten Beispielen, anschließend nur bei gesondertem Auftrag begrenzte Installation. Kein Ersatz bewährter Framing-Funktion aufgrund dieser Evidenz.
