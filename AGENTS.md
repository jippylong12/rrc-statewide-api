# AGENTS.md

## Project Goal
Create a python module `rrc-statewide-api` to parse and process the Texas Railroad Commission (RRC) **Statewide API Data** provided in dBase (`.dbf`) format.

## Context
- **Format**: dBase III/IV (`.dbf`) Binary format (MAF016 derived).
- **Source**: RRC "Statewide API Data" download (GIS/Mapping dataset).
- **Core Dependencies**: `dbfread` for binary parsing.
- **Structure**: Record-based attribute tables linking API numbers to Lease IDs, Districts, and Counties.
- **Parser Class**: `RRCStatewideParser` in `src/rrc_statewide_api`.

## Key Files
- `src/rrc_statewide_api/parser.py`: Core logic for reading DBF records and handling RRC-specific data types.
- `src/rrc_statewide_api/utils.py`: Helpers for formatting Lease IDs (padding) and District codes.
- `tests/test_parser.py`: Unit tests using sample DBF fragments.

## Development Status
- **[RELEASE]** Version 1.0.0 released.
- **[NEW]** Confirmed support for DBF format using `api329.dbf` verification.
- **[NEW]** Tests passing with real data found in `tests/data/api329.dbf`.

## Post-Round Maintenance
After each development round, the agent MUST:
1.  **Update `AGENTS.md`**: Reflect new capabilities and current status.
2.  **Update `README.md`**: Ensure documentation matches new features.
3.  **Update `CHANGELOG.md`**: Record changes under a new version.
4.  **Verify Field Names**: Ensure compatibility with RRC's headers (e.g., handling both `LEASE_NUM` and `LEASE_ID`).
5.  **Bump Version**: Increment the minor version in `pyproject.toml`.