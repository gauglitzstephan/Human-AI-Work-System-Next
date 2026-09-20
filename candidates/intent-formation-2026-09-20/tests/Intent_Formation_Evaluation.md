# Intent Formation Evaluation

**Urteil:** Der Kandidat ist als eigenständige, instruktionsbasierte Intent-Formation-Capability technisch und verhaltensbezogen tragfähig für eine begrenzte menschliche Abnahme. Er ist **nicht installiert** und kein nachgewiesen universell zuverlässiger Ersatz für bestehendes Framing. Ein beobachteter früher Qualification-Fehler wurde nach einem erfolglosen ersten Reparaturversuch gezielt behoben. Menschliche UX-/Ownability-Evidenz bleibt offen; der verfügbare aufgabenbezogene AI-Proxy ist ausdrücklich begrenzt.

## Evidenz und Verfahren

Reference Map und Bestandsanalyse wurden lokal vor Architektur committen (`f3ecf5e`). Der ursprüngliche ausführbare Kern liegt in `c9189e0`, die erste Nachschärfung in `e63653c`, die operative Reparatur in `c67efb7`. Exakte Paketdateien/Hashes, Laufzuordnung und Umfangsproxies liegen unter `evidence/`. Die Läufe wurden real in frischen Agent-Kontexten ausgeführt, bei Fortsetzung im selben oder ausdrücklich frischen Kontext. Modell wurde nicht überschrieben. Es gab keine Produktionsänderung durch die Szenarien.

Die Fälle sind realistisch ausgearbeitete Fixtures. D01 ist durch den vorhandenen persönlichen Real-Use-Fall motiviert; Episoden, Zahlen, Präferenzantworten, Annahme und Suchbefunde in den Tests sind **synthetisch**. Keine davon ist eine Entscheidung Stephans über die Capability. Die unabhängige Review in `runs/review/independent-review.md` prüfte die ursprünglichen Ausgaben ohne Eltern-Designberichte. D10 prüfte drei isolierte Intents ohne Entstehungsdialog anhand konkreter Leseraufgaben.

## Alle 26 Contract-Testklassen

