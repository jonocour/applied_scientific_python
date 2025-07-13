TASK 05 – Semantic Versioning Changelog
=======================================

Goal:
-----
Create or update `CHANGELOG.md` following Semantic Versioning and bump your project version accordingly.

Instructions:
-------------
Complete the TODOs below:

```md
# TODO: Add "Unreleased" section in CHANGELOG.md
## [Unreleased]
- TODO: Add patch entry for bug fix
- TODO: Add minor entry for new feature
```

```diff
# TODO: Update version in setup.py or pyproject.toml
- version = "1.2.3"
+ version = "1.3.0"  # bump minor for the new feature
```

- TODO: Commit both updated `CHANGELOG.md` and version metadata file.

Hint:
-----
SemVer format is `MAJOR.MINOR.PATCH`. Patch for bug fixes; minor for backward-compatible features.

Advanced:
---------
Write a script to parse your changelog and auto-increment the version number.
