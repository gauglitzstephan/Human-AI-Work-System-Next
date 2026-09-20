# AI-Native Intent Formation — Abschlussbericht

## Aktueller Reviewstand — 20.09.2026

**Die bisherige Abnahmeempfehlung ist ausgesetzt. Die Übergabefähigkeit des Intents innerhalb der gesamten Arbeitskette muss am ausgeführten Beispiel fachlich nachvollziehbar bewertet werden.**

Die Nutzerkritik verlangt keine vollständige Discovery oder pauschale Wirtschaftlichkeitsprüfung vor jedem Intent. Discovery und Exploration können in mehreren Teilen der Arbeitskette erforderlich sein. Maßgeblich ist die im Work Contract geforderte semantische Grenze: Was muss für Zweck, Problem/Opportunity, beabsichtigte Wirkung und wesentliche Grenzen bereits geklärt sein, und welche Fragen gehören begründet in Specification, Planning oder spätere Evaluation?

R21 klärt anhand einer synthetischen Alltagsepisode, dass Erfassen als funktionierend vorausgesetzt wird und das Wiederaufgreifen von Zusagen das Anliegen ist. Der Lauf erklärt danach die Formation für abgeschlossen und Recherche für unnötig. Das allein beweist weder ausreichende professionelle Qualifikation noch die Notwendigkeit zusätzlicher externer Recherche. Die bisherige Evaluation begründet nicht ausreichend, warum die verbleibende Unschärfe — insbesondere welche realen Verpflichtungen und welche Bedeutung von „rechtzeitig“ gemeint sind — für diesen Übergang vertretbar ist. Die einmalige Rückfrage belegt eine Verbesserung der Klärung, aber noch keine vollständige Behebung dieses Qualitätsproblems.

Referenzwissen und Economics müssen dort beitragen, wo sie die jeweilige Entscheidung verbessern. Ihre pauschale Vorverlagerung in Intent Formation wäre ebenfalls eine Fehlinterpretation des Auftrags. Die Recherche zur Gestaltung des Skills ersetzt keinen Nachweis seines angemessenen Verhaltens im einzelnen Fall.

Der Kandidat ist durch diese Reviewkorrektur nicht repariert oder erneut abgenommen. Bestehende Recherche, Artefakte und Laufbelege bleiben erhalten. Die folgenden Aussagen dokumentieren den ursprünglichen Abschlussstand; insbesondere dessen allgemeine Fertig- und Abnahmeaussagen gelten nicht als aktuelles Urteil.

---

## Ursprünglicher Abschlussstand

20.09.2026 · Kandidat R2 · **Nicht installiert, nicht gemergt**

**Ergebnis:** Eine ausführbare, installierbare Intent-Formation-Capability samt Recherche, Methodik, Templates, tatsächlichen Verhaltenstests und Installations-/Rollback-Handover liegt vor. Sie endet beim qualifizierten Intent oder einem begründeten offenen/abgebrochenen Zustand. Die autorisierten Entwicklungsarbeiten sind ausgeführt. Eine echte menschliche Ownability-Abnahme und produktive Aktivierung sind noch nicht erfolgt.

**Empfehlung:** Den Kandidaten separat fachlich abnehmen und an den bereitgestellten Beispielen menschlich prüfen. Bewährtes Framing unverändert erhalten. Installation erst gesondert beauftragen; der Work Contract schließt sie ohne eigene Autorisierung ausdrücklich aus.

[Vollständiger Kandidat und Dateiverzeichnis](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/tree/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20) · [Evaluation](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/tests/Intent_Formation_Evaluation.md) · [Abnahmekriterien](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/tests/Acceptance_Crosswalk.md)

## Was untersucht wurde

40 Referenzen wurden nach Mechanismus, Zweck, Ein-/Ausgabe, menschlicher und AI-Rolle, Evidenzstatus sowie Intent-/Spec-Grenze eingeordnet. Dazu gehören aktuelle offizielle OpenAI-/Anthropic-Praxis, GitHub Spec Kit, Product Discovery, Needs Engineering, NASA, Human–AI Interaction, Entscheidungsqualität und unterschiedliche Verwendungen von „Intent Engineering“. Gesperrte Norm-/Verlagstexte und die begrenzte institutionelle Analystenbasis sind als Quellenlücken ausgewiesen. Eine wiederholte Bezeichnung wurde nicht zum Standard erklärt.

