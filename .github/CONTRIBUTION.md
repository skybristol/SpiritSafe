# Contributing to SpiritSafe

Thank you for your interest in contributing to SpiritSafe! This registry thrives on community contributions to expand and refine entity profiles for the Global Knowledge Commons.

## Ways to Contribute

- **Create a new entity profile** for a type not yet in the registry
- **Enhance an existing profile** with additional properties or improved validation
- **Improve documentation** for better clarity and usability
- **Report issues** with existing profiles or infrastructure
- **Update SPARQL queries** for controlled vocabularies

## Before You Start

1. **Check existing profiles** to see if a similar entity type already exists
2. **Review the documentation** at [SpiritSafe.md](https://github.com/skybristol/gkc/blob/main/docs/SpiritSafe.md)
3. **Open an issue** to discuss significant new profiles or breaking changes
4. **Understand the YAML schema** used for profile definitions

## Contribution Workflow

### Creating a New Profile

1. **Fork the repository** and clone your fork locally
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/SpiritSafe.git
   cd SpiritSafe
   ```

2. **Create a feature branch**
   
   ```bash
   git checkout -b profile/my-entity-type
   ```

3. **Create the profile directory structure**
   
   ```bash
   mkdir -p profiles/MyEntityType/queries
   ```

4. **Create required files** in `profiles/MyEntityType/`:
   
   - **`profile.yaml`** — Entity profile definition following the schema
   - **`metadata.yaml`** — Profile metadata (see template below)
   - **`README.md`** — Comprehensive documentation (see template below)
   - **`CHANGELOG.md`** — Version history (start with [Unreleased] or [0.1.0])
   - **`queries/`** — SPARQL queries (if profile uses SPARQL-driven choice lists)

5. **Validate locally** (optional but recommended)
   
   ```bash
   python -c "import yaml; yaml.safe_load(open('profiles/MyEntityType/profile.yaml'))"
   ```

6. **Commit your changes**
   
   ```bash
   git add profiles/MyEntityType/
   git commit -m "feat: add MyEntityType profile"
   ```

7. **Push to your fork**
   
   ```bash
   git push origin profile/my-entity-type
   ```

8. **Create a pull request** on GitHub
   
   - Provide a clear description of the entity type
   - Explain the use case and rationale
   - Reference any related issues or discussions

9. **CI validation runs automatically**
   
   - YAML syntax check
   - Metadata validation
   - Documentation presence check
   - SPARQL query validation

10. **Address review feedback** from maintainers

11. **Merge** — Your profile becomes part of the registry!

### Updating an Existing Profile

1. **Fork and create a branch**
   
   ```bash
   git checkout -b profile/tribal-government-update
   ```

2. **Edit profile files** in `profiles/[ProfileName]/`
   
   - Modify `profile.yaml`, `README.md`, or other files as needed

3. **Update CHANGELOG.md**
   
   ```markdown
   ## [Unreleased]
   
   ### Added
   - New property for X
   
   ### Changed
   - Updated validation constraints for Y
   
   ### Fixed
   - Corrected reference pattern for Z
   ```

4. **Increment version in `metadata.yaml`**
   
   Follow [semantic versioning](https://semver.org/):
   
   - **MAJOR** (1.0.0 → 2.0.0): Breaking changes incompatible with previous version
   - **MINOR** (1.0.0 → 1.1.0): New features, backward compatible
   - **PATCH** (1.0.0 → 1.0.1): Bug fixes, backward compatible

5. **Update `published_date`** in `metadata.yaml` to today's date

6. **Commit, push, and create PR**

7. **CI runs and maintainer reviews**

8. **Merge** — New version is tagged and released automatically

## File Templates

### `metadata.yaml` Template

```yaml
name: My Entity Type
description: >
  Brief description of what this entity type represents and its purpose
  in the Global Knowledge Commons.

version: 1.0.0
status: stable  # or beta, deprecated
published_date: 2026-03-01  # ISO 8601 date

authors:
  - name: Your Name

maintainers:
  - name: Your Name

source_references:
  - name: Relevant Wikidata EntitySchema or external reference
    url: https://example.org

related_profiles:
  - OtherRelatedProfile

community_feedback:
  issue_tracker: https://github.com/skybristol/SpiritSafe/issues

# Profile capabilities summary (for discovery)
datatypes_used:
  - item
  - url
  - time

statements_count: 5
references_required: true
qualifiers_used:
  - point_in_time

sparql_sources:
  - my_sparql_query
```

### `README.md` Template

```markdown
# My Entity Type

**Profile version:** 1.0.0  
**Status:** Stable  
**Maintainer:** Your Name

---

## What is this entity?

A clear, plain-language explanation of what this entity type represents.

## When to use this profile

Specific guidance on when to apply this profile and when NOT to use it.

## Key Statements

List of primary properties defined by this profile.

## Example Entities

Links to real Wikidata items that exemplify this type.

## Statement Details and Guidance

Detailed documentation for each statement property.

## Known Issues and Limitations

Any current limitations or future considerations.

## Contributing

How to propose changes to this profile.
```

### `CHANGELOG.md` Template

```markdown
# Changelog: MyEntityType

All notable changes to this profile will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-03-01

### Added

- Initial stable release
- Statement properties: ...
- SPARQL-driven choice lists for ...

### Documentation

- Comprehensive README with usage guidance
- Metadata and version tracking
```

## Profile Quality Standards

### Required Elements

- ✅ **Valid YAML syntax** — Profile must parse without errors
- ✅ **Complete metadata** — All required fields in `metadata.yaml`
- ✅ **Comprehensive README** — Clear entity description and usage guidance
- ✅ **Version tracking** — Proper semantic versioning and CHANGELOG
- ✅ **Validation policies** — Thoughtful handling of existing data (`allow_existing_nonconforming` where appropriate)
- ✅ **Inline guidance** — `guidance` fields for complex statements
- ✅ **Reference patterns** — Proper use of YAML anchors for reusability

### Best Practices

- 📌 **Be curator-friendly** — Write for humans creating data, not just machines validating it
- 📌 **Provide examples** — Real Wikidata items help curators understand usage
- 📌 **Document constraints** — Explain WHY constraints exist, not just WHAT they are
- 📌 **Use SPARQL wisely** — Only use SPARQL-driven lists when the vocabulary is large or changes frequently
- 📌 **Test with real data** — Validate your profile against existing Wikidata items
- 📌 **Link related profiles** — Document relationships between entity types

## Code of Conduct

- **Be respectful** — Treat all contributors with respect and kindness
- **Be collaborative** — Work together to improve profiles for everyone
- **Be constructive** — Provide helpful feedback in reviews
- **Be patient** — Maintainers review PRs on a volunteer basis

## Questions or Help?

- **Open an issue**: [SpiritSafe Issues](https://github.com/skybristol/SpiritSafe/issues)
- **Check the docs**: [SpiritSafe.md](https://github.com/skybristol/gkc/blob/main/docs/SpiritSafe.md)

## License

By contributing, you agree that your contributions will be licensed under the same license as this repository. Profiles and documentation are dedicated to the public domain or available under CC0 1.0 Universal where applicable.

---

**Thank you for helping build the Global Knowledge Commons!**
