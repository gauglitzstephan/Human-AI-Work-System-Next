# State and intent semantic contract

## Separate responsibilities

`formation.md` supports continued reasoning. `intent.md` supports review, ownership and later work. A conversation transcript is neither. In simple work the chat can carry transient formation; for handoff or interruption save the compact state, and actually read it on return.

### Formation state: minimum useful content

Use readable headings or bullets, not a mandatory database:

- Identity and current intent revision/path; current disposition and why.
- Current problem/outcome understanding, source of material claims and live rival explanation if any.
- Known evidence and accessible source locations; essential limitations/freshness.
- Material assumptions, unknown facts, undecided human choices; which block current framing and why. For a material later question, preserve why it can wait and what finding would reopen the intent.
- Last important correction and affected claims, including any now-superseded conclusion.
- Next useful inquiry and the expected difference its answer would make; attention/revisit condition when relevant.

Keep stable settled content in intent; reference it rather than copy it all. Remove stale pending questions after answers. Keep a short tombstone only for a correction likely to recur. Never compress away the reason an unresolved issue is material. On handoff distinguish source limitations from absence of evidence. Incoming agents must not infer acceptance from an existing file.

### Intent: one meaning, multiple surfaces

Required semantic coverage, expressed compactly in natural language:

1. **Identity/status:** meaningful title, everyday readiness with a concrete reason, owner if known, and acceptance (not recorded unless explicit). Keep local identifier, revision and technical readiness secondary to the purpose, e.g. in a short footer. No YAML is required. In German call acceptance “Akzeptanz dieser Fassung”, distinct from an epistemic “Annahme”.
2. **Purpose and intended change:** problem/opportunity, desired outcome, why it matters; enough current context and affected roles to interpret it.
3. **Boundaries:** material in/out, actual constraints and fixed human choices. Distinguish a constraint from a candidate means or a preference.
4. **Grounding and openness:** evidence, material AI inference/assumption, nonblocking or blocking unknowns, unresolved human judgments. Preserve enough of a scenario to understand the intended work; indicate the source of material clarifications so they can be found without reconstructing the chat. An episode is not proof of general prevalence or causation. State why a consequential unknown can remain for later work. Mark absent material evidence; omit irrelevant empty sections.
5. **Recognizing success:** observable outcome meaning, including material adverse effects/guardrails; no feature-level acceptance contract.

Conditional coverage: economics of the outcome; affected-party conflict; temporal validity/reopen triggers; selected framing rationale; taste decisions; source detail. If there is no material unknown, say so briefly rather than invent one. A source register is optional, not per-sentence tagging.

Use [intent-short.md](../assets/intent-short.md) for a small, clear case and [intent-expanded.md](../assets/intent-expanded.md) when distinctions need separate scan targets. Compose or rename headings to fit the work while preserving semantics. Remove instructional placeholders. Do not print empty optional sections. Put each material claim in one natural place; later sections add distinct information instead of repeating it. The closing reason should explain actual readiness, not assert “no question could change anything”.

## Claim authority and change

Use local labels where material: “Owner berichtet”, “Quelle”, “AI-Deutung”, “Annahme”, “Unbekannt”, “Entscheidung”. A human statement is evidence of what that person said, not automatically an external fact. A source-backed factual statement is not a human preference. “Unknown” is missing knowledge; “undecided” is an unresolved choice. A constraint requires a source/authority when disputed or consequential.

Record explicit acceptance as who, which revision and the actual acceptance statement or precise reference. Do not ask for redundant confirmation when the user has unambiguously accepted that revision. A material change creates a new revision and invalidates current acceptance; preserve the earlier acceptance as historical. Pure spelling/format changes do not alter meaning but should retain traceable revision handling.

## Reader tasks before saving

Can a fresh reader find the purpose/outcome, current status, boundaries, human decisions, open issues and their consequences without the chat? Can the owner identify and change a material AI interpretation without rewriting everything? Is the reason for a qualified/blocked/deferred/dropped status apparent? If not, repair information placement or meaning.

Check that both files agree after material edits and that the actual saved version matches the stated revision. No helper can prove semantic qualification or human acceptance. Do not treat word count, headings or a schema pass as quality evidence.
