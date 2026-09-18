# Versionsfälle 6–9

## Entscheidungsgrundlage

Repositoryfassung, freigegebenes Betriebsziel, installierte Fassung, tatsächlich gelesene Fassung und tatsächliche Anwendung sind getrennte Nachweisgegenstände. Die vollständige Byte-Identität im Dossier klärt die Versions- und Readfragen; erneute Versionssuche würde hier keine offene Hypothese entscheiden. In jedem Output fehlen zwei ausdrücklich benannte v2-Anforderungen: stärkster Rivale und Umstiegsbedingung. Zwei vorhandene Alternativen allein belegen noch nicht die fachliche Qualität ihres Vergleichs.

| Fall | Freigegebenes Ziel | Installiert / gelesen | Installationsbefund | Befund zur Aussage „nach v2 gearbeitet“ |
|---|---|---|---|---|
| 6 | v1 | v1 / v1 | Kein Versionsfehler gegenüber dem Betriebsziel | Falsche Angabe der verwendeten Fassung; v2-Anwendung nicht erfüllt |
| 7 | Unbekannt | v1 / v1 | Verpflichtung zu v2 nicht entscheidbar | Falsche Angabe der verwendeten Fassung; v2-Anwendung nicht erfüllt |
| 8 | v2, Aktualisierung freigegeben | v1 / v1 | Belegte Abweichung vom freigegebenen Ziel | Falsche Angabe der verwendeten Fassung; v2-Anwendung nicht erfüllt |
| 9 | v2 | v2 / v2 | Kein Versionsfehler | v2 wurde gelesen, aber zwei ihrer Anforderungen wurden nicht angewandt |

Damit sind **drei falsche Angaben über die verwendete Methodenfassung** belegt (6–8). Unter vier Fällen gibt es **eine belegte Installationsabweichung**, **zwei belegte Übereinstimmungen mit dem Betriebsziel** und **einen offenen Zielabgleich**. Kein Output erfüllt die beiden zusätzlichen v2-Anforderungen. Daraus folgt nicht, dass v2 in allen vier Fällen der verpflichtende Betriebsmaßstab war.

## Fall 6 — v1 ist das ausdrücklich freigegebene Betriebsziel

**Diagnose.** Die erste belegte Abweichung liegt in der Ergebnisbehauptung, nicht in der Installation: v1 war freigegeben, installiert und gelesen. Die ungeprüfte v2 im Candidate-Branch begründet weder eine Installationspflicht noch eine Freigabe. Das Fehlen der zusätzlichen v2-Schritte ist gegenüber v1 kein belegter Pflichtverstoß.

**Rivalenprüfung.** Die Erklärung „veraltete Installation verursacht das Fehlverhalten“ würde eine Abweichung vom freigegebenen Ziel voraussetzen. Der vorliegende Zielnachweis widerlegt diese Erklärung. Eine falsche oder unzureichend geprüfte Ergebniskennzeichnung ist dagegen unmittelbar belegt. Warum diese Kennzeichnung entstand, ist nicht belegt.

**Konkrete Korrektur.** Den Satz „nach v2 gearbeitet“ ersetzen durch: „Installiert und vollständig gelesen wurde v1. Der Output enthält zwei Alternativen. Die zusätzlichen v2-Anforderungen wurden nicht bearbeitet.“ v1 bleibt aktiv. Für die vorliegende Versionsbehauptung genügt diese lokale Korrektur; eine Installation wäre unzulässig und würde die bereits freigegebene Basis verändern.

**Stärkste alternative Maßnahme und Umstiegsbedingung.** Eine v2-Übernahme wäre nur als gesonderte, qualifizierte Candidate-Promotion plausibel. Zu ihr wechseln, wenn ein sachlicher Bedarf an den Zusatzanforderungen festgestellt, der Candidate geprüft und v2 als konkretes Betriebsziel einschließlich Installationspfad freigegeben ist. Keine dieser Voraussetzungen darf aus dem bloßen Vorhandensein im Branch abgeleitet werden.

**Nachweisgrenze.** Belegt sind die korrekte aktive Version und die falsche Versionsbehauptung. Nicht belegt sind ein vollständiger fachgerechter v1-Vergleich, die innere Ursache der Fehlkennzeichnung oder die Eignung von v2. Ein Systemumbau ist nicht begründet.

## Fall 7 — freigegebenes Betriebsziel unbekannt

**Diagnose.** Die falsche Versionsbehauptung ist entschieden; ein Installationsdefekt bleibt offen. Die beiden Erklärungen „v1 ist weiterhin das legitime Betriebsziel“ und „v2 ist freigegeben, wurde aber nicht installiert“ sind mit den beobachteten Repository-, Installations- und Readdaten vereinbar. Die fehlende Zielinformation im vollständigen zugänglichen Dossier lässt sich nicht durch Wiederholung derselben Reads ersetzen.

