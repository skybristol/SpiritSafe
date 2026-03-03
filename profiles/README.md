# SpiritSafe Entity Profile Registry

This directory contains **GKC Entity Profiles**—declarative YAML schemas that define the structure, constraints, and metadata for real-world entities in the Global Knowledge Commons.

---

## What Are Entity Profiles?

Entity Profiles serve as:

- **Data validation schemas** — enforce constraints, datatypes, and cardinality rules
- **Form generation blueprints** — drive interactive wizards for data curation
- **Cross-platform mapping** — link Wikidata items to Wikimedia Commons, Wikipedia, and OpenStreetMap
- **Domain-specific guidance** — embed expert knowledge about entity types directly in the schema

Each profile is fundamentally based on the **Wikibase/Wikidata model** but incorporates linkages to other platforms in The Commons.

---

## Profile Directory Structure

Every profile lives in its own subdirectory with this standard layout:

```
ProfileName/
├── profile.yaml         # Main profile definition (required)
├── metadata.yaml        # Profile metadata and versioning (required)
├── CHANGELOG.md         # Version history (required)
├── README.md            # Human-readable profile documentation (optional)
└── queries/             # SPARQL queries for allowed-items hydration (optional)
    ├── query_one.sparql
    └── query_two.sparql
```

### File Descriptions

| File | Purpose |
|------|---------|
| **profile.yaml** | Complete entity definition: labels, descriptions, statements, sitelinks, constraints, allowed-items lists |
| **metadata.yaml** | Profile metadata: name, version, authors, schema_version, profile graph edges |
| **CHANGELOG.md** | Semantic versioning change log (follows [Keep a Changelog](https://keepachangelog.com/)) |
| **README.md** | (Optional) Extended documentation for complex profiles or domain-specific guidance |
| **queries/*.sparql** | SPARQL queries referenced by `allowed_items.query_ref` in profile.yaml; executed during cache hydration |

---

## Current Profiles

### TribalGovernmentUS

Federally recognized Native American tribes in the United States. Comprehensive profile documenting tribal nomenclature, federal recognition, governmental structure, and cross-platform links.

**Key Features:**

- Multi-language support (English, Cherokee, Navajo)
- SPARQL-driven allowed-items (BIA Federal Register issues, Wikidata language items)
- Profile graph link to OfficeHeldByHeadOfState
- Fixed-value statements with variable references

**Directory:** [TribalGovernmentUS/](TribalGovernmentUS/)

---

### OfficeHeldByHeadOfState

Public offices held by heads of government (tribal leadership positions, executive offices, etc.). Designed for use as a related entity to government profiles.

**Key Features:**

- Minimal required fields (allows quick entity creation)
- Works as secondary profile in multi-entity curation packets
- Cardinality enforcement (1:1 office-to-government relationship)

**Directory:** [OfficeHeldByHeadOfState/](OfficeHeldByHeadOfState/)

---

## Using Profiles

### For Data Curators

Launch the GKC Wizard with a profile to create guided curation workflows:

```bash
poetry run gkc wizard TribalGovernmentUS
```

The wizard loads the profile and generates a 5-step interface for entity creation.

### For Developers

Load profiles programmatically via the `spirit_safe` module:

```python
from gkc.spirit_safe import load_profile

profile = load_profile("TribalGovernmentUS")
print(profile.metadata.name)  # "Tribal Government (US)"
print(profile.statements[0].label)  # "instance of (classification)"
```

### For Profile Architects

Create new profiles by:

1. Creating a new subdirectory in `profiles/`
2. Writing `profile.yaml`, `metadata.yaml`, and `CHANGELOG.md`
3. (Optional) Adding SPARQL queries to `queries/` subdirectory
4. Testing with `poetry run gkc validate-profile <ProfileName>`

---

## Profile Graph

Profiles can reference other profiles via **entity_profile** statement types. This creates a **profile graph** enabling multi-entity curation workflows.

**Example:** TribalGovernmentUS → OfficeHeldByHeadOfState

When a curator creates a tribal government, the wizard offers to create the associated office in the same session. Both entities are bundled into a **GKC Curation Packet** with cross-references maintained via `packet_id` placeholders.

## Implemented Schema Fields (Phase 1)

The following fields are now part of the active SpiritSafe profile design and are validated in CI.

### Statement-level linkage (`profile.yaml`)

Use on statements that include `entity_profile`.

```yaml
- id: office_held_by_head_of_state
    type: statement
    entity_profile: OfficeHeldByHeadOfState
    form_policy: target_only
    linkage:
        target_profile: OfficeHeldByHeadOfState
        relationship:
            type: office_of_head_of_state
            direction: bidirectional
            reverse_statement_hint: applies_to_jurisdiction
        cardinality:
            min: 0
            max: 1
        workflow_policy:
            create: allowed
            select_existing: allowed
        traversal:
            max_depth: 1
```

Required linkage keys:

- `target_profile`
- `relationship.type`
- `relationship.direction`
- `cardinality.min`
- `cardinality.max`
- `workflow_policy.create`
- `workflow_policy.select_existing`
- `traversal.max_depth`

### Metadata profile graph (`metadata.yaml`)

```yaml
profile_graph:
    neighbors:
        - OfficeHeldByHeadOfState
    edges:
        - target_profile: OfficeHeldByHeadOfState
            via_statement: office_held_by_head_of_state
            relationship_type: office_of_head_of_state
            cardinality:
                min: 0
                max: 1
            traversal:
                max_depth: 1
```

Required metadata graph keys:

- `profile_graph.neighbors`
- `profile_graph.edges[*].target_profile`
- `profile_graph.edges[*].via_statement`
- `profile_graph.edges[*].relationship_type`
- `profile_graph.edges[*].cardinality.min`
- `profile_graph.edges[*].cardinality.max`
- `profile_graph.edges[*].traversal.max_depth`

### Registry manifest (`cache/manifest.json`)

The production manifest now includes, per profile:

- Profile metadata used by consumers (`name`, `description`, `status`, `related_profiles`, `profile_graph`)
- Query inventory (`queries[*].source_path`, `queries[*].cache_path`)
- Statement linkage inventory (`statement_linkages` extracted from `profile.yaml`)
- File references (`files.profile_yaml`, `files.metadata_yaml`, `files.readme`, `files.changelog`)

Top-level manifest traceability fields are:

- `generated_at`
- `commit_sha`
- `commit_timestamp`

---

## Documentation

For detailed documentation on profile structure, schema, and design patterns:

- **[GKC Entity Profile Documentation](https://datadistillery.org/gkc/profiles/)** — Complete profile schema reference
- **[GKC Architecture Overview](https://datadistillery.org/gkc/architecture/)** — How profiles fit in the larger GKC pipeline
- **[GKC Wizard Documentation](https://datadistillery.org/gkc/wizard/)** — How wizards consume profiles to generate UIs

---

## Schema Version

Current profile schema: **1.0.0**

All profiles in this registry conform to this schema version. See [Profile Schema Reference](https://datadistillery.org/gkc/profiles/#schema-version) for compatibility notes.

---

**Maintained by:** GKC Profile Architect  
**Repository:** [skybristol/SpiritSafe](https://github.com/skybristol/SpiritSafe)