Die Reference Map wurde vor der Zielarchitektur versioniert. Tatsächlich geprüft wurden intent/v1, der vorhandene persönliche Capture-Arbeitsstand, die Framing-Audits, der v2-Referenzcarrier, der sichtbare persönliche Skill-Stand und einschlägige Repository-Quellen. Der abgeschlossene Framing-v0.1.4-Audit empfiehlt **KEEP**. Der vollständige aktuell aktive Framing-Code war nicht zugänglich; ein vollständiger direkter A/B-Test dieses Skills wird deshalb nicht behauptet.

## Übernommen, angepasst und verworfen

| Entscheidung | Mechanismus und Grund |
|---|---|
| Übernommen | Current Working Model, alternative Problemdeutungen, lokale Korrektur, Evidenz-/Autoritätstrennung und legitimes Defer/Drop aus gültigen Vorarbeiten. |
| Übernommen | Eigenständige Prüfung mit optionalem Übergang zu späterer Arbeit, wie bei [Spec Kit Assessment](https://github.github.io/spec-kit/guides/assessment.html). Der Kandidat startet diesen Übergang nicht automatisch. |
| Angepasst | Problem-/Whole-Problem- und Nichtbauen-Prüfung aus [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works): materialitätsbezogen, ohne eine komplette Discovery-Phase für jede Kleinigkeit. |
| Angepasst | Kleine Skill-Einstiege und bedarfsweise Referenzen aus der [offiziellen Skill-Dokumentation](https://learn.chatgpt.com/docs/build-skills): ein Kern mit optionalen Methoden, keine erfundene Orchestrierungsruntime. |
| Verworfen | Universalformular mit nachgelagerten Abnahme-, Test-, Telemetrie- und Planungsfeldern als Pflichtinhalt jedes Intents. Ebenso automatische Specification, Zustimmung aus Schweigen und Überstimmen menschlicher Werte durch AI. |

## Gebaute Capability

`form-intent` übernimmt rohe Ideen, Probleme, Opportunities oder Analyse-/Entscheidungsbedarfe. Ein kleiner Entry Check berücksichtigt Relevanz, Timing, konkurrierende Pflichten, weiteren Aufwand, Risiko, Reuse und Nichtstun. Danach wählt der Skill direkte Formation, gezielte Klärung oder Discovery passend zum Fall.

Arbeitsstand und akzeptierbares Artefakt sind getrennt: `formation.md` trägt Fortsetzung und aktuelle Inquiry; `intent.md` trägt dauerhafte Bedeutung. Qualifikation, menschliche Annahme und Ausführungsbefugnis bleiben verschiedene Dinge. Persönliche Präferenzen, Werte und Commitments werden nicht von AI ersetzt.

Das installierbare Paket enthält genau acht Dateien:

- `SKILL.md` und `agents/openai.yaml`
- `references/selection.md`, `references/inquiry.md`, `references/state-and-artifact.md`, `references/boundary.md`
- `assets/intent-short.md` und `assets/intent-expanded.md`

Forschung, Design, Test-Router und Testdaten gehören nicht zur aktiven Installation. Alle geforderten Research-/Design-Dokumente sind im [Dateiverzeichnis](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/README.md) einzeln verlinkt. Das Gesamtpaket umfasst 149 überprüfte Dateien einschließlich Evidenz und Originalausgaben.

## Testergebnis

Alle 26 Prüfklassen sind mit konkreten Läufen ausgewertet; T15 wurde als aufgabenbezogener AI-Reviewer-Proxy ausgeführt, **nicht als menschlicher Nutzertest**. Fachqualität, Formation, Interaction UX, Artifact UX und Downstream Utility werden getrennt berichtet, ohne Gesamtscore.

| Befund | Beobachtete Evidenz |
|---|---|
| Substanzieller fachlicher Beitrag | DGUV-Idee anhand von Primärquellen reframed; Helpdesk-Fall trennt Antwortzeit, Ticketdauer und tatsächlichen Arbeitsverlust. |
| Proportionalität | Vollständig beschriebene Kontaktkorrektur ohne Rückfrage; unklare Erfahrung bzw. Werte mit gezielter Frage; folgenreiche Idee bleibt begründet offen. |
| Korrektur und Kontinuität | Frischer Handoff entfernt absichtlich falsche AI-Ableitung, repariert abhängige Aussagen und hält alte Akzeptanz nur historisch fest. |
| Stop | Eigener FAQ-Assistent wird nach neuer Reuse-Evidenz beendet, trotz bereits investierter Interviews und Recherche. Kein Ersatzprojekt eröffnet. |
| Boundary | Kandidatenläufe erzeugen keine ungefragte Specification, Planung oder Implementierung. Technische Wunschliste wird nicht zu verbindlichen Vorgaben. |
| Beobachteter Fehler und Reparatur | Früher Capture-Lauf qualifiziert zu pauschal. Erste abstrakte Nachschärfung wirkungslos; zweite operative Regel führt zu einer materialen Frage und anschließend qualifiziertem Intent. Klarer Kontrollfall bleibt direkt. |

Im identischen ersten Capture-Fall entstanden mit intent/v1 2.993 Wörter, mit direkter Raw-Baseline 324 und mit dem ursprünglichen Kandidaten 439. Mehr Struktur lieferte keinen entsprechenden Erkenntnisgewinn; v1 ergänzte ungefragte Abnahme-/Planungslogik. Im kleinen Korrekturfall leitete v1 fälschlich eine Intent-Annahme aus dem Sachbeschluss ab. Der Kandidat vermied diese Verwechslung. Die Raw-Baseline war beim einfachen Fall am kürzesten und inhaltlich brauchbar.

Der v2-Referenzansatz stellte eine wertvolle Bedeutungsfrage und erzeugte nach Klärung ebenfalls ein starkes Intent. **Eine allgemeine Überlegenheit des Kandidaten gegenüber v2 ist nicht belegt.** Die zwei tatsächlich geprüften Skill-Architekturen waren im klaren Fall ähnlich; im Mischfall brachte der separate Router zusätzliche Nebenformation und eine unklarere Fragefolge. Deshalb bleibt ein Einstieg mit optionalen Methoden die begründete Auswahl für diesen Kandidaten.

## Erhalt und Grenzen

Framing v0.1.4, aktuelle kanonische Support-Skills und `prepare-chatgpt-prompts` bleiben unverändert. Bestehende intent/v1-Artefakte bleiben erhalten. Nur seine Rolle als universelles Pflichtformular sollte nach einer späteren Annahme des Kandidaten deprecated werden; keine automatische Migration.

Offen bleiben reale menschliche Verständlichkeit und Belastung, langfristige Persistenz, automatische Skill-Auswahl und Verhalten nach Installation. Die Stichprobe ist klein, die Kontexte waren frisch, aber das Dateisystem gemeinsam. Manche komplexen Artefakte und historischen Arbeitsstände könnten knapper sein. Alte Antwortlinks zeigen auf aktuelle Dateien; Archivfassungen sichern den früheren Inhalt. Status wie `dropped` muss mit Bezugsgegenstand gelesen werden, damit beendeter Neubau und weiterhin gültiger Bedarf nicht verwechselt werden.

Der Kandidat und seine 149 Dateien wurden gegen den veröffentlichten Kandidatenstand bytegenau über Git-Blob-Hashes verifiziert. Der kanonische Hauptstand blieb unverändert. Keine Installation, kein Merge, keine Ersetzung bestehender Artefakte.

## Konkrete nächste menschliche Entscheidung

Zur Abnahme eignet sich der [finale persönliche Intent](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/tests/runs/R21/intent.md): Ist der Zweck nachvollziehbar, sind gesetzte Punkte erkennbar und lässt sich eine Grenze gezielt korrigieren? Als zweites Beispiel dient der [nichttechnische Entscheidungs-Intent](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/tests/runs/D03/intent.md). Die Szenarien sind Testdaten, keine behaupteten persönlichen Entscheidungen des Auftraggebers.

[Migration und Kompatibilität](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/handover/Migration_and_Compatibility.md) · [Installationsanleitung](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/handover/Installation.md) · [Rollback](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/c2074ffdd215ac8c07deecd28964049885fbcd40/candidates/intent-formation-2026-09-20/handover/Rollback.md)
