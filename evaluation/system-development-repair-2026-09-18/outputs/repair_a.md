# Beurteilung und Reparatur der drei fiktiven Fälle

Grundlage ist ausschließlich das vollständige Dossier. Die Fälle sind unabhängig. Die folgenden Korrekturen betreffen die im Dossier dargestellten Ergebnisse; vorgeschlagene Änderungen an Arbeitswegen sind nicht in einer realen Installation ausgeführt worden.

## Fall 1 — Entscheidungsmemo vervollständigen

**Diagnose und Entscheidung.** Die Entscheidung für A ist sachlich richtig, aber unvollständig begründet: Die ausdrücklich geforderte Umstiegsbedingung fehlt. Die richtige Methode ist vollständig gelesen worden und enthält die Operation. Damit liegt die erste belegte Abweichung in ihrer Anwendung auf das Memo, nicht in einer fehlenden Methodenanforderung. Warum diese Anwendung unterblieb, ist nicht sichtbar. Ein erstmaliges dokumentiertes Versäumnis unter zwölf vergleichbaren Aufgaben begründet eine lokale Korrektur und keine generelle Änderung der Methode oder Arbeitsarchitektur.

**Unmittelbar verwendbare Korrektur des Schlusses:**

> Wir wählen A. A und B erfüllen dieselben Anforderungen; A kostet 80 Euro und B 100 Euro pro Monat. A spart damit 20 Euro pro Monat. B ist die maßgebliche Alternative. Wir behalten A, solange A höchstens so teuer wie B ist; bei Preisgleichheit bleibt es bei A. Sobald A teurer als B wäre, wechseln wir ohne Wechselkosten zu B. Bei einem unveränderten Preis von B liegt die Umstiegsbedingung somit bei einem A-Preis von mehr als 100 Euro pro Monat. Die verbindlichen Preise dieses Vergleichs lösen keinen Wechsel aus.

**Angemessene Prüfung.** Am korrigierten Absatz lassen sich Alternative, Erfüllung der Anforderungen, Preisvergleich und strenge Umstiegsschwelle direkt kontrollieren: 80 < 100 ergibt A; 100 = 100 würde weiterhin A ergeben; A > B würde B ergeben. Die beiden letzteren Aussagen prüfen die Entscheidungsregel hypothetisch und behaupten keine Änderung der verbindlichen Preise. Damit ist die ausgelassene Arbeit erledigt. Eine zusätzliche Erinnerung, Neuinstallation oder neue Prüfinstanz ist für diesen Befund nicht erforderlich.

**Nachweisgrenze.** Belegt sind die richtige Entscheidung und die vollständige Regel für diesen Fall. Die Häufigkeit ist ein dokumentiertes Vorkommnis unter zwölf Aufgaben, keine belastbare allgemeine Fehlerquote und kein Nachweis eines strukturellen Defekts. Auch die interne Ursache des Auslassens ist damit nicht erklärt.

## Fall 2 — Wiederholte Auslassung wirksam begrenzen und den Mechanismus ändern

**Diagnose.** Vier von fünf unabhängigen Durchläufen übergehen Ausschlusskriterien: beobachtet sind 80 Prozent Fehler in dieser kleinen Serie. Die gültige Quelle wurde nach aufgezeichnetem Readback jedes Mal vollständig gelesen. Fehlende Zugänglichkeit oder ungelesene Anforderungen erklären den Befund daher nicht. Die erste belegte Abweichung ist die Nichtanwendung der Kriterien bei der Ergebnisbildung beziehungsweise Freigabe. Eine bestimmte interne Modellursache ist nicht nachgewiesen. Zwei wirkungslose Erinnerungen sprechen gegen eine dritte Erinnerung als tragfähige Reparatur. Wiederholung, 18 Minuten menschliche Nacharbeit pro Fall und mögliche nicht erfüllbare Leistungszusagen rechtfertigen eine Änderung des tatsächlichen Ausführungs- und Freigabewegs.

**Vergleich der materiellen Handlungswege:**

