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
    CSVFile: data.csv
    Parse result: 10 rows, 3 columns

    JSONFile: config.json
    Parse result: 5 top-level keys

    XMLFile: record.xml
    Parse result: 12 tags
"""

# === Base class DataFile ===
class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        return "Generic parse result"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.filename}"


# === Subclass – CSVFile ===
class CSVFile(DataFile):
    def parse(self):
        return "10 rows, 3 columns"


# === Subclass – JSONFile ===
class JSONFile(DataFile):
    def parse(self):
        return "5 top-level keys"


# === Subclass – XMLFile ===
class XMLFile(DataFile):
    def parse(self):
        return "12 tags"


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    files = [
        CSVFile("data.csv"),
        JSONFile("config.json"),
        XMLFile("record.xml")
    ]

    for f in files:
        print(f)
        print("Parse result:", f.parse())
        print()
