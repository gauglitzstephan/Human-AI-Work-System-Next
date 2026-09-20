# Research Synthesis

Stand: 20.09.2026. Quellen, Klassifikation, Evidenzgrenzen und vollständige Links stehen in der vor Architekturarbeit erstellten [Reference Map](Intent_Formation_Reference_Map.md). Kennungen R01–R40 beziehen sich auf diese Tabelle. Die folgenden Entscheidungen sind **eigene Synthese**, keine vermeintliche gemeinsame Norm der Quellen.

## Was die Referenzen gemeinsam tragen

**Problem und gewünschte Wirkung vor Lösungsbindung.** GOV.UK Discovery (R21), SVPG (R16–18), Torres (R19–20), Double Diamond (R22) und Needs Engineering (R23–27) unterscheiden jeweils in anderer Form Bedürfnisse, Wirkung, Lösungsraum und Umsetzung. Gemeinsam tragfähig ist die Prüfung, ob der Eingangsauftrag das eigentliche Problem trifft. Nicht tragfähig wäre eine vorgeschriebene mehrwöchige Discovery für jedes Anliegen oder die Annahme, alle Referenzen hätten dieselbe Intent-Datei.

**Professionelle Formation trägt Erkenntnis bei.** Stakeholderperspektiven, reale Nutzungssituationen, Gegenhypothesen, alternative Systemgrenzen und entscheidende Annahmen sind mehr als Umformulieren. Fachliche Modelle dienen als Linsen, nicht als zusätzliche Pflichtabschnitte. Die relevanten Ergebnisse gehören ins Intent; der vollständige Forschungsweg nicht.

**Qualifikation ist eine Entscheidung unter verbleibender Unsicherheit.** Spec Kit Assessment (R12–15) lässt Prüfung und Delivery getrennt und kennt Stop-Ausgänge. Decision Quality (R32) ergänzt angemessenen Rahmen, Alternativen, Information, Werte und Commitment. Daraus folgt: Nicht jede unbekannte Tatsache blockiert. Eine offene Frage blockiert dann, wenn eine plausible Antwort Zweck, Zielkonflikt, Betroffenheit oder wesentliche Grenze verändern würde.

**Menschen liefern nicht bloß fehlende Felder.** Mixed Initiative (R28), Human–AI Interaction Guidelines (R29) und Preference Construction (R33) begründen Aufgabenverteilung, korrigierbare Initiative und Unterstützung noch ungebildeter Präferenzen. Fachliche AI-Synthese darf den Raum verbessern; sie darf keine Wertentscheidung als Nutzerwunsch ausgeben. Eine relevante Frage braucht eine erkennbare Konsequenz, keine Rechtfertigungszeremonie.

**Kontinuität braucht expliziten Zustand.** Context Engineering und dokumentierte Anbieterpraxis (R05–10) stützen knappe, wiederlesbare Arbeitsstände und überprüfbare Ergebnisse. Das ist besonders für Kontextwechsel relevant. Ein Markdown-State macht keine versteckte Persistenzzusage: Der Agent muss ihn tatsächlich speichern, später finden und lesen können.

## Unterschiede, die nicht eingeebnet werden dürfen

| Referenzbereich | Nützlicher Mechanismus | Grenze der Übernahme |
|---|---|---|
| Anthropic AI-Native SDLC (R01) | menschlicher Ursprung/Owner, Zweck und Grenzen, prüfbare Artefaktkette | Software-Lifecycle; Beispiele enthalten schon Lösungskontext. Commit- oder Workflow-Übergang zu Spec wird ausdrücklich nicht übernommen. |
| OpenAI Skills / Work (R02–08) | gezielter Einstieg, progressive Referenzen, Steering und überprüfbare Ergebnisse | Skill ist Instruktion, kein garantierter Zustandsautomat. API-Orchestrierung ist keine zugesicherte Work-Funktion. |
| Spec Kit Assessment (R12–15) | eigenständiges Assessment, Gegenbelege, legitimes Kill/Clarify, Erweiterbarkeit | Fünf Assessment-Dateien sind kein minimales Intent-Artefakt und kein Pflichtprozess für Nichtsoftware. |
| Needs/Requirements Engineering (R23–27) | betroffene Rollen, Bedürfnisse, rationale Grenzen, Outcome-Validierung | Normenübersichten sind keine gelesenen Normvolltexte; Systemdesign, Requirements und formale Verifikation bleiben außerhalb. |
| Product Discovery (R16–22) | Value/Usability/Feasibility/Viability, Opportunities, Annahmen | Produktteamspezifische Praktiken nicht überall verpflichtend; Softwareprototypen nicht vom vorliegenden Auftrag gedeckt. |
| HCI / Decision Support (R28–33) | Status, Erklärbarkeit, direkte Korrektur, Erinnerung entlasten | Allgemeine Prinzipien belegen keine konkrete UX-Wirkung des neuen Skills. |

