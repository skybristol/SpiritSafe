# Federally Recognized Tribe

**Profile version:** 1.0.0  
**Status:** Stable  
**Maintainer:** Sky Bristol

---

## What is this entity?

A Federally Recognized Tribe is a Native American tribe formally recognized by the United States Bureau of Indian Affairs (BIA) under the authority of the Secretary of the Interior. Federal recognition establishes a government-to-government relationship between the United States and the tribe, granting the tribe certain rights, privileges, and responsibilities including sovereignty over tribal lands, eligibility for federal services, and authority to govern tribal affairs.

This profile provides a comprehensive structure for representing federally recognized tribes in Wikidata, focusing on:

- Official tribal nomenclature and native names
- Federal recognition documentation and references
- Governmental structure and leadership
- Geographic location and territorial information
- Cultural and linguistic attributes
- Integration with OpenStreetMap territorial data
- Sitelinks to Wikipedia and other knowledge platforms

---

## When to use this profile

Use the **TribalGovernmentUS** profile when creating or editing Wikidata items for:

- **A specific federally recognized Native American tribe** currently recognized by the United States Bureau of Indian Affairs
- Tribes that appear on the official BIA list published annually in the Federal Register

**Do NOT use this profile for:**

- Historical tribes that pre-date federal recognition systems
- State-recognized tribes that lack federal recognition
- Tribal subdivisions, bands, or clans (unless they have independent federal recognition)
- Indigenous peoples or nations outside the United States
- Individual tribal members or tribal government officials

---

## Key Statements

This profile defines the following primary properties:

### Required/Core Statements

- **Instance of (P31)**: Fixed to Q7840353 (federally recognized Native American tribe in the United States)
  - Must reference a Federal Register notice as source

### Identity and Nomenclature

- **Native name (P1705)**: Native language name(s) with language qualifiers
- **Aliases**: Alternative names including official U.S. government designations

### Government and Administration

- **Office held by head of state (P1906)**: The governmental position (e.g., "Principal Chief")
  - Links to `OfficeHeldByHeadOfState` profile
- **Official website (P856)**: Tribal government website
- **Headquarters location (P159)**: Physical address with qualifiers for street address, postal code, and coordinates

### Demographics and History

- **Member count (P2124)**: Tribal enrollment numbers with point-in-time qualifiers
- **Inception (P571)**: Date of formal federal recognition or establishment

### Geographic and External Identifiers

- **OpenStreetMap relation ID (P402)**: Link to OSM territorial boundaries
- **Flag image (P41)**: Tribal flag from Wikimedia Commons

### Sitelinks

- English Wikipedia article connection with validation for uniqueness

---

## Example Entities

The following Wikidata items exemplify proper use of this profile:

- **Cherokee Nation**: [Q5093](https://www.wikidata.org/wiki/Q5093)
- **Navajo Nation**: [Q13310](https://www.wikidata.org/wiki/Q13310)

*(Note: These items may not yet fully conform to this profile but represent the entity types this profile is designed for)*

---

## Statement Details and Guidance

### Instance of (P31)

**Fixed value**: Q7840353 (federally recognized Native American tribe in the United States)

**References required**: At least one Federal Register notice that lists the tribe as federally recognized. The profile provides a SPARQL-driven list of suitable reference items representing annual Federal Register publications.

**Validation policy**: `allow_existing_nonconforming` — Existing items may have additional P31 values; this profile adds/validates the primary classification.

---

### Official Website (P856)

**Behavior**: `auto_derive` references — The profile automatically generates a reference URL (P854) from the statement value

**Qualifiers**: Language of work (P407) is fixed to Q1860 (English)

**Guidance**: Prefer the official tribal government website (`.gov` or tribally-controlled domains). Verify the website is current and actively maintained.

---

### Native Name (P1705)

**Type**: Monolingual text (requires language code)

**Qualifiers**: Language of work or name (P407) to specify the language

**Guidance**: 

- Use the tribe's preferred self-designation in their native language(s)
- Consult tribal language preservation resources or official tribal communications
- Multiple native names may be appropriate if the tribe uses multiple languages
- Language choices are populated from a SPARQL-driven list of Wikidata language items

---

### Headquarters Location (P159)

**Type**: Item (Wikidata location item)

**Qualifiers**:

- **Street address (P6375)**: Monolingual text (typically English)
- **Postal code (P281)**: String
- **Coordinate location (P625)**: Globe coordinate with building-to-city level precision

**Guidance**: 

- Use the official administrative offices of the tribal government
- Precision should be appropriate (building-level for specific addresses, city-level if exact location is sensitive or not publicly documented)
- Respect tribal privacy considerations; do not include restricted information

---

### Member Count (P2124)

**Type**: Quantity (integer-only constraint)

**Qualifiers**: Point in time (P585) — Date the count applies to

**References required**: Official tribal enrollment reports or census data

**Guidance**:

- Member count should reflect official tribal enrollment, not population estimates
- Include the point-in-time qualifier to provide temporal context
- Update when new official enrollment data becomes available
- Be aware that enrollment criteria vary by tribe (blood quantum, descent, etc.)

---

### OpenStreetMap Relation ID (P402)

**Type**: External identifier (numeric format)

**Validation**: Profile validates that the relation exists on OpenStreetMap

**Guidance**:

- Link to OSM relation representing tribal territorial boundaries or reservation lands
- Ensure the OSM relation is properly tagged and maintained
- Consider contributing to OSM if tribal boundaries are not yet mapped

---

### Office Held by Head of State (P1906)

**Type**: Item (links to entity using `OfficeHeldByHeadOfState` profile)

**Form policy**: `target_only` — Curators are directed to create/edit the office item separately

**Guidance**: 

- This property references the **office itself**, not the current officeholder
- Examples: "Principal Chief of the Cherokee Nation", "President of the Navajo Nation"
- The office item should use the `OfficeHeldByHeadOfState` profile
- Use P35 (head of state) to link to individual persons holding this office over time

---

## SPARQL-Driven Choice Lists

This profile uses the following SPARQL queries to populate controlled vocabularies:

1. **bia_federal_register_issues.sparql**: Federal Register notices for instance-of references
2. **wikidata_language_items_en.sparql**: Language items for native name qualifiers

These queries are executed during cache hydration and provide current, validated choice lists for form generation and validation.

---

## Known Issues and Limitations

- **Sitelinks**: Currently support English Wikipedia only; future versions may expand to other language editions
- **Geographic coordinates**: Precision constraints are defined but may need adjustment based on tribal privacy policies
- **Tribal subdivisions**: No explicit support for bands, clans, or subdivisions yet

---

## Future Enhancements

Planned additions for future versions:

- Support for historical tribal names and reorganizations
- Properties for treaty relationships and land cessions
- Enhanced support for tribal language and cultural heritage attributes
- Integration with additional external identifiers (Library of Congress, tribal catalogs)

---

## Contributing

To propose changes to this profile:

1. **Fork** the SpiritSafe repository
2. **Create a feature branch**: `git checkout -b profile/tribal-government-update`
3. **Edit** `profiles/TribalGovernmentUS/profile.yaml` and update this README accordingly
4. **Update** `CHANGELOG.md` with a description of your changes
5. **Increment version** in `metadata.yaml` following semantic versioning
6. **Submit a pull request** with a clear explanation of the proposed changes
7. **Await maintainer review** and address feedback

For questions or discussion, open an issue in the [SpiritSafe issue tracker](https://github.com/skybristol/SpiritSafe/issues).

---

## License

This profile is released under the same license as the SpiritSafe repository. Profile structure and documentation are dedicated to the public domain or available under CC0 1.0 Universal where applicable.
