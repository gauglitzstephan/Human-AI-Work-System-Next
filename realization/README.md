# Runtime / Realization Navigation

This directory contains current Runtime realization artifacts **and** historical/superseded lineage. File recency, version number or the presence of executable-looking text does not by itself establish current authority.

**Controlling program state:** `../CURRENT.md`.

## Current package

Current repository-promoted Runtime semantics and compiled views after PR #13:

| Role | Current artifact | Status / use |
|---|---|---|
| Canonical Runtime semantics | `E2E-RUNTIME-CANONICAL-SEMANTIC-SOURCE-v0.1.md` | semantic source for current compilation |
| Canonical compilation contract | `E2E-RUNTIME-CANONICAL-COMPILATION-CONTRACT-v0.1.md` | compilation/trace discipline |
| Global compiled view | `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.5.md` | current Global installation view |
| System Development Project view | `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md` | current first-Project view |
| Installation bundle | `E2E-INSTALLATION-BUNDLE-v0.4.md` | current external-transition bundle |
| Handoff / Commitment / Promotion | `E2E-HANDOFF-COMMITMENT-PROMOTION-CONTRACT-v0.1.md` | current boundary/control contract |
| Interaction / Control Return | `E2E-INTERACTION-FRONTIER-COMPILATION-CONTRACT-v0.1.md` | current interaction compiler |
| Capability / Method / Provider map | `E2E-CAPABILITY-METHOD-PROVIDER-MAP-v0.1.md` | current realization mapping |
| Chat / Work surface allocation | `E2E-CHAT-WORK-SURFACE-ALLOCATION-v0.1.md` | current surface guidance |

Method carrier: `../methods/METHOD-REGISTRY-v0.1.md` and referenced packs.

## Current installation identities

Global v0.5:

```text
LF:       4,991
CRLF:     4,997
SHA-256:  865cc07b101a907b42adaa5506537f27db554d9195a70077ae7050d7cf84d72f
```

System Development Project v0.4:

```text
LF:       5,172
CRLF:     5,181
SHA-256:  338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b
```

Do not paraphrase or select an older payload merely because it remains in repository history.

## Superseded / history — do not install

The following remain for provenance, regression comparison and recovery only unless `CURRENT.md` explicitly changes their status.

### Earlier solution-forming Global experiments

- `GLOBAL-CI-SOLUTION-FORMATION-CANDIDATE-v0.1.md` — superseded framing; do not install.
- `GLOBAL-CI-SOLUTION-FORMING-ACTIVATION-CANDIDATE-v0.2.md` — superseded by the E2E Runtime line; do not install.

### Earlier Global E2E compiled views

- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.1.md`
- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.2.md`
- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.3.md`
- `GLOBAL-E2E-RUNTIME-KERNEL-CANDIDATE-v0.4.md`

All are superseded for installation by Global v0.5.

### Earlier System Development Project views

- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.1.md`
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.2.md`
- `SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.3.md`

All are superseded for installation by Project v0.4.

### Earlier installation bundles

- `E2E-INSTALLATION-BUNDLE-v0.1.md` — tombstone / do not install.
- `E2E-INSTALLATION-BUNDLE-v0.2.md` — tombstone / do not install.
- `E2E-INSTALLATION-BUNDLE-v0.3.md` — tombstone / do not install.

All are superseded by Bundle v0.4.

### Migration manifests

- `E2E-RUNTIME-MIGRATION-MANIFEST-v0.1.md`
- `E2E-RUNTIME-MIGRATION-MANIFEST-v0.2.md`
- `E2E-RUNTIME-MIGRATION-MANIFEST-v0.3.md`
- `E2E-RUNTIME-MIGRATION-MANIFEST-v0.4.md`

These document migration/compilation history. They do not override the post-PR13 `CURRENT.md` state or authorize installation of the versions they mention.

## Rollback material

`rollback/` contains explicit pre-E2E / prior-carrier snapshots. Rollback artifacts are recovery controls, not current target configurations.

## Status and authority rules

```text
historical artifact ≠ current instruction
newer-looking file ≠ controlling state
repository Promotion ≠ external settings installation
session-effective load ≠ independent persistent UI readback
compiled view ≠ canonical Runtime semantic authority
```

When in doubt:

1. read `../CURRENT.md` from `main`;
2. resolve the current package named there;
3. confirm any material external transition/readback evidence;
4. use historical files only for provenance, comparison, regression or rollback.

## Current transition

After the post-PR13 hygiene candidate is promoted and read back, the parent program resumes at persistent external-settings readback reconciliation where required, then Runtime conformance preflight and genuine E2E real-use validation.
