## Urteil

**`PROCEED WITH BOUNDED CONDITIONS`**

Route B wurde durch die externe Prüfung nicht falsifiziert. Es ist derzeit die plausibelste Realisierung des geschlossenen Target Architecture v0.2, weil es Native Primary als einzigen operativen Owner erhält, Formation begrenzt, professionelle Methoden auslagert und Subagents nur als Provider behandelt.

Es ist aber noch nicht robust genug für unbedingte Installation. Die größte Gefahr ist nicht eine fachlich falsche Architektur, sondern dass ihre semantischen Sicherungen im Runtime-Verhalten zu einem zweiten Controller, einem Method-Monolithen und einer selbstverstärkenden Kontrollschicht werden.

Das [Target Architecture v0.2](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/main/architecture/TARGET-ARCHITECTURE-BASELINE-v0.2.md) bleibt geschlossen. Route B bleibt ein unpromoted, non-installed Source Candidate. Keine Datei wurde geändert, nichts installiert oder getestet.

## Fünf unabhängige Linsen

| LinseStärkste BestätigungStärkste FalsifikationsgefahrErgebnis |                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                               |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Native-Agent-Architektur                                       | Native Primary bleibt Manager; Spezialisten sind begrenzte Provider. Das entspricht dem „agents as tools“-Muster.                   | ChatGPT/Codex orchestriert Spawn, Follow-up, Wait, Thread Closure und Synthese bereits nativ. Jede zweite Orchestrierungsschicht wäre Duplikation. [OpenAI Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [OpenAI Orchestration](https://developers.openai.com/api/docs/guides/agents/orchestration)                                                                                                                                           | Conditional PASS              |
| Context Engineering                                            | Kernel, Formation und Methods können per Progressive Disclosure getrennt geladen werden; Subagents schützen den Primary Context.    | Langer Kernel, vollständige Method Registry, State Cards und Return Contracts können den gewonnenen Context wieder auffüllen. Frontier-Praxis bevorzugt minimale High-Signal-Instruktionen und Just-in-time-Retrieval. [OpenAI Skills](https://learn.chatgpt.com/docs/build-skills), [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)                                                                   | Conditional PASS              |
| Human–AI Collaboration                                         | Authority, Acceptance, Commitment, Human contribution und Human Gate sind sauber getrennt.                                          | Formale Entscheidungsrechte garantieren noch keine wirksame Agency: Menschen können zu Reviewern fertiger AI-Arbeit werden, kritisches Denken und Autorschaft verlieren oder nur noch rubber-stampen. Die Microsoft-Studie zeigt eine Assoziation zwischen hohem AI-Vertrauen und weniger kritischem Denken; sie ist jedoch nicht kausal. [CHI-2025-Studie](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf) | Partial PASS                  |
| Arbeits-/Organisationsdesign                                   | Strategy, Operating, Work, Execution und Learning/Change bleiben getrennte Verantwortungen; CCR-06 schützt vor lokaler Optimierung. | Route B ist episodenorientiert. Koordinationskosten, kumulative Human-Capability-Effekte und reale Nutzungsergebnisse können zwischen Episoden verschwinden.                                                                                                                                                                                                                                                                                                              | Partial PASS                  |
| Brittleness/unintended harm                                    | Die v0.1→v0.8-Linie enthält echte Gegenbeweise und demotet FAIL/UNVERIFIED statt sie wegzuerklären.                                 | Alle Kontrollen werden überwiegend vom gleichen probabilistischen System interpretiert. Neue Fehler können immer neue Regeln erzeugen, die Context, Latenz und Konflikte erhöhen und dadurch weitere Fehler verursachen.                                                                                                                                                                                                                                                  | Hohe Runtime-Restunsicherheit |

## Stärkste Argumente für Route B

1. **Es ergänzt die native Plattform, statt sie grundsätzlich zu ersetzen.** Native Primary besitzt Episode, Planung, Routing und Synthese; Route B liefert die semantischen Grenzen.
2. **Es adressiert reale, wiederholte Fehlerklassen.** Die Linie umfasst premature solutioning, fehlende professionelle Referenzbasis, Evidence-Slice-Scope-Collapse, fehlenden Bootstrap, Parent Drift und falschen Operator-Handback.
3. **Es operationalisiert die bereits akzeptierte Adaptive Work Selection**, ohne einen permanenten Work Engine, zentralen State Store oder festen Lifecycle einzuführen.
4. **Es passt zur aktuellen Agent-Praxis:** ein Manager, enge Spezialistenverträge, wenige Provider, parallele Arbeit nur bei echter Zerlegbarkeit. OpenAI empfiehlt ausdrücklich, mit einem Agenten zu beginnen und nur bei geändertem Capability-, Policy- oder Prompt-Contract zu splitten.
5. **Die Human–AI-Allokation ist differenzierter als „Human in the loop“.** Die P&G-Feldstudie zeigt sowohl starke AI-Komplementarität als auch verbleibenden Wert menschlicher evaluativer Auswahl. [Cybernetic Teammate](https://pubsonline.informs.org/doi/10.1287/orsc.2025.20702)
6. **Die Requirements sind outcome- und wirtschaftsorientiert.** CR-10–CR-12 verhindern zumindest semantisch, dass Agentenzahl, Dokumente oder Prozesskonformität als Erfolg gelten. [Requirements v0.2](https://github.com/gauglitzstephan/Human-AI-Work-System-Next/blob/main/foundation/CONCERNS-AND-REQUIREMENTS-v0.2.md)

## Stärkste Argumente gegen Route B

1. **Formation kann trotz gegenteiliger Deklaration zum versteckten Controller werden.** Wer Readiness, Method, Human contribution, Provider, Persistence, Assurance und nächste Transition bestimmt, kontrolliert faktisch einen Großteil der Episode. „Terminates“ allein verhindert keine sofortige Reaktivierung.
2. **Der Method Layer besitzt natürliche Monolith-Tendenzen.** Jeder neue Qualitätsfehler kann zu einem neuen Pack, Anti-Pattern, Qualifikationsschritt oder Assurance-Contract führen. Damit würde die alte Material-Work-Monolithik lediglich in einen Method-Monolithen verschoben.
3. **Subagents sind kein genereller Qualitätsverstärker.** Eine kontrollierte Studie über 180 Konfigurationen fand Verbesserungen bis +81 % bei parallelisierbaren Aufgaben, aber Verschlechterungen von 39–70 % bei sequenziellen Aufgaben. Unabhängige Agenten verstärkten Fehler bis zu 17,2-fach. [Scaling Agent Systems](https://arxiv.org/html/2512.08296v1)
4. **Fresh Context ist keine echte Unabhängigkeit.** Derselbe Modelltyp, dieselben Quellen, dieselben Instruktionsannahmen und dieselbe Bewertungsmethode können hoch korrelierte Fehler erzeugen.
5. **Semantische Kontrolle ist noch keine mechanische Kontrolle.** In ChatGPT Work teilen Subagents die Tool-Oberfläche des Parent Chats; Permission- und Connector-Grenzen bleiben surface-spezifisch. [OpenAI Permission Controls](https://learn.chatgpt.com/docs/agent-configuration/subagents)
6. **Human–AI-Synergie darf nicht angenommen werden.** Eine Meta-Analyse von 106 Experimenten fand Human–AI-Kombinationen im Mittel schlechter als den jeweils besseren Human- oder AI-only-Ansatz; Vorteile waren stark aufgabenspezifisch. [Nature Human Behaviour](https://www.nature.com/articles/s41562-024-02024-1)

## Annahmen, die bereits obsolet oder nicht mehr haltbar sind

- Eine Skill-Schicht müsse Spawn, Wait, Follow-up, Thread Management oder Ergebnisaggregation implementieren.
- Mehr Agenten oder ein zusätzlicher Reviewer verbesserten Qualität grundsätzlich.
- Ein separater Agent sei automatisch ein unabhängiger Prüfer.
- Mehr explizite Regeln erzeugten zuverlässig besseres Runtime-Verhalten.
- Chat, Work und Codex hätten identische Orchestrierungs-, Permission- und Steuerungsmöglichkeiten.
- Formale Human Gates oder reservierte Entscheidungskompetenz reichten aus, um Human Agency und Capability zu erhalten.
- Ein statischer Method-Katalog sei ein geeigneter universeller Eingang für professionelle Arbeit.

Nicht obsolet sind dagegen: Parent-/Authority-Integrität, Probe ≠ Candidate, semantische Return/Rebind-Prüfung und claim-matched assurance. Diese werden nicht vollständig durch native Transportmechanismen übernommen.

## Top 10 plausible Failure Modes

| #Failure ModeMechanismusBehandlung |                                    |                                                                                                       |                                                               |
| ---------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1                                  | Hidden Formation Controller        | Formation reaktiviert sich nach jeder Transition und besitzt faktisch die Episode.                    | Source repair; bei wiederholtem Auftreten Architecture reopen |
| 2                                  | Method-Layer-Monolith              | Packs akkumulieren Orchestration, Evidence, QA und Control statt nur Domain Method.                   | Source repair; struktureller Kill Trigger                     |
| 3                                  | Native-Capability-Duplikation      | Adapter reproduziert Spawn/Wait/Synthesis/Permissions und driftet von der Plattform.                  | Source repair                                                 |
| 4                                  | Over-delegation                    | „Material“ wird zu leicht als Subagent-Trigger interpretiert.                                         | Source repair + Runtime observation                           |
| 5                                  | Context fragmentation              | Child Packets verlieren implizite Anforderungen; Return-Summaries verlieren Caveats.                  | Source repair + Runtime observation                           |
| 6                                  | Stale-world integration            | Parent verändert sich, ohne dass Child oder Primary die relevante Delta-Dimension erkennt.            | Runtime observation; sofortiger FAIL bei Integration          |
| 7                                  | False independent assurance        | Reviewer teilt Modell-, Quellen- oder Methodenfehler und gibt trotzdem PASS.                          | Source repair + Runtime observation                           |
| 8                                  | Human capability/authority erosion | Der Human wird zu Abnahme, Korrektur oder Autorisierung bereits festgelegter AI-Arbeit reduziert.     | Source repair + längsschnittliche Observation                 |
| 9                                  | Process-success/outcome-failure    | Formation, Packets und Gates sind korrekt, aber Work Product, Nutzung oder Ergebnis bleiben schlecht. | Runtime observation; Learning/Change handoff                  |
| 10                                 | Control ratchet                    | Jeder Fehler erzeugt zusätzliche Regeln; Context und Latenz steigen; neue Regelverletzungen folgen.   | Source repair; bei Wachstum ohne Nutzen Architecture reopen   |

Die MAST-Studie bestätigt insbesondere Specification Drift, Conversation Reset, Information Withholding, Task Derailment, Premature Termination sowie fehlende oder falsche Verification als empirische Multi-Agent-Fehlerklassen. [MAST/NeurIPS 2025](https://arxiv.org/pdf/2503.13657)

## Fehlende Verantwortungsallokationen

Keine neue Top-Level-Verantwortung ist derzeit erforderlich. Drei bestehende Verantwortungen sind in Route B jedoch noch nicht hinreichend operationalisiert:

- **Human capability trajectory:** dauerhafter Owner bei Human + Operating/Learning, nicht nur lokaler CCR-07-Trigger.
- **Platform compatibility:** Operating/Execution muss Änderungen an Skills, Permissions, Subagents und Surfaces beobachten; der Adapter darf keine dauerhaft gültigen Plattformannahmen enthalten.
- **Post-delivery outcome/economics:** Learning/Change oder der reale Empfänger muss Human correction, Rework, Use und Outcome beobachten. Formation darf dies nicht selbst übernehmen.

## Failure Modes außerhalb von Requirements v0.2

Kein wesentlicher Problemtyp ist vollständig unowned. Requirements v0.2 deckt die Klassen bereits abstrakt ab. Nur fünf Mechanismen sind unterexpliziert:

- Interferenzen zwischen Global-, Project-, Skill- und Provider-Instruktionen;
- verlustbehaftete Context-Kompression und divergierende Agent-World-States;
- kumulative Capability-Erosion über viele lokal „immaterielle“ Episoden;
- Regelalterung, Retirement und Control-Complexity-Debt;
- Need-to-know-Context und Least-Privilege pro Subagent.

Das rechtfertigt derzeit Source Safeguards, keine Requirements- oder Target-Architecture-Änderung.

## Erforderliche Safeguards vor Installation

1. Formation darf nur bei einem benannten Material Delta aktiviert werden und sich nicht selbst reaktivieren.
2. Native Primary bleibt alleiniger Episode-, Composition- und Final-Answer-Owner.
3. Der Adapter darf keine nativen Spawn-/Wait-/Permission-/Synthesis-Mechanismen nachbauen.
4. Der Method Layer enthält nur scoped Method/Reference-Pointer, wird just-in-time geladen und besitzt weder Control noch Authority.
5. Subagent-Einsatz braucht explizite Zerlegbarkeit, Context-Isolation- oder Assurance-Value; sequenzielle Arbeit bleibt standardmäßig single-agent.
6. Reviewer-Unabhängigkeit muss über unterschiedliche Evidenz, Methode oder deterministische Checks entstehen – nicht nur über einen frischen Thread.
7. Parent permission mode, Context-Minimierung und tool-specific authority müssen vor Dispatch gebunden sein.
8. Evaluation muss Time-to-useful-outcome, Human correction/rework, Intended-use quality, Use und Capability-Effekt messen – nicht Formation- oder Agent-Compliance.
9. Jede neue Kontrollregel braucht einen belegten Failure Mode, einen erwarteten Nutzen und eine Retirement-/Simplification-Prüfung.

## Explizite Falsifiers / Kill Criteria

Route B wird demotet oder strukturell reopened, wenn eines der folgenden Kriterien eintritt:

1. **Sofortiger Kill:** unauthorized write/action, Acceptance, Promotion oder „continue“ als Autorisierung.
2. **Sofortiger Kill:** Integration eines stale Provider Return ohne Parent-Reconciliation.
3. **Sofortiger Kill:** Probe, plausible Output oder Child Result wird als Candidate/Parent Completion promoted.
4. **Architecture reopen:** Formation reaktiviert sich in zwei repräsentativen Fällen ohne neue Evidenz, Parent Delta oder externe Transition.
5. **Architecture reopen:** derselbe generische Method-Prozess wird in drei unabhängigen Domains zum faktischen Pflicht-Gateway.
6. **Composition kill:** Subagents verschlechtern bei fünf vergleichbaren realen Fällen mediane Time-to-useful-output oder Human-Rework um mindestens 50 %, ohne vorab benannten Qualitäts- oder Assurance-Gewinn.
7. **Sequential-task kill:** mehr als ein Agent wird wiederholt für stark abhängige/sequenzielle Arbeit eingesetzt.
8. **Assurance kill:** ein Reviewer gibt PASS ohne failure-detecting Method oder übersieht zweimal denselben materiellen Fehler wie der Producer.
9. **Outcome kill:** zwei formal PASSende Episoden scheitern anschließend an Recipient Use, realer Entscheidung oder Work-Product-Qualität.
10. **Control-growth kill:** zwei aufeinanderfolgende Reparaturen vergrößern die erforderliche Kontrollquelle um insgesamt über 20 %, ohne nachweisbare Reduktion von Fehlern, Latenz oder Human correction.

## Klassifikation der Findings

| BehandlungFindings                 |                                                                                                                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Architecture change jetzt**      | Keine                                                                                                                                                                                                                                |
| **Source repair vor Installation** | Formation activation/re-entry; Method anti-monolith; native-duplication exclusion; Subagent eligibility; permission/context minimization; echte Assurance-Unabhängigkeit; cumulative Human-capability handoff; complexity retirement |
| **Runtime observation only**       | tatsächliche Skill-Aktivierung; Formation-Termination; Context-Verluste; stale reconciliation; Agent economics; Human correction/ownership; recipient/use outcomes                                                                   |
| **Architecture-reopen Trigger**    | Formation bleibt faktischer Controller; Method Layer lässt sich nicht von Control trennen; Native Primary verliert Final Ownership; kumulative Capability/Outcome-Verantwortung bleibt dauerhaft unowned                             |

## Control Return

Die externe Architecture Challenge ist abgeschlossen. Route B ist **konzeptionell nicht falsifiziert**, aber nur unter den genannten Source- und Runtime-Bedingungen fortsetzbar. Requirements v0.2 und Target Architecture v0.2 bleiben unverändert; Candidate v0.3 bleibt uninstalled und unpromoted.

**Nächster legitimer Frontier:** ausschließlich die benannten Source Safeguards gegen den bestehenden v0.3-Text prüfen und gegebenenfalls minimal reparieren; danach separate Source Acceptance und erst anschließend eine Installation-/Runtime-Entscheidung.

**Disposition:** **`PROCEED WITH BOUNDED CONDITIONS`** **— Source repair/assurance next; Installation and Promotion remain blocked.**

[material-work-entry v0.8-candidate]