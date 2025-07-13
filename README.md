# Applied Scientific Python

A hands-on, 4-day intensive course for scientists, engineers, and analysts who want to write efficient, testable, and deployable scientific code in Python.

---

## Course Overview

This workshop bridges the gap between scientific scripts and engineering-quality software.

You'll learn how to:

- Write clean, idiomatic Python using `functools`, `itertools`, and the standard library
- Structure reusable scientific models using OOP and modules
- Manage experimental data with SQLAlchemy ORM
- Analyze and clean large datasets using pandas and NumPy
- Profile and optimize performance with Cython, multiprocessing, and vectorized techniques
- Debug and test with pytest, unittest, pdb, and traceback
- Build command-line tools using argparse and click
- Package and distribute Python tools (`setup.py`, metadata, editable installs)
- Automate testing and deployment using GitLab CI/CD pipelines

---

## Course Structure

Each day includes short lectures, live walkthroughs, and hands-on tasks.

| Day | Focus                                             |
|-----|---------------------------------------------------|
| 1   | [Pythonic Code, Testing & Debugging](#day-1)      |
| 2   | [Object-Oriented Programming & CLI Tools](#day-2) |
| 3   | [ORM, Performance Tuning & Pipelines](#day-3)     |
| 4   | [Packaging, CI/CD, and Deployment](#day-4)        |

---

## Daily Breakdown

### Day 1

**[AM – Python Refresher](day_1/am/)**  
Functions, generators, comprehensions, `functools`, `itertools`

- Tutorials: `01_recap.py`, `02_intro_to_functools.py`, `03_intro_to_itertools.py`
- Tasks: `tasks/01_recap_task.py`, `02_functools_task.py`, `03_itertools_task.py`

**[PM – Testing & Debugging](day_1/pm/)**  
pytest, unittest, traceback, pdb

- Tutorials: `01_intro_to_pytest.py`, `02_intro_to_unittest.py`, `03_debugging.py`
- Tasks: `tasks/01_pytest_task.py`, `02_unittest_task.py`, `03_debugging_tasks.py`

---

### Day 2

**[AM – OOP Essentials](day_2/am/)**  
OOP patterns, class composition, real-world abstractions

- Tutorials: `01_intro_to_oop.py`, `02_intro_to_abstraction.py`, `03_real_world_example_abstraction.py`
- Tasks: `tasks/01_oop_task.py`, `02_abstraction_task.py`, `03_inheritance_task.py`

**[PM – Command-Line Interfaces](day_2/pm/)**  
argparse, click, CLI tool packaging

- Tutorials: `01_python_and_cli.py`, `02_using_cli_tools.py`
- Tasks: `tasks/01_cli_tools_task.py`, `02_create_your_own.py`

---

### Day 3

**[AM – SQLAlchemy ORM](day_3/am/)**  
ORM modelling, relationships, querying patterns

- Tutorials: `01_intro_to_data_models.py`, `02_intro_to_sqlalchemy.py`, `03_intro_to_sqlalchemy_modelling.py`

**[PM – Performance Tuning](day_3/pm/)**  
Vectorization, multiprocessing, Cython, N+1 fixes

- Tutorials: `01_query_optermisation.py`, `02_pandas_cleaning_task.py`, `03_cython_multiprocessing.py`
- Tasks: `01_find_the_optermisation_task.py`, `02_using_pandas_task.py`

---
### Day 4

**[AM – Packaging & Versioning](day_4/am/)**  
_setup.py, requirements, semantic versioning_  

- **Tutorials:**  
  - `01_setup_recap/`  
  - `02_versioning_strategies/`  
  - `03_installation_strategies/`  
- **Tasks:**  
  - `01_semantic_versioning_changelog.md`  
  - `02_installation_strategy_comparison.md`  

**[PM – CI/CD with GitLab](day_4/pm/)**  
_.gitlab-ci.yml, test automation, publishing_  

- **Guides:**  
  - `02_writing_effective_gitlab_ci.md`  
  - `03_twine_and_pypi_deployment.md`  
  - `04_automated_cli_jobs.md`  
- **Tasks:**  
  - `01_write_and_run_pytest_ci.md`  
  - `02_deploy_dry_run.md`  


## Requirements

- Python 3.9+
- Git (with GitLab access)
- Code editor (VS Code, PyCharm, etc.)

Install dependencies:

```bash
pip install -r requirements.txt
```
