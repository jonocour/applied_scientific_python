
# TASK 07 – Write and Run Pytest in GitLab CI

## Goal:
Add pytest tests to your codebase and integrate them into your GitLab CI pipeline.

---

## Instructions:

### 1. Write Your Tests

Note: `mypkg` and `math_utils` are example names. Replace them with your actual package and module names.

**`tests/test_happy_path.py`**
```python
# Example of a happy-path pytest function
def test_add_positive():
    from mypkg.math_utils import add  # Replace with your actual package and module
    assert add(2, 3) == 5
```

**`tests/test_error_path.py`**
```python
# Example of an error-path pytest function
import pytest
from mypkg.math_utils import divide  # Replace with your actual package and module

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

---

### 2. Configure Your GitLab CI Job

**`.gitlab-ci.yml` Example**
```yaml
run_pytest:
  image: python:3.10
  script:
    - pip install pytest
    - pytest --maxfail=1 --disable-warnings
```

This configuration will:
- Install `pytest`
- Run all tests in your repository
- Output test results directly to the GitLab CI job logs
- Pass the pipeline if all tests succeed, fail it if any tests fail

---

### 3. Push and Validate

- Push your changes to a feature branch in your GitLab repository
- Check the CI pipeline logs in GitLab to confirm the tests ran and passed

Pipeline outcomes:
- Green pipeline: Tests passed successfully
- Red pipeline: One or more tests failed

---

## Optional Advanced Challenge

- Install `pytest-cov` to measure code coverage
- Add coverage enforcement in CI with `--cov=mypkg --cov-fail-under=80`

---

## You Are Done

Your tests are now automated with CI — ensuring continuous feedback every time you push code.
