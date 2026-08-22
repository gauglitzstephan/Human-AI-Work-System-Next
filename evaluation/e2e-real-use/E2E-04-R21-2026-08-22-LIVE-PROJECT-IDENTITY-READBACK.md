# E2E-04 R21 — Live Project identity readback and carrier divergence

**Status:** LIVE UI CONTENT READBACK PASS / PROJECT v0.5 CANDIDATE IDENTIFIED / REPOSITORY BASELINE REMAINS v0.4 / NO UI CHANGE, REPAIR OR RUNTIME PROMOTION  
**Date:** 2026-08-22  
**Parent:** R21 native-state and candidate-lineage reconciliation  
**Surface:** ChatGPT System Development Project instructions UI → Human-supplied full payload → repository comparison

## 1. Question under test

Resolve the previously open deployment fact:

> Which exact Project Instructions payload is persistently present in the live System Development Project?

This is a carrier-identity and state-reconciliation question. It does not test general behavioral conformance and does not authorize a Project setting change.

## 2. Evidence

The Human opened the live Project Instructions UI and supplied the full visible payload without editing it.

Repository comparison found content identity with:

- path: `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.5.md`;
- source branch: `repair/r20-cold-start-admission-v0.1`;
- normalized identity recorded by that artifact:
  - UTF-8 LF characters: 6,143;
  - LF line breaks: 9;
  - SHA-256 UTF-8 LF: `16b46d87d98926e3e676957782569061f84faa2f5060d9d6e590c6e98853842b`.

The repository-promoted Project baseline on `main` remains:

- `realization/SYSTEM-WEITERENTWICKLUNG-PROJECT-INSTRUCTIONS-CANDIDATE-v0.4.md`;
- UTF-8 LF characters: 5,172;
- SHA-256 UTF-8 LF: `338a01576cfa3e330b0e120dba509ee447f516cd4675a212924efc91388dd69b`.

Chat transport can normalize line endings. The supported identity claim is therefore exact visible-content identity after LF normalization, not an independently machine-measured UI byte identity.

## 3. Reconciled state

```text
Repository-promoted Project baseline       v0.4
Live persistent Project payload            v0.5 Candidate
Live payload content readback              PASS
v0.5 repository provenance                 repair/r20-cold-start-admission-v0.1
v0.5 repository/runtime Promotion          NONE
UI modification during readback            NONE
```

The v0.5 branch artifact described itself as not installed. That statement remains historical branch-state evidence but is superseded for the current deployment fact by the later direct UI readback. It does not become a Promotion claim.

## 4. Claim boundary

Supported:

- the previously unresolved live Project payload identity is now resolved;
- the live Project carrier contains the v0.5 Candidate payload by normalized content;
- live deployment and repository Promotion state currently diverge;
- `main` remains the controlling repository authority until a legitimate merge/promotion transition.

Not supported:

- raw UI byte identity independent of chat transport;
- v0.5 general behavioral effectiveness;
- v0.5 acceptance or Promotion;
- a need to repair, rollback or change the Project UI;
- universal v0.6 qualification.

## 5. Qualification-loop correction

Provider return/rebind and the bounded negative control remain useful future evidence, but they do not block truthful repository-state reconciliation. They should be observed in genuine use rather than manufactured as a mandatory precondition for this repository convergence.

```text
Live Project identity                     PASS
Provider return/rebind                    UNVERIFIED / MONITOR IN GENUINE USE
Bounded negative control                  UNVERIFIED / MONITOR IN GENUINE USE
Active synthetic qualification loop       STOPPED
Skill/Runtime repair or Promotion          NONE
Project UI change                          NONE
```

[material-work-entry v0.6-candidate]
