"""
01_python_and_cli.py
=====================

Intro to Command-Line Interfaces (CLI) in Scientific Python
-----------------------------------------------------------

Why Use CLI Tools?
------------------
- Scientific scripts often require parameters: mass, temperature, dataset path, etc.
- Instead of editing the Python file each time, it's better to pass arguments via the terminal.
- This makes code more reusable, automatable, and shareable with other scientists.

Learning Outcomes:
------------------
- Understand why CLI tools matter in scientific computing
- Recognize when to use argparse, Click, or Typer
- Learn how to run scripts with parameters from the shell

"""

# =======================================================
# 0. MOTIVATION – Why not hardcode values into scripts?
# =======================================================

# Imagine you're running a physics script:

# mass = 2.5
# acceleration = 9.8
# force = mass * acceleration
# print(force)

# This works, but every time you want to try new values, you have to edit the script.
# Instead, run it like this from the command line:

# $ python force.py --mass 2.5 --acceleration 9.8

#  Cleaner, safer, reproducible — you don't touch the code, just change the inputs.

# =======================================================
# 1. CLIs ENABLE AUTOMATION & PIPELINES
# =======================================================

# By using CLI tools, you can automate workflows:

# $ python analyze.py --input experiment1.csv
# $ python analyze.py --input experiment2.csv

# Or in a shell loop:
# $ for f in *.csv; do python analyze.py --input $f; done

# This kind of usage is common in high-performance computing, batch jobs, and pipelines.

# =======================================================
# 2. CLIs ENABLE REPRODUCIBILITY
# =======================================================

# Running code with explicit CLI parameters helps you keep track of what was done:

# $ python fit_model.py --alpha 0.05 --iterations 1000 --seed 42

#  You can copy this command into a README, notebook, or log file.
#  Anyone (including future you) can re-run the exact same experiment.

# =======================================================
# 3. CLIs MAKE YOUR CODE SHAREABLE
# =======================================================

# You can wrap a Python script with CLI tools and share it with a lab colleague:

# $ python temp_convert.py --celsius 37

# They don’t need to know Python — just how to run a terminal command.

# =======================================================
# 4. WHICH TOOL TO USE?
# =======================================================

# | Tool       | Best For                                 | Why Use It                                                           |
# | ---------- | ---------------------------------------- | -------------------------------------------------------------------- |
# | argparse   | Built-in basics                          | No install, good for learning or short scripts                       |
# | Click      | Simpler syntax, mid-size tools           | Great for productivity, includes validation/help                     |
# | Typer      | Production-quality tools with type hints | Best for long-term code, uses type hints for safety and autocomplete |

# You'll learn all three in this section.

# =======================================================
# 5. COMMON CLI USE CASES IN SCIENCE
# =======================================================

# Tool Goal                       | Example Command
# -------------------------------|---------------------------------------------
# Run a simulation                | $ python simulate.py --particles 1000 --steps 5000
# Analyze experimental data       | $ python analyze.py --input data.csv --normalize log
# Convert between units           | $ python convert_temp.py --celsius 37
# Batch rename genome files       | $ python rename_genomes.py --pattern "chr*.fa"

# =======================================================
# 6. WHAT YOU SHOULD REMEMBER
# =======================================================

# In a real environment, you shouldn’t change the Python code every time you want a new result.
#  You should write a script once, and let the inputs drive it — that’s what CLI tools are for.

