# Intent boundary

Classify by semantic function, not file name. Intent conveys why/for whom/what change and meaningful boundaries. Specification determines what the solution must do and how its behavior is accepted; planning determines work and resources. An `intent.md` containing detailed requirements is still specification leakage.

Discovery, exploration, reference knowledge and economics can contribute at several points in the work chain. Allocate the question by the decision it informs, not by labeling all research “upstream” or all uncertainty “downstream”. Formation qualifies the meaning of the selected work; it does not finish every investigation, prove a solution works or authorize the next stage.

| A question could change… | Treatment at the intent boundary |
|---|---|
| Who benefits, what problem is addressed, what improvement means, a necessary trade-off or an actual boundary | Resolve enough to establish the intended work; otherwise keep a specific framing blocker. A vague shared denominator is not a resolution. |
| What the intended research/analysis will discover or which option a later decision will select | May remain open when the investigation's purpose, decision owner and relevant criteria are grounded. Do not perform the investigation merely to qualify its intent. |
| How a solution behaves, which means work best, detailed requirements or design | Leave to solution exploration/specification unless plausible answers already defeat the purpose or a binding constraint. Preserve the consequential unknown and reopen condition. |
| How work is sequenced, staffed or implemented | Leave to planning; retain only genuinely fixed resource/timing limits that shape intent. |
| Whether the eventual intervention actually produces the desired benefit | Preserve the meaning of success and the material unproven causal assumption. Detailed tests/measurement and realized effectiveness belong to later evaluation. |

For small work, express the relevant distinction in one sentence rather than printing this table. Scope-controlling terms need an ordinary-language meaning when interpretations would change the intended work; they do not need a full taxonomy, data model or rules engine. Conversely, leaving a term unexplained is not solution openness when a later reader must decide what the user meant.

| Content | Intent treatment |
|---|---|
| “I want open commitments to reliably return to my attention” | Outcome. |
| “Support three inboxes, API endpoint X, daily cron job” | Design/requirements; do not derive or add. If present in raw input, separate proposed means from need. |
| “The owner has already committed to the existing platform” | Record as an inherited human constraint with provenance; no architecture design. Challenge only if it materially defeats the purpose. |
| “Usable during a brief interruption” | Experiential outcome/constraint. A protocol latency budget with percentile and test setup is downstream unless it is a genuine externally set boundary; preserve that boundary without elaborating a test suite. |
| “Fewer missed obligations without more organizing burden” | Outcome and guardrail. Button behavior and feature acceptance criteria are downstream. |
| “We do not know whether delays arise before or after approval” | Material question, reason it matters and evidence sufficiency belong in formation. An implementation/research project plan with tasks, owners and dates does not. |
| “Existing checklist may already meet the need” | Reuse hypothesis/selection evidence. Do not turn it into a tool purchase or rollout plan. |
| “Need a decision basis on location A vs B” | Legitimate nonsoftware intent; alternatives are the subject of later analysis, not a requirement to decide them now. |
| “Offer expires Friday; after then reconsider the opportunity” | Temporal validity; no automatic scheduled action. |

When downstream detail is supplied, retain the original as source and mark only materially relevant inherited decisions in intent. Do not delete user commitments or turn them into new AI choices. If the user asks for implementation during formation, explain the current stopping point and finish the authorized intent; a changed or separately authorized scope must be handled as a distinct assignment, not a hidden continuation.

An intent may be **qualified but unaccepted**, or **accepted but now stale**. Downstream needs the current revision, grounding, open issues, human decisions and validity conditions. It does not inherit permission to execute from the file’s existence or status.
