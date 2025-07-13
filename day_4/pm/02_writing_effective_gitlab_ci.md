# Writing Effective `.gitlab-ci.yml` Pipelines

In this section, we'll learn how to create automated pipelines using GitLab CI/CD that can install dependencies, run tests, and deploy scientific tools in a reproducible manner.

---

## Why Use CI/CD in Scientific Code?

- **Consistency** across environments
- **Early detection** of errors before publication
- **Reproducibility** and maintainability of research

---

## Basic Structure of `.gitlab-ci.yml`

```yaml
stages:
  - install    # Install project dependencies
  - test       # Run automated tests
  - deploy     # Package and deploy the project
```

---

## Example: A Simple Pipeline

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
      - .venv                      # Persist the virtual environment

# Step 2: Run automated tests
run_tests:
  stage: test
  image: python:3.10
  script:
    - source .venv/bin/activate    # Activate the environment
    - pytest tests/                # Execute tests with pytest
  dependencies:
    - install_dependencies          # Depends on the install_dependencies job

# Step 3: Deploy the package (only on main branch)
deploy:
  stage: deploy
  image: python:3.10
  before_script:
    - pip install twine            # Install Twine for package upload
  script:
    - source .venv/bin/activate
    - python setup.py sdist bdist_wheel  # Build source and wheel distributions
    - twine upload dist/*                # Upload to PyPI/TestPyPI
  only:
    - main                         # Run only on the main branch
  dependencies:
    - install_dependencies
  variables:
    TWINE_USERNAME: $TWINE_USERNAME
    TWINE_PASSWORD: $TWINE_PASSWORD
```

---

## Summary

This pipeline:

1. Sets up a **Python virtual environment** and installs dependencies  
2. **Runs tests** using `pytest`  
3. **Builds and deploys** the package on the `main` branch  
