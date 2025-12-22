# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-12-22
### Changed
- Reverted to standard `.dbf` parsing using `dbfread`.
- Renamed parser back to `RRCStatewideParser`.
- Removed `MAF016Parser` and fixed-width logic as input is confirmed to be DBF.

### Added
- `RRCStatewideParser` using `dbfread`.
- Date normalization for RRC format strings.
- Initial project structure.
