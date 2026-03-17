# SpiritSafe

SpiritSafe is the declarative artifact registry for the Global Knowledge Commons.

It stores version-controlled Data Distillery Wikibase-derived artifacts that the `gkc` runtime consumes directly.

## Directory Structure

- `profiles/` - JSON Entity Profiles keyed by QID (`profiles/<QID>.json`).
- `queries/` - SPARQL files keyed by value-list QID (`queries/<QID>.sparql`).
- `cache/entities/` - cached Wikibase entity JSON used as profile/value-list substrate.
- `cache/queries/` - hydrated value-list JSON keyed by QID (`cache/queries/<QID>.json`).
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

- **Cache From Wikibase** (`cache-from-wikibase.yml`) - refreshes `cache/entities/` and exports `profiles/<QID>.json`.
- **Hydrate Value Lists** (`hydrate-value-lists.yml`) - exports `queries/<QID>.sparql` and hydrates `cache/queries/<QID>.json`.
- **Build Manifest** (`build-manifest.yml`) - runs `gkc --json spiritsafe manifest build --source local --local-root .` and commits `cache/manifest.json` when changed.
- **Validate Profile** (`validate-profile.yml`) - baseline structural checks for pull requests.
- **PR Auto-Merge** (`pr-automerge.yml`) - squash auto-merge for eligible pull requests.

## Artifact Authorship

Files under `profiles/`, `queries/`, `cache/entities/`, `cache/queries/`, and `cache/manifest.json` are generated artifacts.

Do not hand-edit generated artifacts. Update source Wikibase content or run workflows.

## Runtime Integration

The `gkc` package consumes:

- `profiles/<QID>.json` for profile structure and packet scaffolding.
- `cache/queries/<QID>.json` for allowed-item lists.
- `cache/manifest.json` for registry/discovery tooling.

Packet assembly is manifest-independent and loads profile JSON directly.
