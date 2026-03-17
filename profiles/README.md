# SpiritSafe Profiles

This directory stores generated JSON Entity Profiles built from SpiritSafe cache/entities data.

## Current Layout

Profiles are written as one JSON file per profile QID:

- Q4.json
- Q39.json
- <QID>.json

These are generated artifacts produced by:

- the Cache From Wikibase GitHub Actions workflow
- the gkc CLI route `gkc profile export-json`

## Generation Contract

Each generated profile file is built from the per-entity cache and currently includes:

- entity
- identification
- statements
- metadata

The files in this directory should be treated as exported build outputs rather than hand-maintained profile packages.
