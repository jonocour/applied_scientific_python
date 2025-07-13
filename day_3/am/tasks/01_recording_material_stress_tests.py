"""
TASK 01 – Recording Material Stress Tests
=========================================

Goal:
-----
- Use SQLite to store and read material test results from simulated stress trials
- Reinforce SQL basics (CREATE, INSERT, SELECT) using Python's sqlite3 module

Extra Goals:
------------
- Practice safe data insertion using parameter substitution
- Reflect real-world testing scenarios in aerospace engineering

Scenario:
---------
You’re logging data from a series of aeronautical material tests. Each sample has a name
and a recorded yield strength (in MPa).

What is MPa?
------------
MPa stands for "megapascal", a unit of stress or pressure.
It's used in engineering to describe how strong a material is under load.
1 MPa = 1,000,000 pascals = 1,000,000 newtons per square meter (N/m²)

Example:
    A yield strength of 930.5 MPa means the material can withstand
    930.5 million N/m² of stress before it permanently deforms.

Instructions:
-------------
Complete the TODOs below to:
    1. Connect to a database file ("stress_tests.db")
    2. Create a table called `aero_materials` if it doesn't exist
    3. Insert one material result: name = "Titanium Alloy", yield_strength = 930.5
    4. Read and print all entries

Expected Output:
----------------
Material added!
(1, 'Titanium Alloy', 930.5)
"""

import sqlite3

# === TODO 1: Connect to a database file named "stress_tests.db"
conn = None
cursor = None

# === TODO 2: Create a table 'aero_materials' with:
#     - id (INTEGER PRIMARY KEY AUTOINCREMENT)
#     - material_name (TEXT)
#     - yield_strength (REAL, in MPa)
# Note: REAL is a numeric type used in SQLite for storing floating-point numbers (i.e., decimals).

# === TODO 3: Insert "Titanium Alloy" with yield_strength 930.5
# Use parameter substitution (?, ?, ...)

# === TODO 4: Commit and confirm with a print message like "Material added!"

# === TODO 5: Select and print all rows from the table

# === TODO 6: Close the database connection


# =====================================================
# Bonus Reference – Additional Aerospace Materials
# =====================================================
# | Material             | Yield Strength (MPa) | Notes                                    |
# | -------------------- | -------------------- | ---------------------------------------- |
# | Aluminum 7075-T6     | ~503 MPa             | High-strength aerospace-grade aluminum   |
# | Titanium Grade 5     | ~830 MPa             | Lightweight, corrosion-resistant, strong |
# | Steel AISI 1045      | ~530 MPa             | Medium carbon steel, general engineering |
# | Inconel 718          | ~1030 MPa            | Superalloy for high temps (jet engines)  |
# | Magnesium AZ31       | ~200 MPa             | Ultra-light metal, lower strength        |
# | Stainless 316        | ~290 MPa             | Corrosion-resistant, used in harsh envs  |
# | Copper (pure)        | ~70 MPa              | Soft, good conductor, not structural     |
