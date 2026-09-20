# R3 — Diagnose und Änderungsgrund

## Befund vor Änderung

Die Nutzerkritik machte fehlende Nachvollziehbarkeit der professionellen Qualifikation und ihrer Einordnung in die gesamte Arbeitskette sichtbar. Die darauf folgende Behauptung des Hauptagenten, im R21-Fall sei zusätzliche Discovery beziehungsweise externe Recherche zwingend und der Qualifikationsabschluss deshalb falsch, war zu weitgehend.

Ein unabhängiger Agent prüfte ausschließlich Originalauftrag, Rohverlauf und R2-Skill. Sein [Befund](qualification-review-independent.md): Der Status `qualified` ist nach der sehr ausführlichen synthetischen Folgeantwort tragfähig. „Rechtzeitig“ ist durch mögliche vereinbarte Erfüllung ausreichend beschrieben; ein allgemeiner Minutenwert, zusätzliche Anekdoten, Produktrecherche und Business Case sind hier nicht erforderlich. Der Lauf liefert jedoch keinen robusten Nachweis für die Behandlung noch unklarer oder widersprüchlicher Antworten. Die frühere globale Fertig-/Reparaturbewertung war deshalb nicht ausreichend begründet.

Konkrete Verbesserungsgegenstände: absolute Abschlussaussagen ohne Bindung an die vorliegende Evidenz; knappe bis unklare Begründung, warum Material später offen bleiben kann; unpräziser Verweis auf die Nachlieferung; wiederholte Aussagen und dominante Prozess-/Statussprache. Der ausführbare Kern enthielt bereits wesentliche fachliche Mechanismen. Diese bleiben erhalten.

## Änderung am bestehenden Kern

- Qualifikation richtet sich ausdrücklich nach der Bedeutung der ausgewählten Arbeit und der nächsten Verantwortungsgrenze. Ein Analyse-Intent kann qualifiziert sein, obwohl sein Untersuchungsgegenstand offen ist. Ein Lieferziel wird deshalb nicht stillschweigend zu Forschung umgedeutet.
- Nach einer Episode wird die Deutung erneut geprüft. Auftreten, Verbreitung, Ursache und gewünschte Veränderung sind unterschiedliche Aussagen.
- Materiale Unsicherheiten werden anhand ihrer Auswirkung auf Zweck/Scope, spätere Lösungsentscheidungen oder spätere Evaluation zugeordnet. Der Abschluss nennt die konkrete Grundlage und den Grund, warum weitere Formation jetzt wenig zusätzlichen Wert hat.
- Referenzklassen dienen als begründete fachliche Linse. Weder das Vorliegen persönlicher Erfahrung noch die bloße Erwähnung einer Methode ersetzt unabhängige Faktenarbeit; zugleich entsteht keine Recherchepflicht für klare einfache Fälle.
- Purpose zuerst, Status in Alltagssprache, technische Metadaten nachgeordnet; eindeutiger Akzeptanzbegriff und weniger Wiederholung. Quellen, Entscheidungen und Grenzen bleiben erhalten.
- Installationshinweise unterscheiden den tatsächlichen Host und vorbereiteten Handoff von erfolgter Aktivierung.

Die fachliche Grenze ist in [Intent_Spec_Boundary.md](../research/Intent_Spec_Boundary.md) mit erneut geprüften Primärreferenzen erläutert. Kein neuer Router, kein neuer Lifecycle, keine zusätzliche Pflichtphase, kein numerisches Qualification-Gate.

## Prüfdesign und Herkunft

Die [Kriterien](../tests/Qualification_Repair_R3.md) wurden vor der Änderung festgehalten (lokal `bad1253`). Unverändertes R2 ist in `skill-history/R2/` erhalten. Die sieben geänderten Paketdateien sind in Kernrevision `0cbdb91` festgehalten; UI-Metadaten bleiben unverändert. Neue Läufe erhalten eine eingefrorene Kopie dieses Pakets. Ergebnisse stehen nach Ausführung in der aktuellen Evaluation. Die vorab gespeicherten Folgeantworten sind synthetische Testdaten, keine Nutzerpräferenzen oder tatsächliche Nutzererfahrung.

## Ergebnis der begrenzten Nachprüfung

Acht Formation-/Fortsetzungsfälle und ein kontextfreier Leser-Test wurden auf der unveränderten R3-Paketkopie ausgeführt. Ein separater Reviewer prüfte alle acht Rohverläufe gegen den Originalauftrag, ohne die Reparaturdiagnose zu lesen. Er stellte keinen sicher belegten materiellen Fehler fest; Q36 blieb fachlich angemessen offen. Die aktuelle Evaluation führt begrenzte UX-/Semantikschwächen und nicht erbrachte weitergehende Nachweise ausdrücklich auf. Dies ist keine vollständige Regression aller früheren Klassen und keine menschliche Abnahme.
