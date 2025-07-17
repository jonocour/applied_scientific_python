# Writing Effective `.gitlab-ci.yml` Pipelines

In this section, we'll learn how to create automated pipelines using GitLab CI/CD that can install dependencies, run tests, and deploy scientific tools in a reproducible manner.

---

## Why Use CI/CD in Scientific Code?

- **Consistency** across environments — code runs the same way every time  
- **Early detection** of errors before publication or deployment  
- **Reproducibility** and maintainability of research and tools  

---

## What is Twine?

**Twine** is a utility for securely uploading Python packages to repositories like [PyPI](https://pypi.org/) or [TestPyPI](https://test.pypi.org/).  
It handles authentication and package uploads, making it a standard tool in the Python packaging ecosystem.  

> You need to set `TWINE_USERNAME` and `TWINE_PASSWORD` as **CI/CD variables** in your GitLab project settings (Settings ➔ CI/CD ➔ Variables).  

---

## Basic Structure of `.gitlab-ci.yml`

```yaml
stages:
  - install    # Install project dependencies
  - test       # Run automated tests
  - deploy     # Package and deploy the project
```

---

## Example: A Simple CI/CD Pipeline

```yaml
# Define pipeline stages
stages:
  - install
  - test
  - deploy

# Step 1: Install Python dependencies
install_dependencies:
  stage: install
  image: python:3.10               # Base Python Docker image
  script:
    - python -m venv .venv         # Create a virtual environment
    - source .venv/bin/activate    # Activate the environment
    - pip install -r requirements.txt  # Install dependencies
  artifacts:
    paths:
      - .venv                      # Persist the virtual environment for other jobs

# Step 2: Run automated tests
run_tests:
  stage: test
  image: python:3.10
  script:
    - source .venv/bin/activate    # Activate the environment from artifacts
    - pytest tests/                # Execute tests with pytest
  dependencies:
    - install_dependencies          # Relies on the output of install_dependencies

# Step 3: Deploy the package (only on main branch)
deploy:
  stage: deploy
  image: python:3.10
  before_script:
    - pip install twine            # Install Twine for package upload
  script:
    - source .venv/bin/activate
    - python setup.py sdist bdist_wheel  # Build source and wheel distributions
    - twine upload dist/*                # Upload to PyPI or TestPyPI
  only:
    - main                         # Ensures deployment only happens on the main branch
  dependencies:
    - install_dependencies
  variables:
    TWINE_USERNAME: $TWINE_USERNAME
    TWINE_PASSWORD: $TWINE_PASSWORD
```

---

## Why Use Artifacts and Dependencies?

- **Artifacts** allow jobs to share files, like a virtual environment or built packages, between pipeline stages.  
- **Dependencies** ensure a job waits for previous jobs and retrieves required artifacts.  
- In GitLab CI, each job runs in isolation, so artifacts and dependencies are essential for pipeline coordination.  

---

## Summary

This example pipeline:  

1. Sets up a **Python virtual environment** and installs dependencies  
2. **Runs tests** using `pytest`  
3. **Builds and deploys** the package only when code is pushed to the `main` branch  

It demonstrates good practices for CI/CD in Python projects and introduces you to critical tools like **Twine** for secure deployments.  

---

## Reminder for Students:

- Make sure **GitLab CI/CD Variables** for `TWINE_USERNAME` and `TWINE_PASSWORD` are set.  
- Deployment will only occur when changes are pushed to the `main` branch — a safeguard to prevent accidental releases.  
