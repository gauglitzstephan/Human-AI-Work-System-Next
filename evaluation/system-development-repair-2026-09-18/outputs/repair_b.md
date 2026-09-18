# Reparaturentscheidungen anhand des vollständigen Dossiers

Die drei Fälle sind unabhängig. Grundlage sind ausschließlich das jeweilige Dossier und die unten dokumentierte Methodenfamilie. Alle Aussagen über tatsächlichen Zustand beziehen sich auf dessen Darstellung im Dossier. Es wurden keine realen Konten, Repositorys oder Installationen verändert.

## Fall 1 — Entscheidungsmemo vervollständigen

### Diagnose und Entscheidung

Der Entwurf erfüllt den Auftrag nicht vollständig: „Wir wählen A“ enthält die verlangte Umstiegsbedingung nicht. Die richtige Methode enthält diese Anforderung und wurde vollständig gelesen. Damit liegt die erste belegte Abweichung bei ihrer Anwendung beziehungsweise der Überführung in das Memo. Eine fehlende Regel oder falsche Methodenversion ist nach dem Dossier keine tragfähige Erklärung. Warum die Anforderung intern ausgelassen wurde, ist nicht belegt.

Die Sachentscheidung A bleibt richtig. Beide Alternativen erfüllen dieselben Anforderungen; A kostet monatlich 80 Euro, B 100 Euro. A spart damit 20 Euro pro Monat. B ist der stärkste verfügbare Rivale; weitere Alternativen sind im vollständigen Dossier nicht enthalten. Die Schwelle lautet genau **A ≤ B**: Bei Preisgleichheit bleibt A zulässig. Ein Wechsel zu B ist erforderlich, sobald A teurer als B ist. Wechselkosten verändern diese Schwelle nicht, weil sie null sind.

### Konkrete Korrektur

Den unvollständigen Schluss durch folgenden entscheidungsfähigen Text ersetzen:

> Wir wählen A. A und der stärkste Rivale B erfüllen dieselben Anforderungen. Mit 80 Euro statt 100 Euro pro Monat ist A monatlich 20 Euro günstiger. Die Wahl gilt, solange A höchstens so teuer wie B ist; bei Preisgleichheit bleiben wir bei A. Sobald A mehr als B kostet, wechseln wir ohne Wechselkosten zu B. Bei einem unveränderten Preis von B liegt die Umstiegsschwelle somit oberhalb von 100 Euro pro Monat für A. Mit den verbindlichen Vergleichspreisen ist diese Bedingung derzeit nicht erfüllt.

Danach genügt eine gezielte Prüfung des korrigierten Memos: Sind beide Alternativen, die gemeinsame Anforderungserfüllung, die 20-Euro-Differenz und die Bedingung einschließlich Gleichheit korrekt enthalten? Der vorstehende Text erfüllt diese Punkte. Eine neue Methode, globale Regel, zusätzliche dauerhafte Prüfinstanz oder Architekturänderung ist nicht erforderlich.

### Grenze des Nachweises

Das Ergebnis ist für die vollständigen angegebenen Sachwerte berechnet und die konkrete Auslassung textlich behoben. Das erste dokumentierte Versäumnis in zwölf vergleichbaren Aufgaben begründet diese lokale Reparatur, aber keine allgemeine Behauptung über Zuverlässigkeit oder eine strukturell defekte Architektur. Die korrigierte Formulierung beweist auch nicht, dass künftige Aufgaben die Bedingung automatisch berücksichtigen. Bei weiterer echter Nutzung ist auf Wiederholung zu achten, ohne dafür ein zusätzliches ständiges Verfahren einzurichten.

## Fall 2 — Ausführungsweg begrenzt ersetzen oder technisch absichern

### Diagnose