**Konkrete Korrektur.** Den Satz „nach v2 gearbeitet“ durch dieselbe präzise Versions- und Leistungsangabe wie in Fall 6 ersetzen. Keine Installation vornehmen.

**Ausführbarer nächster Schritt.** Einen isolierten Entscheidungsgegenstand für die zuständige Betriebsautorität bereitstellen:

- Gesicherter Istzustand: installiert und gelesen v1; Repository v2.
- Konkretes v2-Delta: zusätzlich stärksten Rivalen benennen und eine Umstiegsbedingung formulieren.
- Offene Entscheidung: Welche exakte Fassung ist für welchen Zielpfad das freigegebene Betriebsziel?
- Autorisierter Arbeitsstand: Diagnose und isolierter Candidate; keine Installation.
- Bedingte Folge: Bei bestätigtem Ziel v1 bleibt die Installation bestehen. Bei bestätigtem Ziel v2 ist die Versionsabweichung belegt; eine spätere Installation benötigt zusätzlich die entsprechende Autorisierung.

Damit ist die offene Entscheidung vorbereitet. Es wird weder eine neue Freigabe unterstellt noch bereits vorliegende Autorisierung unnötig erneut angefordert.

**Stärkster Rivale und Umstiegsbedingung.** Zur vorläufigen Maßnahme „Kennzeichnung korrigieren und aktive Fassung erhalten“ ist die stärkste alternative Maßnahme eine v2-Aktualisierung. Zu ihr erst wechseln, wenn Zielversion, Zielpfad und Installationsautorisierung verbindlich feststehen. Der entscheidende Nachweis ist die gültige Betriebsentscheidung, nicht ein weiterer Vergleich von v1 und v2.

**Nachweisgrenze.** Aus dem Dossier ist keine abschließende Aussage „Installation richtig“ oder „Installation falsch“ möglich. Ebenso wenig lässt sich die fehlende Information als Versäumnis einer bestimmten Person oder als Beweis fehlender Freigabe deuten. Ein Candidate bleibt ein Candidate; seine Bearbeitung stellt keinen Betriebswechsel her.

## Fall 8 — freigegebene Aktualisierung, Installationsfläche fehlt

**Diagnose.** Die erste belegte Zustandsabweichung liegt zwischen freigegebenem Betriebsziel v2 und installierter v1. Der Read entspricht zwar der Installation, erreicht aber nicht das freigegebene Ziel. Zusätzlich ist die Versionsbehauptung im Output falsch. Diese beiden Beiträge verlangen unterschiedliche Korrekturen.

**Rivalenprüfung.** „v1 ist noch legitim“ ist durch das dokumentierte Ziel v2 ausgeschlossen. „v2 wurde gelesen, aber nicht angewandt“ ist durch den belegten Read v1 als Beschreibung dieser Episode ausgeschlossen. Belegt ist die Bereitstellungsabweichung; weshalb die Aktualisierung unterblieb, bleibt unbekannt. Der v1-Read bedeutet zugleich, dass die v2-Zusatzanforderungen über diese gelesene Quelle nicht bereitgestellt wurden. Er beweist nicht die alleinige innere Ursache des Weglassens.

**Konkrete Korrektur jetzt.** Die unzutreffende Aussage ersetzen durch: „Betriebsziel ist v2; installiert und vollständig gelesen wurde v1. Die Ausarbeitung erfüllt die zusätzlichen v2-Anforderungen noch nicht. Die freigegebene Aktualisierung wurde in diesem Dossier nicht ausgeführt, weil die Installationsfläche nicht verfügbar ist.“

**Vorbereiteter Ausführungsablauf für die bereits freigegebene Aktualisierung.** Sobald die konkrete freigegebene Zielumgebung verfügbar ist:

1. Die bereits dokumentierte Freigabe an die exakte v2-Fassung und den darin bezeichneten Zielpfad binden.
2. Ausschließlich diese v2 an diesem Zielpfad installieren; keine weitere Freigabeschleife für die bereits autorisierte Aktualisierung einführen.
3. Den Inhalt am tatsächlichen Zielpfad zurücklesen und vollständige Byte-Identität mit der freigegebenen v2 feststellen. Falls Auswahlzeiger die geladene Fassung bestimmen, ihre Übereinstimmung im betroffenen Umfang prüfen.
4. Den tatsächlichen vollständigen v2-Read in der folgenden Bearbeitung nachweisen.
5. Die betroffene Ausarbeitung unter v2 korrigieren: Alternativen begründet vergleichen, den stärksten Rivalen auswählen und eine konkrete Bedingung nennen, unter der zu ihm gewechselt würde.
6. Installationserfolg und Anwendungserfolg getrennt prüfen: Byte-identische Installation und Read einerseits; sachhaltige Erfüllung der drei inhaltlichen Anforderungen andererseits. Bei Fehlprüfung die betroffene Erfolgsaussage zurückhalten und die Abweichung korrigieren.

