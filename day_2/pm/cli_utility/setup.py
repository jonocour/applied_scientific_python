# setup.py
# ========
# This script allows you to package and install your CLI tool.
# After running `pip install .` (or `pip install -e .` for development),
# you'll be able to run your CLI command from any terminal.

from setuptools import setup, find_packages

setup(
    # --- Basic Metadata ---
    name="cli_script",             # Package name for installation
    version="0.1",                 # Version number (use semantic versioning)

    # --- Package Discovery ---
    packages=find_packages(),     # Automatically find all packages (with __init__.py)

    # --- Dependencies ---
    install_requires=[
        "click",                  # CLI framework required at runtime
    ],

    # --- Entry Points for CLI Access ---
    entry_points={
        "console_scripts": [
            # Maps `force-cli` terminal command to the cli() function
            # in cli_utility/cli_script.py
            "force-cli = cli_utility.cli_script:cli"
        ]
    },

    # --- Additional Metadata ---
    description="A simple force calculator",
    author="Ed",
    # Optional fields:
    # url="https://github.com/yourname/cli_script",
    # license="MIT",
    # classifiers=[...],
)

"""
How to use this tool
====================

1. From the 'pm' directory, install the package in editable mode:

    $ pip install -e .

2. You can now use the CLI command anywhere:

    $ force-cli --mass 2 --acceleration 9.81
    
3. To Uninstall:
-------------
    $ pip uninstall sci-tools

"""
