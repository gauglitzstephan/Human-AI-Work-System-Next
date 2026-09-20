---
schema: "intent/v1"
id: "INT-YYYY-NNNN"
title: "<kurzer Ergebnistitel>"
status: "discovery"
intent_type: "feature"
profile: "standard"
risk_tier: 2
decision_type: "two_way"
originator: "<Name oder Rolle>"
owner: "<Name oder Rolle>"
decision_owner: "<Name oder Rolle>"
reviewers: []
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
review_by: "YYYY-MM-DD"
expires_at: null
commitment_status: "uncommitted"
source_of_truth: "repo"
supersedes: null
superseded_by: null
tags: []
links:
  evidence: []
  related_intents: []
  spec: null
  plan: null
  decisions: []
  scenarios: []
  tests: []
  telemetry: []
  incidents: []
---

# Intent: <Titel>

## 0. Decision Capsule

| Feld | Inhalt |
|---|---|
| Beabsichtigte Veränderung | <ein Satz> |
| Entscheidung, die jetzt benötigt wird | <accept / experiment / reject / clarify> |
| Warum jetzt | <Trigger, Cost of Delay oder Lernfenster> |
| Aktuelle Empfehlung | <inklusive `noch keine`> |
| Konfidenz | <niedrig / mittel / hoch, mit Begründung> |
| Blocker | <offene Punkte, die eine Entscheidung verhindern> |

## 1. Original Intent — unverändert

> <Wörtliche oder möglichst quellnahe Aussage des Originators. Rechtschreibung darf korrigiert werden; Bedeutung nicht.>

**Quelle und Zeitpunkt:** <Gespräch, Ticket, Incident, Kundenbeobachtung; Datum>

## 2. Problemraum und Kontext

### 2.1 Beobachtbarer Ist-Zustand

<Beschreibe Verhalten und Auswirkungen, nicht bereits die gewünschte Lösung.>

### 2.2 Betroffene Akteure und Jobs-to-be-done

| Akteur | Kontext / Job | Heutiger Schmerz oder entgangener Nutzen | Exposition |
|---|---|---|---|
| <...> | <...> | <...> | <Häufigkeit / Größenordnung> |

### 2.3 Baseline und Systemgrenze

- Baseline: <heutige Messwerte oder `unbekannt`>
- Betroffene Systeme/Prozesse: <...>
- Nicht betroffene Systeme/Prozesse: <...>
- Relevanter Zeitraum und Population: <...>

## 3. Evidenz- und Erkenntnisregister

Jede relevante Aussage erhält einen epistemischen Typ. Sprachliche Glätte ist kein Beleg.

| ID | Aussage | Typ | Quelle | Konfidenz | Frische / Review | Owner |
|---|---|---|---|---|---|---|
| E-001 | <...> | observation / data / source / inference / assumption / decision | <Link oder Herkunft> | <0–100 % oder L/M/H> | <Datum> | <...> |

**Widersprechende Evidenz:**  
<Was spricht gegen die Problemdeutung oder gegen die aktuelle Empfehlung?>

**Bekannte Evidenzlücken:**  
<Welche Information fehlt und wie entscheidungsrelevant ist sie?>

## 4. Zielbild und kausale Hypothese

### 4.1 Beabsichtigtes Outcome

<Welche beobachtbare Veränderung soll bei welchen Akteuren eintreten?>

### 4.2 Kausale Hypothese

> Wenn wir <Interventionsklasse, noch ohne technische Lösung>, dann <Verhaltens-/Systemänderung>, weil <Mechanismus>. Unter <Bedingungen> erwarten wir <Outcome>.

### 4.3 Nicht behauptet

<Was folgt ausdrücklich nicht aus der Hypothese? Welche Kausalität ist noch unbewiesen?>

## 5. Success Contract

### 5.1 Outcomes

| Signal | Baseline | Ziel | Mindestakzeptanz | Messfenster | Datenquelle | Owner |
|---|---:|---:|---:|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <...> | <...> |

### 5.2 Guardrails

| Guardrail | Heutiger Wert | Nicht überschreiten/unterschreiten | Reaktion bei Verletzung |
|---|---:|---:|---|
| <...> | <...> | <...> | <pause / rollback / investigate> |

### 5.3 Vorab festgelegte Verdict-Regeln

- **Validated:** <Bedingung>
- **Partial:** <Bedingung>
- **Failed:** <Bedingung>
- **Inconclusive:** <Bedingung>
- **Sofortiger Abbruch:** <Bedingung>

## 6. Scope und Abgrenzung

### In Scope

- <...>

### Non-Goals

- <...>

### Später möglich, aber heute nicht entschieden

- <...>

## 7. Constraints, Invarianten und Präferenzen

| ID | Aussage | Klasse | Begründung / Quelle | Owner | Ablauf/Review |
|---|---|---|---|---|---|
| C-001 | <...> | invariant / constraint / preference | <...> | <...> | <...> |

**Regel:** Invarianten sind nicht optimierbar. Constraints begrenzen den Lösungsraum. Präferenzen dürfen bei besserer Evidenz überstimmt werden.

## 8. Requirements Elasticity und delegiertes Judgment

Definiere bewusst, wo Präzision nötig ist und wo das Umsetzungsteam oder ein Agent urteilen darf.

| Dimension | Zielwert | Akzeptabler Bereich | Harte Grenze | Wer darf abweichen? | Eskalationstrigger |
|---|---|---|---|---|---|
| <z. B. Latenz, Termin, UX-Form, Kosten> | <...> | <...> | <...> | <Agent / Engineer / PO> | <...> |

