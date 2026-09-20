# Boundary Contract: Intent → Specification

Die Grenze folgt der **semantischen Funktion**, nicht dem Dateinamen. Intent beschreibt das relevante Problem oder die Opportunity, den menschlichen Zweck, die beabsichtigte Wirkung und die Grenzen des zulässigen Lösungsraums. Specification legt erforderliches Lösungsverhalten und dessen Abnahme fest; Planning ordnet Umsetzung, Abhängigkeiten und Ressourcen. Diese Abgrenzung ist die Synthese dieses Auftrags; nicht jede Anbieterreferenz zieht sie identisch.

## Präzisierung aus dem Review R3

Discovery, Exploration, Referenzwissen und Economics können an mehreren Stellen der Arbeitskette nötig sein. Sie sind keine vollständig vor Intent zu erledigende Phase. Eine offene Frage wird danach zugeordnet, welche Entscheidung ihre Antwort verändern würde:

| Gegenstand | Vor dem Intent-Abschluss nötig | Darf begründet später bleiben |
|---|---|---|
| Problem und gewünschte Veränderung | Situation, betroffene Rollen, relevante Bedeutungsunterscheidung, menschlicher Zweck und wesentliche Grenzen | Vollständige Ursachenanalyse, sofern sie den bereits hinreichend begründeten Zweck nicht blockiert |
| Intent einer Analyse/Discovery | Was soll gelernt oder entschieden werden, für wen und nach welchen relevanten Gesichtspunkten? | Ergebnisse der beauftragten Analyse, einschließlich Nachfrage, Kosten oder Optionenbewertung |
| Lösungsarbeit / Specification | Zweckprägende Machbarkeits- oder Constraint-Konflikte sichtbar halten | Mittelvergleich, Verhalten, Requirements, Design und deren konkrete Prüfung |
| Planning | Tatsächlich gesetzte Ressourcen- und Zeitgrenzen | Durchführung, Arbeitspakete, Sequenz und Ressourcenverteilung |
| Evaluation | Woran wäre der gewünschte Nutzen erkennbar; welche Wirkung ist bislang nur angenommen? | Detailliertes Mess-/Testdesign und Nachweis der realisierten Wirkung |

Eine verbleibende Frage wird nicht allein durch das Wort „downstream“ nichtblockierend. Ihre mögliche Auswirkung und der Grund für das Offenlassen müssen erkennbar sein. Spätere Erkenntnisse können Formation gezielt wieder öffnen. Ebenso ist ein klares Untersuchungsziel nicht deshalb unqualifiziert, weil sein Untersuchungsergebnis noch fehlt.

Diese Zuordnung ist die auf den Contract zugeschnittene Synthese. Im [Anthropic-Playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) enthält Intent bereits offene Fragen; der anschließende Spec-Review prüft deren Behandlung. [NASA](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) begründet die verständliche Darstellung von Stakeholdererwartungen, Erfolg aus Stakeholdersicht und Herkunft der Aussagen. [GOV.UK](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) trennt Problemverständnis von Bauentscheidung und macht den Erkenntniszweck für Umfang und Abschluss der Discovery maßgeblich. Die vollständigen Prozessmodelle dieser Quellen werden nicht in Intent importiert. Originale am 20.09.2026 erneut gelesen.

## Was der nächste verantwortliche Leser erhalten muss

Aktuelle Identität/Revision und Readiness; explizite Akzeptanz oder deren Fehlen; Zweck, Wirkung und Why; interpretierbarer Kontext mit betroffenen Rollen; geltende Grenzen und menschliche Entscheidungen; materiale Evidenz/Annahmen/Unknowns einschließlich Konsequenz; Bedeutung von Erfolg und gegebenenfalls Gültigkeits-/Reopen-Bedingungen. Das erlaubt einen begründeten nächsten Auftrag, ohne die Absicht aus dem Chat rekonstruieren zu müssen. Ein Dateiübergang ist keine Beauftragung.

## Grenzfälle

| Aussage | Funktion / Behandlung |
|---|---|
| „Offene Zusagen kommen rechtzeitig wieder in meinen Blick“ | Erwünschte Wirkung; Intent. |
| „Jeden Morgen Push-Nachricht um 8 Uhr mit drei Aktionen“ | Lösungsverhalten; Specification. Nicht als notwendige Operationalisierung des Outcomes hineinziehen. |
| „Erfassen muss in einer kurzen Alltagspause möglich sein“ | Nutzungskontext/Erlebnisgrenze; Intent. |
| „95. Perzentil unter 200 ms, gemessen unter Lastprofil X“ | Normalerweise technische Anforderung und Prüfspezifikation. Eine tatsächlich extern gesetzte Grenze darf als ererbte Bedingung dokumentiert werden, ohne Tests zu entwerfen. |
| „Vorstand hat bestehende Plattform verbindlich vorgegeben“ | Menschliche Entscheidung/Constraint mit Herkunft. Intent darf sie bewahren, obwohl sie den Lösungsraum einschränkt. |
| „Wir brauchen React, PostgreSQL und vier Sprints“ | Wenn bloße Idee: vorgeschlagenes Mittel vom Zweck lösen. Wenn schon beschlossen: relevante Bindung kennzeichnen; keine Architektur oder Planung hinzufügen. |
| „Erfolg ist weniger verlorene Arbeitszeit, ohne Mehrarbeit für die Anfragenden“ | Outcome plus Guardrail. Detaillierte Telemetrie und Feature-Akzeptanzkriterien bleiben downstream. |
| „Die Ursache des Wartens ist unklar und könnte den Problemrahmen ändern“ | Formation-Frage mit Materialitätsbegründung. Erforderliche Erkenntnis benennen; kein Projektplan zur Datenerhebung. |
| „Bis Freitag entscheiden, sonst verfällt das Angebot“ | Zeitliche Gültigkeit/Entscheidungsfenster. Keine automatische Erinnerung oder Task-Erzeugung. |
| „Analyse soll zwei Standortoptionen vergleichbar machen“ | Nichtsoftware-Intent. Die Entscheidung selbst gehört nur dann hierher, wenn sie eine notwendige menschliche Framing-Entscheidung ist. |

## Unvollständigkeit und Readiness

Ein Intent darf downstream zu klärende Fragen enthalten, sofern ihre Antworten Zweck, relevante Grenzen oder den wesentlichen Trade-off nicht verändern. „Nutzerproblem noch unbekannt“ ist kein nichtblockierendes Detail; „konkretes Dateiformat der späteren Lösung offen“ ist keine Formation-Lücke. Für jedes materiale offene Thema zählt der Grund, weshalb es blockiert oder noch offen bleiben darf.

Die Akzeptanz bezieht sich auf diese Bedeutung in einer bestimmten Revision. Nach materieller Änderung oder abgelaufener Gültigkeitsbedingung ist der alte Akzeptanznachweis kein Freibrief. Quellen- und Entscheidungshistorie erhalten, aktuelle Readiness neu beurteilen. Der Kandidat beendet seinen Auftrag an dieser Stelle. Das Verhalten wird insbesondere in D02, D03 und D09 semantisch geprüft; bloßes Nichtvorhandensein einer Datei namens `spec.md` reicht nicht.
