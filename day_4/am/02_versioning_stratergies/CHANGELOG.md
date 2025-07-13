# Changelog
This is an example **Changelog** for for the applied_scientific_python repo.
All notable changes to **pipeline** will be documented in this file.  

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- Latest -->

## [1.2.0] – 2025-07-13
### Added
- **Cython acceleration module** (`cy_fastmath`) for heavy numerical loops.
- **Automatic version tagging** in GitLab CI: release tags are now created when the pipeline passes on `main`.
- `docs/performance.md` with benchmark tables and usage tips.

### Changed
- Default NumPy dtype promoted from `float32` ➜ `float64` to avoid underflow in edge cases.

### Fixed
- Bug in `stats.average_measurement()` where zero-length inputs raised an unhelpful `ZeroDivisionError`; now returns `np.nan` and logs a warning.
- CI pipeline now caches wheels correctly, shaving ~40 s from builds.

### Deprecated
- `analysis.quick_histogram()` — will be removed in **2.0.0**; use `viz.plot_histogram()` instead.

---

## [1.1.1] – 2025-06-18
### Fixed
- Typo in README install command (`pip3` → `pip`).
- Incorrect unit conversion in `units.to_mpa()` for US customary inputs in`psi`.

---

## [1.1.0] – 2025-05-30
### Added
- **Pandas I/O utilities** (`io.to_parquet` / `io.from_parquet`) for faster data storage.
- Example notebooks under `examples/` with real lab data.

### Changed
- Tightened tolerance in `calibration.curve_fit()` (r² threshold 0.95 → 0.98).

---

## [1.0.0] – 2025-05-01
### Added
- First stable release: core ORM, analysis, and plotting modules.
- GitLab CI with test and lint stages.
- MIT License and comprehensive README.

---

## [0.5.0] – 2025-03-15
### Added
- Initial prototype for internal lab use.

### Security
- Configured Dependabot to scan for vulnerable dependencies weekly.

