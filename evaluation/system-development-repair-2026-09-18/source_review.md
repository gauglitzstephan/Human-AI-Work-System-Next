# Quellenreview des Reparaturkandidaten

**Datum:** 2026-09-18  
**Prüfobjekt:** `/workspace/scratch/cda19bcc7083/repair_candidate`, gelesener Zwischenstand vor den unten empfohlenen Korrekturen.  
**Auftrag:** statischer Review gegen `System_Development_Reparaturauftrag_2026-09-18.md`, insbesondere R1–R5, Schutzfunktionen, Reichweite und materielle Verpackungsfehler.  
**Umfangsgrenze:** Keine Laufoutputs gelesen und keine Verhaltens-, Auswahl- oder Installationsaussage geprüft. Receipt, Bewertungen und historische Korrekturbelege waren noch in Arbeit; ihre Abwesenheit wird nicht als Skilldefekt bewertet. Keine Änderung am Kandidaten vorgenommen.

## Ergebnis

**Ein materieller Restbefund mittlerer Schwere an zwei Stellen.** Die eigentlichen Operationen korrigieren die zentralen Ebenen- und Testregeln schlüssig. Zwei beibehaltene Fehlermoden sind dagegen noch unqualifiziert und können hinreichend begründete Interventionen erneut ausschließen. Eine eng begrenzte Präzisierung genügt; ein weiterer Methodenumbau ist dadurch nicht begründet.

Für den Anspruch „alle materiell widersprechenden R1-Stellen konsistent repariert“ ist dieser gelesene Zwischenstand `NOT_FIT_FOR_STATED_USE`. Das Urteil betrifft die beiden unten genannten Passagen, nicht die Brauchbarkeit aller anderen Methoden. Laufzeitwirkung, automatische Auswahl und Einsatzzuverlässigkeit bleiben durch diesen Quellenreview unbelegt.

## SR-01 — Fehlermoden begrenzen weiterhin die Intervention nach ihrer Form

**Schwere: mittel.** Direkter Textbefund; mögliche Fehlsteuerung einer hinreichenden Reparatur. Kein Nachweis, dass ein tatsächlicher Lauf dadurch fehlgeschlagen ist.

### Fundstellen und exakte Passagen

1. `skills/system-development/references/RCA-FAILURE-LOCALIZATION-METHOD.md`, Abschnitt `Failure modes`, Zeile 50:

   > process/agents added to compensate for a provider/tool problem;

2. `skills/system-development/references/EXISTING-SYSTEM-RECOVERY-METHOD.md`, Abschnitt `Failure modes`, Zeile 36:

   > new architecture replacing a local repair;

### Kriterium und Konsequenz

R1 verlangt, lokale Reparatur, anderen Provider/Mechanismus, engere Nutzung und gegebenenfalls weitergehende Änderung an derselben erforderlichen Leistung zu beurteilen. Zuständigkeit und der Ort des Problems dürfen die geeignete Intervention nicht vorentscheiden. Diese beiden Fehlermoden nennen jedoch weder fehlende Wirksamkeit noch fehlende Begründung als Bedingung der Fehlklassifikation.

Die erste Passage typisiert bereits das Hinzufügen eines Prozesses oder Agenten zur Kompensation eines Provider-/Toolproblems als Fehler. Ein eng begrenzter, nachweislich wirksamer Ausführungs- oder Prüfmechanismus kann bei einer dokumentierten Providergrenze aber gerade eine der hinreichenden Alternativen sein. Das steht in Spannung zu RCA Schritt 6, der Ausführungsmechanismen ausdrücklich in den Vergleich aufnimmt.

Die zweite Passage nennt schon das Ersetzen einer lokalen Reparatur durch Architektur als Fehler, ohne zu verlangen, dass die lokale Reparatur die benötigte Leistung tatsächlich ausreichend herstellt. Eine lokale Nacharbeit kann einen einzelnen Output korrigieren und beim wiederholten Problem dennoch unzureichend sein. Der unqualifizierte Satz kann damit die neue Unterscheidung zwischen vorhandenem lokalen Eingriff und hinreichender Intervention wieder aufheben.

