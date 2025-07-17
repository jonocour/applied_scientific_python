# Automated CI Jobs: Testing & Deployment

This guide focuses on automating test execution (`pytest`, `unittest`) and deploying packages via GitLab CI/CD—without redefining global stages.

---

## Why Automate Testing and Deployment Together?

Automating both ensures your code is validated before it reaches users — reducing risks of bugs or packaging errors slipping through.  
CI/CD helps maintain reproducibility, consistency, and reliable collaboration within scientific projects.

---

## 1. Automated Running of Tests

### Pytest

#### When to Use:
- Recommended for new projects or detailed feature testing  
- Rich plugin ecosystem and better assertion introspection  

1. **Install pytest and plugins**:
   ```bash
   pip install pytest pytest-cov
   ```

2. **Write tests** under `tests/`, e.g.:
   ```python
   # tests/test_example.py
   import pytest
   from mypkg import math_utils

   def test_add():
       assert math_utils.add(1, 2) == 3

   def test_divide_by_zero():
       with pytest.raises(ZeroDivisionError):
           math_utils.divide(1, 0)
   ```

3. **Run pytest** with coverage and JUnit reporting:
   ```bash
   pytest      --maxfail=1      --disable-warnings      --junitxml=report_pytest.xml      --cov=mypkg --cov-report=xml
   ```

#### CI Job Snippet for Pytest

```yaml
run_pytest:
  image: python:3.10
  script:
    - pip install -r requirements-dev.txt     # includes pytest, pytest-cov
    - pytest --maxfail=1 --disable-warnings         --junitxml=report_pytest.xml         --cov=mypkg --cov-report=xml
  artifacts:
    when: always
    reports:
      junit: report_pytest.xml               # GitLab UI test report
    paths:
      - report_pytest.xml                    # Persist report
      - coverage.xml                         # Coverage report
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - .cache/pip                           # Speed up pip install
```

*Artifacts allow sharing reports between stages/jobs and visualization in GitLab UI.*

---

### unittest

#### When to Use:
- Suitable for legacy code or projects already using unittest  
- Good for quick checks or simple unit tests  

1. **Write `unittest` tests**:
   ```python
   # tests/test_example_unittest.py
   import unittest
   from Calculator import add, div

   class CalculatorTests(unittest.TestCase):
       def test_add(self):
           self.assertEqual(add(2, 3), 5)

       def test_divide_by_zero(self):
           with self.assertRaises(ZeroDivisionError):
               div(1, 0)

   if __name__ == '__main__':
       unittest.main()
   ```

2. **Run tests** and generate XML report:
   ```bash
   python -m unittest discover -v --buffer > report_unittest.txt
   # For JUnit XML, install xmlrunner:
   pip install unittest-xml-reporting
   python -m xmlrunner discover -v --output test-reports
   ```

#### CI Job Snippet for unittest

```yaml
run_unittest:
  image: python:3.10
  script:
    - pip install -r requirements-dev.txt     # includes xmlrunner if needed
    - python -m xmlrunner discover -v --output test-reports
  artifacts:
    when: always
    reports:
      junit: test-reports/*.xml              # GitLab UI test report
    paths:
      - test-reports/                        # Persist XML reports
```

---

## 2. Deploying from GitLab CI: Packaging & Distribution

### Packaging Options

- **Legacy:**  
  ```bash
  python setup.py sdist bdist_wheel
  ```

- **Recommended Modern Approach (PEP 517/518):**  
  ```bash
  pip install build
  python -m build
  ```

---

### Deployment CI Job Example

```yaml
deploy_package:
  image: python:3.10
  before_script:
    - pip install twine
  script:
    - python -m build                       # Build both sdist and wheel
    - twine upload dist/*                   # Upload using secure credentials
  only:
    - main
  variables:
    TWINE_USERNAME: $TWINE_USERNAME
    TWINE_PASSWORD: $TWINE_PASSWORD
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - .cache/pip
```

- Use **`python -m build`** for modern Python packaging  
- Use **TestPyPI** first for testing uploads:  
  ```bash
  twine upload --repository testpypi dist/*
  ```
- Always use **CI/CD Variables** for secrets  
- Cache pip to speed up installations in repeated builds  

---

## Final Checklist

Tests run automatically on every push or merge request  
Test reports and coverage collected and visualized in GitLab CI/CD  
Deployment triggered only after successful tests on the `main` branch  
Sensitive credentials stored securely in CI/CD variables  
Builds optimized with caching for efficiency  
Use of TestPyPI for deployment dry-runs before live deployment  

---

## Summary

By automating testing and deployment, you gain confidence in your software quality, streamline your release process, and maintain reproducibility across environments.  
CI/CD allows you to detect problems early, automate routine tasks, and ensure your scientific code is reliable and maintainable.
