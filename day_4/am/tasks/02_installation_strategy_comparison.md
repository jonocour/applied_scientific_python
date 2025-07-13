TASK 06 – Installation Strategy Comparison
==========================================

Goal:
-----
Compare editable installation vs locked-environment installation and verify identical outcomes.

Instructions:
-------------
Complete the TODOs below:

```bash
# Method A: Editable install
# TODO: Create and activate venvA
python -m venv venvA && source venvA/bin/activate
# TODO: Install project in editable mode
pip install -r requirements.txt
pip install -e .
```

```bash
# Method B: Locked-environment install
# TODO: Export locked environment to environment.lock.txt
# e.g., conda env export > environment.lock.txt
python -m venv venvB && source venvB/bin/activate
pip install --upgrade pip
# TODO: Install using locked requirements
pip install -r environment.lock.txt
```

```bash
# TODO: In each venv, run version check
python - <<EOF
import mypkg
print("Version:", mypkg.__version__)
EOF
```

- TODO: Verify both environments print the same version and import correctly.

Hint:
-----
Use virtual environments to isolate and prevent cross-contamination.

Advanced:
---------
Automate both installations and the version check in a CI job; fail the job if outputs diverge.
