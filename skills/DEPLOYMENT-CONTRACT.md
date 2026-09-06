# Skill Source and Deployment Contract

## Active source

`main/skills/` is authoritative after promotion; `skills/` on a Candidate branch is proposed source only. This Candidate portfolio contains:

- `work-formation`
- `adaptive-exploration`
- `decision-analysis`
- `evaluate-work-product`
- `system-development`

`research-evidence` remains demoted and absent from active discovery. The archived versions of all three packages remain historical evidence under `legacy/archive-2026-09-02/skills/`; they do not override revised Candidate/current source. Restoring repository discovery does not reinstall a Personal Skill.

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

