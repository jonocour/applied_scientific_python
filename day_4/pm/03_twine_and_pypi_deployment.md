# Twine & PyPI Deployment

In this guide, we'll dive deep into using Twine within GitLab CI to publish your Python packages.

---

## 1. Why Twine?

- Standard tool for uploading **Source Distributions (SDist)** and **Wheel** packages  
- Validates metadata before upload to catch common packaging errors  
- Handles retries, secure TLS connections, and authentication  
- Recommended by the Python Packaging Authority (PyPA)  

---

## 2. Understanding Package Types

- **SDist (Source Distribution):** The original source code packaged for distribution  
- **Wheel:** A pre-built, binary-compatible Python package (faster to install)  

---

## 3. Setting Up Secrets

To authenticate securely during deployment:

1. Go to **Settings → CI/CD → Variables** in your GitLab project  
2. Add the following variables (mark them **masked** and **protected**):  
   - `TWINE_USERNAME` — often `__token__` if using PyPI tokens  
   - `TWINE_PASSWORD` or `TWINE_TOKEN` — your PyPI API token or GitLab token  

Example in `.gitlab-ci.yml`:

```yaml
variables:
  TWINE_USERNAME: $TWINE_USERNAME
  TWINE_PASSWORD: $TWINE_PASSWORD
```

---

## 4. Deployment to PyPI with Twine

Recommended pipeline step to upload a validated package:

```yaml
deploy_to_pypi:
  stage: deploy
  image: python:3.10
  before_script:
    - pip install twine
  script:
    - python setup.py sdist bdist_wheel
    - twine check dist/*                 # Optional: Validate metadata before upload
    - twine upload dist/*                # Upload to PyPI
  only:
    - main
```

---

## 5. Using GitLab Package Registry

Instead of PyPI, you can publish your package directly to **GitLab’s built-in Python Package Registry** using the CI Job Token:

```yaml
deploy_to_gitlab_registry:
  stage: deploy
  image: python:3.10
  before_script:
    - pip install twine
  script:
    - python setup.py sdist bdist_wheel
    - twine check dist/*
    - |
      twine upload dist/*         --repository-url "$CI_API_V4_URL/projects/$CI_PROJECT_ID/packages/pypi"         --username "gitlab-ci-token"         --password "$CI_JOB_TOKEN"
  only:
    - main
```

### What do these variables mean?
- `$CI_API_V4_URL` — The GitLab API endpoint for your instance  
- `$CI_PROJECT_ID` — The unique ID of your project in GitLab  
- `$CI_JOB_TOKEN` — An auto-generated token that grants CI jobs permissions to upload artifacts  

---

## 6. Best Practices

- Always validate your packages with `twine check` before uploading  
- Keep your PyPI or GitLab credentials secret — never hardcode them in the repo  
- Use protected variables and deploy only on protected branches (like `main`)  
- Monitor upload logs for success or failure messages  

---

## Summary

Twine is your gateway to publishing Python packages securely and reliably.  
With GitLab CI, you can automate both PyPI and GitLab Package Registry deployments as part of your continuous delivery pipeline.  
This ensures that your scientific tools are always packaged, tested, and ready for the community or your team.
