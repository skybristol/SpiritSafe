# Cache / Queries

This directory contains hydrated value-list JSON files, one per value-list QID. Each file is produced by executing the corresponding SPARQL query in `queries/` against the Data Distillery SPARQL endpoint.

## File Structure

Each `QID.json` file contains two top-level keys:

- `metadata` — `entity_uri`, `source`, `query_ref` (path to the `.sparql` file used), `updated` (ISO timestamp), and `count` (number of items).
- `items` — Array of objects with at minimum `item` (entity URI) and `itemLabel` (English label). Items are deduplicated by `item` URI and sorted by `itemLabel` then `item`.

## Authorship

These files are generated artifacts written by the `Hydrate Value Lists` workflow. Do not hand-edit them.
