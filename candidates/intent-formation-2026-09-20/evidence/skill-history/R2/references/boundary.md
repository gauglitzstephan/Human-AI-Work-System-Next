# Intent boundary

Classify by semantic function, not file name. Intent conveys why/for whom/what change and meaningful boundaries. Specification determines what the solution must do and how its behavior is accepted; planning determines work and resources. An `intent.md` containing detailed requirements is still specification leakage.

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
