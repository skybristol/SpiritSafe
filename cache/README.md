# SpiritSafe Cache

This directory stores generated cache artifacts sourced from Data Distillery Wikibase.

## Current Layout

- entities/: per-entity Wikibase JSON cache files.
- refresh/last_run_summary.json: recentchanges refresh summary written by the cache workflow.

## Role In The Build Flow

cache/entities is the immediate source for JSON Entity Profile generation.

The Cache From Wikibase workflow refreshes cache/entities first, then runs the gkc profile export route to materialize profile JSON into profiles/.

This cache is committed so profile generation and downstream runtime work can operate without live Wikibase access.
