# SpiritSafe

SpiritSafe is the declarative artifact registry for the Global Knowledge Commons. It stores version-controlled Data Distillery Wikibase content that the `gkc` runtime consumes directly, enabling profile-driven curation and validation without requiring live Wikibase access.

## Directory Structure

- `profiles/` — Generated JSON Entity Profiles, one file per profile QID. These are build artifacts produced by the `Cache From Wikibase` workflow.
- `queries/` — SPARQL query files extracted from Data Distillery Wikibase talk pages, one `.sparql` file per value-list QID. Used as the source queries for cache hydration.
- `cache/entities/` — Per-entity Wikibase JSON used as the build substrate for profile export and value-list discovery.
- `cache/queries/` — Hydrated value-list JSON, one file per value-list QID. Each file contains deduplicated, sorted items produced by executing the corresponding `queries/` SPARQL file.
- `cache/refresh/` — Refresh summaries written by the `Cache From Wikibase` workflow.

## Workflows

- **Cache From Wikibase** (`cache-from-wikibase.yml`) — Manual workflow. Refreshes `cache/entities` from Data Distillery Wikibase recentchanges, then exports JSON Entity Profiles into `profiles/`.
- **Hydrate Value Lists** (`hydrate-value-lists.yml`) — Manual workflow. Pulls SPARQL queries from Wikibase talk pages and writes them into `queries/`, then executes each query and writes hydrated item lists into `cache/queries/`.
- **Validate Profile** (`validate-profile.yml`) — Runs baseline structural checks on pull requests.
- **PR Auto-Merge** (`pr-automerge.yml`) — Squash auto-merges non-draft pull requests to `main` once required checks pass.

## Artifact Authorship

All files in `profiles/`, `queries/`, `cache/entities/`, and `cache/queries/` are generated artifacts. They should not be hand-edited; changes are produced by running the appropriate workflow.

## Runtime Integration

The `gkc` Python package consumes SpiritSafe artifacts directly. Entity Profiles in `profiles/` drive data validation and form generation. Value lists in `cache/queries/` provide the allowed-item sets that profiles reference for constrained fields.
