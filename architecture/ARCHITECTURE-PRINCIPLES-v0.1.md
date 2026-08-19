# Architecture Principles v0.1

**Status:** PROVISIONAL / LINEAGE-DERIVED / PRE-ARCHITECTURE  
**Purpose:** Constrain reconstruction and future architecture decisions so the system scales from one Human + AI to larger organizations without rediscovery, category mixing or unnecessary machinery.  
**Basis:** qualified prior designs in `AI-native-Operating-Model`, `human-ai-work-architecture`, `Human-AI-Work-System`, `PAOS`, plus the lineage and correspondence audits in this repository.

These are **architecture principles**, not a user workflow, runtime prompt, checklist or claim that every mechanism must be visible in every task.

A principle should be retained only while it prevents a recurring category error or materially improves architectural decisions.

---

## AP1 — Optimize the Human–AI work system, not an isolated AI component

For claims about professional work, evaluate the coupled configuration of Human judgment, AI, tools, state, methods, interfaces, authority and receiving context.

A model, agent, prompt, workflow or tool can improve locally while total work-system performance worsens.

**Prevents:** component optimization masquerading as work-system improvement.

---

## AP2 — Model responsibilities and roles before assigning actors

Define what must be owned, decided, produced, checked, accepted, maintained or changed before deciding whether the actor is a Human, AI, tool, workflow, team or external specialist.

Use the distinction:

```text
Responsibility / Role Contract
    = purpose + obligations + required capability + decision/action rights + accountability/interfaces

Actor Binding
    = Human | AI | Human+AI | Tool | Workflow | Team | External Actor
```

A single Human may occupy many roles. One role may later be split across several Humans or AI/tool capabilities without changing the underlying responsibility semantics.

**Prevents:** org-chart-shaped architecture and redesign whenever team size changes.

---

## AP3 — Keep core semantics scale-invariant; activate structures only when scale creates a mechanism

The architecture should scale from:

```text
one Human + one AI
→ one Human + many AI/tool capabilities
→ small Human–AI team
→ organization / enterprise
```

without changing basic semantics for purpose, role, capability, state, authority, quality, economics and learning.

Additional structures earn activation only when scale creates a material new mechanism such as coordination dependency, delegation, competing resource allocation, segregation of duties, organizational memory, cross-team interfaces or institutional governance.

**Prevents:** enterprise ceremony in personal work and personal-work assumptions in organizations.

---

## AP4 — Separate persistent operating architecture from episodic work architecture

A persistent Human–AI setup needs an operating model only for things that must remain coherent across work episodes: capabilities, roles, authoritative state, reusable patterns, permissions, platforms, economics, controls and lifecycle ownership.

A concrete Work Episode composes those resources against current reality and may create/adapt Work Units and Work Products.

```text
persistent operating responsibility
≠ current Work Episode
≠ one execution operation
```

Repeated use alone does not automatically institutionalize a work pattern. Promotion to persistent Operating state requires explicit ownership and lifecycle value.

**Prevents:** turning every task into governance and silently creating competing persistent process truths.

---

## AP5 — Treat economics and scarce resources as architecture inputs

Architecture should optimize expected net work-system value, not maximum automation or formal completeness.

Where material include:

- Human attention and energy;
- elapsed time and coordination latency;
- compute/tool/subscription cost;
- verification and rework;
- maintenance and configuration burden;
- opportunity cost and WIP;
- switching/lock-in cost;
- failure/downside and recovery cost;
- learning and capability effects;
- realized outcome/value.

Economic discipline applies at personal scale as much as enterprise scale; only the accounting mechanism changes.

**Prevents:** architectures that are logically complete but uneconomic to operate.

---

## AP6 — Keep architecture dimensions type-correct

Do not force different architecture objects into one hierarchy.

Keep distinct:

```text
responsibility layer
≠ architecture view
≠ cross-cutting control concern
≠ work-control policy
≠ capability/method
≠ runtime realization/profile
```

The same underlying semantics may appear in several views or runtime projections without becoming several responsibilities.

**Prevents:** rediscovery-by-renaming and false “missing layer” diagnoses.

---

## AP7 — Capability, access, authority, accountability and acceptance remain separate

Actor binding does not transfer authority automatically.

```text
Role assigned
≠ capability exists
≠ access available
≠ action authorized
≠ decision right held
≠ result accepted
≠ outcome/value established
```

AI may perform operational work inside a bounded authority envelope without becoming the legitimate owner of Human values, commitments, risk acceptance or institutional decision rights.

**Prevents:** excessive agency and Human-in-the-loop theater.

---

## AP8 — Make persistent ownership explicit only where divergence has consequences

State, knowledge, capabilities, processes and decisions require canonical ownership when multiple versions can diverge and the divergence can affect future work.

Where persistence is not valuable, do not manufacture registries, ledgers or durable artifacts.

For persistent objects distinguish:

```text
working representation
authoritative state
reusable Knowledge Capital
accepted operating pattern/capability
runtime configuration
```

with owner, write/change authority, validity/freshness, dependent uses and retirement/supersession where material.

**Prevents:** both memory-as-truth and persistence bureaucracy.

---

## AP9 — Proportionality is architectural, not merely conversational style

Simple work must collapse to simple execution. Additional decomposition, state, roles, methods, research, assurance, coordination or artifacts are justified only when they can change expected quality, risk, authority, outcome or net value.

The architecture must therefore support **latent complexity**: rich semantics remain available without becoming visible ceremony or mandatory runtime context.

**Prevents:** process inflation and architecture that performs well only on complex test cases.

---

## AP10 — Design for actor substitution, extensibility and portability

Responsibilities and interfaces should remain stable enough that actor bindings can change as capabilities evolve:

```text
Human performs function today
→ AI assists tomorrow
→ validated workflow performs most of it later
→ Human retains only material judgment/authority
```

Substitution requires re-evaluation of capability, failure modes, authority, economics and Human capability effects; it is not automatic.

Important state, methods and decisions should not become unnecessarily inseparable from one model, vendor, person or product surface.

**Prevents:** architecture rewrite on every model/tool/team change and avoidable platform lock-in.

---

## AP11 — Preserve material semantics through compression and realization

Architecture need not be copied into runtime. But every material function must remain either:

- explicit in the realization;
- reliably activated from a named owner/source;
- demonstrably supplied by another validated mechanism; or
- deliberately deprecated through an authorized decision.

Compression is successful only if behavioral/control semantics survive.

**Prevents:** salience loss and architecture-to-runtime semantic regression.

---

## AP12 — Treat accepted prior architecture as closed-but-reopenable Knowledge Capital

Do not re-derive a qualified prior merely because a new repository, vocabulary or viewpoint is being built.

Reopen only for a named trigger:

- changed System of Interest or claim;
- new external evidence;
- new real-use failure;
- materially stronger/simpler rival;
- conflict among qualified priors;
- implementation impossibility or material platform change;
- evidence that the prior was not actually qualified.

Otherwise:

```text
recover → map → provisionally retain / relocate
```

not:

```text
forget → rederive → rename
```

**Prevents:** circular architecture development and loss of accumulated Knowledge Capital.

---

# Architecture-principle use rule

These principles constrain architecture **decisions**, not every work episode.

For a proposed architectural construct ask:

1. Which responsibility/mechanism does it uniquely add?
2. Which principle would be violated without it?
3. Can the same semantics be represented through an existing layer/view/control/capability?
4. At what scale does it become necessary?
5. What operating/economic cost does it introduce?
6. Which qualified prior already addresses the concern?
7. What evidence would justify promotion, and what would falsify it?

If no material answer exists, do not add the construct.
