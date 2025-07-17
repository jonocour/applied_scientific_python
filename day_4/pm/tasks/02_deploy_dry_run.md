# TASK 02 – Deploy a Dry-Run to TestPyPI or GitLab Package Registry

## Goal
Configure CI/CD to perform a “dry-run” deployment of your Python package to a **non-production registry** (TestPyPI or GitLab Package Registry) and validate your build process.

---

## Your Options
You can choose to configure **either**:
- **GitLab CI/CD** (`.gitlab-ci.yml`)  
- **GitHub Actions** (`.github/workflows/`)  

Both pipelines must:
- Install your project’s dependencies (`pytest`, `SQLAlchemy`, `twine`, `build`)
- Build your package using `python -m build`
- Upload the built artifact to **TestPyPI** or **GitLab Package Registry**

---

## Required Tools in Your `requirements.txt` (or `requirements-dev.txt`)

```text
# Core Scientific Dependencies
sqlalchemy>=1.4

# Testing Tools
pytest>=7.0
pytest-cov>=4.0
coverage>=7.0

# Packaging & Deployment Tools
twine>=4.0
build>=1.0
setuptools>=78.1.1

# Optional (but useful for output/logging)
rich>=13.0
```

Ensure these are listed in your `requirements.txt` for the CI job to install.

---

## Sample CI Snippet for GitLab CI (Deploy to TestPyPI)

```yaml
deploy_test:
  image: python:3.10
  before_script:
    - pip install build twine pytest sqlalchemy
  script:
    - python -m build
    - twine upload dist/*         --repository-url "https://test.pypi.org/legacy/"         --username "$TWINE_USERNAME"         --password "$TWINE_PASSWORD"
  only:
    - ci-deploy-test
```

---

## Sample GitHub Actions Workflow (Deploy to TestPyPI)

```yaml
name: Deploy to TestPyPI

on:
  push:
    branches: [ ci-deploy-test ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install build twine pytest sqlalchemy

      - name: Build package
        run: python -m build

      - name: Upload to TestPyPI
        env:
          TWINE_USERNAME: ${{ secrets.TWINE_USERNAME }}
          TWINE_PASSWORD: ${{ secrets.TWINE_PASSWORD }}
        run: twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

---

## Validation Checklist

-  CI pipeline installs dependencies including `pytest`, `SQLAlchemy`, `twine`, and `build`  
-  Package builds successfully using `python -m build`  
-  Deployment job uploads package to **TestPyPI** or **GitLab Registry**  
-  `ci-deploy-test` branch is used for deployment testing  

---

## Advanced Challenge (Optional)

Add a downstream CI job that:  
- Installs your package from the registry  
- Imports a module or function  
- Runs a simple test (e.g., `pytest --maxfail=1`)  

---

## Reminder

- Store your **Twine credentials** securely in **CI/CD variables** or **GitHub Secrets**  
- Use **TestPyPI** for dry-run uploads before pushing to production PyPI