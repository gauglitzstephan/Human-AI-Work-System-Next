# Fall 4 — Qualifikation vor erster Produktionsfreigabe

## Entscheidung und Begründung

Die vorliegenden Nachweise tragen noch keine Produktionsfreigabe. Lesbare Tabellen belegen die Darstellung, aber weder korrekte Fristentscheidungen noch Vollständigkeitsprüfung oder Schutz vor mehrfacher Auszahlung. Das ist eine offene Eignungsfrage vor Erstnutzung, kein bereits beobachteter Schadensfall und kein Anlass für eine erfundene Ursachenanalyse.

Angemessen ist eine begrenzte, kontrollierte fachliche Abnahme des konkreten Kandidaten in einer Umgebung ohne echte Zahlungen. Dafür müssen wir nicht erst einen produktiven Fehler abwarten. Die Aufgabe verlangt gerade die vor einer Freigabe erforderliche Arbeit. Die interne Methode zur Bewertung echter Nutzung ersetzt diese Abnahme nicht; ihre Beschränkung synthetischer Ursachen-Isolation ist kein sachlicher Grund, hier auf die Prüfung der drei belegten Fachregeln zu verzichten.

## Konkrete Eingaben und Soll-Ergebnisse

Alle folgenden Datensätze sind künstliche Prüfdaten. Alle Uhrzeiten sind ausdrücklich Ortszeiten in `Europe/Berlin`, jeweils im betreffenden Antragsjahr. Ein technisches Datensatzkennzeichen unterscheidet Eingangszeilen; die fachliche Antragskennung bezeichnet den tatsächlichen Antrag. Für die Dublettenprobe ist die fachliche Identität vorgegeben, sodass keine unbewiesene Erkennungsheuristik vorausgesetzt wird.

| Datensatz | Fachlicher Antrag | Eingang | Unterlagen vollständig | Soll nach den belegten Regeln |
|---|---|---|---|---|
| F01 | A01 | 30.09., 17:59:59 | Ja | Fristgerecht und vollständig; fachlich freigabefähig |
| F02 | A02 | 30.09., 18:00:00 | Ja | Fristgerecht und vollständig; Grenzzeitpunkt eingeschlossen |
| F03 | A03 | 30.09., 18:00:01 | Ja | Nicht freigabefähig: verspätet |
| F04 | A04 | 30.09., 18:00:00 | Nein | Nicht freigabefähig: unvollständig trotz fristgerechten Eingangs |
| F05 | A05 | 30.09., 18:00:01 | Nein | Nicht freigabefähig: verspätet und unvollständig |
| D01a | D01 | 29.09., 12:00:00 | Ja | Mit D01b gemeinsam prüfen: ein fachlicher Antrag, höchstens eine Auszahlungsfreigabe |
| D01b | D01 | 30.09., 17:00:00 | Ja | Dublette von D01a; keine zweite Auszahlungsfreigabe |
| P01 | P01 | 30.09., 17:00:00 | Ja | Bei im Testzustand bereits erfolgter Auszahlung keine weitere Auszahlung |

Für P01 wird ausschließlich ein künstlicher Auszahlungsstatus vorbereitet. „Freigabefähig“ bezeichnet hier das Bestehen der drei Dossierkriterien, keine ausgeführte Zahlung. Welche der beiden D01-Eingangszeilen den gemeinsamen Antrag repräsentiert, ist nicht geregelt; die Prüfung darf dafür keine willkürliche fachliche Vorschrift erfinden.

Die vorab berechenbare fachliche Einordnung des Prüfsatzes lautet: A01 und A02 bestehen Frist- und Vollständigkeitsprüfung; A03, A04 und A05 bestehen sie nicht. D01 ist ein weiterer fristgerechter vollständiger fachlicher Antrag, der höchstens einmal berücksichtigt werden darf. P01 darf wegen des simulierten bereits erfolgten Zahlungsereignisses nicht erneut ausgezahlt werden. Eine bloße pauschale Ablehnung sämtlicher Anträge wäre kein Nachweis richtiger fachlicher Auswahl.

## Ausführbarer nächster Schritt

