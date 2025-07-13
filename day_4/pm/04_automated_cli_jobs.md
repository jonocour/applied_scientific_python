# Automated CI Jobs: Testing & Deployment

This guide focuses on automating test execution (`pytest`, `unittest`) and deploying packages via GitLab CI/CD—without redefining global stages.

---

## 1. Automated Running of Tests

### Pytest

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
   pytest \
     --maxfail=1 \
     --disable-warnings \
     --junitxml=report_pytest.xml \
     --cov=mypkg --cov-report=xml
   ```

#### CI Job Snippet for Pytest

```yaml
run_pytest:
  image: python:3.10
  script:
    - pip install -r requirements-dev.txt     # includes pytest, pytest-cov
    - pytest --maxfail=1 --disable-warnings \
        --junitxml=report_pytest.xml \
        --cov=mypkg --cov-report=xml
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

---

### unittest

1. **Use `unittest`** for simple or legacy tests:
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

### Packaging

- **Legacy**:  
  ```bash
  python setup.py sdist bdist_wheel
  ```
- **PEP 517/518**:  
  ```bash
  pip install build
  python -m build
  ```

### CI Job for Deployment

```yaml
deploy_package:
  image: python:3.10
  before_script:
    - pip install twine
  script:
    - python -m build                       # build both sdist and wheel
    - twine upload dist/*                   # uses $TWINE_USERNAME and $TWINE_PASSWORD
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

- Use **`python -m build`** for modern packaging.
- Ensure **secure variables** in GitLab CI/CD settings.
- **Cache pip** to speed up repeated builds.

---

## Summary

- **Pytest & unittest**: automatable with JUnit/coverage reports.
- **CI snippets**: Focus on test execution, reporting, and artifact persistence.
- **Deployment**: Modern packaging + Twine, leveraging cached dependencies.
