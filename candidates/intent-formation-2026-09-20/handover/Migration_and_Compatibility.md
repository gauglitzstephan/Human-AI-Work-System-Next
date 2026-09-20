# Migration and Compatibility

## Empfehlung zum bestehenden System

| Bestehender Bestandteil | Empfehlung | Begründung |
|---|---|---|
| Professional Work Framing v0.1.4 | **Unverändert erhalten** | Abgeschlossener Audit empfiehlt KEEP; breiterer Aufgabenbereich. Vollständiger aktueller Runtime-Code nicht verfügbar, daher keine Ablösebehauptung. |
| Aktuelle kanonische Support-Skills in Human-AI-Work-System-Next | **Unverändert erhalten** | Neue Capability ist ein isolierter Kandidat, keine Rückkehr zur archivierten allgemeinen Work Formation. |
| `prepare-chatgpt-prompts` | **Unverändert erhalten** | Prompt-Erstellung ist ein anderer Auftrag als Problem-/Intent-Formation. |
| `intent/v1` als vorhandenes Artefakt/Archiv | **Erhalten** | Quellen, Entscheidungen, Anforderungen und Verlauf nicht vernichten. |
| `intent/v1` als universelles neues Pflichtformular | **Bei späterer Annahme des Kandidaten deprecaten** | Semantischer Kern bleibt, nachgelagerte Pflichtlast entfällt. Keine automatische Migration bestehender Dateien. |
| v2 Reference Runtime / Inquiry-Schema | **Als Referenz erhalten, nicht zusätzlich aktivieren** | Wertvolle Mechanismen übernommen; doppelter Formation-Owner und widersprüchliche Gates vermeiden. |
| Neuer `form-intent` | **Separat prüfen und erst nach Freigabe installieren** | Enger Intent-Endpunkt; kein Ersatz für alle Framing-/Arbeitsqualifikationsaufgaben. |

## Semantische Migration von intent/v1

| v1-Inhalt | Ziel | Regel |
|---|---|---|
| Origin, Problem, Stakeholder, Baseline | Intent: Zweck/Kontext/Betroffene | Bedeutung erhalten, Redundanz verdichten. |
| Outcome/Kausalhypothese, Why/Value | Intent: Wirkung plus materiale Annahme | Hypothese nicht zu gesicherter Ursache aufwerten. |
| Evidence Register | Kurze lokale Herkunft plus Quellenanhang/State | Materiale Provenance erhalten; nicht jede Aussage bureaucratisieren. |
| Success Contract | Outcome-Bedeutung und relevante Guardrails ins Intent | Messinstrumentierung/Featureabnahme als vorhandenen Downstream-Inhalt getrennt bewahren, nicht neu erarbeiten. |
| Scope, Constraints, Preferences | Intent: Grenzen/Entscheidungen | Tatsächliche Bindung vs Präferenz vs Mittelidee unterscheiden; Werte niemals durch AI-Evidenz „überstimmen“. |
| Requirements Elasticity / Delegation | Separates vorhandenes Downstream-/Autoritätsmaterial | Nicht stillschweigend löschen oder als neue Ausführungsfreigabe übernehmen. |
| Assumptions/Unknowns | Intent, wenn Bedeutung/Übergabe materiell; Inquiry-Details in State | Blocking/nonblocking begründen; Unknown von Undecided trennen. |
| Optionen / Nichtstun | Dauerhafte Framing-Entscheidung ins Intent, Untersuchung in State | Reuse/Stop erhalten, kein Zwang zu beliebigen Alternativen. |
| Pre-mortem / Recovery | Materiale Schadenserwartung in Grenzen/Guardrails | Operative Recovery-Pläne downstream bewahren. |
| Economics | Attention-Entscheidung in State; Outcome-Viability ggf. Intent | Keine Pflichtökonomie für kleine persönliche Arbeit. |
| Holdouts, Telemetrie, Spec/Plan-Links, Outcome Log | Bestehende Downstream-/Verlaufsartefakte | Quelle erhalten und verlinken; nicht als Intent-Formation neu ausfüllen. |

## Verlustarme Durchführung nach späterem Auftrag

Original unverändert sichern und Quellenrevision festhalten. Eine separate neue Intent-Datei erzeugen. Jedes materiale Originalelement erhält einen Verbleib: Intent, Formation State, vorhandenes Downstream-Material, historische Quelle oder gezielte menschliche Klärung. Unklare Entscheidungen nicht rekonstruieren oder akzeptiert nennen. Alte Akzeptanz nur übernehmen, wenn die Bedeutung nachweislich unverändert und ihr Bezug eindeutig ist; sonst neue Revision unakzeptiert markieren.

Migration endet mit einem Inhaltsvergleich anhand Purpose, Grenzen, Entscheidungen, Unsicherheit und Provenance. Keine automatisch generierte Specification aus ausgelagerten Punkten. Dieser Auftrag hat **keine** bestehenden Nutzer-Intents migriert; die Vergleichsläufe sind isolierte Szenarien.

## Koexistenz

Für einen Intent-Formation-Auftrag arbeitet genau ein semantischer Owner. Ein breiter Framing-Skill kann einen bereits geklärten Auftrag übergeben; der Intent-Skill übernimmt Kontext und offene Punkte, statt nochmals dieselben Gates abzufragen. Eine endgültige Beschreibungskollision lässt sich erst nach Installation in der tatsächlichen Discovery prüfen. Bis dahin wird kein bestehendes Triggerverhalten geändert.
