# Rollback

Seit 20.09.2026 ist `form-intent` nach ausdrücklicher Nutzerfreigabe neu installiert. Der [Installationsnachweis](Installation_Verification_2026-09-20.md) beschreibt den genauen Stand. Zuvor vorhandene Skills und kanonische Templates wurden nicht ersetzt oder deaktiviert.

## Rücknahme der erfolgten Neuinstallation

1. Weitere Nutzung des neuen `form-intent` stoppen. Den tatsächlichen installierten Ordner über seinen Frontmatter-Namen identifizieren; nicht auf einen alten generierten Pfad vertrauen.
2. Nur die in der Installationsfreigabe dokumentierte Änderung mit dem vorgesehenen Skill-Verfahren deaktivieren oder zurücknehmen. Ist es eine Neuinstallation, diese entfernen/deaktivieren; wurde nach gesonderter Freigabe ein bestehender Skill ersetzt, exakt dessen gesicherte vorige Revision wiederherstellen. Keine parallelen Änderungen anderer Skills rückgängig machen.
3. Synchronisation und tatsächlichen Aktivierungsstand verifizieren. Bei weiterhin sichtbarer alter UI den Quellstand nicht mit Runtime-Aktivierung gleichsetzen.
4. Erzeugte `intent.md` und `formation.md` erhalten. Ein Skill-Rollback löscht keine Nutzerarbeit und widerruft nicht automatisch menschliche Entscheidungen. Betroffene Intents anhand konkreter Fehlerhinweise prüfen; keine pauschale Neuformung.
5. Einen kleinen Intent-Aufruf prüfen: Der zurückgenommene Skill darf nicht mehr automatisch aktiv werden; die vorherige Arbeitsweise muss weiter nutzbar sein. Einen notwendigen Reparaturauftrag getrennt formulieren.

## Auslöser

Konkrete falsche Akzeptanz, wiederholte Grenzverletzung, schädliche Überschreibung von Nutzerurteilen, State-Verlust oder untragbare Interaktionslast rechtfertigen Rücknahme oder gezielte Reparatur. Ein einzelner kosmetischer Unterschied rechtfertigt keine Systemrücksetzung. Der Gegenstand der Rücknahme ist immer der genaue neue Skill-Stand, nicht das gesamte Arbeitssystem.
