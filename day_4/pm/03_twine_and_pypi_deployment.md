# Twine & PyPI Deployment

In this guide, we'll dive deep into using Twine within GitLab CI to publish your Python packages.

---

## 1. Why Twine?

- Standard tool for uploading SDist and Wheel  
- Validates metadata, handles retries, TLS, etc.

---

## 2. Setting Up Secrets

1. Go to **Settings → CI/CD → Variables**  
2. Add:
   - `TWINE_USERNAME`, masked & protected  
   - `TWINE_PASSWORD` (or `TWINE_TOKEN`)  

Example in `.gitlab-ci.yml`:

```yaml
variables:
  TWINE_USERNAME: $TWINE_USERNAME
  TWINE_PASSWORD: $TWINE_PASSWORD
```

## 3. Using GitLab Package Registry

Instead of PyPI, you can publish your package directly to GitLab’s built-in Python Package Registry using the `CI_JOB_TOKEN`:

```yaml
deploy_to_gitlab_registry:
  stage: deploy
  image: python:3.10
  before_script:
    - pip install twine
  script:
    - python setup.py sdist bdist_wheel
    - |
      twine upload dist/* \
        --repository-url "$CI_API_V4_URL/projects/$CI_PROJECT_ID/packages/pypi" \
        --username "gitlab-ci-token" \
        --password "$CI_JOB_TOKEN"
  only:
    - main
