from setuptools import setup, find_packages

setup(
    name="applied_scientific_python",
    version="1.2.0",
    description="Applied scientific Python tools",
    author="PTR Team",

    packages=find_packages(exclude=["tests*", "tasks*", "day_*"]),
    include_package_data=True,

    install_requires=[
        "pandas>=1.3",
        "numpy>=1.21",
        "sqlalchemy>=1.4",
        "click>=8.0",
        "pytest>=7.0",
        "coverage",
        "pdbpp",
        "cython>=0.29",
        "tabulate",
        "rich",
    ],

    python_requires=">=3.8",
)