Eine wohlwollende Gesamtlektüre kann beide Sätze als Warnungen nur vor *unbegründetem* Ausbau verstehen. Die einschränkende Bedingung steht jedoch nicht in den Passagen. Weil der Auftrag ausdrücklich auch verteilte normative Widersprüche beseitigen soll, ist diese Restspannung materiell und nicht nur stilistisch.

### Kleinste hinreichende Korrektur

Beide Fehlermoden auf **nicht gerechtfertigte oder nicht hinreichend wirksame** Ausweitung eingrenzen. Zum Beispiel:

- RCA: `process/agents added for a provider/tool problem without evidence that the added mechanism sufficiently addresses it and earns its burden against credible alternatives;`
- Recovery: `new architecture replacing an adequate local repair without a demonstrated performance or burden benefit;`

Diese Änderungen erhalten den Schutz vor unnötigem Ausbau und lassen die bereits positiv beschriebene, evidenzgebundene Wahl eines anders platzierten Mechanismus zu. Sie autorisieren selbst keine Architekturänderung.

## Erhaltene und konsistent reparierte Eigenschaften

| Bereich | Quellenbefund |
|---|---|
| R1, Hauptoperationen | SKILL, RCA, Real Use, Architektur, System Learning und Operating Baseline wählen eine hinreichend wirksame Intervention; Wiederholung, Folgen, Unsicherheit und Human-Aufwand sind berücksichtigt. Mehrere Beiträge dürfen gemeinsam repariert werden. Ausnahme: SR-01. |
| R2 | Real Use und System Learning erlauben Ursachenklärung, Änderungs-/Regressionsverifikation und Qualifikation vor Einsatz ausdrücklich. Vorheriger Schaden und unbekannte Ursache sind für die letzten beiden Zwecke keine Voraussetzungen. Kein Widerspruch zur unveränderten Runtime-Compilation-Methode festgestellt. |
| R3, normative Methode | RCA trennt Candidate, unbekannte bzw. begründete Betriebs-Sollversion und tatsächliche Installation. Die v1/v2-Beispiele unterscheiden die drei Sollzustände sowie geladene v2 mit Nichtanwendung. Falsche v2-Anwendungsbehauptungen bleiben unabhängig davon korrigierbar. Bewertung neuer Tests und historische Korrekturbelege wurden nicht geprüft. |
| R4 | Die Auswahlbeschreibung nennt materielle externe Produkt-/Fähigkeitsänderungen wieder ausdrücklich und begrenzt sie auf aktive Systemannahmen oder Arbeitswege. Recovery unterscheidet bestätigte Änderung, UI-Beobachtung und unbestätigten Bericht. Das belegt Beschreibungseignung, keine tatsächliche Auswahl. |
| R5, verfügbare Quellen | CURRENT, README, Registry und Deployment Contract unterscheiden die historische Installation, Candidate-Herkunft, neue Reparatur und nicht erfolgte Übernahme. Die ungeklärte historische Freigabe bleibt offen, ohne daraus Unautorisiertheit oder eine Arbeitssperre abzuleiten. Exakte Finalidentität und Receipt sind nach Fertigstellung gesondert zu prüfen. |
| v0.3-Erhalt | Unterscheidende Ursachenprüfung, Begrenzung unbekannter innerer Ursachen, Realisierung jenseits bloßer Zuständigkeit, vergleichbare Kontexte, zurückgehaltene erwartete Antwort, Gleichstände/Fehlschläge und Schutz vor Verallgemeinerung bleiben gegenüber der installierten Fassung erhalten. |
| Befugnisse und Ergebnisfortführung | Candidate, Autorisierung, Schreiben, Readback und Einstiegspunktkonsistenz bleiben getrennt. SKILL führt bereits autorisierte Implementierung durch Änderung und Prüfung fort. Neue Freigabe-, Controller- oder Skill-Split-Pflichten wurden nicht eingeführt. |

