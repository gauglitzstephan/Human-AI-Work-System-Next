# Skill-Level Reference Architecture

Vorläufige Architekturentscheidung vor Verhaltenstests; abschließende Bewertung in der Evaluation. Quellenbasis: Reference Map R03, R05–15, Bestandsanalyse und Auftrag.

| Variante | Stärke | Konkreter Preis / Risiko | Entscheidung |
|---|---|---|---|
| Monolithischer Formation-Skill | Ein Aufruf, keine Übergabe | Methodenlast bei jedem Fall; Pflege konzentriert alles in einer Datei | Nicht gewählt; kompakter Kern statt Vollkatalog. |
| Selection/Router + eigener Formation-Skill | Auswahl als wiederverwendbare separate Fähigkeit; Portfolio-Fälle gut abgrenzbar | Zweiter Lade-/Handoff-Punkt, Gefahr doppelter Triage | Vergleichsvariante tatsächlich ausführen. |
| Unabhängige Einstiegsskills je Arbeitssituation | Präzise Discovery bei klar verschiedenen Aufgaben | Mehrdeutige Auswahl und divergierende Intent-Semantik | Erst bei beobachtetem Routingproblem begründen, derzeit nicht. |
| **Formation-Kern + optionale Methoden** | Ein Nutzer-Einstieg, gemeinsame Invarianten, kontextabhängige Details | Modell muss relevante Referenz lesen; kein garantierter Automatismus | Kandidat `form-intent`. |
| Orchestrator mit kleinen Skills | Explizite Übergaben, austauschbare Komponenten | Zusätzliche Runtime-/Tool-Annahmen und Konfiguration | Für derzeitigen Work-Kontext unnötig; keine API-Runtime erfinden. |
| Profile/Surfaces mit gleichem Modell | Lesefläche passt zum Fall, Semantik stabil | Renderabweichung kann wichtige Bedeutung verdecken | Zwei optionale Surfaces, keine separaten Formation-Skills. |

## Verantwortung und Handoff

Selection entscheidet nur über Aufmerksamkeit/Route. Formation verantwortet Bedeutung, Grounding und menschliche Urteile. Downstream-Leser erhalten aktuelle Intent-Revision, Readiness, Akzeptanz, Quellen-/Unsicherheitsgrenzen und Gültigkeit; sie erhalten keinen Ausführungsauftrag. Ein extern bereits ausgewähltes Anliegen muss nicht noch einmal durch ausführliche Triage.

Der eingebaute kleine Entry Check implementiert nur den Teil der Auswahl, der unnötige Formation verhindert. Er ist kein Portfoliomanager. Ein zukünftiger Router kann denselben Skill mit einer kurzen, quellenmarkierten Auswahlbegründung aufrufen. Der Kern prüft neue Widersprüche, wiederholt aber keine bereits geklärte Auswahl.

## Tatsächliche Runtime

Kandidat ist ein instruktionsbasierter Skill-Ordner mit `SKILL.md`, vier Methodenreferenzen, zwei optionalen Templates und UI-Metadaten. Keine SDK-Abhängigkeit, keine Hintergrundprozesse, kein automatisches Scheduling und keine behauptete Memory-Garantie. Dateizugriff und Recherche hängen von der aufrufenden Runtime ab. Persistenz erfolgt über deren etablierte Dateifunktionen; die Datei muss beim Wiedereinstieg verfügbar und gelesen sein.

Die Vergleichsvariante unter `tests/variants/selection-router` delegiert im selben verfügbaren Agent-Kontext durch Laden des dedizierten Formation-Kerns. Damit wird ein realistischer instruktionsbasierter Skill-Handoff geprüft, kein technisch erzwungener Multiagent-Orchestrator. Beide Varianten teilen exakt denselben Kern; keine künstlich geschwächte Alternative.

## Entscheidungskriterien für die Tests

Vergleiche Anzahl menschlicher Koordinationsschritte, wiederholte Fragen, unnötige Pflichtdateien/Leselast, Erhalt der Auswahlgründe, Boundary-Verhalten, Readiness, Versions-/Akzeptanztreue und Verhalten bei kleinen versus gemischten Aufgaben. Semantische Duplicationskosten zusätzlich statisch prüfen. Ohne mehrfachen Lauf keine statistische Überlegenheit behaupten. Eine einfachere Variante gewinnt nur bei mindestens vergleichbar tragfähigen Ergebnissen.
