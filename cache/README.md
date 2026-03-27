# Cache

This directory stores generated artifacts sourced from Data Distillery Wikibase.

## Layout

- `entities/` — Per-entity Wikibase JSON files. One file per QID, written by the `Cache From Wikibase` workflow. Used as the build substrate for JSON Entity Profile export and value-list discovery.
- `queries/` — Hydrated value-list JSON, one file per value-list QID. Written by the `Hydrate Value Lists` workflow. Each file contains `metadata` (source query, update timestamp, item count, available columns) and a deduplicated, sorted `items` array.
- `config/wikimedia_sites.json` — Generated Wikimedia site registry artifact sourced from the Meta-Wiki sitematrix API. Written by the `Sync Wikimedia Sites` workflow. Includes active and closed sites, normalized domains, and lookup indexes by `dbname` and `domain`.
- `refresh/last_run_summary.json` — Summary written after each `Cache From Wikibase` run, recording which entities were added, updated, or unchanged.

## Authorship

All files in this directory are generated artifacts produced by GitHub Actions workflows. Do not hand-edit them.
