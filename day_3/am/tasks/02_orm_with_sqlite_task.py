"""
TASK 02 – ORM with SQLite
===============================================================

Goal:
-----
- Use SQLAlchemy Core to create and manage a fluid viscosity test database
- Practice fundamental database operations using Core’s Table and Connection APIs

Scenario:
---------
You are logging viscosity measurements for fluids at different temperatures.
Each record should include:
  - id           (INTEGER PRIMARY KEY AUTOINCREMENT)
  - fluid        (TEXT)   — name of the fluid tested
  - temperature  (REAL)   — degrees Celsius
  - viscosity    (REAL)   — measured in Pascal·seconds (Pa·s)

What is Pa·s?
-------------
Pascal‑second is the SI unit of dynamic viscosity.
It describes a fluid's resistance to flow.
Example:
    Water at 20°C has a viscosity of around 0.001 Pa·s.

Instructions:
-------------
Complete the TODOs below to:
    1. Connect to a SQLite database named "viscosity_tests.db"
    2. Define a `viscosity_tests` table using SQLAlchemy Core
    3. Create the table if it doesn’t already exist
    4. Insert two viscosity test records:
         - Water at 20.0°C, viscosity = 0.001002
         - Glycerin at 20.0°C, viscosity = 1.412
    5. Select and print all records from the table
    6. Update Water’s viscosity to 0.00103
    7. Delete the Glycerin record
    8. Select and print all remaining records

Expected Output:
----------------
Records inserted!
(1, 'Water', 20.0, 0.001002)
(2, 'Glycerin', 20.0, 1.412)
Record updated!
Record deleted!
(1, 'Water', 20.0, 0.00103)
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, select

# === TODO 1: Create an engine connected to "viscosity_tests.db"
# engine = None
# metadata = None

# === TODO 2: Define the "viscosity_tests" table with columns:
#     - id (INTEGER PRIMARY KEY AUTOINCREMENT)
#     - fluid (TEXT)
#     - temperature (REAL)
#     - viscosity (REAL)

# === TODO 3: Create the table in the database (if it doesn't exist)

# === TODO 4: Open a connection and perform INSERT
# with engine.connect() as conn:
#     # Insert two records into the table
#     # Print "Records inserted!"

#     # === TODO 5: SELECT and print all rows

#     # === TODO 6: UPDATE Water's viscosity

#     # === TODO 7: DELETE the Glycerin record

#     # === TODO 8: SELECT and print all rows again

