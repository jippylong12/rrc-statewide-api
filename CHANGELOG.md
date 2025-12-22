# Changelog

## [1.0.1] - 2025-12-22
### Added
- Exposed `fields` property via `parser.get_fields()` to list all DBF column names.
- Patch release bump.

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-12-22
### Added
- **Initial Release**: Supported standard `.dbf` parsing for RRC Statewide API data.
- `RRCStatewideParser`: Wrapper around `dbfread` with field name normalization.
- Utilities: Date normalization (YYYYMMDD) and API number construction.
- Tested against real RRC data (`api329.dbf`).