## Antwort auf die Forschungsfrage

Die kleinste tragfähige Capability braucht drei **Verantwortungsgrenzen**, nicht drei Pflichtphasen:

1. Vor größerem Aufwand prüfen, ob und in welcher Tiefe das Anliegen Aufmerksamkeit verdient. Bestehende Fähigkeiten, Timing, Verpflichtungen und Nichtstun können die Route ändern.
2. Das ausgewählte Anliegen adaptiv formen: rekonstruieren, fachlich challengen, zugängliche Evidenz prüfen, nur echte Erfahrung oder Judgment erfragen und bis zu einer begründeten Konvergenz iterieren.
3. Dauerhaft benötigte Bedeutung in einem lesbaren Intent erhalten: Zweck/Wirkung, Kontext/Betroffene, Grenzen, wesentliche Unsicherheit, Herkunft und menschliche Entscheidungen. Keine automatische Ausführung.

Der geeignete Regelkern ist materialitätsbasiert: Eine nächste Recherche, Frage oder Dokumentsektion ist gerechtfertigt, wenn sie die Ausrichtung, eine relevante Entscheidung, die Tragweite oder die spätere Fehlinterpretation voraussichtlich verändert. Forschungskosten gehören selbst in diese Abwägung. Ein qualitatives Urteil reicht bei kleinen Aufgaben; erfundene Scores verschleiern Unsicherheit.

## Ableitungen für die anschließende Architekturentscheidung

Zu vergleichen sind ein kompakter Kern mit nachgeladenen Methoden und ein eigenständiger Selection-Einstieg mit Formation-Handoff. Beide können Referenzprinzipien erfüllen. Ein monolithischer vollständiger Methodenblock belastet kleine Fälle; getrennte Skills pro Domäne riskieren unterschiedliche Semantik. Ein automatischer Orchestrator ist ohne konkrete Runtime-Notwendigkeit zusätzliche Infrastruktur. Der endgültige Favorit muss sich im Verhaltenstest bewähren.

Formation State und Intent erhalten verschiedene Aufgaben: Der State trägt Fortsetzung und verworfene Deutungen, das Intent trägt aktuelle Bedeutung. Keine Duplizierung vollständiger Forschungsnotizen im akzeptierten Dokument. Kurze und erweiterte Markdown-Flächen können dieselbe Semantik ausdrücken; Pflichtfelder folgen nicht aus Listen in Fachquellen.

## Evidenzgrenzen

Die stärkste Quelle für den **bestehenden** Framing-Stand ist der abgeschlossene Audit, der KEEP empfiehlt; die stärkste Quelle für den **neuen** Kandidaten müssen neue beobachtete Läufe sein. Viele AI-native Quellen sind Anbieterempfehlungen oder dokumentierte Eigenpraxis, keine unabhängigen Wirksamkeitsstudien. ISO/INCOSE/BABOK wurden nur soweit öffentlich zugänglich ausgewertet. Zum Begriff Intent Engineering gibt es unterschiedliche aktuelle Verwendungen, aber in dieser Recherche keine belastbar zugängliche, institutionell konsolidierte Analystenmethodik. Staw 1976 ist bibliographisch identifiziert, der Verlagstext blieb gesperrt; daraus werden keine Effektgrößen oder Detailbefunde abgeleitet.

Diese Grenzen sprechen für einen prüfbaren Kandidaten mit konservativer Migrationsentscheidung, nicht für ein neues universelles Modell oder die Behauptung einer Standardkonformität.
