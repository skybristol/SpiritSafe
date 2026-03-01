# Office Held by Head of State

**Profile version:** 1.0.0  
**Status:** Stable  
**Maintainer:** Sky Bristol

---

## What is this entity?

An Office Held by Head of State is a governmental position or office that serves as the executive leadership role for a political entity. This includes presidencies, chieftainships, chairpersonships, and other titles that designate the head of state or head of government.

This profile is designed to represent the **office itself** as an abstract entity, not the individual people who hold the office over time. For example, "Principal Chief of the Cherokee Nation" is an office that has been held by different individuals throughout history.

This profile provides structure for documenting:

- The formal title and nomenclature of the office
- The jurisdiction the office administers
- The country in which the office exists
- The date the office was established
- Classification of the office type

---

## When to use this profile

Use the **OfficeHeldByHeadOfState** profile when creating or editing Wikidata items for:

- **Executive governmental offices** such as presidencies, chieftainships, or chairpersonships
- **Tribal government leadership positions** (e.g., "Principal Chief of the Cherokee Nation")
- **Head of state or head of government positions** for any political entity
- **Offices that are referenced by other entities** via P1906 (office held by head of state) or similar properties

**Do NOT use this profile for:**

- Individual people who hold or have held these offices (use biographical profiles instead)
- Legislative or judicial positions
- Non-governmental leadership roles
- Honorary or ceremonial titles without governing authority

---

## Key Statements

This profile defines the following primary properties:

### Classification and Context

- **Instance of (P31)**: Type of office (e.g., Q294414 "public office", Q4164871 "position")
- **Country (P17)**: The country where this office exists
- **Applies to jurisdiction (P1001)**: The governmental entity this office administers

### History

- **Inception (P571)**: Date when the office was established or created

---

## Example Entities

The following Wikidata items represent the types of entities this profile is designed for:

- **President of the United States**: [Q11696](https://www.wikidata.org/wiki/Q11696)
- **Principal Chief of the Cherokee Nation**: Would be created using this profile
- **President of the Navajo Nation**: Would be created using this profile

*(Note: Some example items may not yet exist or may not fully conform to this profile)*

---

## Statement Details and Guidance

### Instance of (P31)

**Type**: Item

**Typical values**:

- Q294414 (public office)
- Q4164871 (position)
- Other relevant classification items

**Guidance**: Choose the most specific and appropriate classification for the office type. Multiple instance-of classifications may be appropriate.

**References required**: At least one source documenting the office classification.

**Validation policy**: `allow_existing_nonconforming` — Existing items may have additional P31 values.

---

### Country (P17)

**Type**: Item

**Typical values**:

- Q30 (United States of America) — for tribal government offices in the U.S.
- Other country items as appropriate

**Max count**: 1

**Guidance**: This indicates the country in which the office exists, not necessarily the jurisdiction it administers. For tribal government offices in the United States, always use Q30.

**References required**: At least one source establishing the office's national context.

---

### Applies to Jurisdiction (P1001)

**Type**: Item

**Max count**: 1

**Guidance**: 

- Link to the governmental entity this office serves
- For "Principal Chief of the Cherokee Nation", this would link to the Cherokee Nation item
- This property establishes the relationship between the office and the political entity it governs
- The jurisdiction item should typically use a governmental entity profile (e.g., `TribalGovernmentUS`)

**References required**: At least one source documenting the office's jurisdiction.

---

### Inception (P571)

**Type**: Time

**Precision**: Auto-derived from input format

- `YYYY` → year precision
- `YYYY-MM` → month precision
- `YYYY-MM-DD` → day precision

**Calendar model**: Gregorian calendar (default)

**Guidance**:

- Use the date when the office was formally established
- For offices with complex constitutional or historical evolution, use the date of the most recent formal establishment or reorganization
- If the exact date is unknown, use year or year-month precision as appropriate
- Consult constitutional documents, tribal codes, or official government records

**References required**: At least one source documenting the office establishment date.

---

## Integration with Other Profiles

This profile is designed to work in conjunction with:

### TribalGovernmentUS

Tribal government entities use P1906 (office held by head of state) to reference items created with this profile. The relationship is:

```
Cherokee Nation (TribalGovernmentUS)
  └─ P1906: office held by head of state
      └─ Principal Chief of the Cherokee Nation (OfficeHeldByHeadOfState)
          └─ P1001: applies to jurisdiction
              └─ Cherokee Nation
```

This creates a clear bidirectional linkage between the governmental entity and its executive office.

---

## Known Issues and Limitations

- **Sitelinks**: Currently configured for English Wikipedia only
- **Temporal scope**: No explicit support yet for offices that have been abolished or reorganized
- **Qualifiers**: No qualifier properties currently defined; future versions may add support for term length, appointment method, etc.

---

## Future Enhancements

Planned additions for future versions:

- Properties for term length and term limits
- Properties for appointment or election method
- Support for office reorganizations and name changes
- Enhanced support for historical offices that no longer exist
- Integration with properties for current officeholders (P35, P6)

---

## Contributing

To propose changes to this profile:

1. **Fork** the SpiritSafe repository
2. **Create a feature branch**: `git checkout -b profile/office-update`
3. **Edit** `profiles/OfficeHeldByHeadOfState/profile.yaml` and update this README accordingly
4. **Update** `CHANGELOG.md` with a description of your changes
5. **Increment version** in `metadata.yaml` following semantic versioning
6. **Submit a pull request** with a clear explanation of the proposed changes
7. **Await maintainer review** and address feedback

For questions or discussion, open an issue in the [SpiritSafe issue tracker](https://github.com/skybristol/SpiritSafe/issues).

---

## License

This profile is released under the same license as the SpiritSafe repository. Profile structure and documentation are dedicated to the public domain or available under CC0 1.0 Universal where applicable.