| T | Nachweis | Ergebnis / Grenze |
|---|---|---|
| 01 Daily capture | D01, R01, R21 | R0 und R1 qualifizieren zu pauschal. R2/R21 fragt eine konkrete Bruchstelle, nutzt die Folgeantwort und erzeugt qualifiziertes lösungsoffenes Intent. |
| 02 DGUV/BetrSichV | D02 | Primärquellen verändern Framing; keine pauschale Rechtssicherheitszusage; echte menschliche Richtungsfrage plus verbleibende Betriebsevidenz. |
| 03 Research/Decision | D03 | Nichtsoftware-Analy­sezweck qualifiziert, keine Saalentscheidung vorweggenommen. |
| 04 Already well formed | D04, R04, R24 | Direkter Abschluss ohne Rückfrage, auch nach Reparaturen. |
| 05 Solution-first | D05 | Chatbot-Hypothese gelöst, produktive Arbeitszeit als menschlich vorgegebenes Outcome erhalten. |
| 06 Human judgment | D06 | Persönlicher Wertkonflikt offen; Fixture-Präferenz übernommen, Partnervereinbarung nicht erfunden. |
| 07 Multi-turn/handoff | D01, D01H, D02H | Quellen, Revisionen, Bedeutung und offene Fragen aus Dateien wiederhergestellt. |
| 08 Boundary | D09, D02 | Verbindliche Plattform bewahrt; API/Stack/Sprints nicht übernommen; keine ungefragte Ausführung. |
| 09 Professional challenge | D02, D05 | Rechts-/Verantwortungsrahmen sowie Ticketdaten führen zu substanzieller Challenge. |
| 10 Opportunity preservation | D02, D05, D07 | Nachweis-/Wissens-/Übergabeproblem, nichttechnische Optionen und Reuse bleiben offen. |
| 11 Interaction cost | D04, D07/A01, R21 | Klare Fälle null Fragen; R21 eine materiale Erlebnisfrage; Router zwei unterschiedlich gewichtete Messefragen. Keine menschliche Rekonstruktion zugänglicher Daten verlangt. |
| 12 Orientation | D02H | Frischer Agent benennt Stand, bekannte Evidenz, menschliche Entscheidung und danach offene Fakten allein aus zwei Dateien. |
| 13 Repairability | D01H | Absichtlich injizierte falsche AI-Ableitung in isoliertem State verworfen; Erfolg/Scope konsistent repariert. Neue Revision unakzeptiert, alte Annahme historisch. |
| 14 Re-entry | D10 | Nur drei finale Intents gelesen; Zweck/Outcome/Status/Grenzen/Offenes mit Fundstellen auffindbar. Zeitabstand durch neuen Kontext simuliert. |
| 15 Ownability | D10 | AI-Reviewer unterscheidet Quellen, Entscheidungen, Inferenzen und findet Unklarheiten. **Kein menschlicher Nutzertest**. |
| 16 Artifact IA | D10 | Konkrete Such-/Änderungsaufgaben ausgeführt; abhängige Abschnitte bei Scope-Änderung erkannt. Keine gemessene menschliche Suchzeit. |
| 17 Entry gate | D07, A01 | Heterogene Signale proportional unterschiedlich behandelt; unnötiger Neubau nicht durchformiert. |
| 18 Attention economics | D07 | Ein reservierter Antragstag verändert Route der attraktiven Messeidee; kein Business Case erzwungen. |
| 19 Reuse/don’t build | D07, D08 | Vorhandene Notizfunktionen und gute bestehende Suche verhindern voreiligen Neubau. |
| 20 Portfolio fit | D07, A01 | Verpflichtung und Zeitkonflikt sichtbar, Prioritätsentscheidung beim Menschen. |
| 21 Whole problem | D05, D02 | Fachbereichsfreigaben und Prüforganisation statt enger Toolgrenze einbezogen; als AI-Framing erkennbar. |
| 22 Risk/affected parties | D04 vs D02/D07 | Kleine Korrektur ohne Governance-Aufwand, folgenreiche Fälle mit Verantwortungs-/Betroffenheits-/Evidenzgrenzen. |
| 23 Temporal validity | D03 | Angebotsfrist und geänderte Konditionen als Wiederprüfungsbedingungen. Keine Automatisierung angelegt. |
| 24 Preference formation | D06 | Faire illustrative Kontraste mit Zurückweisungsmöglichkeit; möglicher Ankereffekt bleibt unbelegt. |
| 25 Sunk cost/stop | D08 | Neubau nach neuer Evidenz explizit beendet; kein Folgeprojekt trotz erhaltenem Bedarf. |
| 26 Skill architecture | D07/A01, D04/A02 | Zwei echte Einstiegspfade mit demselben Kern ausgeführt. Ein Einstieg spart im Mischfall Nebenformation/Fragekomplexität; kleine Aufgabe fachlich gleichwertig. Kein statistischer Vorteil bewiesen. |

## Fünf getrennte Qualitätsebenen

### 1. Professional Intent Quality

