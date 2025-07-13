TASK 07 – Write & Run Pytest in CI
==================================

Goal:
-----
Add pytest tests to your codebase and integrate them into your GitLab CI pipeline.

Instructions:
-------------
Complete the TODOs below:

```python
# tests/test_happy_path.py
# TODO: Write a happy-path pytest function
def test_add_positive():
    from mypkg.math_utils import add
    assert add(2, 3) == 5
```

```python
# tests/test_error_path.py
# TODO: Write an error-path pytest function
import pytest
from mypkg.math_utils import divide

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

```yaml
# .gitlab-ci.yml snippet
# TODO: Configure run_pytest job
run_pytest:
  image: python:3.10
  script:
    - pip install pytest
    - pytest --maxfail=1 --disable-warnings --junitxml=pytest-report.xml
  artifacts:
    when: always
    reports:
      junit: pytest-report.xml
```

- TODO: Push to a feature branch and confirm the CI pipeline shows pass/fail status.

Hint:
-----
Use `--junitxml` to generate a test report that GitLab can parse.

Advanced:
---------
Add `pytest-cov` to measure coverage and enforce a minimum threshold in CI.