In vier von fünf unabhängigen Durchläufen wurden harte Ausschlusskriterien übergangen: **80 % der beobachteten Durchläufe** verfehlten diese Eigenschaft. Das ist eine Beschreibung der kleinen vorliegenden Stichprobe, keine verlässlich geschätzte zukünftige Fehlerwahrscheinlichkeit. Anders als in Fall 1 ist die unveränderte Verwendung dieses Arbeitswegs für endgültige Leistungszusagen durch wiederholte Fehler und deren Folgen nicht tragfähig.

Die gültige Quelle war vollständig, zugänglich und in jedem Durchlauf nachweislich gelesen. Fehlende Quelle, fehlender Zugang und eine bloß unterlassene Lektüre erklären das dokumentierte Muster daher nicht. Die erste belegte Abweichung ist die tatsächliche Durchsetzung der gelesenen Ausschlusskriterien im Ergebnis. Ob das intern an Interpretation, Aufmerksamkeit, Schlussbildung oder einer anderen nicht sichtbaren Ursache liegt, bleibt offen. Das Symptom wird nicht als nachgewiesene interne Grundursache ausgegeben.

Zwei ergänzte Erinnerungen änderten das Muster nicht. Eine weitere gleichartige Erinnerung ist deshalb keine hinreichend begründete Reparatur. Die vermeidbare menschliche Nacharbeit und das Risiko nicht erfüllbarer Zusagen rechtfertigen einen Eingriff in den konkreten Ausführungsweg; eine umfassende Architekturänderung folgt daraus nicht.

### Entscheidung und Alternativen

**Sofort tragfähig ist die engere Nutzung ohne endgültige Zusagen.** Der bisherige Weg darf vorbereitende Ergebnisse liefern, aber allein keinen Vorgang als zusagefähig freigeben. Als nächster Ersatzkandidat wird der zugängliche spezialisierte Anbieter an vergleichbarer Arbeit geprüft. Seine zwei korrekten Fälle und der passende Dateityp begründen den Versuch, noch keine unbeaufsichtigte Freigabe. Parallelität der Prüfung ist nicht erforderlich.

| Ausführungsroute | Konkrete Wirkung und vorhandene Evidenz | Entscheidung beziehungsweise offene Voraussetzung |
|---|---|---|
| Bisheriger Weg mit weiteren Erinnerungen | Soll dasselbe Auslassen durch zusätzliche Hinweise verhindern; zwei Erinnerungen wirkten bereits nicht | Als alleinige Absicherung endgültiger Zusagen verwerfen |
| Bisheriger Weg mit engerem Auftrag | Verhindert endgültige Zusagen durch Begrenzung der zulässigen Verwendung; verbessert nicht automatisch die inhaltliche Qualität | Unmittelbare, begrenzte Weiterverwendung ist möglich |
| Spezialisierter Anbieter | Bearbeitet die fachliche Aufgabe; zwei vergleichbare Ergebnisse korrekt, Zugang und benötigter Dateityp vorhanden, 4 Euro pro Fall | Bevorzugter unmittelbar erprobbarer Ersatzkandidat; Ausschlussprüfung und tatsächlicher Nacharbeitsbedarf noch bestätigen |
| Vorhandenen strukturierten Schritt anpassen | Kann die harten Kriterien explizit auswerten und eine Freigabe bei Verstoß oder unzureichenden Daten blockieren | Wiederverwendung sinnvoll, wenn vollständige Kriterienabbildung und zuverlässige Eingangsdaten nachgewiesen werden; die bisherige Prüfung anderer Kriterien genügt nicht |

Eine Kombination aus Anbieter und strukturiertem Schritt ist nur dann gerechtfertigt, wenn beide nachweislich unterschiedliche verbleibende Aufgaben erfüllen. Ein Anbieterwechsel mit zusätzlicher Dauerprüfung wird nicht allein deshalb eingeführt, weil beide Mittel verfügbar sind.

### Ausführbarer nächster Schritt