| Arbeitsweg | Wirkung auf den belegten Fehler | Entscheidung und offene Bedingung |
|---|---|---|
| Bisheriger Weg mit weiterer Erinnerung | Kein neuer Mechanismus; die bisherigen Erinnerungen änderten das Muster nicht | Nicht als Reparatur wählen |
| Bisherige Bearbeitung mit angepasster maschineller Ausschlussprüfung vor einer Freigabe | Kann harte Kriterien unabhängig vom Auslassen im Text prüfen und eine unzulässige Freigabe verhindern | Bevorzugter Reparaturkandidat; Kriterienabbildung, verlässliche Eingangsdaten und tatsächliche Sperrwirkung müssen nachgewiesen werden |
| Spezialisierter Anbieter als Ersatz für die bisherige Bearbeitung | Zwei korrekte vergleichbare Fälle liefern ein positives, begrenztes Anwendungssignal; Zugang und Dateityp passen | Ernsthafte Alternative, insbesondere wenn die strukturierte Prüfung nicht zuverlässig gespeist werden kann; zwei Fälle qualifizieren noch keine endgültigen Zusagen |
| Engere Nutzung ausschließlich für Entwürfe ohne endgültige Zusagen | Begrenzt die Folgen, beseitigt das Auslassen selbst aber nicht | Sofort tragfähige Nutzungsgrenze bis zur Qualifikation eines weitergehenden Wegs; auch dauerhafte Option, falls der geringere Nutzen genügt |

**Konkrete Reparaturentscheidung.** Die bisherige Freigabe verbindlicher Zusagen aus diesem Weg aussetzen und die zulässige Nutzung vorläufig auf Entwürfe begrenzen. Als technischen Reparaturkandidaten den vorhandenen strukturierten Schritt auf die tatsächlichen harten Ausschlusskriterien anpassen. Sein bisheriger Erfolg bei anderen Kriterien reicht dafür nicht aus. Es ist keine zusätzliche dauerhafte Kontrollorganisation erforderlich; entscheidend ist die wirksame Einbindung des vorhandenen Mechanismus an der Freigabestelle.

Der ausführbare nächste Schritt ist eine gebundene Prüfkonfiguration mit folgendem Vertrag:

1. Jedes gültige harte Ausschlusskriterium erhält eine prüfbare Bedingung, die benötigten Eingabefelder und einen Bezug zur maßgeblichen Quelle. Die Vollständigkeit dieser Abbildung ist selbst zu prüfen. Die konkreten Kriterien fehlen im Dossier; ihre Regeln dürfen deshalb hier nicht erfunden werden.
2. Die Eingabefelder werden aus einer nachweisbaren Quelle übernommen und auf die für die Bedingung erforderliche Vollständigkeit und Verlässlichkeit geprüft. Bloßes Übernehmen einer ungeprüften Selbstauskunft des bisherigen Bearbeiters würde den Fehler nur verschieben.
3. Jedes Kriterium liefert „bestanden“, „ausgeschlossen“ oder „nicht entscheidbar“. Mindestens ein Ausschluss verhindert die Freigabe. Fehlende, widersprüchliche oder nicht belastbare Daten verhindern ebenfalls eine endgültige Zusage und führen zur Klärung beziehungsweise zum Fortbestand des Entwurfsstatus. Nur vollständig bestandene Ausschlussprüfungen erfüllen diese notwendige Freigabebedingung; andere fachliche Anforderungen bleiben bestehen.
4. Das erzeugte Ergebnis muss den Prüfstatus tatsächlich übernehmen. Ein Fehler wird korrigiert und erneut geprüft oder das Ergebnis zurückgehalten. Ein Warnhinweis bei trotzdem möglicher unveränderter Freigabe wäre keine ausreichende Reparatur.

**Was vor weitergehender Nutzung noch zu prüfen ist.** Den angepassten Schritt mit bekannten Ausschlussfällen aus der Serie prüfen und zusätzlich frische vergleichbare Fälle mit Ausschluss, erfüllten Kriterien sowie unvollständigen oder widersprüchlichen Daten verwenden. Erwartete Ergebnisse gehören zur unabhängigen Auswertung und werden der Bearbeitung nicht als Lösung mitgegeben. Ein zulässiger Fall prüft außerdem, ob der Mechanismus versehentlich alles sperrt. Das Ergebnis muss nicht nur auf der richtigen Klassifikation, sondern auf der tatsächlich verhinderten unzulässigen Freigabe beruhen. Jeder übergangene Ausschluss oder jede Freigabe trotz unentscheidbarer Pflichtdaten widerlegt die Kandidatenqualifikation für endgültige Zusagen. Wiederholungen bekannter Fehlerfälle belegen Regressionseigenschaften, keine unabhängige Verallgemeinerung.