1. Den tatsächlich zur Freigabe stehenden Kandidaten mit eindeutiger Versionskennung, Konfiguration und vorgesehenem Entscheidungsweg festhalten. Eine andere Implementierung oder bloß eine Tabellenansicht genügt nicht.
2. Den obigen Prüfsatz über diesen Entscheidungsweg verarbeiten. Echte Zahlungsausgänge bleiben technisch unverbunden; ein Testempfänger protokolliert Auszahlungsaufträge. Eingangsdaten, Entscheidungen, Begründungen und Testaufträge sichern.
3. Die tatsächlichen Entscheidungen gegen die vorab festgelegten Soll-Ergebnisse prüfen. Besonders entscheidend sind die eingeschlossene Grenzzeit, der Ausschluss unvollständiger Unterlagen und die gemeinsame Behandlung von D01a/D01b. Bei Datumskonvertierungen muss der Kandidat die angegebene Zone verwenden und darf nicht stillschweigend die Serverzeit zugrunde legen.
4. Den D01-Vorgang im künstlichen Zustand einmal als ausgezahlt verbuchen und die Eingabe erneut verarbeiten. Über beide Durchläufe zusammen darf höchstens ein Test-Auszahlungsauftrag für D01 entstehen. Dadurch wird auch eine Mehrfachzahlung bei wiederholter Verarbeitung geprüft, nicht nur das Aussehen der Tabelle innerhalb eines Durchlaufs. Falls der vorgesehene Produktionsweg parallele Verarbeitung zulässt, ist derselbe Doppelverarbeitungsfall auch dort zu prüfen.
5. Bei Abweichung den konkret verletzten Mechanismus korrigieren und den betroffenen Fall wiederholen. Der zuständigen Freigabeinstanz anschließend Kandidatenidentität, tatsächliche Prüfergebnisse, verbleibende Lücken und eine begründete Freigabeempfehlung vorlegen. Jetzt ist die Entscheidung „fachliche Freigabe noch nicht belegt; Abnahme durchführen“ angemessen.

## Nachweisgrenze

Im Dossier fehlen ein ausführbarer Kandidat, seine konkrete Version und beobachtete fachliche Ausgaben. Deshalb sind hier Soll-Ergebnisse und eine ausführbare Prüfanweisung geliefert, kein behaupteter bestandener Kandidatentest. Die Probe deckt die angegebenen Regeln und gezielt ausgewählte Grenz- und Wiederholungsfälle ab. Sie beweist keine allgemeine Zuverlässigkeit, keine produktive Installation und keinen erfolgreichen realen Zahlungsprozess. Die Erkennung unbekannter Dubletten aus unklaren Identitätsmerkmalen ist ebenfalls nicht nachgewiesen. Nach einer möglichen Freigabe wären tatsächliche Nutzung und Ergebnisse weiterhin gesonderte Evidenz.

# Fall 5 — Gezielte Prüfung der Exportkorrektur

## Diagnose und angemessene Änderung

Die Ursache steht fest: `keep = bool(comment)` entfernt sowohl den leeren String als auch `null`. Damit verletzt die Auswahl bereits vor der Dokumentdarstellung die Pflicht, jede Datensatz-ID genau einmal auszugeben. Betroffen ist die Auswahl der Exportzeilen. Eine erneute Suche nach konkurrierenden Ursachen oder eine Änderung der Gesamtarchitektur ist nicht erforderlich.

Das Entfernen dieses Filters ist die richtige lokale Korrektur. Zusätzlich muss der Export die belegte Reihenfolge nach ID erfüllen. Aus der Angabe „Kandidat entfernt diesen Filter“ folgt noch kein Nachweis einer Sortierung: Ohne vorhandenen Sortierschritt bleiben die Eingabedaten in der Reihenfolge `3, 1, 2`. Falls der tatsächliche Export bereits sortiert, ist dieser Schritt zu erhalten und zu prüfen; andernfalls ist eine Sortierung nach ID die zusätzlich notwendige Korrektur.

## Tatsächlich ausgeführte Dossierprüfung

Die drei bereitgestellten Datensätze wurden lokal in Python verarbeitet. Dabei entspricht `None` dem Dossierwert `null`. Ausgeführt wurden die bekannte fehlerhafte Auswahl, das reine Weglassen des Filters und eine Referenztransformation ohne Filter mit aufsteigender Sortierung:

