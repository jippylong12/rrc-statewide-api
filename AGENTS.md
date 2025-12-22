# AGENTS.md

## Project Goal
Create a python module `rrc-statewide-api` to parse and process the Texas Railroad Commission (RRC) **Statewide API Data** provided in dBase (`.dbf`) format.

## Context
- **Format**: dBase III/IV (`.dbf`) Binary format.
- **Source**: RRC "Statewide API Data" download (GIS/Mapping dataset).
- **Core Dependencies**: `dbfread` for binary parsing.
- **Structure**: Record-based attribute tables linking API numbers to Lease IDs, Districts, and Counties.
- **Parser Class**: `RRCStatewideParser` in `src/rrc_statewide_api`.

## Key Files
- `src/rrc_statewide_api/parser.py`: Core logic for reading DBF records and handling RRC-specific data types.
- `src/rrc_statewide_api/utils.py`: Helpers for formatting Lease IDs (padding) and District codes.
- `tests/test_parser.py`: Unit tests using sample DBF fragments.

## Development Status
- **[NEW]** Project structure initialized as `rrc-statewide-api`.
- **[NEW]** `dbfread` integration established for handling binary `.dbf` streams.
- **[NEW]** Logic implemented to handle `ISO-8859-1` encoding for character support in Survey/Lease names.
- **[NEW]** Standardized mapping for `API_NUM`, `LEASE_NUM`, and `DISTRICT` fields.
- **[NEW]** Implementation of leading-zero padding for Oil (5-digit) and Gas (6-digit) Lease IDs.
- **[NEW]** Testing infrastructure set up with `pytest` and `tests/data` directory.

## Post-Round Maintenance
After each development round, the agent MUST:
1.  **Update `AGENTS.md`**: Reflect new capabilities and current status.
2.  **Update `README.md`**: Ensure documentation matches new features.
3.  **Update `CHANGELOG.md`**: Record changes under a new version.
4.  **Verify Field Names**: Ensure compatibility with RRC's headers (e.g., handling both `LEASE_NUM` and `LEASE_ID`).
5.  **Bump Version**: Increment the minor version in `pyproject.toml`.