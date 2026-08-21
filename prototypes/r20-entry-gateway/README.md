# R20 Two-Pass Entry Gateway Prototype v0.1

**Status:** PROTOTYPE / CANDIDATE — not deployed, promoted, or authoritative.

## Purpose

Test a different enforcement mechanism class after Global-CI-only Entry/Admission failed behaviorally in R20.

The prototype creates a real execution boundary:

```text
Human trigger
→ Pass 1: forced `route_entry` function call
→ host validation of EntryDecision
→ Pass 2: route-specific local developer contract
→ substantive answer
```

Pass 1 cannot return the substantive answer because the Responses API request forces one named function call. The host validates the decision before Pass 2 is allowed to run.

This prototype does **not** modify ChatGPT Global Custom Instructions, Project Instructions, repository authority, or external operational state.

## Why this is materially different from Global v0.6/v0.7

The failed Global candidates depended on permanent text self-activating before ordinary generative work.

Here, the host enforces the sequence:

1. an EntryDecision must exist;
2. its schema and cross-field invariants must pass;
3. only then is substantive generation possible;
4. the second call receives a route-local contract (`BOUND`, `DIRECT`, or `FORMATION`).

The EntryDecision is ephemeral working runtime state. Persistence and Promotion are not implied.

## API basis

Current OpenAI Responses API documentation supports:

- function tools with strict schemas;
- forcing a specific function via `tool_choice`;
- developer/system roles above user instructions;
- GPT-5.6 via the Responses API with function calling and structured outputs.

Reference pages:

- https://developers.openai.com/api/reference/cli/resources/responses/methods/create
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://help.openai.com/en/articles/8555517/function-calling-in-the-openai-api

## Files

```text
gateway.py                  minimal executable two-pass gateway
entry_decision.schema.json forced dispatch schema
r20_cases.json              R20 mechanism test matrix
run_evals.py                multi-turn dispatch/work eval harness
```

## Run

Requires Python 3.10+ and an API key.

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="gpt-5.6"

python prototypes/r20-entry-gateway/gateway.py \
  --show-dispatch \
  "Ich möchte ein Grafik Novel über die Geschichte des Bieres entwerfen"
```

Interactive multi-turn mode:

```bash
python prototypes/r20-entry-gateway/gateway.py --show-dispatch
```

Offline harness validation:

```bash
python prototypes/r20-entry-gateway/run_evals.py --validate-only
```

Execute the R20 matrix:

```bash
python prototypes/r20-entry-gateway/run_evals.py \
  --model gpt-5.6 \
  --json-out /tmp/r20-entry-gateway-eval.json
```

The harness starts a fresh in-memory gateway for each case and preserves state only within multi-turn cases.

## Required R20 dispatch behavior

```text
beer-history Graphic Novel cold start   NEW_CHANGED / FORMATION
translation                             NEW_CHANGED / DIRECT
explicit ideation                       NEW_CHANGED / DIRECT

product description                     NEW_CHANGED / DIRECT
"shorter" continuation                  BOUND / NOT_APPLICABLE
material brand-positioning change       NEW_CHANGED / FORMATION

shipping note                           NEW_CHANGED / DIRECT
translate shipping note                 NEW_CHANGED / DIRECT
new professional loyalty-program child  NEW_CHANGED / FORMATION
```

Dispatch PASS is necessary but not sufficient for Runtime acceptance. The full answer is retained in the eval record for separate behavioral review, because a correct route classification does not by itself prove professional-quality Formation or DIRECT proportionality.

## Host-side invariants

The host rejects:

- `BOUND` with any admission other than `NOT_APPLICABLE`;
- `BOUND` without an existing parent;
- `NEW_CHANGED` with `NOT_APPLICABLE`;
- `FORMATION` without at least one material upstream trigger;
- missing/extra schema fields.

A rejected EntryDecision prevents Pass 2.

## Non-claims / limitations

- No live API execution has been performed by repository creation alone.
- The schema guarantees structure, not semantic correctness of the model's chosen values.
- The prototype holds parent/frontier summaries and transcript in memory only.
- It does not yet integrate authoritative Project/repository state retrieval.
- It does not implement production authentication, rate limiting, retries, observability, privacy controls, cost controls, or persistence.
- It is not evidence that API behavior matches ChatGPT UI behavior.
- Model alias behavior can change; representative validation should record the actual model returned by the API and pin a suitable model/snapshot where available.
