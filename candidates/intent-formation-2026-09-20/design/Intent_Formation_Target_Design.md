# Target Design

## Ziel und kleinste tragfähige Einheit

Ein dedizierter Einstieg `form-intent`, ein gemeinsamer Formation-Kern, vier nur bedarfsweise geladene Referenzen und zwei optionale Leseflächen. Der Skill formt professionelle Bedeutung und endet dort. Kein allgemeines Work OS, kein verpflichtender Router, kein technischer Zustandsautomat. Der Kandidat verändert keinen vorhandenen Skill.

## Arbeitslogik

1. **Zugänglichen Kontext nutzen:** Input, vorhandene Evidenz und bei Fortsetzung Dateien lesen. Ursprung, Interpretation und Autorität auseinanderhalten.
2. **Aufmerksamkeit proportional prüfen:** Bei klaren kleinen Anliegen direkt arbeiten. Bei Konkurrenz, Duplikaten, erheblichem Aufwand oder fraglichem Wert Auswahlgrund prüfen; ggf. zurückstellen oder beenden.
3. **Nächsten erkenntnisreichen Schritt wählen:** Direct Formation, Clarification und Discovery sind wechselbare Arbeitslagen, keine Phasen. Recherche löst sachliche Fragen; persönliche Erfahrung und Wertentscheidungen kommen vom Menschen.
4. **Working Model verändern:** Plausible Gegenhypothese, Whole-Problem-Prüfung oder Referenzlinse einsetzen, sofern materiell. Neue Evidenz korrigiert die aktuelle Deutung und abhängige Aussagen.
5. **Konvergieren:** Nicht Vollständigkeit, sondern stabile Bedeutung und geklärte materiale Entscheidungen bestimmen Readiness. Aufwand rechtfertigt sich durch erwarteten Erkenntniswert.
6. **Intent rendern und speichern:** Nur dauerhafte Bedeutung; klare Statuszeile, erkennbare Entscheidungen/Unknowns. Tatsächlich geschriebene Version prüfen. Stoppen.

## Verantwortung

AI übernimmt Erschließung, Synthese, Recherche, Challenge, Dokumentation und begründete Readiness-Einschätzung. Der Mensch besitzt Zweck, Werte, Taste, Prioritäten und Commitments. AI darf eine Empfehlung aussprechen und einen faktischen Widerspruch zeigen, aber keinen menschlichen Willen aus unbeantworteten Vorschlägen konstruieren. Qualifikation ersetzt keine Akzeptanz; Akzeptanz ersetzt keine Ausführungsbefugnis.

## Zustände und Abbruch

`qualified`, `needs-investigation`, `needs-human-judgment`, `deferred`, `dropped` bezeichnen unterschiedliche entscheidungsrelevante Ausgänge. Ein laufender Entwurf ist als vorläufig gekennzeichnet. Arbeitslagen bleiben interne Prozesswahl; sie erzeugen keine zusätzlichen Artefaktzustände. „Reuse“ ist eine inhaltliche Entscheidung, kein notwendiger sechster Status: Der Build-Intent kann beendet werden, während der zugrunde liegende Zweck bestehen bleibt.

## Proportionalität und Fehlerbehandlung

Kein Pflichtinterview, kein generischer Risikoabschnitt, keine allgemeinen Business Cases. Mehr Tiefe entsteht durch Unsicherheit, Folgen, Irreversibilität und Außenwirkung. Bei unzugänglicher Quelle bleibt die genaue Lücke sichtbar. Bei Korrektur lokal reparieren und veraltete Ableitungen entfernen. Bei Unterbrechung kompakte Orientierung; bei fehlender Dateiverfügbarkeit ehrliche Persistenzgrenze. Methodenregeln sind instruktionsbasiert und müssen sich in tatsächlichen Läufen bewähren.

## Nicht gewählt

Kein Schema-Validator für semantische Qualification oder Acceptance: Er würde falsche Sicherheit erzeugen. Kein eigener Persistenzdienst, automatische Erinnerung oder Installationsskript. Die vorhandene Runtime stellt Datei-/Recherchewerkzeuge; ihre tatsächliche Verfügbarkeit bestimmt, was ausgeführt werden kann. Strukturelle Skill-Validierung bleibt separat von Verhaltensqualität.
