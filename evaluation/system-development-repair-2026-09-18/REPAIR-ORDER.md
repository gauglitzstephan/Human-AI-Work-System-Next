# Workauftrag — System Development gezielt reparieren und prüfen

**Stand:** 18.09.2026  
**Status:** vorbereiteter Ausführungsauftrag; die Reparatur wurde damit noch nicht ausgeführt.  
**Zielobjekt:** `system-development`, installierte Skill-ID `skill-6a8ddd367c6c81919fbd86aa685ac949`.  
**Ergebnis:** ein konkret implementierter, nachvollziehbar geprüfter Reparaturkandidat mit eindeutiger Quellenbasis und vorbereitetem Übernahmeweg.

## Auftrag und gewünschtes Ergebnis

Repariere den System-Development-Skill auf Grundlage des abgeschlossenen Deep Audits vom 18.09.2026. Liefere die geänderten Quelldateien, die dazugehörigen tatsächlichen Prüfbelege und einen klaren Status für Review, Repository und Installation. Ein weiterer allgemeiner Maßnahmenplan oder eine sprachliche Überarbeitung ohne Prüfung erfüllt den Auftrag nicht.

Der Skill soll tragfähige Systemdiagnosen und hinreichende Reparaturen ermöglichen, ohne unnötigen Systemausbau zu erzeugen. Maßgeblich sind fachliche Ergebnisqualität, nachvollziehbare Evidenz, erhaltene Befugnisse und geringe vermeidbare menschliche Nacharbeit. Die kleinste Änderung ist nur dann vorzuziehen, wenn sie die benötigte Wirkung ausreichend herstellen kann.

Arbeite den Auftrag bis zum konkret prüfbaren Ergebnis durch. Triff gewöhnliche, reversible Implementierungsentscheidungen selbst. Frage nicht nach Informationen, die aus den genannten Quellen oder der tatsächlichen Umgebung beschaffbar sind.

## Verbindliche Arbeitsgrundlage

Lies den vollständigen Audit und nutze seine Belege. Die dort dokumentierten Befunde sind der Ausgangspunkt; prüfe ihre fortbestehende Gültigkeit am aktuellen Zielzustand. Wenn neue Primärevidenz einen Befund einschränkt oder widerlegt, dokumentiere die begründete Abweichung statt den Befund mechanisch umzusetzen.

