# SpiritSafe

The Entity Profile Registry for the Global Knowledge Commons.

SpiritSafe is in a reboot phase. The repository is being reset so profile architecture, CI behavior, and cache/export strategy can be rebuilt around the ontology-first workflow.

## Reboot Status

- Legacy profile packages are removed from active registry content.
- Manifest-generation CI has been removed.
- Legacy cache-hydration CI has been removed.
- Pull requests use a no-manual-review fast path for this phase.

## Repository Scope

- profiles/: baseline directory for new profile packages.
- queries/: shared SPARQL query workspace.
- cache/: placeholder for generated artifacts in the upcoming phase.
- .github/workflows/validate-profile.yml: baseline structural checks.
- .github/workflows/pr-automerge.yml: auto-merge enablement for non-draft PRs targeting main.

## PR Policy For Reboot

Non-draft pull requests to main are configured for squash auto-merge once required checks pass.
