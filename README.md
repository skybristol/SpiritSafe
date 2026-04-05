# SpiritSafe

SpiritSafe is the declarative artifact registry for the Global Knowledge Commons.

It stores version-controlled Data Distillery Wikibase-derived artifacts that the `gkc` runtime consumes directly.

## Directory Structure

- `config/` - curated source configuration for the meta-wikibase integration contract.
- `still/` - materialized SpiritSafe artifacts consumed by `gkc`.
- `still/entities/` - cached Wikibase entity JSON used as profile/value-list substrate.
- `still/profiles/` - JSON Entity Profiles keyed by QID (`still/profiles/<QID>.json`).
- `still/value_lists/queries/` - SPARQL files keyed by value-list QID.
- `still/value_lists/cache/` - hydrated value-list JSON keyed by QID.
- `still/manifest.json` - URI-keyed artifact index built from current SpiritSafe artifacts.
- `still/entity_index.json` - normalized entity index built from cached entities.
- `still/logs/` - workflow summaries and sync logs.
- `partners/` - generated partner-facing artifacts that are not part of the core materialized runtime set.
- `partners/wikimedia_sites.json` - Wikimedia sitelink source artifact.

## Manifest Design

`still/manifest.json` is a build artifact index, not a runtime dependency for packet assembly.

Top-level sections:

- `generated_at`
- `source`
- `profiles`
- `entities`
- `queries`
- `value_lists`

`profiles` entries are keyed by `entity` URI and `qid` and include embedded `profile_graph` and `value_list_graph` summaries pulled from each profile metadata section.

## Workflows

- **Cache from Wikibase** (`cache-from-wikibase.yml`) - refreshes `still/entities/` from recent Wikibase updates and writes `still/logs/last_run_summary.json`.
- **Cache Wikibase and Build Profiles** (`cache-wikibase-and-build-profiles.yml`) - refreshes `still/entities/` and exports `still/profiles/<QID>.json` from the refreshed cache.
- **Hydrate Value Lists** (`hydrate-value-lists.yml`) - exports `still/value_lists/queries/<QID>.sparql` and hydrates `still/value_lists/cache/<QID>.json`.
- **Build Manifest** (`build-manifest.yml`) - runs `gkc --json spiritsafe manifest build --source local --local-root .` and commits `still/manifest.json` and `still/entity_index.json` when changed.
- **Build Semantic Anchors** (`build-semantic-anchors.yml`) - runs `gkc --json spiritsafe semantic-anchors build --source local --local-root . --output config/semantic_anchors.json` and commits the configured output path when changed.
- **Validate Profile** (`validate-profile.yml`) - baseline structural checks for pull requests.
- **PR Auto-Merge** (`pr-automerge.yml`) - squash auto-merge for eligible pull requests.

## Artifact Authorship

Files under `still/`, `partners/`, and `config/semantic_anchors.json` are generated artifacts unless explicitly noted otherwise.

Do not hand-edit generated artifacts. Update source Wikibase content or run workflows.

The primary authored integration config is `config/dd-wikibase.yaml`.

`config/semantic_anchors.json` is a generated artifact produced by the semantic-anchor workflow.

## Runtime Integration

The `gkc` package consumes:

- `still/profiles/<QID>.json` for profile structure and packet scaffolding.
- `still/value_lists/cache/<QID>.json` for allowed-item lists.
- `config/semantic_anchors.json` for semantic name-to-entity lookup.
- `still/manifest.json` for registry/discovery tooling.

Packet assembly is manifest-independent and loads profile JSON directly.
