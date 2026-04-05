# Profiles

This directory is retained for authored documentation and any legacy package-style profile materials.

Generated JSON Entity Profiles now live under `still/profiles/`, one file per profile QID.

## Source and Generation

Profiles are produced by the `Cache Wikibase and Build Profiles` workflow, which runs `gkc profile export-json` against `still/entities/`. Each profile is a structured JSON document derived from the corresponding Data Distillery Wikibase entity and its associated claims.

Profiles drive data validation and form generation in the `gkc` runtime. They are build artifacts and should not be hand-edited.

## Contents

Each generated profile file includes:

- `entity` — QID, labels, and descriptions
- `identification` — field definitions for the entity's identifying properties
- `statements` — claim definitions with property, value type, constraints, and allowed-item references
- `metadata` — generation timestamp and source Wikibase URI