## Verpackung und Reichweite

Keine weitere materielle Verpackungsregression festgestellt. Die sechs Methodenlinks aus SKILL lösen im Kandidaten auf. Die operative Quelle bleibt ein Skill mit sechs Referenzmethoden. Die beiden unveränderten Methoden für Promotion/Readback und Runtime Compilation behalten ihre geschützten Trennungen und Prüfregeln.

Der geprüfte lokale Baum ist nach Klärung mit dem Hauptbearbeiter eine selektive Repository-Überlagerung, kein vollständiger Repository- oder Personal-Skill-Installationssatz. `agents/openai.yaml` und `assets/icon.svg` aus der Installation sollen unverändert bleiben. Ihr Fehlen im Überlagerungsbaum ist daher kein Lösch- oder Verpackungsbefund. Ebenso werden fehlende Dateien außerhalb der selektiv abgebildeten Repository-Basis nicht als neu eingeführte kaputte Referenzen bewertet. Die tatsächliche Übernahme muss diesen begrenzten Umfang beibehalten.

Die zusätzlichen Änderungen an Operating Baseline, System Learning und den Einstiegspunkten sind durch verteilte R1-Regeln bzw. R5 gedeckt. Die Plugin-Versionsangabe 0.2.3 wird ausdrücklich als Quellenpaketidentität und nicht als Installationsnachweis geführt. Keine Änderung an Global CI, Project Instructions, CJS oder Native Work Transition festgestellt.

## Identität des gelesenen operativen Zwischenstands

Alle Pfade relativ zu `repair_candidate/skills/system-development/`; SHA-256:

| Datei | SHA-256 |
|---|---|
| SKILL.md | `cf007e6aaf0555836c3ace020958e2f0f3322a2cc8a4a84694ffa7773877aea2` |
| references/EXISTING-SYSTEM-RECOVERY-METHOD.md | `139722a0b674392725e927991acc193b563e6f5bae081d06428660e2f27c7695` |
| references/RCA-FAILURE-LOCALIZATION-METHOD.md | `7ced72f6d102a5ed9aa9e943943aa89af11c3e901827b14d3a87c87e4fb71937` |
| references/REAL-USE-VALIDATION-METHOD.md | `417072245d788d35cd24f3591fb64b5b757fe0041859374e8b2b27d201f6e650` |
| references/REPOSITORY-PROMOTION-READBACK-METHOD.md | `d57864095eaf50abc9f2b9edb7ed05f0a94d7cb24c730faa9164b8fafeb1d83e` |
| references/RUNTIME-COMPILATION-SEMANTIC-REGRESSION-METHOD.md | `9155ced5e6a1c4180183da250121b53953ca5b8563953c790b2e7252feccfe48` |
| references/SYSTEM-ARCHITECTURE-REQUIREMENTS-METHOD.md | `6860368ec90fbf961869e2a72ea5a7029e0082e7d11f4ee7e8eb63a555a1dc13` |

## Prüfgrundlage und Aussagegrenze

Gelesen wurden der Reparaturauftrag, die materiellen Auditbefunde und Kriterien, alle sieben operativen Candidate-Dateien, die einschlägigen System-Learning-/Operating-/CJS-Regeln und die aktuellen Status-/Deploymenttexte. Differenzen wurden gegen `audit_evidence/installed` und den selektiven `audit_evidence/repository`-Snapshot geprüft. Die Bewertung nutzt die Disziplin von evaluate-work-product; die materiellen Kriterien stammen aus dem Auftrag und dem Audit, nicht aus einer Selbstauskunft des Zielskills.

Der Review ersetzt weder Finalpaketprüfung noch Ausführungs- oder Auswahlnachweise. Er bestätigt insbesondere keine allgemeine Zuverlässigkeit, aktuelle Repository-Persistenz, Mergefreigabe oder Installation. Weitere Gegenprüfung ist nach der kleinen SR-01-Korrektur auf die geänderten Stellen und betroffenen Ansprüche zu begrenzen.
