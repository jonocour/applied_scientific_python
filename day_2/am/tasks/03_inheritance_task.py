"""
TASK 03 – Inheritance with Data File Parsers
=============================================

Goal:
-----
Use inheritance to represent different types of data files that all share a common interface.

Learning Outcomes:
------------------
Build a logical class hierarchy using inheritance
Override methods for specialized behavior
Demonstrate polymorphism via shared interface

Instructions:
-------------
- Create an abstract base class `DataFile`:
    - Attribute: filename
    - Abstract method: parse() → returns summary string
    - __str__ should return the filename and type

- Implement 3 subclasses:
    1. CSVFile – returns number of rows and columns
    2. JSONFile – returns number of keys at the top level
    3. XMLFile – returns number of tags found (simulate it!)

- You don’t need real file I/O — just simulate the behavior with dummy values.

Example Output:
---------------
    Parsing: data.csv → 10 rows, 3 columns
    Parsing: config.json → 5 top-level keys
    Parsing: record.xml → 12 tags
"""

import abc

# === TODO: Define abstract base class DataFile ===
# - Attribute: filename
# - Method: parse() → abstract
# - __str__ should show "<ClassName>: filename"


# === TODO: Subclass – CSVFile ===
# Simulate: 10 rows, 3 columns


# === TODO: Subclass – JSONFile ===
# Simulate: 5 top-level keys


# === TODO: Subclass – XMLFile ===
# Simulate: 12 tags


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    files = [
        # CSVFile("data.csv"),
        # JSONFile("config.json"),
        # XMLFile("record.xml")
    ]

    for f in files:
        print(f)
        print("Parse result:", f.parse())
        print()
