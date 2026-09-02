# Current State Recovery — 2026-09-02

**Status:** RECOVERED WORKING STATE / REBASELINE BRANCH ONLY  
**Branch:** `rebaseline/native-delta-2026-09-02`  
**Main is NOT asserted as current runtime authority.**

## 1. Active Global Custom Instructions

The currently installed ChatGPT Global Custom Instructions are the Human-supplied and Human-saved 4,997-character conversation-quality CI established on 2026-09-02. They intentionally do **not** contain explicit repository-local Skill routing, QWS/runtime orchestration, lifecycle, closure, execution, provider registry, or `else native` routing logic.

The final active paragraph is:

> Ask only when the Human’s answer could improve framing, judgment, direction, or quality. Before asking for context, workarounds, or AI-resolvable work, use relevant AI-accessible context and capabilities. Otherwise infer reversibly and continue.

The full active CI remains authoritative in the ChatGPT product setting until an exact persistent copy is separately verified; the legacy repository carrier MUST NOT be treated as its replacement.

## 2. Legacy repo carrier status

`main@53939c328cea2f867e4f73aea1772d366299ca61` contains an older compiled Runtime Global carrier with explicit routing including:

`Route open frame→adaptive-exploration; ... bounded choice→decision-analysis; product fitness→evaluate-work-product; system/runtime→system-development; else native.`

This does **not** represent the active 2026-09-02 Global CI and is therefore stale for runtime-baseline purposes.

## 3. Provider/surface repair candidate disposition

Branch `candidate/method-provider-native-surface-handoff-repair-v0.1` was based on the stale `main` carrier and changed its routing line to broaden provider resolution before native fallback.

Disposition:

- **KEEP AS EVIDENCE:** localization of the provider-space narrowing defect; Strategy / Visual Identity / CV provider-fit investigation; Work-handoff capability-boundary findings.
- **REJECT AS CURRENT GLOBAL-CI IMPLEMENTATION:** the candidate recompiles explicit routing/orchestration into a Global carrier that has already been superseded by the active conversation-quality CI.
- **DO NOT INSTALL.**
- **DO NOT PROMOTE** its Global or Project carrier as the current runtime baseline.
- Any topology/project-specific finding must be requalified against the recovered active baseline before reuse.

## 4. Current rebaseline constraint

Do not derive current runtime state from repository `main` merely because it is promoted or historically authoritative. Before any runtime repair, distinguish:

1. current effective ChatGPT product state;
2. currently installed Global CI;
3. installed Skills/plugins/providers actually accessible in the session;
4. repository source/history;
5. candidate changes.

Repository history is evidence unless exact identity with current effective product state has been established.

## 5. Immediate operating boundary

Until rebaseline resolves authority drift:

- no legacy Global/Project carrier is to be installed from `main` or the provider-repair candidate;
- no new routing logic is to be compiled into the active Global CI;
- current Global CI changes require exact-baseline patch/diff/regression/count discipline;
- existing native ChatGPT capabilities and accessible providers are to be used rather than replaced by inferred custom routing;
- new system architecture is not authorized by this recovery record.

## 6. Known open state

The repository and effective ChatGPT runtime have diverged. This is now an explicit recovered fact, not an implicit assumption. The next rebaseline work must start from the effective product/runtime state and use legacy repositories as evidence to recover durable learnings, not as automatic current authority.