1. **Die gewünschte Eigenschaft festlegen:** Jeder Fall muss gegen alle maßgeblichen harten Ausschlusskriterien geprüft werden. Ein verletztes Kriterium sperrt die Zusage. Ein nicht entscheidbares Kriterium oder fehlende erforderliche Daten erlauben keine positive Freigabe. Quelle, Eingabefassung und Ergebnis müssen demselben Fall zugeordnet bleiben.
2. **Den Anbieter gezielt erproben:** Die ursprünglichen Eingaben und die gültige Quelle der dokumentierten Fälle bereitstellen, ohne spätere Korrekturen oder erwartete Antworten mitzugeben. Seine Ergebnisse anhand derselben Ausschlusskriterien bewerten und Fehler sowie Nacharbeitsminuten festhalten. Die historischen Fälle sind Regressionen; für eine Aussage über neue Arbeit anschließend frische vergleichbare Fälle unter der begrenzten Verwendung beobachten. Vorher die Kriterien festlegen, an denen der Einsatz entschieden wird, statt nur korrekte Dateiform oder überzeugenden Text zu bewerten.
3. **Die strukturierte Alternative auf Realisierbarkeit prüfen:** Für jedes harte Kriterium die erforderlichen Datenfelder, deren maßgebliche Quelle und eine eindeutige Entscheidungsregel abbilden. Die Vollständigkeit und Richtigkeit dieser Eingaben einschließlich einer etwaigen Extraktion müssen prüfbar sein. Die ungeprüfte Einschätzung des bisher auslassenden Arbeitswegs darf nicht einfach zum vermeintlich zuverlässigen Eingang werden. Lässt sich diese Voraussetzung nicht erfüllen, ist die maschinelle Route als alleinige Reparatur nicht qualifiziert.
4. **Bei erfüllter Datenvoraussetzung den vorhandenen Schritt gezielt erweitern:** Er soll drei unterscheidbare Ergebnisse liefern: „Kriterien erfüllt“, „ausgeschlossen“ und „nicht entscheidbar“. Nur das erste darf die Kriterienprüfung passieren; es ist noch keine eigenständige Autorisierung einer Leistungszusage. Mit belegten erfüllenden, ausschließenden und unvollständigen Eingaben prüfen, ob die neue Abbildung korrekt arbeitet und Verletzungen tatsächlich blockiert. Bisher gültige Prüfungen erhalten und bei betroffenen Abhängigkeiten mitprüfen.
5. **Die Route nach Leistung und Gesamtaufwand wählen:** Kriterienabdeckung, falsche Freigaben, Rückgabeintegration im benötigten Dateityp, menschliche Nacharbeit sowie laufenden und einmaligen Aufwand vergleichen. Den Anbieter breiter einsetzen, wenn diese Prüfung seinen Einsatz trägt; den strukturierten Schritt als bevorzugte technische Absicherung einsetzen, falls dessen Datenbasis und Regelabbildung belastbar sind. Bis zur jeweiligen Qualifikation bleibt die engere Nutzung bestehen. Eine dauerhafte menschliche Reparaturschicht ist keine gelöste Automatisierung.

Die konkreten Ausschlusskriterien und Falldaten stehen nicht im Dossier. Deshalb sind diese Schritte ausführbare Prüf- und Anpassungsaufträge, aber weder die Durchführung des Anbietervergleichs noch eine fertige maschinelle Kriterienimplementierung.

### Berechenbarer Aufwand und Nachweisgrenze

Bei durchschnittlich 18 Minuten Nacharbeit je Fall ergeben sich für fünf Fälle **90 Minuten**. Fünf Anbieterfälle kosten **20 Euro**. Würde der Anbieter die gesamten 18 Minuten je Fall einsparen und keinen weiteren Aufwand erzeugen, entsprächen vier Euro je Fall einem Zeitwert von **13,33 Euro pro Stunde**. Erst oberhalb dieses Zeitwerts wäre er unter diesen Annahmen günstiger als die bisherige Nacharbeit. Tatsächliche Einsparung, verbleibende Prüfung, Einrichtungskosten und ein Geldwert der menschlichen Zeit sind nicht gegeben; eine nachgewiesene Kostenersparnis lässt sich deshalb nicht behaupten. Das Risiko falscher Zusagen bleibt ein zusätzliches Entscheidungskriterium.

