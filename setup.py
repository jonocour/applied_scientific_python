from setuptools import setup, find_packages

# === setup() tells setuptools how to package and install your project ===
setup(
    name="applied_scientific_python",  # Package name (as installed via pip)
    version="1.2.0",                   # Semantic versioning: major.minor.patch
    description="Applied scientific Python tools and training resources",
    long_description=open("README.md", encoding="utf-8").read(),  # Detailed description from file
    long_description_content_type="text/markdown",                # Needed if using README.md
    author="PTR Team",                                             # Maintainer/creator name
    author_email="team@PTR.org",                                   # Optional contact info
    url="https://gitlab.com/PTR",                                  # Homepage or Git repo

    license="Proprietary",  # PRIVATE – do not use MIT or open licenses unless intended

    # === This tells setuptools what packages (folders) to include ===
    packages=find_packages(
        exclude=["tests*", "tasks*", "day_*"]  # Exclude teaching/experimental code from install
    ),

    include_package_data=True,  # Include any non-code files listed in MANIFEST.in (if applicable)

    # === Runtime dependencies ===
    install_requires=[
        "pandas>=1.3",         # Data analysis and tabular data manipulation
        "numpy>=1.21",         # Numerical computing, array operations
        "sqlalchemy>=1.4",     # ORM for database-backed scientific data
        "click>=8.0",          # CLI creation (used in Day 2 tools)
        "pytest>=7.0",         # Main testing framework (used across the course)
        "coverage",            # Code coverage analysis for tests
        "pdbpp",               # Better Python debugger (used in debugging labs)
        "cython>=0.29",        # Optional: C-speedup of critical functions (Day 3)
        "tabulate",            # Used to format tables in CLI output
        "rich",                # Pretty-printing/logging in CLI or test reports
    ],

    # === Metadata for packaging tools and indexes (PyPI, etc.) ===
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # maturity level
        "Intended Audience :: Science/Research",        # target users
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent",
        "Private :: Do Not Upload",                     # helpful reminder for internal-only use
    ],

    python_requires=">=3.8",  # Minimum Python version required
)
