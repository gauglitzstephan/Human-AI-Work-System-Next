# Intent Domain Model

Eigenständige Synthese nach Prozessanalyse; Format ist keine Ontologie. Das Modell benennt benötigte Bedeutung, nicht stets erforderliche Felder.

| Begriff | Bedeutung und Beziehung | Materialität |
|---|---|---|
| Intent | Aktuelle, versionierte Bedeutung eines beabsichtigten Vorhabens | Immer; keine Umsetzungsermächtigung. |
| Purpose / Why | Menschlich relevantes Anliegen und Wert | Immer, darf mit Outcome in einem Absatz stehen. |
| Problem / Opportunity | Zu ändernde Situation oder zu erschließender Nutzen | Immer, kein künstliches Problem bei klarer Opportunity. |
| Desired Outcome | Erwünschte Veränderung für relevante Personen/Organisation | Immer; von vorgeschlagenem Mittel trennen. |
| Context / Current State | Ausgangslage zur richtigen Interpretation | Nur notwendige Fakten und Quellen. |
| Actor / affected party | Owner, Nutzer, legitime Stakeholder, mitbetroffene Nichtteilnehmende | Rollen unterscheiden, soweit Konsequenzen variieren. |
| Boundary / Constraint | Was gemeint, ausgeschlossen oder tatsächlich gesetzt ist | Materiale Grenzen; Quelle bei strittiger Autorität. |
| Evidence | Nachvollziehbare Quelle/Beobachtung mit Reichweite | Bei Aussagen, deren Vertrauen oder spätere Korrektur davon abhängt. |
| Human statement | Was eine Person berichtet oder ausdrückt | Belegt ihre Aussage, nicht automatisch eine externe Tatsache. |
| AI inference | Interpretative Ableitung, nicht menschlich übernommen | Sichtbar, wenn materiell; kann durch Entscheidung übernommen werden. |
| Assumption | Vorläufig gesetzte, widerlegbare Prämisse | Benenne Bedeutung, wenn falsch. |
| Unknown | Fehlendes Wissen | Wirkung auf Readiness und spätere Arbeit. |
| Undecided / judgment | Noch nicht getroffene Wert-/Prioritäts-/Commitmententscheidung | Nicht durch Recherche oder AI-Präferenz „lösen“. |
| Human decision | Tatsächlich getroffene, zuordenbare Wahl | Von Empfehlung/Illustration unterscheiden. |
| Outcome validation | Woran Nutzen und relevante schädliche Nebenwirkung erkennbar sind | Immer in angemessener Genauigkeit; kein Featuretest. |
| Validity | Bedingungen, unter denen Bedeutung/Entscheidung noch gilt | Bei zeitabhängigen Quellen, Chancen oder Constraints. |
| Readiness | Begründete Eignung zur qualifizierten Übergabe oder anderer Ausgang | Immer. |
| Acceptance | Explizite menschliche Annahme einer Revision | Eigene Dimension; ohne Aussage „nicht dokumentiert“. |

**Nicht Teil des Modells:** vollständige Requirements, Lösungsarchitektur, Feature-Akzeptanz, Taskgraph, Ressourcen-/Rolloutplan. Vom Nutzer bereits gesetzte technische Bindungen können Constraints sein, ohne neue Solution Design-Arbeit zu erlauben.

## Revision und Beziehungen

Eine stabile lokale ID verbindet Intent, Working State und Quellen. Eine Revision verändert sich bei materieller Bedeutungsänderung. Claim-IDs sind nur für komplexe Reparaturen nützlich; der kleine Fall braucht keine Claim-Datenbank. Ein menschlicher Entschluss kann auf Evidenz beruhen, bleibt aber ein Entschluss. Eine korrigierte Prämisse kann mehrere Abschnitte invalidieren: etwa „Capture scheitert“ → Outcome „Erfassung beschleunigen“ → Erfolg „mehr Notizen“. Deshalb wird die Abhängigkeitskette semantisch geprüft, nicht nur ein Satz ersetzt.

## Trennung zum Formation State

State hält zusätzlich Untersuchungsstand, live Gegenhypothesen, letzte wichtige Korrektur, ausstehende Inquiry und Routenbegründung. Intent hält die aktuelle für Reviewer und Downstream nötige Bedeutung. Historische Pfade werden nicht vollständig dupliziert. Beide können auf gleiche Quellen verweisen. Unresolved material claims dürfen bei der Kompression nicht verschwinden.
