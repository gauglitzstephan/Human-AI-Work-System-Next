# Fall 4 — Qualifikation vor der ersten Produktionsfreigabe

## Entscheidung und Begründung

Auf der vorliegenden Evidenz ist die Produktionsfreigabe noch nicht fachlich begründet. Belegt ist lediglich, dass der Kandidat lesbare Tabellen erzeugt. Ob er Frist, Vollständigkeit und Einmaligkeit einer Auszahlung korrekt berücksichtigt, wurde nicht beobachtet. Das ist eine Nachweislücke, kein bereits belegter fachlicher Fehler.

Angemessen ist eine kleine kontrollierte Prüfung vor der folgenreichen Verwendung. Sie darf und soll ohne vorherigen realen Schaden stattfinden. Sie betrifft genau die Regeln, deren Verletzung zu einer falschen Auszahlung oder zum Ausschluss eines zulässigen Antrags führen könnte. Eine Ursachenanalyse, ein Methodenvergleich oder ein allgemeines Benchmarkprogramm sind dafür nicht erforderlich.

## Konkrete Arbeit vor der Entscheidung

1. Den tatsächlich freizugebenden Kandidaten samt Version beziehungsweise unveränderlichem Stand und vorgesehener Ausführungsumgebung festhalten. Das Dossier enthält diese Identität noch nicht. Die Prüfung muss diesen konkreten Stand über den vorgesehenen fachlichen Arbeitsweg ausführen.
2. Die drei belegten Fachregeln als Prüfkriterien festlegen. Auszahlungseffekte vollständig durch eine lokale Simulation ersetzen; keine echten Zahlungen und keine Änderungen an realen Installationen oder Konten.
3. Dem Kandidaten die unten stehenden Eingaben und die Fachregeln geben. Die erwarteten Ergebnisse verbleiben getrennt bei der Auswertung. Entscheidungen, Ausschlussgründe und alle simulierten Auszahlungsanweisungen aufzeichnen.
4. Tatsächliche Ergebnisse gegen die Erwartungen prüfen. Bei einer Abweichung die Freigabe zurückstellen, den konkreten Fehler korrigieren und die betroffenen Regeln erneut prüfen. Bei vollständigem Bestehen ist eine begrenzte fachliche Qualifikation dieser Regeln belegt; die Produktionsfreigabe bleibt die Entscheidung der zuständigen Stelle.

### Prüfeingaben

Das Jahr 2026 ist ausschließlich ein synthetisch gewähltes Testjahr. Alle folgenden Zeitangaben sind ausdrücklich Ortszeit in **Europe/Berlin**. Der Stichtag des Testfalls lautet **30.09.2026, 18:00:00 Europe/Berlin**. Es wird keine Zeitzonenregel aus externen Quellen ergänzt.

`Antragsschlüssel` bezeichnet die vorgegebene fachliche Identität des Antrags. Gleiche Schlüssel sind in diesem Test belegte Dubletten; unterschiedliche Zeilen-IDs machen daraus keine verschiedenen Anträge. `Vollständig` ist ein Testeingabemerkmal, weil das Dossier keine Liste erforderlicher Dokumente enthält.

| Zeilen-ID | Antragsschlüssel | Eingang am 30.09.2026 | Vollständig |
|---|---|---|---|
| R1 | A | 17:59:59 Europe/Berlin | ja |
| R2 | B | 18:00:00 Europe/Berlin | ja |
| R3 | C | 18:00:01 Europe/Berlin | ja |
| R4 | D | 17:59:59 Europe/Berlin | nein |
| R5 | E | 17:59:59 Europe/Berlin | ja |
| R6 | E | 18:00:00 Europe/Berlin | ja |

### Zu prüfende Ergebnisse

| Antragsschlüssel | Erwartete Entscheidung | Anzahl simulierter Auszahlungen | Begründung |
|---|---|---:|---|
| A | zur Auszahlung auswählen | 1 | fristgerecht und vollständig |
| B | zur Auszahlung auswählen | 1 | der exakte Stichtag ist eingeschlossen |
| C | keine Auszahlung | 0 | nach dem Stichtag eingegangen |
| D | keine Auszahlung | 0 | Unterlagen unvollständig |
| E | genau einmal zur Auszahlung auswählen | 1 | beide Eingänge sind zulässig, gehören aber zu einer Dublette |

