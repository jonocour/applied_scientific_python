TASK 02 – Installation Strategy Comparison
==========================================

Goal:
-----
Compare editable installation vs locked-environment installation and verify identical outcomes.

Why this matters:
-----------------
- Editable installs are useful for active development.
- Locked-environment installs ensure consistency and reproducibility.
- This task will help you understand how and when to use each strategy.

Instructions:
-------------

Important:
----------
Activate a fresh virtual environment for each method.  
Use `deactivate` between installs to prevent cross-contamination.

Method A — Editable Install
---------------------------
```bash
# Create and activate venvA
python -m venv venvA
source venvA/bin/activate

# Install dependencies and the project in editable mode
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# Run version check
python - <<EOF
import make_env_here
print("Version (Editable Install):", make_env_here.__version__)
EOF

# Deactivate environment
deactivate
```

Method B — Locked-Environment Install
-------------------------------------
```bash
# Export exact installed packages from Method A
pip freeze > environment.lock.txt

# Create and activate venvB
python -m venv venvB
source venvB/bin/activate

# Install using the locked requirements
pip install --upgrade pip
pip install -r environment.lock.txt

# Run version check
python - <<EOF
import make_env_here
print("Version (Locked Install):", make_env_here.__version__)
EOF

# Deactivate environment
deactivate
```

Verification:
-------------
- Both environments should report the same version number.
- Confirm that both installs import your package correctly.

Hint:
-----
Use virtual environments to isolate and prevent cross-contamination.

Reflection:
-----------
- What happens if you edit a source file after Method A’s install?  
- Does Method B pick up that change? Why or why not?

Advanced:
---------
Automate both installations and the version check in a CI job; fail the job if outputs diverge.