```python
from collections import Counter

rows = [
    {'id': 3, 'comment': 'ok'},
    {'id': 1, 'comment': ''},
    {'id': 2, 'comment': None},
]

old = [r for r in rows if bool(r['comment'])]
filter_removed_only = list(rows)
corrected = sorted(rows, key=lambda r: r['id'])

assert [r['id'] for r in old] == [3]
assert [r['id'] for r in filter_removed_only] == [3, 1, 2]
assert Counter(r['id'] for r in corrected) == Counter({1: 1, 2: 1, 3: 1})
assert [r['id'] for r in corrected] == [1, 2, 3]
assert corrected == [
    {'id': 1, 'comment': ''},
    {'id': 2, 'comment': None},
    {'id': 3, 'comment': 'ok'},
]
```

Alle Assertions bestanden. Die Ergebnisse sind:

| Transformation | Ausgegebene IDs | Beurteilung |
|---|---|---|
| Bekannter Filter | `3` | IDs 1 und 2 fehlen; Fehler reproduziert |
| Nur Filter weglassen, ohne weitere Verarbeitung | `3, 1, 2` | Alle IDs genau einmal, aber falsche Reihenfolge |
| Kein Kommentarfilter, nach ID sortieren | `1, 2, 3` | Für diesen Datensatz vollständig, eindeutig und richtig geordnet |

Das vollständige berechenbare Soll-Ergebnis lautet:

```json
[
  {"id": 1, "comment": ""},
  {"id": 2, "comment": null},
  {"id": 3, "comment": "ok"}
]
```

## Prüfung vor Wiederverwendung und Nachweisgrenze

Der nächste konkrete Schritt ist, dieselben drei Eingaben durch den tatsächlich geänderten Dokumentexport zu schicken und das erzeugte Dokument zu lesen. Die Datensatzzeilen müssen die ID-Folge `1, 2, 3` ergeben, jede ID muss genau einmal vorkommen, und die beiden Zeilen ohne Kommentar dürfen auch beim Rendern nicht verschwinden. Das prüft den betroffenen Fehler und die ausdrücklich vorgeschriebene Reihenfolge mit einem kleinen, fehlerempfindlichen Regressionstest.

Die oben ausgeführte Prüfung belegt die Wirkung des bekannten Filters und die Korrektheit der gezeigten Referenztransformation für die gegebenen Daten. Sie ist kein ausgeführter Test des nicht vorliegenden Exportprogramms oder eines erzeugten Dokuments. Insbesondere ist nicht belegt, ob im Kandidaten bereits sortiert wird oder ob eine spätere Exportstufe erneut Zeilen unterdrückt. Eine erfolgreiche Prüfung am tatsächlichen Kandidaten trägt die begrenzte Aussage, dass dieser Export die drei vorliegenden Datensätze regelgerecht behandelt; sie beweist keine Fehlerfreiheit für sämtliche künftigen Eingaben.

# Methodeneinsatz und tatsächlich gelesene Methodenpfade

Die Methode wurde nach Anspruch abgegrenzt verwendet: Kandidat und tatsächliche Leistung bleiben getrennt; vor einer Freigabe ist angemessene Evidenz erforderlich. Für den bekannten Exportfehler genügt die lokale Korrektur mit gezielter Nachprüfung. Es wurden keine zusätzlichen Ursachenhypothesen, Repository-Freigaben oder Architekturänderungen konstruiert. Die spezielle Methode für Runtime-Kompilation ist auf diese Fachfälle nicht unmittelbar anzuwenden; es wird keine solche Kompilation behauptet. Die Methode zur Bewertung echter Nutzung liefert ebenfalls keinen Ersatz für eine Erstqualifikation.

Tatsächlich gelesen wurden:

- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/SKILL.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/REAL-USE-VALIDATION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/REPOSITORY-PROMOTION-READBACK-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/RCA-FAILURE-LOCALIZATION-METHOD.md`
- `/workspace/scratch/cda19bcc7083/audit_evidence/installed/references/RUNTIME-COMPILATION-SEMANTIC-REGRESSION-METHOD.md`
