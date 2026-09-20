# Installation und tatsächliche Work-Läufe — 20.09.2026

**Status: `form-intent` installiert und in vier neuen Work-Chats erprobt.** Der Nutzer hat nach der R3-Entwicklungsprüfung ausdrücklich Installation und Test veranlasst. Die ursprüngliche Begrenzung des Entwicklungsauftrags wurde damit für die Installation aufgehoben. Ein Merge des Systemrepositories ist damit nicht verbunden und wurde nicht ausgeführt.

## Installierter Gegenstand

Installiert wurde ausschließlich das geprüfte Paket `form-intent` aus Kandidatenrevision `b92e3df137c82b3e7f9b5b187708393ac695d3e2`. Sieben Dateien mit Arbeitsanweisungen, Referenzen und Vorlagen stimmen bytegenau mit dem getesteten Paket überein. Die Plattform hat `agents/openai.yaml` normalisiert und ein Standard-Icon sowie Plattform-/Aufrufmetadaten ergänzt; Anzeigename, Kurzbeschreibung und Startprompt blieben semantisch identisch. Die implizite Auswahl ist aktiviert. Die strukturelle Validierung wurde auf dem tatsächlichen Installationsordner ausgeführt und bestand.

Die Installation ist sowohl im persönlichen Skill-Speicher als auch in der ChatGPT-Oberfläche unter **Installiert → Intent Formation** bestätigt. Die 48 zuvor vorhandenen verwalteten Dateipfade und zwei unverwalteten Dateien anderer Arbeit blieben unverändert. [Technischer Abgleich](../evidence/installation-2026-09-20/installation-evidence.json).

[Installierter Skill](https://chatgpt.com/skills?skill_id=6aafd04c456481919402bea400007c92)

## Tatsächliche Aufrufe

Alle vier Aufträge wurden über die sichtbare ChatGPT-Work-Oberfläche in getrennten neuen Chats eingegeben. Verwendet wurde das dort vorausgewählte **GPT-5.6 Sol, Leicht/Light**. Kein Kandidatenpfad und kein erzeugtes Soll-Ergebnis wurde den Chats mitgegeben. Die Fälle sind ausdrücklich fiktiv und keine persönlichen Zusagen des Nutzers.

| Lauf | Auftrag und Beobachtung | Ergebnis |
|---|---|---|
| [I01: ausdrücklicher Aufruf](https://chatgpt.com/c/6aafd12e-6048-83eb-9e69-abc53df709f1) | `@form-intent` wurde im Eingabefeld als Skill-Auswahl aufgelöst. Der fiktive Fall einer Doppelzusage bei der Materialausleihe führte zu einer gespeicherten Intent-Datei. App, vorhandene Werkzeuge und Prozessänderung blieben offen. KI-Deutung, Einzelfallgrenze und fehlende menschliche Akzeptanz waren sichtbar. | Aufruf und Ausgabe erfolgreich; gespeicherte Datei separat wieder gelesen. |
| [I02: Auftrag ohne Skill-Nennung](https://chatgpt.com/c/6aafd19c-aa5c-83eb-9ae0-662020233b14) | Ein Intent für eine Entscheidungsgrundlage zu Museumsöffnungszeiten wurde ohne `@` oder Skill-Pfad angefordert. Der Chat kündigte die Verwendung von Intent Formation an und speicherte einen passenden Intent. Besucher-/Kostenfragen blieben als Untersuchungsgegenstände offen. | Passender Auftrag ohne ausdrückliche Skill-Auswahl erfolgreich verarbeitet. |
| [I03: gewöhnliche Ausführung](https://chatgpt.com/c/6aafd1d4-98fc-83eb-b36a-79b05c9e9261) | Aus Angaben zur Materialausleihe sollte eine Mitteilung in höchstens drei Sätzen entstehen. | Genau der Text wurde geliefert; keine Intent-Bildung, Rückfrage oder zusätzliche Datei. |
| [I04: Wiederaufnahme](https://chatgpt.com/c/6aafd284-4a04-83eb-9820-a3221f3fae7d) | Ein weiterer neuer Chat erhielt nur `@form-intent`, den Namen der I01-Datei und die Bitte um Zweck, Akzeptanzstatus und eine offene Frage. Der ursprüngliche Falltext wurde nicht mitgegeben. | Inhalt korrekt aus der gespeicherten Fassung wiederaufgenommen. Ein anschließender Inhalts- und Änderungszeitvergleich bestätigte, dass die Datei unverändert blieb. |

[Gesicherte UI-Verläufe, Aufträge und Dateilesenachweise](../evidence/installation-2026-09-20/runtime-evidence.json) · [I01-Ergebnis](../evidence/installation-2026-09-20/Installationstest_Materialausleihe_intent.md) · [I02-Ergebnis](../evidence/installation-2026-09-20/Installationstest_Museumszeiten_intent.md)

## Reichweite der Aussage

Dies ist ein tatsächlich ausgeführter Installations- und Nutzungstest im Zielhost. Die sichtbaren Gesprächsverläufe und gespeicherten Ergebnisse tragen die beschriebenen Beobachtungen. Vollständige interne Aufruf- und Routing-Traces sind nicht exportiert; bei I02 stützt sich die Zuordnung des Skills auf die sichtbare Nutzungsaussage und das resultierende Verhalten. Ein einzelner positiver und negativer Auswahlfall beweist keine allgemeine Auswahlsicherheit.

Die zwei neuen Intents wurden auf Zweck, Problemdeutung, Lösungsoffenheit, Akzeptanz und Persistenz geprüft. Die erzeugten Artefakte bleiben recht ausführlich. Diese Prüfung ist kein neuer unabhängiger Nachweis universeller Intent-Qualität und keine menschliche Gebrauchstauglichkeitsstudie; die Grenzen der R3-Evaluation bleiben bestehen. Die laufende ältere Skill-Liste dieses Ausgangschats zeigte den neuen Skill noch nicht; die neu geöffneten Work-Chats und die tatsächliche Skill-Oberfläche waren verfügbar.

## Verwendung und Rücknahme

In einem neuen Work-Chat `@form-intent` auswählen und das Anliegen beschreiben; bei Fortsetzung die bestehende Datei nennen oder auswählen. Es wird weder automatische persönliche Akzeptanz noch nachfolgende Spezifikation oder Umsetzung ausgelöst. Für eine Rücknahme ausschließlich `form-intent` nach dem regulären Skill-Verfahren deaktivieren und die erzeugten Intents erhalten. [Rollback](Rollback.md).
