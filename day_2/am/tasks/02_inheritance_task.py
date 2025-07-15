"""
TASK 02 – Inheritance with Data File Parsers
=============================================
Goal:
-----
Use inheritance to represent different types of data files that all share a common interface.

Learning Outcomes:
------------------
- Build a logical class hierarchy using inheritance
- Override methods for specialized behavior
- Demonstrate polymorphism via shared interface

Instructions:
-------------
- Create a base class `DataFile`:
    - Attribute: filename
    - Method: parse() → returns summary string (can be overridden)
    - __str__ should return "<ClassName>: filename"

- Implement 3 subclasses:
    1. CSVFile – returns "10 rows, 3 columns"
    2. JSONFile – returns "5 top-level keys"
    3. XMLFile – returns "12 tags"

- You don’t need real file I/O — simulate with dummy values.

Example Output:
---------------
    Parsing: data.csv → 10 rows, 3 columns
    Parsing: config.json → 5 top-level keys
    Parsing: record.xml → 12 tags
"""

import abc

# === TODO: Define abstract base class DataFile ===
# - Attribute: filename
# - Method: parse() → default implementation
# - __str__ shows "<ClassName>: filename"



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
