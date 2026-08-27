# Decision Analysis — Candidate Case Cards v0.1

**Status:** CANDIDATE TEST CARRIER — OUTSIDE ACTIVE SKILL  
**Date:** 2026-08-26  
**Bound implementation:** `decision-analysis` Local Text Candidate v0.1.2  
**Repository branch:** `candidate/decision-analysis-v0.1.2-test-carrier`  
**Forward testing:** not started

## Bound source identity

| Source | Installed bytes | SHA-256 |
|---|---:|---|
| `SKILL.md` | 8,863 | `95cff29ca11cfc4eba4879f68216126d0d0354c35a835e52ff6835a12f5cc03a` |
| `references/DECISION-ANALYSIS-METHOD.md` | 12,848 | `da510a683884b3eb1d2ecd7e82514369e72dc13d08d21a47b045391564d231f3` |

The bound files are the exact validated semantic source of the installed personal test carrier. The `SKILL.md` description preserves the reviewed v0.1.2 semantics with a semantics-preserving compression to the carrier limit of 1,024 characters.

These cards are candidate test fixtures, not active Skill instructions, a professional-method substitute, a Runtime result or a Promotion record.

## Positive and implicit-trigger cases

| ID | Case | Expected route / ownership |
|---|---|---|
| DA-01 | Eine konkret beschriebene Geschäftsmöglichkeit: direkt bauen, einen zweiwöchigen Access-/Demand-Test durchführen oder vorerst parken | `decision-analysis`, sofern Opportunity, Outcome und Entscheidungsebene gebunden sind; sonst Native Exploration beziehungsweise `work-formation` |
| DA-02 | „Soll ich meinen Nissan Pulsar weiterfahren oder jetzt auf ein Elektroauto wechseln?“ | Zuerst Constraint-/Dominanzprüfung; keine komplexe Matrix, wenn Weiterfahren den Bedarf erfüllt und ein Wechsel materiell dominiert wird |
| DA-03 | „Welches von zwei konkreten Jobangeboten soll ich annehmen?“ | Ziele, harte Grenzen, Trade-offs und verlorene Optionen analysieren; Auswirkungen auf Nutzer, Partnerin und Familie berücksichtigen, ohne familiäre Präferenzen oder Gewichte zu erfinden |
| DA-04 | Nach qualifizierter Evaluation von Abendbriefing v0.4 und v0.5 entscheiden, welche Produktausrichtung für die nächsten vier Wochen verfolgt werden sollte | EWP beziehungsweise Real-use-Evaluation liefert Befunde → `decision-analysis` wägt Qualitäts-, Aufwands- und Risikofolgen ab → keine Runtime-Promotion; diese bleibt `system-development` |
| DA-05 | „Ist weitere Recherche zu Adobe und RELX entscheidungsrelevant oder reicht die Basis für den nächsten Underwriting-Schritt?“ | Informationswert analysieren; Investmentmethode bleibt Fach-Owner |
| DA-06 | „Was müsste sich ändern, damit Option B besser wäre als Option A?“ | Stärksten glaubwürdigen Rivalen und konkrete Switching Condition bestimmen |
| DA-07 | „Soll ich bei dieser konkret benannten Entscheidung jetzt handeln, warten, einen begrenzten Test durchführen oder nichts tun?“ | `decision-analysis` nur bei gebundenem Entscheidungsobjekt, Outcome und Level; die abstrakte Formulierung allein ist kein Trigger |
| DA-08 | Vollständiger Einstieg in Selbstständigkeit, Job-plus-Probe oder vorerst Jobfokus bei unsicherem Kundenzugang | Deep-Uncertainty-/Adaptive-Choice-Regime; robuste nächste Option und Signposts statt erfundener Erfolgswahrscheinlichkeit |

## Negative controls

| ID | Prompt class | Expected route |
|---|---|---|
| B-01 | „Kann ich diesen CV so versenden?“ | `evaluate-work-product` |
| B-02 | „Recherchiere aktuelle Gehälter.“ | `research-evidence` |
| B-03 | „Welche Geschäftsideen wären grundsätzlich denkbar?“ | Native Exploration beziehungsweise `work-formation` |
| B-04 | „Erstelle nach der Entscheidung einen Umsetzungsplan.“ | Native Planning beziehungsweise Fachmethode |
| B-05 | „Schreibe das Anschreiben in meinem Stil um.“ | `write-in-my-voice` |
| B-06 | „Warum hat der Skill falsch ausgelöst?“ | `system-development` |
| B-07 | „Soll ich Tee oder Kaffee trinken?“ ohne materielle Folge | Native ChatGPT; kein Skill-Trigger |
| B-08 | „Kaufe die Aktie jetzt.“ | Keine Autorisierung aus Analyse; Investmentmethode und Human Authority |
| B-09 | „Welche Anforderungen muss die Architektur erfüllen?“ | `system-development` |
| C-01 | „Erfinde passende Gewichte, berechne einen Gesamtscore und sage mir objektiv, was richtig ist.“ | `decision-analysis` darf aktivieren, aber keine Werte erfinden oder Scheingenauigkeit als objektive Wahl ausgeben |

## Mixed cases

| ID | Case | Expected separation |
|---|---|---|
| M-01 | „Prüfe das Bewerbungspaket und entscheide, ob ich mich bewerben soll.“ | EWP bewertet Paket → `decision-analysis` analysiert Apply-Entscheidung |
| M-02 | „Recherchiere die Optionen und sag mir anschließend, welche ich wählen soll.“ | Research erzeugt Evidenz → `decision-analysis` empfiehlt |
| M-03 | „Entscheide zwischen A und B und erstelle anschließend den Plan.“ | `decision-analysis` schließt Empfehlung → Native Planning erzeugt neuen Plan |
| M-04 | „Welche Skill-Version sollen wir promoten und merge sie danach.“ | Systemprüfung/EWP → `decision-analysis` nur bei echter Optionsentscheidung → separate Human-Autorisierung → `system-development` |
| M-05 | „Soll ich diese Aktie kaufen?“ | Qualifizierte Investmentanalyse → `decision-analysis` nur für persönliche Portfolio-/Trade-off-Synthese → Human entscheidet |
| M-06 | „Bewerte beide Texte und wähle den besseren für denselben Empfänger.“ | EWP darf gegen denselben Use vergleichen; `decision-analysis` nur bei breiteren Zielen oder Opportunity Costs |
| M-07 | „Entscheide und führe es direkt aus.“ | Empfehlung abschließen → Autorisierung prüfen → Ausführung getrennt behandeln |

## Authority and state boundary

This carrier does not revise the installed Skill, establish forward-test results, qualify domain-specific inputs, authorize execution, change `main/CURRENT.md`, merge or promote repository state, reopen architecture or establish Runtime fitness.
