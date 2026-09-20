# Installation — vorbereitet, nicht ausgeführt

Der Work Contract autorisiert ausdrücklich **keine Installation und keinen Merge**. Der Ordner `skills/form-intent` ist der installierbare Kandidat. Forschung, Design, Tests und der Test-Router gehören nicht in die aktive Skill-Installation.

## Konkreter Freigabegegenstand

Nur `form-intent` neu aktivieren, mit den geprüften Dateihashes aus dem Release-Manifest. Keinen vorhandenen Framing-/Formation-/Prompt-Skill ersetzen, deaktivieren oder ändern. Keine kanonischen Templates überschreiben. Ob `intent/v1` künftig als Standard deprecated werden soll, ist eine separate Systementscheidung.

## Schritte nach ausdrücklicher Autorisierung

1. Die aktuelle persönliche Skill-Verwaltung und deren geltende Creator-/Installationsanweisung lesen. Den geprüften Kandidatenstand und einen Snapshot des bisherigen persönlichen Skill-Baums festhalten. Vorhandene uncommittete Änderungen anderer Arbeiten unberührt lassen.
2. Prüfen, ob bereits ein Skill mit Frontmatter-Name `form-intent` existiert. Bei Namenskollision Inhalt/Autorität prüfen; nicht blind überschreiben. Nur den freigegebenen Kandidatenordner in den vorgesehenen persönlichen Skill-Checkout übernehmen.
3. Den bereitgestellten strukturellen Skill-Validator auf genau diesem Installationsordner ausführen. Referenzpfade, UI-Metadaten und Paketmanifest vergleichen. Es sind keine zusätzlichen Python-/Node-Pakete oder API-Schlüssel nötig.
4. Nur diese Skill-Änderung mit dem vorgesehenen persönlichen Skill-Speicher synchronisieren. Die vom System gegebenenfalls neu zugewiesene Ordnerkennung über den exakten Skill-Namen wiederfinden. Quellstand und Runtime-Sicht getrennt verifizieren.
5. In einem neuen verfügbaren Kontext einen kleinen Intent explizit mit `$form-intent` aufrufen und die tatsächliche Dateipersistenz prüfen. Zusätzlich automatische Auswahl bei einem Intent-Auftrag und Nichtaktivierung bei gewöhnlicher Umsetzung prüfen. Diese Discovery-/Installationsnachweise wurden im vorliegenden Kandidatenlauf bewusst nicht vorgetäuscht.
6. Nur bei erfolgreicher Aktivierungs-/Persistenzprüfung Installation bestätigen. Keine automatische Migration, kein Folgeskill, kein Spec/Plan-Auftrag.

## Freigabekriterien und Grenzen

Der strukturelle Validator wurde auf dem isolierten Kandidaten ausgeführt; Verhaltenstests nutzen denselben Ordner direkt. Das belegt Installierbarkeit des Formats und instruktionsbasiertes Verhalten, nicht produktive Aktivierung. Echte Nutzer-UX, langfristige Persistenz und Discovery-Kollisionen bleiben gesonderte Beobachtungen nach einem freigegebenen begrenzten Einsatz.

In Work verwenden Formation-Dateien die etablierten Speicherfunktionen und den vereinbarten Ort. In einer lokalen Codex-Umgebung kann es ein Projektordner sein. Der Skill enthält keinen eigenen Storage-Dienst und verlangt keine erfundene Integration.