Zwei korrekte Anbieterfälle belegen nur diese Fälle. Die vorhandene maschinelle Prüffähigkeit belegt weder passende neue Regeln noch verlässliche Eingaben. Ein bestandener begrenzter Vergleich belegt nur die geprüften Konstellationen; Bewährung in weiterer tatsächlicher Arbeit bleibt erforderlich. Eine exakte interne Ursache des Auslassens muss für diese begründete Begrenzung und Erprobung nicht erfunden werden.

## Fall 3 — Rechenquelle aktualisieren und die Prüfung auf den Sachanspruch ausrichten

### Diagnose und korrigiertes Ergebnis

Es bestehen zwei getrennte Fehler:

1. **Zustands- und Aktualisierungsfehler:** Das autorisierte Update auf die freigegebene Quelle v2 wurde im installierten und geladenen Zustand nicht wirksam. Die erste belegte Abweichung liegt vor der Rechnung: Aktiv blieb v1. Ob Schreiben, Auswahl, Aktualisierung eines Verweises oder erneutes Laden scheiterte, ist im Dossier nicht unterscheidbar. Die Rechnung 70 ist mit den v1-Werten rechnerisch richtig, für den freigegebenen aktuellen Auftrag aber falsch.
2. **Ungeeignete fachliche Prüfung:** Das Vorhandensein zweier Produktzeilen prüft weder Preise noch Mengen, Summe oder Aktualität. Dass auch 999 akzeptiert wurde, ist ein unmittelbarer Gegenbeleg zur behaupteten sachlichen Prüfung. Die Prüfung ist für die Aussage „geprüft und aktuell“ nicht ausreichend.

Aus der maßgeblichen v2 ergibt sich:

| Produkt | Preis laut v2 | Menge | Teilbetrag |
|---|---:|---:|---:|
| A | 12 | 3 | 36 |
| B | 8 | 5 | 40 |
| **Gesamt** | | | **76** |

**12 × 3 + 8 × 5 = 76.** Der bisherige Gesamtpreis 70 liegt um **6** zu niedrig. Eine Währung ist für diesen Fall nicht angegeben.

Den Bericht sachlich wie folgt korrigieren:

> Nach der freigegebenen Rechenquelle v2 beträgt der Gesamtpreis 76: A trägt bei einem Preis von 12 und einer Menge von 3 den Teilbetrag 36 bei; B trägt bei einem Preis von 8 und einer Menge von 5 den Teilbetrag 40 bei. Die bisher berichteten 70 wurden mit dem veralteten Preis für A aus v1 berechnet. Die korrigierte Rechnung ist anhand der im Dossier angegebenen v2-Werte nachvollzogen. Die tatsächliche Installation und das Laden von v2 sowie die Ausführung einer geeigneten fachlichen Prüfung sind anhand dieses Dossiers noch nicht nachgewiesen.

Die pauschale bisherige Aussage „geprüft und aktuell“ wird damit ersetzt, nicht lediglich neben dem neuen Wert stehen gelassen.

### Ausführbare Reparatur des Arbeitswegs

