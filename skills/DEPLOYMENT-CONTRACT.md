# Skill Source and Deployment Contract

## Active source

`main/skills/` is the authoritative repository source only for the active custom portfolio:

- `decision-analysis`
- `evaluate-work-product`
- `system-development`

The demoted packages are historical source under `legacy/archive-2026-09-02/skills/`; they are not active plugin or repository-discovery providers.

## Discovery and packaging

- `.codex-plugin/plugin.json` packages the active `skills/` directory.
- `.agents/skills/*` contains symbolic links only for the active packages.
- standalone Personal Skills are separately installed deployment copies.

No discovery view or installed copy becomes an independent semantic source. Do not hand-edit a deployment copy and treat it as accepted repository source.

## State distinctions

```text
repository source
≠ plugin package
≠ installed copy
≠ activation
≠ correct method execution
≠ professionally fit result
≠ outcome
```

A repository merge does not update or uninstall a Personal Skill automatically.

For deployment judgments bind the repository candidate, approved operating target, actual installed/loaded copy and adoption status separately. A newer repository source is not by itself an obligation to install it. If the approved target is unknown, preserve that uncertainty while continuing independently authorized candidate work. A false claim about the version used is correctable even when the operating target is unresolved.

The [2026-09-18 repair receipt](../inventory/system-development-repair-2026-09-18/REPAIR-RECEIPT.md) records the observed historical installation, candidate provenance, bounded verification and proposed adoption path. Package 0.2.3 does not assert an installed update.

## Change flow

1. establish a demonstrated semantic, discovery, execution or maintenance need;
2. compare native/specialist ownership, reuse, repair, archive and no-action;
3. change the canonical package on a dedicated branch;
4. validate the exact candidate and preserve unaffected semantics;
5. obtain Human acceptance and separate merge authorization;
6. merge and read back authoritative repository state;
7. only with separate authorization, install/update/uninstall the external copy and read it back;
8. learn from genuine use within the bounded claim.

Increment plugin version when the installable active package materially changes. Never create a new Skill merely because a requirement or failure exists.
