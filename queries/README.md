# Queries

This directory contains SPARQL query files for value lists defined in Data Distillery Wikibase. Each file is extracted from the `Item_talk:QID` page of the corresponding value-list entity.

## Source and Generation

Query files are written by the `Hydrate Value Lists` workflow, which calls `gkc profile value-lists hydrate`. The workflow fetches the first `<sparql>...</sparql>` block from each value-list entity's talk page and writes it here as `QID.sparql`.

These files are generated artifacts. The authoritative source for each query is the Wikibase talk page.

## Execution

After extraction, the same workflow executes each query against the configured SPARQL endpoint and writes results into `cache/queries/QID.json`. Query results must return at minimum `?item` and `?itemLabel` bindings.
