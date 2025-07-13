TASK 08 – Deploy a Dry-Run to TestPyPI / GitLab Registry
========================================================

Goal:
-----
Configure CI to perform a “dry-run” deployment to a non-production Python registry and validate your package.

Instructions:
-------------
Complete the TODOs below:

```yaml
# .gitlab-ci.yml snippet for TestPyPI
# TODO: Create deploy_test job targeting TestPyPI
deploy_test:
  image: python:3.10
  before_script:
    - pip install build twine
  script:
    - python -m build
    - twine upload dist/* \
        --repository-url "https://test.pypi.org/legacy/" \
        --username "$TWINE_USERNAME" \
        --password "$TWINE_PASSWORD"
  only:
    - ci-deploy-test
```

```yaml
# .gitlab-ci.yml snippet for GitLab Package Registry
# TODO: Create deploy_to_gitlab job targeting GitLab Registry
deploy_to_gitlab:
  image: python:3.10
  before_script:
    - pip install build twine
  script:
    - python -m build
    - twine upload dist/* \
        --repository-url "$CI_API_V4_URL/projects/$CI_PROJECT_ID/packages/pypi" \
        --username "gitlab-ci-token" \
        --password "$CI_JOB_TOKEN"
  only:
    - ci-deploy-test
```

- TODO: Merge `ci-deploy-test` into `main` and confirm your artifact appears in the chosen registry.

Hint:
-----
TestPyPI upload URL: `https://test.pypi.org/legacy/`

Advanced:
---------
Add a downstream CI job that installs your test package from the registry and verifies import.