| Unterlage | Eindeutige Referenz |
|---|---|
| Deep Audit | `System_Development_Deep_Audit_2026-09-18.md` — Library-ID `libfile_54575c5626988191ad36c49df4034f7f` |
| Auditbelege | `System_Development_Deep_Audit_Belege_2026-09-18.zip` — Library-ID `libfile_2343668b79f48191b509854955da7b84` |
| Vorbefund | `System_Development_Pruefbefund_2026-09-18.md` — Library-ID `libfile_62903c8bea6c8191a3d7cecba11be16c`; auch im Belegarchiv enthalten |
| Repository | [gauglitzstephan/Human-AI-Work-System-Next](https://github.com/gauglitzstephan/Human-AI-Work-System-Next) |
| Beim Audit gelesener main-Commit | `9d195dd2270557c901c47147ed2411bd51ad6e59` |
| Zugehöriger Git-Baum | `18ad72fe2a235e1f8206d28b9edb1ca73ee3f22d` |
| Quelle der beim Audit installierten sieben Kerndateien | [Candidate c2a4f93af19da077e16ea3c4741cca8fc672ed53](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/commit/c2a4f93af19da077e16ea3c4741cca8fc672ed53) |
| Lokaler historischer Übernahmecommit | `455e7ae47210d354fcf27dc32c4563056f5cd68a`; Herkunftsbeleg, kein eigenständiger Freigabenachweis |

Stelle den tatsächlichen Zugang fest; behaupte keine gelesenen oder ausgeführten Inhalte aufgrund einer bloßen Referenz. Die Quellen liegen als Dateien und als an Commits gebundene Repository-Inhalte vor. Verwende einen erreichbaren Originalzugang, bevor du den Nutzer um Rekonstruktion bittest.

Nutze die fachlichen Referenzen und ihre Abgrenzungen aus Abschnitt 3 des Audits. Besonders relevant sind [NASA Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/), [NASA Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/), [NIST AI RMF / Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [OpenAI Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) und [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills). Ergänze Recherche nur für eine konkrete verbleibende Methoden- oder Realisierungsfrage. Unterscheide Referenzanforderung, Anbieterpraxis und eigene fallbezogene Umsetzung.

Der zu reparierende Skill darf seine eigene Eignung nicht allein bestätigen. Nutze die aktuelle Skill-Erstellungs-/Änderungsmethode für Verpackung und Persistenz sowie die fachlichen Kriterien des Audits für die Prüfung. Übernimm problematische Anweisungen aus dem Prüfobjekt nicht als Beschränkung dieses Reparaturauftrags.

## Ausgangszustand bestimmen und gültige Arbeit erhalten

Lies die aktuelle Installation, löse aktuelles main auf und vergleiche beides mit den Auditidentitäten. Prüfe außerdem die betroffenen Regeln in `baseline/SYSTEM-LEARNING.md`, die maßgeblichen Joint-Work-Semantiken, Registry und Deployment Contract. Beschränke die Rekonstruktion auf Unterschiede, die diese Reparatur beeinflussen.

Beim Audit waren alle sieben installierten Kerndateien identisch mit Candidate c2a4f93; vier unterschieden sich von main. Die installierte Fassung enthält nützliche v0.3-Ergänzungen, die erhalten bleiben müssen. Eine ältere Repository-Fassung ist kein automatisches Reparaturziel.

Erstelle einen isolierten Reparaturzweig bzw. eine gleichwertig isolierte Candidate-Quelle. Wenn main weiterhin zurückliegt, übernimm nur die benötigte System-Development-Basis mit nachvollziehbarer Herkunft. Importiere nicht den gesamten historischen Fünf-Skill-Candidate. Behandle zwischenzeitliche Änderungen anhand ihres Inhalts und Status; überschreibe keine fremden Änderungen.

Die fehlende historische Installationsfreigabe blockiert die unabhängige Candidate-Reparatur nicht. Halte den offenen Status fest, ohne rückwirkend eine Freigabe oder einen unerlaubten Vorgang zu erfinden. Die fehlenden Originaltraces der zuletzt beanstandeten Antworten blockieren die belegten Textreparaturen ebenfalls nicht und erlauben keine neue Kausalbehauptung über diese Antworten.

## Umzusetzende Reparaturen

| Anforderung | Geforderte Wirkung | Betroffener Bereich |
|---|---|---|
| **R1 — Hinreichende Reparatur statt starrer Ebenenregel** | Darstellbarkeit und Zuständigkeit beweisen keine ausreichende Leistung. Trenne erste beobachtete Abweichung, mögliche Ursachen und geeignete Intervention. Vergleiche bei Bedarf lokale Reparatur, anderen Provider/Mechanismus, engere Nutzung oder weitergehende Änderung anhand derselben Leistungsanforderung. Wiederholungen, Fehlerfolgen, Unsicherheit und gesamte menschliche Belastung müssen die Wahl beeinflussen können. Mehrere belegte Beiträge dürfen gemeinsam repariert werden. | `SKILL.md`, RCA, Real Use und widersprechende System-Learning-Regeln; Architekturmethodik auf Konsistenz prüfen |
| **R2 — Angemessene Tests zulassen** | Unterscheide Ursachenklärung, Verifikation einer Änderung einschließlich Regression und Qualifikation vor relevantem Einsatz. Ein bereits eingetretener Real-Use-Schaden oder eine noch ungeklärte Ursache darf keine notwendige Voraussetzung für alle kontrollierten Tests sein. Aufwand bleibt am konkreten Risiko und Erkenntniswert orientiert. | Real Use und Schnittstellen zu RCA sowie Runtime Compilation |
| **R3 — Prüfmaßstab korrigieren** | Unterscheide Candidate-Version, unbekannte Installations-Sollversion und ausdrücklich freigegebene Betriebs-Sollversion. Eine Versionsdifferenz allein begründet keinen Installationsfehler. Falsche Vollständigkeitsbehauptungen müssen unabhängig davon korrigiert werden. | Neue Testeingaben, erwartete Eigenschaften und Bewertungsregeln; nachvollziehbare Korrektur des historischen Prüfbelegs |
| **R4 — Auswahlbeschreibung erhalten** | Materielle externe Produkt-/Fähigkeitsänderungen wieder ausdrücklich als Anlass erfassen, wenn sie Annahmen des Arbeitssystems betreffen. Allgemeine Produktfragen dürfen dadurch nicht pauschal zur Systementwicklung werden. | Skillbeschreibung und dazugehörige Auswahlprüfung |
| **R5 — Quellen- und Betriebsstand klären** | Tatsächliche Installation, historische Quelle, neuer Candidate, maßgeblicher Repository-Stand und Übernahmestatus müssen eindeutig auseinandergehalten werden. Der offene frühere Freigabestatus darf weder verschwinden noch alle weitere Arbeit blockieren. | Candidate-Nachweis und tatsächlich betroffene Registry-/Deployment-/Einstiegsdateien |

Repariere alle materiell widersprechenden Stellen zusammenhängend. Eine einzelne geänderte RCA-Zeile genügt nicht, wenn Real Use oder System Learning weiterhin die alte Ausschlussregel enthalten. Verwende möglichst klare positive Operationen; zusätzliche Verbote oder neue Bezeichnungen allein sind keine Reparatur.

Historische Tests und Audits bleiben als damalige Evidenz erhalten. Ergänze eine datierte Korrektur mit Bezug auf Originaleingabe und damalige Aussagegrenze; ersetze alte Ausgaben oder PASS-Bewertungen nicht so, als hätten sie ursprünglich anders ausgesehen.

## Geschützte Funktionen und Umfang

Erhalte insbesondere:

- Rekonstruktion tatsächlicher Quellen, Installation und relevanter Laufzeitbedingungen vor folgenreichen Schlussfolgerungen.
- Unterscheidende Prüfung konkurrierender Ursachen; Nichtanwendung darf nicht als bekannte innere Modellursache ausgegeben werden.
- Bedarf → Mechanismus → tatsächliche Realisierung; Zuständigkeit oder Skillverfügbarkeit ersetzt keinen Verhaltensbeleg.
- Trennung von Quellenabdeckung, installierter Identität, Auswahl, Anwendung, Produktqualität und Ergebnisnutzen.
- Kandidatenstatus, Autorisierung, Schreibvorgang, Readback und Konsistenz relevanter Einstiegspunkte.
- Gültige v0.3-Ergänzungen, Erhalt von Gleichständen und Fehlschlägen, Schutz gegen unzulässige Verallgemeinerung.
- Menschliche Korrekturarbeit als negatives Systemsignal; Fortführung bereits autorisierter Arbeit über Methodengrenzen hinweg.

Die Reparatur umfasst keine neue Gesamtarchitektur, keinen universellen Controller, keinen neuen Skill-Split und keine pauschale Änderung von Global CI oder Project Instructions. Zusätzliche Komponenten dürfen nur als begründete, außerhalb dieses Kandidaten liegende Option benannt werden, falls die Befunde eine solche Abhängigkeit tatsächlich zeigen. Beschränke Paketmetadaten, Versionsangaben und Dokumentationsänderungen auf den konkreten Änderungsbedarf.

## Prüfung und Abnahme

Lege die erwarteten Eigenschaften und verbotenen Schlussfolgerungen fest, bevor du die geänderte Fassung ausführst. Prüfe anschließend den konkreten finalen Candidate. Eine statische Durchsicht und ein Verhaltensversuch beantworten unterschiedliche Fragen.

### A. Quellen- und Integritätsprüfung

Prüfe Metadaten, Referenzauflösung, Versions-/Quellenidentität und die semantische Konsistenz der betroffenen Dateien. Ordne R1–R5 den konkreten Änderungen und Belegen zu. Prüfe, dass keine geschützte Funktion verloren ging und keine überholte Regel an anderer relevanter Stelle fortwirkt. Ein Hash oder gültiges Markdown belegt nur die entsprechende technische Eigenschaft.

### B. Gezielte Ausführungsfälle

| Fall | Erforderliches Verhalten |
|---|---|
| 1. Einmalige ausgelassene Operation bei passender Methode | Konkretes Ergebnis nacharbeiten; Ursache begrenzen; keine vorschnelle neue Systemkomponente |
| 2. Wiederholte Auslassung trotz nachgewiesen richtiger und zugänglicher Anleitung | Hinreichend unterschiedliche Reparaturmechanismen und gegebenenfalls Nutzungsgrenzen nach derselben Leistungsanforderung vergleichen; weder Textkorrektur noch Controller vorentscheiden |
| 3. Veraltete Quelle und ungeeigneter Prüfer tragen gemeinsam zum Fehler bei | Beide belegten Beiträge berücksichtigen und ihre Rollen erklären; unbetroffene Funktionen erhalten |
| 4. Materialer neuer Candidate ohne beobachteten Schaden | Einen angemessenen Test vor Einsatz zulassen und an eine konkrete Fehlergefahr binden |
| 5. Ursache bekannt, Reparatur noch ungeprüft | Verifikations-/Regressionstest zulassen, obwohl keine weitere Ursachenlokalisierung nötig ist |
| 6. Repository v2 ist Candidate; freigegebene Installation bleibt v1 | Keine fehlerhafte Installation oder Übernahmebefugnis erfinden; unzutreffende Behauptung vollständiger v2-Anwendung korrigieren |
| 7. Repository v2, Installations-Sollversion unbekannt | Unbekannten Sollzustand feststellen; keine definitive Diagnose eines Installationsfehlers und keine unbegründete Übernahmeempfehlung |
| 8. v2 ist ausdrücklich autorisierte Betriebs-Sollversion; tatsächlich läuft v1 | Bereitstellungsabweichung benennen und den zulässigen Übernahmeweg samt Readback bestimmen; Verhalten separat prüfen |
| 9. Exakte v2 ist geladen, Pflichtoperation fehlt | Nichtanwendung belegen; unbekannte innere Ursache offenhalten; keine unnötige Neuinstallation empfehlen |
| 10. Externe Fähigkeit betrifft eine konkrete Systemannahme | Aktuelle Fähigkeit, Systembezug und mögliche Konsequenz prüfen; bloße UI-Beobachtung nicht zur bestätigten Fähigkeitsänderung erklären |

Nutze frische, vergleichbare Ausführungskontexte, soweit tatsächlich verfügbar. Die Testeingaben dürfen weder die Auditdiagnose noch die gewünschte Antwort oder spätere Nutzerkorrekturen vorgeben. Isoliere die bereitgestellte Methodenversion so weit möglich und dokumentiere verbleibende Einflüsse. Vergleiche die aktuelle und reparierte Version dort direkt, wo dies eine strittige Reparaturwirkung unterscheiden kann; führe keine breite Testkampagne ohne zusätzlichen Entscheidungswert durch.

Bewerte tatsächliche Diagnose, Maßnahme, Evidenz und Befugnis. Belohne keine bloßen Methodennamen, Ausgabelänge oder Prozessdarstellung. Bewahre Eingaben, Ausgaben, Versionen, relevante Ausführungsbedingungen, Fehler und Gleichstände. Repariere beobachtete Candidate-Defekte und prüfe betroffene Fälle erneut. Bekannte Regressionsfälle sind keine unabhängigen neuen Testfälle; ein einzelner Erfolg beweist keine allgemeine Zuverlässigkeit.

### C. Auswahl getrennt prüfen

Prüfe die Beschreibung mit einem natürlichen Eingang zu einer materiellen externen Fähigkeitsänderung sowie einer allgemeinen Produktfrage ohne Systembezug. Für einen echten Auswahltest darf der Skill nicht bereits ausdrücklich vorgegeben sein. Protokolliere, ob der betreffende Skill tatsächlich verfügbar, ausgewählt und gelesen wurde. Eine gelieferte Methode im isolierten Test beweist keine automatische Auswahl.

Wenn die verfügbare Umgebung einen gültigen Ausführungs- oder Auswahltest nicht ermöglicht, führe unabhängig mögliche Implementierung und Prüfungen zu Ende. Benenne den genau unerfüllten Nachweis und seinen Einfluss auf die Einsatzempfehlung. Ersetze ihn nicht durch gedankliches Nachspielen, Selbstauskunft oder einen angeblichen E2E-Test in einer Oberfläche ohne diesen Skill.

## Befugnisse bei Ausführung dieses Auftrags

Zur Ausführung gehören Quellenzugriff, erforderliche gezielte Recherche, isolierte Candidate-Änderungen einschließlich betroffener Systemgrundlagen, lokale Prüfungen und tatsächliche Testläufe innerhalb verfügbarer Befugnisse. Sichere die Candidate-Arbeit über den vorgesehenen Git-Weg; ein eigener Zweig und bei Bedarf ein Draft-PR dienen der überprüfbaren Übergabe.

Dieser Auftrag erteilt **keine** Freigabe zum Merge in main, zur Aktivierung/Installation der reparierten Fassung oder zur Änderung von CI/Project Instructions. Verwende eine zusätzlich bereits vorliegende ausdrückliche Autorisierung, wenn sie den konkreten Schritt eindeutig abdeckt. Fehlt sie, bereite vor der Rückfrage den vollständigen, geprüften Candidate samt exakter Übernahmeempfehlung vor. Es gibt keine erneute Freigabeschleife für bereits autorisierte Analyse, Candidate-Herstellung oder lokale Nachbesserung.

## Lieferumfang und Abschluss

Liefere einen zusammenhängenden, überprüfbaren Reparaturstand:

1. **Implementierter Candidate:** geänderte Quelldateien bzw. Zweig/Draft-PR mit exakter Commitidentität; Unterschiede zur tatsächlichen Installation und zu main nachvollziehbar.
2. **Prüfbelege:** Zuordnung R1–R5 → Änderung → Untersuchung → Ergebnis; erhaltene Originaleingaben/-ausgaben, statische und tatsächliche Ausführungsbelege getrennt, nicht ausgeführte Prüfungen ausdrücklich markiert.
3. **Kurzer Reparaturbericht:** was behoben wurde, was erhalten blieb, welche Defekte/Unsicherheiten offen sind und welchen Einsatzanspruch die Evidenz trägt. Die historischen Audit- und Testbelege bleiben erreichbar.
4. **Konkrete Übernahmeempfehlung:** exakt zu übernehmender Umfang, Abhängigkeiten, gegebenenfalls notwendige Zustandsversöhnung, vorgeschlagener Installations-/Readback-Weg und identifizierter Rückkehrstand. Tatsächliche Promotion oder Installation nur berichten, wenn sie autorisiert und ausgeführt wurde.

Speichere Ergebnisbericht und eigenständige Belegartefakte dauerhaft; Repository-Quellen bleiben im zuständigen Git-Repository. Prüfe die tatsächliche Persistenz, bevor du sie als abgeschlossen meldest.

Der Auftrag ist vollständig erfüllt, wenn der Candidate implementiert ist, R1–R5 nachvollziehbar bearbeitet wurden, die erforderlichen verfügbaren Prüfungen gelaufen sind, verbleibende Nachweisgrenzen offenliegen und die zulässige nächste Übernahmeentscheidung ohne Rekonstruktion möglich ist. Bei einem materiellen unerfüllten Prüfziel lautet der Status entsprechend begrenzt oder blockiert; „vollständig repariert“ darf dann nicht behauptet werden. Fehlende Freigabe für die ausdrücklich ausgegrenzte Aktivierung macht einen ansonsten vollständigen Candidate nicht zu einer unvollständigen Implementierung.