| Dimension | Stärken | Defizit / Trade-off |
|---|---|---|
| Purpose Fidelity | D03 priorisiert Programmumfang wie vorgegeben; D06 übernimmt genau die Fixture-Präferenz; D09 erfindet keine technische Bindung. | Frühes D01 machte Capture-Verbesserung zu schnell zum Outcome; R21 klärt die Bruchstelle vorher. |
| Problem/Opportunity Quality | D05 trennt Reaktionskennzahl von Arbeitsverlust; D02 untersucht Ursachen statt nur Kalender. | D02s breiter Organisationszweck ist noch ein Vorschlag und zu Recht nicht qualifiziert. |
| Outcome Quality | Nutzen statt Features; D03 Erreichbarkeit umfasst Weg und Zugang; R21 Zusagen rechtzeitig aufgreifen. | Konkrete Nutzenwirkung wurde nicht real beobachtet. |
| Reference Grounding | D02 öffentliche Primärquellen mit materieller Framing-Folge; Methodenarchitektur aus R01–40. | Rechtsprüfung nicht vollständig, Analysten-/Normzugang begrenzt. Kein „mehr Quellen = besser“. |
| Opportunity Preservation | Reuse, Prozessänderung, Nachweisentlastung, keine Intervention sichtbar. | Vollständigkeit möglicher Chancen nicht beweisbar. |
| Challenge Quality | D02 Rechtsversprechen, D05 falscher Antwortzeitanker, D07 Messvalidität. | D05 formuliert die Empfehlung im Chat bestimmter als im Intent; der Vorschlagsstatus bleibt im Artefakt sichtbar. |
| Evidence Discipline | D05 62 % Tickets ≠ 62 % Arbeitsverlust; D08 19/20 plus Korrektur ≠ nachgewiesener 20/20-Retest. | Kleine AI-Leitplanken teils erst im State eindeutig zugeordnet. |
| Proportionality | 151-Wörter-Intent D04, kein Interview; D02 mehr Evidenz wegen Tragweite; D07 selektive Aufmerksamkeit. | D03/D05 und persönliche Fortsetzungsstände könnten knapper sein. |
| Intent/Spec Boundary | Candidate D09 bewahrt nur echte Plattform-/Zugriffsgrenzen; keine Requirements/Tasks. | Baseline B01v1 überschreitet semantisch die Grenze trotz Dateiname intent.md. |
| Actionable Downstream Meaning | D10 rekonstruiert Bedeutung ohne Chat und erkennt abhängige Stellen einer Scope-Änderung. | Nachgelagerte produktive Nutzung absichtlich nicht ausgeführt. |

Keine starke Dimension kompensiert einen materiellen Fehler in einer anderen. Insbesondere legitimiert D01s gute Lesbarkeit nicht sein zu endgültiges frühes Qualification-Urteil.

### 2. Formation Quality

Eigenständige fachliche Arbeit ist in D02/D05 nachweisbar; D06 benötigt menschliche Werte statt Recherche. D08 respektiert den Stop und trennt berichtete neue Evidenz von unabhängiger Prüfung. D01H repariert bewusst fehlerhaften State und verhindert eine stille Übertragung alter Akzeptanz. D02H hält neben dem aktuellen menschlichen Gate die nachfolgende faktische Blockade sichtbar. Der finale R2-Kern behebt das konkrete Defizit der reinen Symptomschilderung, ohne bereits geklärte Arbeit neu zu öffnen.

Die Änderungen sind nicht nur plausibel beschrieben: R01 zeigte, dass die erste abstrakte Nachschärfung **nicht** genügte; erst R21 änderte das Verhalten. R24 belegt weiterhin direkte Formation im klaren Fall. Wiederholungen beschränkten sich auf das konkrete Risiko. Alle früheren Beobachtungen beziehen sich auf ihren damaligen Kernstand; daraus wird keine komplette Regressionserprobung des finalen Stands behauptet.

### 3. Human–AI Interaction UX