**Stärkste alternative Maßnahme und Umstiegsbedingung.** Eine reine Textkorrektur behebt den falschen Anspruch, lässt aber die belegte Betriebsabweichung bestehen. Sie ist die angemessene sofortige Teilkorrektur, solange die Installationsfläche fehlt. Zur kombinierten Aktualisierung und inhaltlichen Nachbearbeitung wechseln, sobald diese Fläche verfügbar ist; die nötige Autorisierung liegt bereits vor. Eine bloße Neuinstallation ohne Anwendungskontrolle wäre ebenfalls unzureichend.

**Nachweisgrenze.** Es wurde weder installiert noch ein erfolgreicher Readback behauptet. Ohne reale Zielumgebung lassen sich die Installation, der nächste Read und die spätere v2-Anwendung nicht nachweisen. Ohne die eigentlichen fachlichen Alternativen kann auch der inhaltlich stärkste Rivale der ursprünglichen Ausarbeitung nicht seriös eingesetzt werden. Der Ablauf ist konkret vorbereitet, aber nicht als durchgeführt ausgegeben. Es werden keine nicht dokumentierten Pfade oder Installationsbefehle erfunden.

## Fall 9 — v2 installiert und vollständig gelesen

**Diagnose.** Die erste belegte Abweichung liegt zwischen der verfügbaren, vollständig gelesenen v2-Anforderung und dem produzierten Output. Der stärkste Rivale und die Umstiegsbedingung wurden nicht angewandt. Repository, Betriebsziel, Installation und Read stimmen überein. „v2 gelesen“ ist wahr; „nach v2 gearbeitet“ ist als unqualifizierte Erfüllungsbehauptung nicht gedeckt.

**Rivalenprüfung.** Fehlende Anforderungen in der Quelle, Installation einer anderen Fassung und fehlender vollständiger v2-Read sind durch das Dossier ausgeschlossen. Nicht unterscheidbar sind beispielsweise ein Ausführungsversäumnis während der Bearbeitung und ein späterer Verlust bereits gebildeter Inhalte bei der Ausgabe. Dafür wären zusätzliche Ablauf- oder Zwischenproduktdaten nötig; das vorliegende Dossier enthält sie nicht. Eine Behauptung über Aufmerksamkeit, Verständnis, Kontextverlust oder die innere Modellursache wäre spekulativ.

**Konkrete Korrektur.** Die Aussage ändern zu: „v2 wurde vollständig gelesen; der Output hat den stärksten Rivalen und die Umstiegsbedingung ausgelassen.“ Anschließend die ursprüngliche Ausarbeitung gezielt nachbearbeiten: den sachlichen Vergleich der vorhandenen Alternativen prüfen, den stärksten Rivalen zur bevorzugten Alternative mit Begründung benennen und eine beobachtbare Entscheidungsbedingung formulieren, bei deren Eintreten die Alternative vorzuziehen wäre. Die fachlichen Inhalte fehlen im Dossier, daher lässt sich diese inhaltliche Ergänzung hier nicht erfinden.

**Prüfung und angemessene Reichweite.** Die nächste Ausführung am konkreten Arbeitsprodukt anhand der drei v2-Anforderungen prüfen. Fehlt ein Element, muss diese Prüfung unmittelbar zur Nachbearbeitung oder zur Einschränkung des Erfüllungsanspruchs führen. Für den belegten Einzelfehler sind lokale Korrektur und diese Kontrolle angemessen. Die bereits richtige Installation bleibt erhalten; Neuinstallation würde keine belegte Abweichung beheben.

**Stärkste alternative Maßnahme und Umstiegsbedingung.** Eine Änderung des Ausführungsmechanismus ist die stärkste plausible Alternative zur lokalen Nachbearbeitung, etwa eine verbindliche inhaltliche Abschlussprüfung mit direktem Korrekturschritt. Zu einem weitergehenden Mechanismus wechseln, wenn erneute vergleichbare Bearbeitungen trotz gültiger, zugänglicher v2 und lokaler Korrektur dieselben wesentlichen Auslassungen zeigen oder die Folgen bereits einen stärkeren Kontrollbedarf belegen. Die bloße erneute Wiederholung der Anweisung wäre dann kein ausreichender Reparaturnachweis. Ein Architekturumbau erfordert darüber hinaus einen belegten strukturellen Bedarf und eine begründete geeignete Lösung.

**Nachweisgrenze.** Belegt ist die Nichtanwendung zweier v2-Anforderungen, nicht ihre innere Ursache. Eine erfolgreiche Einzelkorrektur würde die konkrete Ausarbeitung qualifizieren, aber weder dauerhafte Zuverlässigkeit noch allgemeine fachliche Ergebnisqualität beweisen.

## Tatsächlich gelesene Methodenpfade

- /workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/SKILL.md
- /workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/RCA-FAILURE-LOCALIZATION-METHOD.md
- /workspace/scratch/cda19bcc7083/repair_candidate/skills/system-development/references/REPOSITORY-PROMOTION-READBACK-METHOD.md
