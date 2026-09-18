# Fall 3 – Bericht, aktiver Rechenstand und Prüfung korrigieren

Der fachlich richtige Gesamtpreis beträgt **76**. Zu korrigieren sind der Bericht, die Übernahme des bereits freigegebenen Rechenstands v2 sowie die inhaltlich ungeeignete Prüfung. Eine bloße Änderung von 70 auf 76 würde die beiden Fehler im Arbeitsweg bestehen lassen.

## Diagnose und belegte Ursachenbeiträge

Der maßgebliche Sollstand ist v2: Seine Freigabe und das autorisierte Update sind im Dossier belegt. Installiert und geladen blieb dagegen v1. Die erste belegte wesentliche Abweichung liegt damit zwischen freigegebenem Betriebsziel und tatsächlichem Installationsstand; auch die geladene Quelle entspricht nicht dem Soll. Hier ist der Versionsunterschied ein nachgewiesener Übernahmefehler und nicht lediglich das Vorhandensein eines neueren Entwurfs.

Die Zahl 70 ist für die tatsächlich verwendeten v1-Daten rechnerisch richtig: 10 × 3 + 8 × 5 = 70. Das Dossier belegt daher keinen Fehler in Multiplikation oder Addition. Es belegt die Anwendung einer veralteten Preisquelle. Die genaue technische Ursache des unterbliebenen Updates – etwa falscher Zielpfad oder fehlgeschlagener Schreibvorgang – ist nicht beschrieben. Eine bloße Neuladung wäre als vollständige Reparatur unzureichend, weil bereits der installierte Stand v1 ist. Ob nach dessen Korrektur zusätzlich ein Ladeproblem besteht, muss am geladenen Stand geprüft werden.

Unabhängig davon ist die Prüfung für den Anspruch „geprüft und aktuell“ ungeeignet. Zwei vorhandene Produktzeilen belegen weder aktuelle Preise noch einen korrekten Gesamtpreis. Dass sie auch den absichtlich falschen Wert 999 akzeptiert, widerlegt ihre Eignung als rechnerische Ergebniskontrolle unmittelbar. Dieser Mangel hat den falschen Berichtsstatus ermöglicht; er erklärt nicht für sich allein das unterbliebene Update. Beide Beiträge benötigen eine Korrektur.

## Konkrekte Berichtskorrektur

| Produkt | Preis laut v2 | Menge | Teilbetrag |
|---|---:|---:|---:|
| A | 12 | 3 | 36 |
| B | 8 | 5 | 40 |
| **Gesamt** | | | **76** |

Der bisherige Gesamtpreis unterschreitet den freigegebenen Wert um **6**. Eine Währung ist nicht angegeben und wird nicht ergänzt.

Die ersetzende Berichtsaussage lautet:

> Auf Grundlage der im Dossier freigegebenen Rechenquelle v2 ergibt sich für A: 12 × 3 = 36 und für B: 8 × 5 = 40, insgesamt 76. Der frühere Wert 70 wurde mit dem veralteten Stand v1 berechnet. Die Aussage „geprüft und aktuell“ war nicht gedeckt. Die korrigierte Summe ist anhand der Dossierwerte nachgerechnet; die tatsächliche Installation, das Laden von v2 und die Wirksamkeit der reparierten Prüfung sind hier nicht nachgewiesen.

Damit ist das im Fall berechenbare Berichtsergebnis korrigiert, ohne eine nicht erfolgte Dateireparatur zu behaupten.

## Ausführbarer nächster Arbeitsweg

1. **Freigegebenes Ziel übernehmen:** Im betroffenen Arbeitskontext den autorisierten Updatepfad und das tatsächliche Installationsziel feststellen. Die freigegebene Quelle v2 dort übernehmen und anschließend den installierten Inhalt zurücklesen: A = 12, B = 8, Mengen A = 3 und B = 5. Eine Erfolgsmeldung oder ein Versionsetikett allein genügt nicht. Die vorhandene Autorisierung verlangt keine erneute Freigabeschleife für dasselbe Update.
2. **Tatsächliche Anwendung sichern:** Den Rechenlauf mit dieser Quelle neu starten beziehungsweise neu laden. Die wirklich geladenen Werte und ihre Herkunft mit dem zurückgelesenen Installationsstand abgleichen. Stimmen installierter und geladener Stand nicht überein, den betroffenen Ladepfad korrigieren. Erst dann den Bericht neu erzeugen.
3. **Prüfung fachlich ergänzen:** Den freigegebenen Stand mit den verwendeten Eingaben vergleichen, die Teilbeträge unabhängig vom berichteten Gesamtwert nachrechnen und mit dem tatsächlich ausgegebenen Bericht abgleichen. Die Prüfung muss bei falscher Quelle oder falschem Ergebnis die Kennzeichnung „geprüft und aktuell“ verhindern und eine konkrete Korrektur auslösen.
4. **Betroffene Ansprüche gezielt nachprüfen:** Den korrigierten Bericht mit v2 und 76 akzeptieren; einen Lauf mit v1 und 70 wegen veralteter Quelle zurückweisen; einen Bericht mit v2 und absichtlich gesetzter Summe 999 wegen falschen Ergebnisses zurückweisen. Den bekannten 999-Versuch ausdrücklich als Regression des beobachteten Prüfversagens verwenden. Erst nach tatsächlicher Durchführung darf behauptet werden, dass diese Prüfungen bestanden wurden.

Diese kombinierte lokale Reparatur behandelt die belegten Fehler. Ein Austausch der gesamten Rechenlogik oder ein Architekturumbau ist durch das Dossier nicht begründet.

## Was erhalten bleiben kann

- Die Freigabe von v2 und der fachliche Prüfauftrag bleiben gültig.
- Die Mengen, Produktzuordnung und die B-Werte bleiben unverändert; B ergibt weiterhin 40.
- Die Rechenregel „Preis × Menge, dann summieren“ kann erhalten bleiben. Ihre konkrete technische Implementierung ist damit nicht allgemein geprüft.
- Der Zeilenvollständigkeitscheck kann als begrenzte Strukturprüfung bestehen bleiben; die fachliche Ergebnisfreigabe darf nicht auf ihm beruhen.
- v1 und der alte Bericht können als eindeutig historischer Nachweis erhalten bleiben. Aktive Verweise im betroffenen Arbeitsweg müssen auf v2 zeigen. Die alte Zahl 70 bleibt als v1-Ergebnis nachvollziehbar, verliert aber ihren Status als aktuelles Ergebnis.

## Grenze des Nachweises

Das vollständige Dossier trägt die Diagnose der Soll-Ist-Abweichung, den Nachweis der ungeeigneten Prüfung und die nachgerechnete Summe 76. Tatsächliche Dateien, Installationsprotokolle und neue Prüfläufe liegen nicht vor. Es wurden daher keine reale Installation, keine reale Berichtsdatei und kein realer Prüfer verändert. Der dargestellte Arbeitsweg ist ein ausführbarer Reparatur- und Nachweisauftrag; seine erfolgreiche Umsetzung und eine allgemeine Zuverlässigkeitssteigerung sind noch nicht belegt.

## Tatsächlich gelesene Methodenpfade

- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/SKILL.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/RCA-FAILURE-LOCALIZATION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REPOSITORY-PROMOTION-READBACK-METHOD.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REAL-USE-VALIDATION-METHOD.md`
