# Chat ↔ Work Cooperation — 2026-09-02

**Status:** CURRENT PRODUCT-REALITY NOTE / REBASELINE EVIDENCE

## Finding

Chat and Work are distinct ChatGPT experiences with complementary roles.

OpenAI currently describes:

- **Chat** for fast conversational assistance, questions, search, brainstorming and everyday help.
- **Work** as an agent for longer, multi-step work and finished deliverables such as research, analysis, documents, spreadsheets, presentations, reports and Sites.
- Chat and Work conversations appear together in Recents on desktop.
- Cloud Work conversations sync across supported web, mobile and desktop surfaces.
- From a ChatGPT Project, a user can explicitly start either a Chat thread or a Work thread using that Project's context.
- Installed Skills may be automatically used when helpful, but availability and syncing can differ by product and surface.

## Important negative finding

Current official product documentation does **not** establish a guaranteed automatic conversion or handoff of an arbitrary existing Chat thread into Work when a task becomes substantial.

A prior UI suggestion or pop-up may occur in product behavior, but absence of such a prompt in one conversation is not evidence that Work is unavailable and should not be replaced by a custom surface router.

## Rebaseline implication

The rebaseline must preserve **surface cooperation** without recreating **surface orchestration**.

The useful distinction is:

- use **Chat** as the conversational thinking space for exploration, discrimination, framing, research dialogue, judgment, feedback and lightweight actions;
- use **Work** when the actual work benefits materially from an agentic multi-step production environment, finished/reviewable deliverables, persistent artifact work or Work-only Skills/capabilities;
- use a **Project** when related chats, Work threads, files and instructions need a shared durable context across an ongoing effort.

This is a product-role model, not a mandatory lifecycle. A task may begin directly in Work, remain entirely in Chat, or move between separate Chat/Work threads as useful.

## Handoff principle

When conversation has formed enough context for substantial production and Work would materially improve execution, the useful operation is a **context-complete Work handoff**, not continued artifact simulation in Chat and not a custom global router.

A handoff should preserve only what the Work task materially needs: intended outcome, current decisions, qualified evidence/context, constraints, open uncertainties, relevant source locations, quality/recipient criteria and any explicit non-goals. It should not dump the entire chat transcript merely for completeness.

Where Project context already contains the necessary durable basis, prefer starting the Work thread from that Project rather than manually duplicating context.

## Known user/product state

For this account's current working setup:

- six repo-derived Personal Skills are installed and discoverable on the **Work** surface;
- ordinary Chat does not expose them in the same way;
- absence from ordinary Chat is therefore not evidence of non-installation;
- the System-Development Project exists separately and its Project instructions apply only when work is run inside that Project;
- the present rebaseline conversation was intentionally conducted outside that Project.

## System boundary

Do **not** add Chat→Work routing rules to Global CI solely to force this behavior.

Treat failures here first as product-surface/handoff evidence:

1. Was Work materially useful for the task?
2. Was the relevant Work/Project surface actually available?
3. Was a context-complete handoff offered or performed when useful?
4. Did Work receive the qualified basis it needed?
5. Did Work use the appropriate Skills/providers and produce a fit-for-use deliverable?

Only persistent evidence that native product behavior cannot support this cooperation would justify additional custom machinery.