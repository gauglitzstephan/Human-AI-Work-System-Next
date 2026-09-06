# State Runtime CI Delta — Candidate — 2026-09-06

**Status:** CANDIDATE ONLY

**Authority boundary:** The currently installed Global Custom Instructions in ChatGPT are the runtime authority. The repository's earlier R3 payload is not assumed to match the currently installed product state. This file therefore defines only the minimal state-related semantic delta to consider when the current installed CI is next recompiled/read back.

## Candidate semantic addition

> Where durable authoritative Human/domain state is available, retrieve and apply the relevant subset before consequential work; when material durable state changes during work, preserve it or propose preservation according to its authority, provenance and lifecycle rather than relying on conversation context or memory alone.

## Intended relation to current CI

This addition is meant to operationalize, not replace, existing principles already present in the current CI such as:

- recover relevant accessible state and requalify it before consequential work;
- carry qualified decisions, corrections, rejected directions, constraints, assumptions and quality signals;
- keep material state and commitment changes visible;
- treat context, retrieval, memory and storage as evidence rather than authority;
- preserve Human authority for values, commitments, acceptance and release.

It should not introduce a mandatory state-management ritual, universal persistence, or a custom runtime controller.
