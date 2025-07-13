Reference Sheet
=============================

Semantic Versioning for Scientific Python Projects
--------------------------------------------------
Use format:

MAJOR.MINOR.PATCH

E.G: 1.2.0

What is SemVer?
---------------
A structured versioning system that clearly communicates:
- What changed
- Whether it's safe to upgrade
- If results or interfaces may break

Format:
    MAJOR – Breaking changes (API or output)
    MINOR – New features, non-breaking
    PATCH – Bug fixes, tweaks, documentation

--------------------------------------------------

Examples
--------

| Version | Description                                         |
|---------|-----------------------------------------------------|
| 1.0.0   | First stable release                                |
| 1.1.0   | Added a new data model or analysis helper           |
| 1.1.1   | Fixed a bug in a formula, no interface change       |
| 2.0.0   | Changed return structure or removed old method      |
| 2.1.0   | New visualization tools added                       |
| 2.1.1   | Minor optimizations, typos, docstring fixes         |

--------------------------------------------------

Scientific-Specific Guidance
----------------------------
 Breaking = Changing how users *interact* with the module  
“Different results” != breaking, unless the interface changes*

| Action                                              | Version bump |
|-----------------------------------------------------|--------------|
| Changed output format (e.g. dict → DataFrame)       | MAJOR        |
| Renamed or deleted public function/class            | MAJOR        |
| Changed default behavior/thresholds                 | MINOR        |
| Improved performance (same output)                  | PATCH        |
| Fixed math bug that alters results                  | MINOR (or PATCH w/ warning) |

--------------------------------------------------

Practical Steps
---------------

In your `setup.py` or `__init__.py`:
```python
__version__ = "1.2.0"