1. **Die bereits autorisierte Änderung vollständig ausführen, sobald die realen Dateien vorliegen:** Die freigegebene v2 an den vorgesehenen aktiven Zielort bringen und den betroffenen Ladevorgang auf diese Fassung ausrichten. Dazu die tatsächliche Quelle, den installierten Träger und die im Berechnungslauf geladenen Daten getrennt identifizieren. Eine weitere Freigabe desselben bereits autorisierten Updates ist nicht nötig.
2. **Den aktiven Zustand zurücklesen:** Nicht nur die abgelegte Quelldatei oder ein Versionsetikett ansehen, sondern den tatsächlich geladenen Inhalt mit v2 vergleichen: A=12, B=8, Mengen A=3 und B=5. Eine genaue Dateiidentität, etwa durch Inhaltsvergleich oder Hash, kann diesen Abgleich unterstützen. Sie ersetzt den Nachweis nicht, dass der betreffende Lauf genau diese Fassung verwendet. Falls aktive Verweise, Manifeste oder Einstiegspunkte v1 auswählen, nur diese betroffenen Stellen berichtigen und erneut zurücklesen. v1 darf als eindeutig historische Fassung erhalten bleiben, ohne als aktive Quelle auswählbar zu erscheinen.
3. **Den Bericht aus der bestätigten aktiven v2 neu erzeugen:** Beide Teilbeträge und die Gesamtsumme übernehmen. Betroffene abgeleitete Aussagen korrigieren; nicht betroffene Inhalte erhalten.
4. **Die fachliche Prüfung um die fehlenden Eigenschaften ergänzen:** Eingabepreise und Mengen unabhängig gegen die freigegebene v2 prüfen, Teilbeträge und Gesamtsumme nachvollziehen und die Quellenidentität des tatsächlichen Berichtslaufs kontrollieren. Dieselbe möglicherweise veraltete aktive Eingabe bloß ein zweites Mal zu summieren würde Aktualität nicht prüfen.
5. **Die Prüfung gezielt widerlegbar erproben:** Der korrekte v2-Bericht mit 76 muss bestehen. Ein ansonsten gleich aussehender Bericht mit 999 muss an der Summenprüfung scheitern. Ein v1-Lauf mit 70 muss an Quellen-/Werteaktualität scheitern, obwohl seine interne Rechnung stimmt. Auch ein als v2 beschrifteter Bericht mit A=10 darf den Werteabgleich nicht bestehen. Diese Gegenproben prüfen genau die im Dossier sichtbaren Lücken; sie sind keine allgemeine Testkampagne.
6. **Nur passende Erfolgsaussagen zurückgeben:** „Aktualisiert“ erst nach dem Rücklesen des aktiven Zustands; „fachlich geprüft“ erst nach wirksamer Prüfung am daraus erzeugten Bericht. Die Dateiablage, der Ladevorgang, die korrekte Rechnung und die funktionierende Prüfung sind getrennte Nachweise.

### Erhaltbare Teile und Grenze des Nachweises

Die fachliche Freigabe von v2, der autorisierte Updateauftrag, Preis B=8, beide Mengen und die grundlegende Berechnung als Summe der Preis-Mengen-Produkte bleiben verwendbar. Die Prüfung auf zwei Produktzeilen kann als Strukturprüfung erhalten bleiben; ihre Aussage reicht ausschließlich bis zum Vorhandensein dieser Zeilen. Eine bestehende Berichtsstruktur kann ebenfalls erhalten bleiben, soweit sie die richtigen Werte und begrenzten Prüfaussagen darstellen kann. Es gibt keinen Beleg, dass eine umfassende Systemneugestaltung nötig wäre.

**Hier abgeschlossen sind die rechnerische und textliche Berichtskorrektur sowie die Eingrenzung der beiden Fehler.** Die tatsächlichen Dateien sind nur im Dossier repräsentiert. Deshalb wurden Installation, Laden, erneute Berichtserzeugung und Gegenproben nicht ausgeführt und können nicht als erfolgreich bescheinigt werden. Ihre bereits autorisierte Durchführung benötigt die realen Zielartefakte, nicht eine neue inhaltliche Freigabe. Die genaue technische Ursache des ausgebliebenen Updates bleibt bis zur dortigen Zustandsprüfung offen.

## Tatsächlich gelesene Methodenpfade

- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/SKILL.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/RCA-FAILURE-LOCALIZATION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/SYSTEM-ARCHITECTURE-REQUIREMENTS-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/RUNTIME-COMPILATION-SEMANTIC-REGRESSION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/REPOSITORY-PROMOTION-READBACK-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/REAL-USE-VALIDATION-METHOD.md`
