# Repository Inventory and Disposition

**Bound source:** authoritative `main@c4a517b3682c95ceb356421c6cb8c5e2bdfab4c2`  
**Source tree:** `638516562f62bc0985a0442f82da5d3cb3b68642`  
**Inventory:** 223 files, 2,237,130 bytes; recursive tree response not truncated

Dispositions are based on content inspection of all current/rebaseline/Skill sources, the controlling historical requirements/architecture/runtime sources, representative decisions/evidence/reference/method/review artifacts and material genuine-use records. Folder policies below follow those content findings; they are not inferred from names or old status labels alone.

## Source-tree disposition

| Source area | Files | Disposition | Defensible basis | Candidate location |
|---|---:|---|---|---|
| Root `CURRENT.md`, `README.md` | 2 | `PROMOTE` through replacement | Correct authority boundary but stale/branch-specific navigation and too much historical detail; replace with one obvious current entry and compact navigation | root |
| `rebaseline/` | 6 | exact CI `PROMOTE`; other five `EXTRACT` then `LEGACY` | Rebaseline corrected authority/product model and contains the ten required lessons; semantics are compacted into active baseline/evidence/learning records | exact CI remains; five files archived |
| `skills/` | 19 | three packages `KEEP-SKILL`; three packages `LEGACY`; registry/contracts `PROMOTE` through replacement | Package and method inspection plus current provider inventory show differentiated value only for decision, evaluation and scoped system development | active `skills/`; demoted packages archived |
| `.codex-plugin/`, `.agents/plugins/` | 2 | `PROMOTE` with manifest narrowing | Legitimate packaging/discovery carriers once limited to the active portfolio | unchanged locations |
| `.agents/skills/` | 6 links | three `PROMOTE`; three `DELETE-CANDIDATE` | Links are duplicate discovery views, not evidence; remove views for demoted packages while preserving canonical packages in archive | active links only |
| `foundation/` | 5 | controlling v0.3 `EXTRACT`; remainder `LEGACY` | Durable principles survive, but former universal Requirements scope is not the current native-first system | archive |
| `architecture/` | 9 | Target Architecture v0.2 `EXTRACT`; remainder `LEGACY` | Responsibility/state/change distinctions survive as principles/lenses; architecture objects are not required runtime | archive |
| `realization/` | 72 | v0.6 PWB/Topology `EXTRACT`; remainder `LEGACY` | Contains durable execution, provider, surface and assurance semantics but also the obsolete custom Runtime/QWS/routing line | archive |
| `evaluation/` | 31 | selected genuine-use records `EXTRACT`; remainder `LEGACY` | Real failures support current learning; old validation matrices and version-specific tests do not control present behavior | archive |
| `evidence/` | 12 | `LEGACY` | Strong provenance/evidence discipline but lineage-heavy and already represented in current principles/system learning | archive |
| `decisions/` | 4 | `LEGACY` | Preserves Human acceptance and former authority transitions; no ADR remains current system authority after rebuild | archive |
| `methods/` | 7 | `LEGACY` | Earlier method copies/registry are superseded by active `system-development` package and retain provenance value | archive |
| `references/` | 8 | `LEGACY` | Broad research map remains useful historical basis but is not current architecture or a mandatory research program | archive |
| `reviews/` | 40 | selected assurance lessons `EXTRACT`; remainder `LEGACY` | Reviews establish source/claim separation and prior repair evidence; version-specific PASS states do not transfer | archive |

## Active target basis

- one root current-state entry point and one root navigation file;
- three compact baseline notes;
- the exact unchanged 4,991-character intended Global CI source;
- three differentiated active Skill packages and narrow packaging/discovery carriers;
- four inspectable rebuild-assurance files;
- one explicit Legacy boundary with the full pre-rebuild evidence corpus.

No historical blob is discarded. The only immediate `DELETE-CANDIDATE` objects are three symbolic discovery links for demoted Skills; they contain no independent method or evidence semantics.

The complete file-level classification for the 223-file bound source is `inventory/FILE-DISPOSITION.csv`.