**Berechenbares Gesamtergebnis:** drei auszuzahlende Anträge, nämlich A, B und E; keine Auszahlung für C oder D. Welche der beiden Zeilen R5/R6 den Antrag E repräsentiert, ist durch die Regeln nicht festgelegt und darf nicht als zusätzliches Bestehenskriterium erfunden werden. Zwei Auszahlungen für E sind dagegen eindeutig falsch. Auszahlungsbeträge sind nicht berechenbar, da keine Beträge vorliegen.

Die Einmaligkeit muss am simulierten Auszahlungsergebnis geprüft werden. Eine Tabelle mit nur einem sichtbaren Eintrag für E genügt nicht, wenn der weitere Arbeitsweg dennoch zwei Zahlungsanweisungen erzeugt. Soweit der vorgesehene Workflow bereits ausgezahlte Anträge erneut verarbeiten kann, folgt deshalb ein zweiter lokaler Durchlauf mit denselben Eingaben und einem simulierten Auszahlungsstand, in dem A, B und E bereits ausgezahlt sind: **null neue Auszahlungen**. Falls der Workflow diesen relevanten Vorzustand nicht berücksichtigen kann, ist die Einmaligkeit über Wiederholungen noch nicht belegt. Daraus folgt keine Vorgabe für eine bestimmte technische Architektur.

Die Prüfung endet nach beobachteter Ausführung dieser Fälle und Auswertung aller drei materiellen Regeln. Jeder unberechtigte Ausschluss, jede Auszahlung für C/D und jede Mehrfachauszahlung widerlegt die jeweilige Freigabeannahme. Bereits ein solcher Befund verhindert eine positive Qualifikation des geprüften Stands; bestandene andere Fälle werden nicht unterschlagen.

## Grenze des Nachweises

Hier liegen weder ausführbarer Kandidat noch tatsächliche Kandidatenausgaben vor. Daher wurden die erwarteten Ergebnisse bestimmt und eine ausführbare Prüfaufgabe vorbereitet, aber **kein Bestehen des Kandidaten beobachtet**. Auch ein späteres Bestehen dieser Fälle belegt nur die geprüften Regeln und den tatsächlich ausgeführten Arbeitsweg. Es belegt insbesondere keine Erkennung unbekannter Dubletten ohne vorgegebenen Schlüssel, keine eigenständige Prüfung konkreter Dokumente und keinen bereits eingetretenen produktiven Auszahlungserfolg. Nach einer begründeten Freigabe bleibt tatsächliche Verwendung die Evidenz für Leistung im Betrieb; reale Auszahlungen werden mit diesem Auftrag nicht autorisiert oder ausgeführt.

# Fall 5 — Prüfung der Exportkorrektur

## Diagnose und angemessene Korrektur

Die Ursache des Zeilenverlusts ist bereits eindeutig belegt: `keep = bool(comment)` verwirft sowohl den leeren String als auch `null`. Eine erneute Ursachensuche oder konkurrierende Ursachenhypothesen würden hier keine offene Entscheidung klären. Das Entfernen des Filters ist die passende lokale Korrektur dieses Fehlers.

Die geforderte Änderungskontrolle muss anschließend den gesamten betroffenen Ergebnisanspruch prüfen: alle IDs genau einmal und nach ID sortiert. Filterentfernung allein weist die Sortierung nicht nach. Falls der bestehende Export bereits sortiert, ist diese Funktion zu erhalten und zu überprüfen. Falls nicht, ist zusätzlich nach ID zu sortieren. Eine allgemeine Deduplizierungslogik lässt sich aus den drei unterschiedlichen Eingabe-IDs nicht ableiten und wird nicht vorsorglich eingeführt.

## Berechnetes Ergebnis und tatsächlich ausgeführte Prüfung

