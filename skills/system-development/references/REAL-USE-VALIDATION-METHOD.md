# Professional Work Evaluation Method v0.2

**Status:** scoped internal evaluation method for the current Human–AI Work System.  
**Use when:** genuine work provides evidence about whether the current working setup is helping or harming professional output.

## Purpose

Evaluate the system through real professional work, not through synthetic testing of ordinary ChatGPT product behavior or process-compliance exercises.

The evaluation question is:

> Did the working setup help produce a professionally usable result with appropriate reality contact, method quality, Human burden and proportionality?

## Default: work first

Do not create a test task merely because a Skill, tool, Subagent or surface exists.

Use ordinary genuine work. Record or analyze system evidence only when it materially changes a decision about the working setup.

A controlled/synthetic isolation test is justified only when an observed failure cannot otherwise be localized and the result would change a concrete repair decision.

## Evaluate the work product and work experience

Use only dimensions material to the actual task:

### Intended-use professional quality
Did the result meet the professional/craft standard needed by its real recipient/use? Was an adequate method/reference basis used where validity depended on it?

### Reality and evidence integrity
Were material facts/current state correctly grounded? Were assumptions, uncertainty and conflicting evidence handled honestly?

### Judgment and outcome fidelity
Did the work solve the actual need rather than a proxy/process artifact? Were important alternatives/trade-offs handled at the right level?

### Human burden and agency
Did the Human contribute where judgment, values, authorship, context, acceptance or authority genuinely mattered? Negative signals include the Human having to detect AI-resolvable defects, reconstruct lost state, repeatedly redirect meta-work, or translate an immature object into usable work.

### Proportionality
Did research, process, tools, Skills, Subagents, artifacts and review earn their cost? Was useful work delayed by ceremony?

### State/authority integrity when material
For work involving persistent state or effects, were working/candidate/authoritative states, authorization, execution and readback kept distinct?

### Transition/use when material
If success depends on a recipient or downstream use, distinguish artifact production from readiness, use, performance and outcome.

## Failure handling

When a material failure appears:

1. state the failed professional/work claim and evidence;
2. localize the lowest responsible mechanism using the System Failure Localization method when useful;
3. repair only that layer;
4. preserve unaffected qualified state;
5. continue genuine work and observe whether the failure recurs.

Do not automatically add a rule, Skill, reviewer, artifact or new version.

## Evidence standard

A single successful task can support only that bounded result. A single failure can justify a local repair when its mechanism is clear, but not a general architecture rule by itself.

Human corrections are evidence, not merely feedback. If the Human detects an AI-resolvable material defect, count that as a negative system signal.

## Output

For a material system-learning event, keep the record minimal:

```yaml
real_work_context: required
failed_or_supported_claim: required
professional_quality_evidence: optional
human_burden_or_correction: optional
responsible_mechanism: optional
bounded_change_implication: optional
claim_limit: required
```

Do not create a record for routine successful work unless continuity or a concrete change decision requires it.

## Non-goals

Do not:

- test ordinary ChatGPT capabilities for their own sake;
- score whether Skills activate as a product feature unless an observed work failure depends on activation;
- construct synthetic coverage matrices merely to exercise every component;
- treat process adherence as professional quality;
- average heterogeneous work into a universal quality score;
- infer architecture superiority from one case;
- make the Human the standing evaluator of AI work.

The system earns confidence through sustained useful work, low avoidable Human correction and evidence-bound repair — not through ceremony.