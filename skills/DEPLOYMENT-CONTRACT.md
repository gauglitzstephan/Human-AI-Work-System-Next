# Skill Source, Discovery, Deployment, and Learning Contract

## Purpose

Keep one authoritative skill source while supporting the actual discovery and installation mechanisms of ChatGPT and Codex.

## Authoritative source

`main/skills/` is the only active source for the six reusable skill packages.

The following are views or deployment copies, not independent sources:

- `.codex-plugin/plugin.json` packages the same `skills/` directory for plugin installation;
- `.agents/skills/*` points to the same package directories for repository-local Codex discovery;
- an installed ChatGPT or Codex copy is a deployment state that must be compared back with `main`.

Do not hand-edit a deployment copy and treat it as accepted source.

## Top-down flow

```text
controlling Requirements / architecture
→ portfolio responsibility and boundary
→ canonical package under skills/
→ native discovery or plugin packaging
→ explicit install/update transition
→ installed-content readback
→ genuine-use evidence
→ bounded runtime claim
```

Repository merge does not update an installed plugin or Personal Skill automatically. Packaging presence does not establish installation, activation, correct execution, or outcome quality.

## Bottom-up learning flow

```text
genuine work observation or failure
→ bind the failed/supported claim and runtime environment
→ localize the lowest responsible mechanism
→ repair the canonical package or packaging layer only if evidence supports it
→ validate candidate
→ promote to main through the authorized repository path
→ reinstall/update the deployment copy
→ read back installed content
→ continue genuine work
```

This is controlled reconciliation, not automatic two-way synchronization. Runtime evidence may propose a source repair; it cannot silently write back, accept, or promote one.

## Discovery contracts

### Skill selection

ChatGPT and Codex discover a Skill primarily from its `name` and `description`. Descriptions therefore front-load the positive trigger and retain only boundaries needed to prevent likely misrouting. Full instructions load only after selection; references load only when the selected Skill requires them.

### Codex repository discovery

Codex discovers repository-scoped Skills under `.agents/skills`. Each entry in this repository is a symbolic link to the corresponding canonical directory under `skills/`; it is not a duplicate package.

### ChatGPT and cross-surface distribution

The repository root is a skills-only plugin package through `.codex-plugin/plugin.json`. The manifest points directly to `./skills/`.

Plugin packaging is the distribution mechanism. A supported installation surface, explicit install/update action, and installed-content readback remain separate requirements.

## Version and change rules

- Change a Skill only for a demonstrated semantic, discovery, execution, or maintenance need.
- Increment plugin version when the installable package materially changes.
- Keep source promotion, installation, activation, method execution, and outcomes as separate registry states.
- Preserve unaffected package semantics and evidence.
- Do not create a new Skill merely because a requirement exists; Native ChatGPT and narrower professional methods remain valid owners.