Die drei bereitgestellten Datensätze wurden lokal in Python ausgewertet. Dabei wurden der belegte alte Filter sowie eine minimale Referenztransformation ohne Filter und mit ID-Sortierung ausgeführt. Es wurden keine realen Daten oder Installationen verändert.

| ID | Optionaler Kommentar |
|---:|---|
| 1 | leerer String (`''`) |
| 2 | `null` |
| 3 | `ok` |

Ergebnisse der ausgeführten Berechnung:

- Alter Filter: ausschließlich ID **3**; **zwei fehlende Zeilen**, IDs 1 und 2.
- Filterentfernung bei bloßem Beibehalten der Eingabereihenfolge: IDs **3, 1, 2**; vollständig, aber nicht vorschriftsmäßig sortiert. Dies ist eine berechnete Variante, keine Beobachtung einer unbekannten Sortierfunktion des Kandidaten.
- Referenztransformation ohne Kommentarfilter und mit Sortierung: IDs **1, 2, 3**; **drei Zeilen**, jede ID genau einmal; Kommentare unverändert.

Die folgenden Prüfungen wurden erfolgreich ausgeführt:

```python
from collections import Counter

rows = [
    {"id": 3, "comment": "ok"},
    {"id": 1, "comment": ""},
    {"id": 2, "comment": None},
]

old_result = [row for row in rows if bool(row["comment"])]
filter_removed_only = list(rows)
reference_result = sorted(rows, key=lambda row: row["id"])

assert Counter(row["id"] for row in reference_result) == Counter({1: 1, 2: 1, 3: 1})
assert [row["id"] for row in reference_result] == [1, 2, 3]
assert reference_result == [
    {"id": 1, "comment": ""},
    {"id": 2, "comment": None},
    {"id": 3, "comment": "ok"},
]
```

Damit sind sowohl der berechenbare Sollzustand als auch die Wirkung der vorgeschlagenen minimalen Transformation konkret geprüft. Die Zählprüfung erkennt fehlende, zusätzliche und vervielfachte IDs; die Reihenfolgeprüfung erkennt eine unterlassene Sortierung. ID 3 schützt den zuvor funktionierenden Fall mit gefülltem Kommentar, während IDs 1 und 2 die beiden belegten Verlustfälle abdecken.

## Nächster Schritt vor Wiederverwendung und Nachweisgrenze

Den unveränderten Eingabesatz durch den **konkreten korrigierten Exportkandidaten** bis zum fertigen Dokument ausführen. Am tatsächlich erzeugten Dokument prüfen, dass dessen Datensatzzeilen genau die ID-Folge `[1, 2, 3]` enthalten, jede ID genau einmal vorkommt und ID 3 weiterhin den Kommentar `ok` trägt. Leerer String und `null` dürfen im Dokument als leere Kommentarfelder erscheinen; ihre Datensatzzeilen müssen erhalten bleiben. Es ist keine neue Darstellungskonvention für fehlende Kommentare zu erfinden.

Wenn das Dokument diese Bedingungen erfüllt, ist die gezielte Regression für diese drei Datensätze bestanden. Bei fehlenden Zeilen, Mehrfachvorkommen oder falscher Reihenfolge ist die entsprechende lokale Korrektur vor Wiederverwendung erforderlich.

**Grenze:** Der reale Exportcode und das erzeugte Dokument sind nicht Teil des Dossiers. Die erfolgreiche lokale Referenzprüfung ist deshalb kein Nachweis, dass der konkrete Kandidat oder die Dokumenterzeugung bereits funktioniert. Der abschließende Kandidatenlauf bleibt offen. Der bekannte Fehlerfall ist außerdem kein unabhängiger unbekannter Testfall; sein Bestehen belegt eine begrenzte Regression, keine allgemeine Exportfehlerfreiheit. Zusätzliche großflächige Tests oder neue dauerhafte Freigabeverfahren sind aus dem Dossier nicht begründet.

# Tatsächlich gelesene Methodenpfade

- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/SKILL.md`
- `/workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REAL-USE-VALIDATION-METHOD.md`
