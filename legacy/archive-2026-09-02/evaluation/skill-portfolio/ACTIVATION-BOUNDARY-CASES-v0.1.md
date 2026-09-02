# Six-Skill Portfolio — Activation and Boundary Cases v0.1

**Purpose:** static description-level routing carrier.  
**Claim limit:** expected ownership from source semantics; not evidence of implicit runtime activation.

## Direct positive cases

| ID | Request | Expected owner |
|---|---|---|
| P-01 | “Welche wirklich unterschiedlichen Geschäftsmodelle wären mit meinem Profil denkbar? Noch nicht bewerten.” | `adaptive-exploration` |
| P-02 | “Zeig mir kontrastierende visuelle Richtungen, damit ich merke, was zu uns passt.” | `adaptive-exploration`, or narrower design ideation if it fully owns the task |
| P-03 | “Bevor du schreibst: Für wen und wofür soll dieses Dokument eigentlich funktionieren?” | `work-formation` when the missing intended use changes the next route |
| P-04 | “Wir wollen das bestehende System reparieren, kennen aber den aktuellen verbindlichen Stand nicht.” | `work-formation` for the missing basis, then the responsible method |
| P-05 | “Welche aktuellen offiziellen Regeln gelten dafür und wie sicher ist die Quellenlage?” | `research-evidence`, or the narrower domain research method |
| P-06 | “Diese zwei Primärquellen widersprechen sich. Welche Aussage ist tragfähig?” | `research-evidence` |
| P-07 | “Ich habe drei konkrete Jobangebote. Welches passt unter Familie, Gehalt, Autonomie und Downside am besten?” | `decision-analysis` |
| P-08 | “Soll ich jetzt fest zusagen, warten oder erst einen reversiblen Test machen?” | `decision-analysis` |
| P-09 | “Kann ich diese konkrete Bewerbung in diesem Stand versenden?” | `evaluate-work-product` |
| P-10 | “Ist dieser Bericht für den Vorstand belastbar und übergabefähig?” | `evaluate-work-product` |
| P-11 | “Warum hat unser Human–AI Work System den Parent-State verloren?” | `system-development` |
| P-12 | “Promoviere den validierten Skill-Candidate sauber ins Repo und lies `main` zurück.” | `system-development` |

## Collision and composition cases

| ID | Request | Expected routing |
|---|---|---|
| C-01 | “Brainstorme Geschäftsmodelle und entscheide anschließend das beste.” | close `adaptive-exploration`, then use `decision-analysis` only after the decision is bounded |
| C-02 | “Welche Gegenhypothesen gibt es, und welche davon wird durch aktuelle Daten gestützt?” | exploration first; material evidence acquisition separately through `research-evidence` |
| C-03 | “Vergleiche zwei CV-Versionen für dieselbe konkrete Stelle.” | `evaluate-work-product`; not `decision-analysis` unless wider option consequences drive the choice |
| C-04 | “Bewerte den Bericht und überarbeite ihn direkt.” | evaluate the original product first; revision is Native production and creates a new product state |
| C-05 | “Soll ich mich bewerben?” while role, intended outcome, and decision level are unclear | `work-formation`; do not force premature decision analysis |
| C-06 | “Ist der installierte Skill wirklich wirksam?” | `system-development`; source evaluation alone cannot establish runtime fitness |

## Negative and native cases

| ID | Request | Expected owner |
|---|---|---|
| N-01 | “Übersetze diesen kurzen Absatz ins Englische.” | Native ChatGPT |
| N-02 | “Setze die ausgewählte Landingpage jetzt um.” | Native production or narrower implementation method |
| N-03 | “Nenne mir drei spielerische Namen für die interne Session.” | Native ChatGPT unless material exploration quality is genuinely required |
| N-04 | “Welche der beiden unkritischen Uhrzeiten ist praktischer?” | Native ChatGPT; no material decision method needed |
| N-05 | “Weiter.” after a proposal that would require a new external write | no Skill creates authorization; bind the actual authorized transition first |
| N-06 | “Teste jeden Skill synthetisch, nur damit alle einmal gelaufen sind.” | no default test program; use genuine work unless a concrete failure requires isolation |

## Acceptance criteria

The portfolio passes this static carrier when:

1. every direct positive case has one primary owner;
2. mixed cases preserve sequential ownership without a universal controller;
3. ordinary native work does not attract a Skill merely because one exists;
4. no Skill creates Human acceptance, authorization, execution, or outcome;
5. same-use product comparison remains distinct from wider option choice;
6. open exploration remains distinct from missing-basis formation; and
7. static routing expectations are not promoted as runtime activation evidence.