### Entscheidungsheuristiken

1. <Beispiel: Nutzerverständlichkeit vor interner Modelltreue, solange keine falsche Information entsteht.>
2. <...>

### Nicht delegierbare Urteile

- <Werteentscheidung, Risikoakzeptanz, regulatorische Auslegung, Budget-/Commitment-Änderung>

## 9. Annahmen, Unbekannte und Falsifikation

| ID | Annahme / Frage | Relevanz | Widerlegende Beobachtung | Nächster günstigster Test | Owner | Fällig | Blockierend? |
|---|---|---|---|---|---|---|---|
| A-001 | <...> | <...> | <...> | <...> | <...> | <...> | ja/nein |

### Was würde unsere Meinung ändern?

<Explizite Evidenz, bei der Ziel, Scope, Priorität oder Lösungsrichtung neu bewertet werden muss.>

## 10. Optionen und Entscheidungsvorbereitung

Mindestens `nichts tun` und `kleinster reversibler Versuch` betrachten.

| Option | Erwarteter Nutzen | Kosten / Zeit | Hauptrisiken | Reversibilität | Informationsgewinn |
|---|---|---|---|---|---|
| O-0 Nichts tun | <...> | <...> | <...> | <...> | <...> |
| O-1 Kleinster Versuch | <...> | <...> | <...> | <...> | <...> |
| O-2 <...> | <...> | <...> | <...> | <...> | <...> |

**Entscheidungskriterien und Gewichtung:** <...>

## 11. Obstacle Analysis und Pre-Mortem

> Angenommen, das Vorhaben gilt in sechs Monaten als Fehlschlag. Was ist wahrscheinlich passiert?

| Failure Mode / Hindernis | Ursache | Frühes Signal | Prävention | Containment | Rollback / Recovery | Owner |
|---|---|---|---|---|---|---|
| F-001 | <...> | <...> | <...> | <...> | <...> | <...> |

Berücksichtige insbesondere: falsches Problem, falsche Population, Goodhart/Proxy-Gaming, versteckte Abhängigkeit, Missbrauch, Security/Privacy, Datenqualität, Betriebsüberlastung, Migration, menschliche Umgehungsstrategien und Agent-Fehlinterpretation.

## 12. Economics und Value of Information

Zahlen als Bandbreiten angeben; Scheingenauigkeit vermeiden.

| Größe | Low | Base | High | Quelle / Annahme |
|---|---:|---:|---:|---|
| Nutzen pro Zeitraum | <...> | <...> | <...> | <...> |
| Cost of Delay pro Zeitraum | <...> | <...> | <...> | <...> |
| Build-/Change-Kosten | <...> | <...> | <...> | <...> |
| Laufende Betriebs-/Review-/Modellkosten | <...> | <...> | <...> | <...> |
| Erwarteter Schaden bei Fehlentscheidung | <...> | <...> | <...> | <...> |

- Evidence Budget vor Commitment: <...>
- Nächster günstigster informationsgewinnender Schritt: <...>
- One-way oder Two-way Door: <...>
- Kill-/Pause-Kriterien: <...>
- Opportunitätskosten: <...>

## 13. Verifikation, Szenarien und Produktionslernen

### 13.1 Akzeptanz- und Holdout-Szenarien

| ID | Szenario | Beobachtbares Ergebnis | Testort | Darf Implementierer es sehen? |
|---|---|---|---|---|
| S-001 | <...> | <...> | <test / staging / production simulation> | ja/nein |

### 13.2 Adversarial und unerwünschtes Verhalten

- <...>

### 13.3 Telemetrie und Awareness Requirements

| Requirement/Outcome | Runtime-Signal | Aggregation / Zeitraum | Kontrollband | Aktion bei Verletzung |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### 13.4 Qualitative Evidenz

<Kundeninterviews, Support-Traces, Screen Recordings, Incident Replays, Beobachtungen>

## 14. Traceability und Ableitungen

| Artefakt | Status | Beziehung zum Intent | Link / ID |
|---|---|---|---|
| `spec.md` | <...> | operationalisiert | <...> |
| ADR | <...> | entscheidet technische Option | <...> |
| `plan.md` | <...> | setzt um | <...> |
| Tests/Evals | <...> | verifizieren | <...> |
| Telemetrie | <...> | validiert Outcome | <...> |

**Coverage-Lücken:** <Intent-Aussagen ohne Downstream-Nachweis oder Downstream-Artefakte ohne Intent-Bezug>

## 15. Entscheidung, Dissens und Commitment

- Entscheidung: `pending | clarify | accepted | experiment | rejected`
- Entscheidungsdatum: <...>
- Decision Owner: <...>
- Begründung: <...>
- Akzeptiertes Restrisiko: <...>
- Dokumentierter Dissens: <...>
- Commitment-Status: `uncommitted | funded | scheduled | in_delivery`
- Nächster Gate-Termin: <...>

## 16. Änderungs- und Outcome-Log

| Datum | Änderung / Beobachtung | Semantisch? | Autor | Folge |
|---|---|---|---|---|
| <...> | <...> | ja/nein | <...> | <none / re-review / supersede> |

### Outcome Verdict

- Verdict: `not_evaluated | validated | partial | failed | inconclusive`
- Beobachtungszeitraum: <...>
- Evidenz: <...>
- Unerwartete Effekte: <...>
- Entscheidung: <beibehalten / ausweiten / korrigieren / zurückrollen / superseden>
- Neues Intent: <ID oder `nicht erforderlich`>
