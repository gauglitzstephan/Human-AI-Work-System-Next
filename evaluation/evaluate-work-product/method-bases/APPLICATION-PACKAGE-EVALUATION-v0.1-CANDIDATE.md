# Application Package Evaluation Method — Candidate v0.1

**Status:** bounded task-local professional evaluation basis; Candidate only  
**Date:** 2026-08-26  
**Scope:** evaluation of a concrete application package for a concrete role and a sufficiently reconstructable selection context

This method is not a career decision method, a document-creation or repair method, an interview-outcome predictor, a submission method, or a universal recruiting standard.

## Evidence basis and limits

This Candidate combines a bounded cross-domain evaluation structure with the following professional and technical references:

- The [Bundesagentur für Arbeit guidance on CVs](https://web.arbeitsagentur.de/bildung/bewerbung/lebenslauf) supports clear structure, readable typography, restrained design, role tailoring, and a concise document, commonly up to two pages. It supplies a general application-quality floor, not a senior, leadership, or executive-search ceiling.
- [Europass CV guidance](https://europass.europa.eu/de/create-europass-cv) supports relevance, tailoring, clarity, and readability.
- The [CIPD Selection methods factsheet](https://www.cipd.org/uk/knowledge/factsheets/selection-factsheet/) distinguishes shortlisting from later assessment and supports role-related, structured, and objective selection. It is employer-side and UK-contextual; transfer to a German candidate-side evaluation is limited.
- [ISO 24495-1](https://www.iso.org/es/contents/data/standard/07/89/78907.html) supplies general reader-oriented plain-language principles. It is not a complete visual-design or accessibility standard for application documents.
- [WCAG contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum) and the [W3C PDF reading-order technique](https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3) supply technical accessibility floors. They do not establish professional CV design quality by themselves.
- The [Bundesagentur für Arbeit application-template guidance](https://www.arbeitsagentur.de/vor-ort/ahlen-muenster/bewerbungsvorlagen) supports considering machine readability. Any ATS assessment here remains a proxy and does not guarantee processing by a specific employer system.

This basis is sufficient with limits for the bounded EWP-03 forward test. It is not established as a universal method, an installable Skill, an executive-search or legal evaluation method, or a guarantee of ATS performance.

## 1. Bind the evaluation object and claims

Bind only what is needed to distinguish the evaluated state:

- the exact current job advertisement and material employer context;
- the exact CV, cover letter and other package components actually present;
- the application route or portal and its known required fields;
- the current package state, including version or location where needed;
- the intended use, normally responsible reliance for a concrete send-readiness judgment; and
- each materially distinct evaluation claim.

At minimum, keep content and role fit, claim integrity, professional document design, technical transfer, package completeness and coherence, and overall fit distinct whenever they may produce different conclusions.

Do not convert an absent document, unknown portal field, or unconfirmed human preference into a global negative judgment when the affected claim can be separated.

## 2. Reconstruct the receiving and selection context

Identify only the selection functions materially supported by the concrete role, organization, process, or package. Do not assume that every possible actor participates.

| Possible selection function | Evaluation interest |
|---|---|
| Portal or automation | Extractability, file format, required fields and consistent data |
| Recruiting or Talent Acquisition | Basic fit, career coherence, seniority plausibility and salient risks |
| Direct hiring manager | Relevant capability, evidence, problem understanding and likely contribution |
| Strategic or skip-level leader | Leadership, transformation, organizational impact and positioning |
| HR or administration | Availability, compensation information and formal completeness |

Derive the plausible reading order, attention limits, questions and rejection risks of the relevant functions. Mark uncertain participation as an assumption rather than presenting a generic stakeholder inventory as fact.

## 3. Derive role-relative criteria

Translate the job and receiving context into a bounded criterion set:

- must-have and differentiating capabilities;
- responsibilities and expected contribution;
- the role's balance of subject expertise, leadership, transformation and organizational influence;
- credible seniority and positioning;
- material selection risks or transfer gaps;
- requested information and application components; and
- qualities required for responsible reliance at the intended send stage.

Do not reward keyword overlap without demonstrated relevance, evidence or contribution.

## 4. Select the required evaluation operations

### A. Role and value fit

Assess whether the package makes the relevant capability, motivation, transfer logic and likely contribution legible for the bound role. Distinguish qualification fit from evidence of future performance.

### B. Claim integrity

Check material claims against available career evidence and package-internal consistency. Identify unsupported inflation, misleading titles, responsibility drift, false precision, unexplained contradictions and material omissions. Preserve truthful restraint where it protects credibility.

### C. Reader pathway and information architecture

Evaluate whether relevant readers can find and interpret the most decision-relevant information in a plausible scan sequence. Check hierarchy, ordering, labels, density, repetition, evidence placement and the relationship between summary, experience and skills.

### D. Professional document design

Inspect the actually rendered document with a suitable visual method. Evaluate:

- visual hierarchy and salience;
- typography and readability;
- density, spacing, alignment and whitespace;
- page balance and page breaks;
- consistency across sections and package components;
- individuality and restraint appropriate to the target context; and
- overall professional effect for the relevant receiving functions.

Mechanical PDF validity, successful rendering or clean text extraction does not establish professional design quality. If the rendered document cannot be inspected adequately, return `INSUFFICIENT_BASIS` for the visual-design claim.

### E. Technical usability

Use suitable deterministic or specialist checks for rendering, text extraction, reading order, links, fonts and special characters, file naming, file size and relevant ATS proxies. State the tested properties and system limits. Do not convert proxy success into a universal ATS-compatibility claim.

### F. Package coherence and completeness

Assess whether CV, cover letter and other present components complement rather than contradict or merely repeat each other. Check whether motivation, transfer logic, dates, titles, claims and required information are coherent.

Keep these questions separate:

- Is each existing component professionally fit?
- Is an optional component strategically useful?
- Are mandatory package or portal elements missing?
- Is the portal state complete enough to submit?

### G. Personal representation and human acceptance

The evaluator may assess whether voice, tone, emphasis and seniority positioning are coherent with qualified personal evidence or exemplars. The human retains authority over whether the package authentically represents them, whether a positioning trade-off is acceptable, whether to apply, and whether to send.

An open human acceptance state must not substitute for professional evaluation. Conversely, a positive professional evaluation does not authorize application or submission.

## 5. Challenge material failure modes

Test at least the failure modes material to the bound package, such as:

- professionally polished but generic;
- credible but materially underselling the candidate;
- leadership-heavy positioning for a primarily individual-contributor role;
- apparent fit without a legible contribution;
- clean layout with a weak scan path;
- strong visual design with fragile technical transfer;
- ATS-oriented wording that is weak for human readers;
- incoherence between documents or portal data;
- human approval being used in place of evaluation; and
- portal completeness being used in place of application quality.

## 6. Reach separated dispositions

Apply the `evaluate-work-product` dispositions separately where material:

- role and value fit;
- claim integrity;
- professional document design;
- technical usability;
- package completeness and coherence; and
- overall fit for the bound use.

Use only:

- `FIT_FOR_STATED_USE`
- `FIT_FOR_STATED_USE_WITH_LIMITS`
- `NOT_FIT_FOR_STATED_USE`
- `INSUFFICIENT_BASIS`

Report authority states separately:

```text
HUMAN ACCEPTANCE: OPEN | GIVEN | DECLINED
APPLY DECISION: NOT OWNED
SUBMISSION: NOT AUTHORIZED | NOT PERFORMED
```

An overall disposition must not hide a materially different property disposition.

## 7. Method and provider separation

- `evaluate-work-product` owns the bounded fit-for-use synthesis.
- This Application Package Evaluation Method Candidate supplies the task-local professional evaluation basis.
- `research-evidence` or another qualified research method supplies current job, employer and selection-process evidence when needed.
- document and PDF methods supply rendering, visual inspection and technical checks.
- Google Drive or the responsible file system supplies the actual current package state.
- Native ChatGPT owns work-episode integration and the final response.
- The human owns authentic representation, application choice and submission authority.

No provider may silently expand this method into document creation, repair, career choice or submission.

## 8. Stop rule

Stop when the material failure modes have been examined sufficiently for each bound claim, enough evidence exists for its disposition, or missing evidence or method requires `INSUFFICIENT_BASIS`.

Do not continue into writing, repair, application choice, submission, repository promotion, Skill creation or installation without a separate task and the responsible owner.

## Authority boundary

This Candidate authorizes no document change, application decision, portal action, submission, Skill installation, repository merge or promotion. It is a bounded Candidate method basis for explicit use in the EWP-03 forward test only.

## Qualification

```text
Method Candidate formation: COMPLETE
Evidence basis: SUFFICIENT WITH LIMITS
Fit for bounded EWP-03 forward-test use: YES
Fit as universal application-evaluation standard: NO
Fit as installable Skill: NOT ESTABLISHED
Executive-search / legal / guaranteed ATS claims: OUT OF SCOPE
Repository status: CANDIDATE ONLY
Forward test: NOT STARTED
```