| Dimension | Beobachtung |
|---|---|
| Orientation | D02H erschließt Stand selbst; mit 432 Wörtern eher ausführlich. |
| Cognitive Load | Kurzer klarer Fall kompakt; v1-Capture 2.993 Wörter erzeugt sichtbar mehr Lesefläche. Keine menschliche Lastmessung. |
| Interaction Cost | Keine erkennbar redundanten Fragen in klaren Kandidatenfällen; R21s zusätzliche Frage hat materiale Konsequenz. |
| Progressive Disclosure | Methoden werden nicht als Pflichtfragen an Nutzer ausgegeben; komplexer rechtlicher Rahmen erklärt sich aus der Aufgabe. |
| Mixed Initiative | AI recherchiert/challengt; Mensch liefert Präferenz, Erfahrung und Priorität. |
| Agency & Control | Vorschläge markiert, andere Rahmungen möglich; kein Schweigen als Zustimmung. |
| Explainability at Decision Points | D02 erklärt Bedeutung des Richtungsentscheids; D06 erklärt Trade-off; R21 erklärt, warum Bruchstelle zählt. |
| Repairability | D01H repariert falsche Ableitung plus Scope und Akzeptanzstatus, ohne alte Aussagen als aktuell zu führen. |
| Continuity | Neue Threads lesen State/Intent ohne Nutzerrekonstruktion; tatsächliche Langzeit-Persistenz bleibt ungetestet. |
| Closure Clarity | D08 beendet; D04/D09 schließen; D02 bleibt begründet offen. |

Quantitative Proxies stehen in `evidence/proxy-metrics.json`. Fragezeichen in URLs oder wiedergegebenen Fragen sind **nicht** automatisch Rückfragen; die obige Beurteilung ist semantisch. Gesamte Tokenkosten, menschliche Antwortzeit und subjektive Belastung wurden nicht gemessen.

### 4. Intent Artifact UX / Ownability

D10 konnte aus X/Y/Z Zweck, Outcome, Grenzen, Entscheidungen, AI-Deutungen, offene Fakten/Werte, Readiness und Reopen-Bedingungen benennen. Beim probeweise engeren Helpdesk-Scope erkannte der Leser die Mehrdeutigkeit von „innerhalb des Helpdesks“ und die betroffenen Abschnitte, statt blind Text zu ersetzen. Er fand zugleich, dass nicht jede Erfolgsaussage eindeutig separat menschlichen Ursprungs ist. Das ist nützliche beobachtete Reviewbarkeit, kein Beweis menschlicher Verständlichkeit oder tatsächlicher Annahme.

Die finale Oberfläche ist überwiegend menschenlesbar und scanbar. Die kleinen Statusbegriffe benötigen weiterhin Verständnis; für eine Einmalkorrektur ist der Mehrwert der Lifecycle-Spur begrenzt. Persönliche State-Dateien enthalten noch mehr historische Wiederholung als minimal nötig. Alte Antwortlinks auf `intent.md` zeigen nach Revisionen auf den neuesten Stand; archivierte Inhalte und Revisionsbezug erlauben Rekonstruktion, garantieren aber keinen unveränderlichen historischen Chatlink.

### 5. Downstream Utility

Das fertige Intent vermittelt Meaning ohne Requirements: D03 ermöglicht einen späteren Analyseauftrag, D09 einen späteren Auftrag innerhalb echter Plattform-/Zugriffsgrenzen, R21 eine spätere Ausgestaltung des Wiederaufgreifens. Offene Lösungstechnik ist kein Intent-Mangel. D02s offene Betriebsevidenz ist dagegen ein tatsächlicher Qualifikationsblocker. Kein Candidate-Lauf erzeugte ungefragt Specification, Plan oder Implementierung; die Boundary wurde auch inhaltlich geprüft.

Readiness und Akzeptanz dürfen nicht als Ausführungserlaubnis konsumiert werden. Ein nachgelagerter Parser muss Statusbegründung und Bezugsgegenstand erhalten: In D08 ist der Neubau beendet, der Zweck nicht als erfüllt bewiesen. Ein nacktes `dropped` ohne diese Bedeutung wäre verlustbehaftet.

## Direkter Vergleich

