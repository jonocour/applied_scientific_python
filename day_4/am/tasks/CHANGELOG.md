# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- _(leave this here for next sprint’s feature entries)_

### Fixed
- _(leave this here for next sprint’s bug‑fix entries)_

### Changed
- _(leave this here for next sprint’s breaking/non‑breaking updates)_

---

## [0.2.0] – 2025‑07‑16

### Added
- Export processed data as JSON files for easier downstream analysis  
  _(ensures flexibility in data pipelines)_

### Fixed
- Corrected rounding error in `standard_deviation()` function (was truncating `.999` → `0.99`)  
  _(improves accuracy of statistical summaries)_

### Changed
- Refactored `plotting.py` to Matplotlib 4.0 API (updated axes object return patterns)  
  _(maintains compatibility with latest plotting features)_

> **Rationale:** Bumped to **0.2.0** because we’ve added new JSON export functionality (minor feature) and performed a non‑breaking API refactor.

---

## [0.1.0] – 2025‑06‑01

### Added
- Initial release with basic data‑processing functions:  
  - CSV import/export  
  - Mean and standard‑deviation calculations  