Den Anbieter auf derselben fachlichen Grundlage vergleichen, falls seine Leistung die Wahl des Arbeitswegs ändern kann: Ausschlussabdeckung, Umgang mit fehlenden Daten, inhaltlich brauchbare Integration im benötigten Dateityp und verbleibende menschliche Nacharbeit. Die zwei bereits korrekten Fälle erhalten ihren begrenzten positiven Evidenzwert. Falls der strukturierte Schritt keine verlässlichen Eingaben erhalten kann, ist seine angebliche Sicherheit nicht gegeben; dann den Anbieter qualifizieren oder die engere Nutzung beibehalten. Ein Architekturumbau ist erst dann begründet, wenn eine materielle Lücke mit diesen realisierbaren Wegen offen bleibt.

**Berechenbare Kostenaussage.** 18 Minuten entsprechen 0,3 Stunden menschlicher Nacharbeit pro Fall. Bei einem angesetzten Stundenwert von \(h\) Euro sind das \(0{,}3h\) Euro. Vier Euro Anbieterpreis entsprechen diesem Betrag bei \(h = 4/0{,}3 = 13{,}33\) Euro pro Stunde. Diese Schwelle gilt nur unter der zusätzlichen Annahme vollständig entfallender Nacharbeit und ohne weitere Kostendifferenzen. Tatsächlich müssen verbleibende Nacharbeit, bisherige Ausführungskosten sowie Einrichtungs- und Betriebskosten verglichen werden; eine Nettoersparnis ist aus dem Dossier nicht berechenbar. Auf fünf Fälle hochgerechnet entsprechen die gegebenen Mittelwerte 90 Minuten Nacharbeit beziehungsweise 20 Euro Anbieterentgelt, ohne damit gleiche Zuverlässigkeit zu unterstellen.

**Nachweisgrenze.** Schon jetzt tragfähig ist die Beschränkung auf unverbindliche Entwürfe. Die angepasste maschinelle Prüfung ist ein begründeter, noch nicht qualifizierter Reparaturkandidat; der Anbieter ist eine zugängliche, aussichtsreiche Alternative. Weder die interne Fehlerursache noch die zukünftige Fehlerfreiheit eines der Wege ist bewiesen. Nach begrenzter Qualifikation liefern tatsächliche Anwendungsfälle weitere Evidenz; eine kleine fehlerfreie Prüfserie ersetzt diese nicht.

## Fall 3 — Falschen Stand und unwirksamen Prüfnachweis gemeinsam korrigieren

**Diagnose.** Hier bestehen mindestens zwei getrennte Beiträge zum Fehler:

- **Installation beziehungsweise Ladung:** v2 ist freigegeben und das Update autorisiert, tatsächlich installiert und geladen blieb v1. Anders als ein bloßer Versionsunterschied ist dies eine belegte Abweichung vom geltenden Soll. Sie liegt vor der Berechnung. Welcher technische Update- oder Auswahlfehler sie verursachte, ist im Dossier nicht sichtbar.
- **Prüfung und Berichtsbehauptung:** Der vorhandene Zeilencheck prüft weder die verwendeten Preise noch die Rechnung oder Aktualität. Dass er auch 999 akzeptierte, ist konkreter Gegenbeleg gegen seine Eignung zur Bestätigung des Gesamtpreises. „Geprüft und aktuell“ ist für den vorliegenden Bericht unhaltbar.

Die Berechnung mit v1 ist für sich arithmetisch richtig: \(10 \times 3 + 8 \times 5 = 70\). Der erste Fehler ist die unzulässige Datengrundlage, nicht ein Rechenfehler innerhalb von v1. Ein bloßes Ersetzen der Zahl oder ein bloßes Update würde jeweils einen der beiden wesentlichen Beiträge ungelöst lassen.

**Korrigiertes Berichtsergebnis anhand des Dossiers:**