| Gleicher erster Input | Raw direkt | intent/v1 | Kandidat R0 | Schluss |
|---|---:|---:|---:|---|
| Capture | 324 Wörter | 2.993 Wörter | 439 Wörter | Candidate klarer in Herkunft/Readiness, aber zunächst kein besserer Outcome-Abschluss als Raw. v1 mehr Formlast und unerbetene Abnahmelogik. |
| Kleine Kontaktkorrektur | 101 Wörter | 418 Wörter | 151 Wörter | Raw genügt inhaltlich am knappsten; Candidate trennt Verifikation/Sachbeschluss/Intent-Annahme. v1 erfindet `accepted`. |

Wörter sind whitespace-basierte Zählungen der Artefakte, keine Qualitätsnoten. Der Kandidat gewinnt nicht durch möglichst kurze Texte. Der v2-Referenzansatz lieferte im ersten Turn die sinnvolle Bedeutungsfrage nach bewusstem Überblick versus Wiederaufgreifen ohne Nachsehen; diese Beobachtung informierte die schmale Qualification-Reparatur. Vollständige aktive Framing-v0.1.4-A/B-Evidenz liegt nicht vor; dessen historisches KEEP wird deshalb nicht überstimmt.

**V2-Fortsetzung:** Nach derselben inhaltlichen Fixture-Präzisierung wie R21 erzeugte B01v2 ein fertiges, gut begründetes Intent. Besonders hilfreich ist dort die ausdrücklich begrenzte Wirkannahme: Wiederaufgreifen ermöglicht Erfüllung, garantiert sie aber nicht. Der Kandidat R21 stellt dafür Revision, Qualification und fehlende Akzeptanz deutlicher heraus. Beide finalen Artefakte bewahren Lösungsoffenheit und die Grenze zwischen Zusage und Idee. Eine allgemeine fachliche Überlegenheit des Kandidaten gegenüber v2 ist damit **nicht** belegt. Die unabhängige Review beurteilte B01v2 vor diesem zweiten Turn; die Fortsetzung wurde anschließend vom Hauptagenten geprüft.

## Architekturentscheidung

Gewählt bleibt **ein Formation-Kern mit optionalen Methoden und einem kleinen Entry Check**. D07 behandelt den tatsächlichen Prioritätskonflikt, während A01 zusätzlich die ohnehin klare Kontaktkorrektur als Haupt-Intent formt und zwei Messefragen stellt. D04/A02 sind fachlich nahezu gleichwertig; A02 ist etwas ausführlicher. Beide Pfade benötigen keinen manuellen zweiten Skill-Aufruf. Der Router hat daher in den ausgeführten Fällen keinen nachgewiesenen Nutzen, der einen zusätzlichen Einstieg rechtfertigt.

Dies ist ein begrenztes Auswahlurteil, kein genereller Anti-Router-Befund. Ein separates Portfolio-Angebot könnte später eigenen Nutzen haben. Gemeinsamer Kern verhindert semantische Duplikation in beiden Varianten; der getestete Handoff erfolgt instruktionsbasiert im gleichen Runtime-Agenten, nicht über einen behaupteten technischen Workflow-Dienst.

## Review-Abwägung und Entscheidung

Die unabhängige Review priorisiert Qualification, Statusbezug beim Stop und historische Links. Qualification wurde tatsächlich repariert und neu geprüft. Bei D08 steht der Bezugsgegenstand bereits unmittelbar in Titel und Statuszeile; deshalb wird kein neuer Statuskatalog eingeführt. Die Gefahr einer losgelösten Enum-Auswertung bleibt als Schnittstellengrenze dokumentiert. Historische Linkstabilität wird nicht behauptet; die gesicherten Originalversionen bleiben im Evidenzpaket.

**Empfohlener menschlicher Entscheid:** Kandidat und Erhaltsempfehlung fachlich abnehmen; menschlichen Ownability-Review an den bereitgestellten Beispielen durchführen; Installation nur separat beauftragen. Kein pauschaler Ersatz von Framing, keine Migration oder produktive Aktivierung durch diesen Auftrag.
