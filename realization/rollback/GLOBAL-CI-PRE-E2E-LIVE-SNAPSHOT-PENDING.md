# Pre-E2E Live Global CI Rollback Snapshot — PENDING

**Status:** BLOCKING PRE-INSTALLATION DEPENDENCY  
**Date:** 2026-08-20

The Human reports that the legacy Global Custom Instructions are still the live external runtime control.

The exact installed payload is **not established from repository evidence**. Prior Global-CI candidates must not be treated as the live rollback payload merely because they descend from earlier runtime work.

Before replacing the live Global Custom Instructions:

1. copy the exact currently installed Global Custom Instructions text;
2. persist it as `realization/rollback/GLOBAL-CI-PRE-E2E-LIVE-SNAPSHOT.txt`;
3. record capture time, exact character count/hash and relevant account/workspace context;
4. Human confirms that the persisted text equals the currently live pre-E2E payload.

Until that happens:

```text
GLOBAL E2E KERNEL INSTALLATION = BLOCKED
```

This blocker protects rollback identity and prevents a new runtime candidate from erasing the only exact representation of the currently operating configuration.
