# SpiritSafe

SpiritSafe is the declarative artifact registry for the Global Knowledge Commons.

It stores version-controlled Data Distillery Wikibase-derived artifacts that the `gkc` runtime consumes directly.

## Directory Structure

- `config/` - curated source configuration for the meta-wikibase integration contract.
- `profiles/` - JSON Entity Profiles keyed by QID (`profiles/<QID>.json`).
- `queries/` - SPARQL files keyed by value-list QID (`queries/<QID>.sparql`).
- `cache/entities/` - cached Wikibase entity JSON used as profile/value-list substrate.
- `cache/queries/` - hydrated value-list JSON keyed by QID (`cache/queries/<QID>.json`).
- `cache/config/` - generated configuration artifacts built from curated config and cached entities.
- `cache/manifest.json` - URI-keyed artifact index built from current SpiritSafe artifacts.
- `cache/refresh/` - cache refresh summaries from refresh workflows.

## Manifest Design

`cache/manifest.json` is a build artifact index, not a runtime dependency for packet assembly.

Top-level sections:

- `generated_at`
- `source`
- `profiles`
- `entities`
- `queries`
- `value_lists`

`profiles` entries are keyed by `entity` URI and `qid` and include embedded `profile_graph` and `value_list_graph` summaries pulled from each profile metadata section.

## Workflows

- **Cache from Wikibase** (`cache-from-wikibase.yml`) - refreshes `cache/entities/` from recent Wikibase updates and writes `cache/refresh/last_run_summary.json`.
- **Cache Wikibase and Build Profiles** (`cache-wikibase-and-build-profiles.yml`) - refreshes `cache/entities/` and exports `profiles/<QID>.json` from the refreshed cache.
- **Hydrate Value Lists** (`hydrate-value-lists.yml`) - exports `queries/<QID>.sparql` and hydrates `cache/queries/<QID>.json`.
- **Build Manifest** (`build-manifest.yml`) - runs `gkc --json spiritsafe manifest build --source local --local-root .` and commits `cache/manifest.json` when changed.
- **Build Semantic Anchors** (`build-semantic-anchors.yml`) - runs `gkc --json spiritsafe semantic-anchors build --source local --local-root . --output config/semantic_anchors.json` and commits the configured output path when changed.
- **Validate Profile** (`validate-profile.yml`) - baseline structural checks for pull requests.
- **PR Auto-Merge** (`pr-automerge.yml`) - squash auto-merge for eligible pull requests.

## Artifact Authorship

Files under `profiles/`, `queries/`, `cache/entities/`, `cache/queries/`, `cache/config/`, and `cache/manifest.json` are generated artifacts.

Do not hand-edit generated artifacts. Update source Wikibase content or run workflows.

The primary authored integration config is `config/dd-wikibase.yaml`.

`config/semantic_anchors.json` is a generated artifact produced by the semantic-anchor workflow.

## Runtime Integration

The `gkc` package consumes:

- `profiles/<QID>.json` for profile structure and packet scaffolding.
- `cache/queries/<QID>.json` for allowed-item lists.
- `config/semantic_anchors.json` for semantic name-to-entity lookup.
- `cache/manifest.json` for registry/discovery tooling.

Packet assembly is manifest-independent and loads profile JSON directly.