| Produkt | Preis laut freigegebenem v2 | Menge | Teilbetrag |
|---|---:|---:|---:|
| A | 12 | 3 | 36 |
| B | 8 | 5 | 40 |
| Gesamt | | | **76** |

Die Korrektur beträgt **+6** gegenüber dem bisherigen Gesamtpreis 70. Eine Währung ist für diesen Fall nicht angegeben.

> Laut dem im Dossier repräsentierten freigegebenen Rechenblatt v2 beträgt der Gesamtpreis 76: 12 × 3 + 8 × 5. Der bisherige Wert 70 beruhte auf v1. Die Behauptung „geprüft und aktuell“ wird zurückgenommen; der bisherige Check bestätigte nur das Vorhandensein der zwei Produktzeilen. Die v2-Rechnung ist anhand der Dossierwerte nachvollzogen. Eine tatsächlich installierte und geladene v2-Datei ist damit nicht nachgewiesen.

**Ausführbarer Reparaturweg innerhalb der bereits bestehenden Autorisierung:**

1. Den autorisierten Zielstand v2 am maßgeblichen Installationsort herstellen und im verwendeten Arbeitsweg laden. Den aktiven Auswahlverweis beziehungsweise Ladepfad kontrollieren, soweit er die Abweichung erklären kann. Anschließend den tatsächlich installierten und geladenen Stand zurücklesen: Identität v2, Preise A=12 und B=8 sowie Mengen A=3 und B=5. Eine erfolgreiche Schreibmeldung allein genügt nicht. Eine erneute Grundsatzfreigabe des bereits autorisierten Updates ist nicht nötig.
2. Den Bericht aus diesem bestätigten Stand neu berechnen: A=36, B=40, Gesamt=76. Die im Bericht ausgewiesene Grundlage an den tatsächlich gelesenen Stand binden.
3. Den Zeilencheck als begrenzte Strukturprüfung behalten und um unabhängige Prüfungen der Quellenidentität, Werte, Multiplikationen und Gesamtsumme ergänzen. Der Prüfschritt muss gegen die freigegebenen Eingaben rechnen, statt lediglich die Berichtszahl nochmals zu übernehmen.
4. Die geänderte Prüfung gezielt herausfordern: Mit v2 und korrektem Bericht muss 76 akzeptiert werden; ein Bericht mit Gesamtpreis 70 oder 999 bei denselben v2-Eingaben muss scheitern. Eine weiterhin aktive v1-Grundlage muss als Aktualitätsfehler scheitern, selbst wenn deren Rechnung 70 korrekt ist. Die bestehende Zeilenprüfung muss fehlende Produktzeilen weiterhin erkennen. Nur tatsächliche Ergebnisse dieser Kontrollen rechtfertigen anschließend einen entsprechend begrenzten Prüfvermerk.

**Was erhalten bleibt.** Die Freigabe von v2 und des fachlichen Prüfauftrags, die Mengen A=3/B=5, der unveränderte Preis B=8, die Rechenregel „Preis mal Menge, dann summieren“ sowie brauchbare Berichtsstruktur können erhalten bleiben. Die bisherige Strukturprüfung bleibt für ihren engen Zweck sinnvoll. Die alte Rechnung 70 darf als historisches Ergebnis unter v1 nachvollziehbar bleiben, aber nicht als aktueller Preis. Eine neue Architektur oder eine Überarbeitung unbetroffener Methoden folgt daraus nicht.

**Nachweisgrenze.** Das korrigierte Ergebnis 76 und die beiden Fehlerbeiträge sind durch das Dossier gedeckt. Da reale Dateien ausschließlich darin repräsentiert sind, wurden weder eine Installation noch ein Readback oder eine Änderung des Prüfprogramms tatsächlich ausgeführt. Die genannten Tests sind konkrete Sollprüfungen mit erwarteten Ergebnissen, keine behaupteten Testdurchläufe. Ein späterer Vollzug muss genau diese offenen technischen Nachweise liefern.

## Tatsächlich gelesene Methodenpfade

- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/SKILL.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/RCA-FAILURE-LOCALIZATION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/SYSTEM-ARCHITECTURE-REQUIREMENTS-METHOD.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REPOSITORY-PROMOTION-READBACK-METHOD.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REAL-USE-VALIDATION-METHOD.md`
