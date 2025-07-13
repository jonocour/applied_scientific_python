"""
01_intro_to_data_models.py
===========================

Why Use an ORM (Object-Relational Mapper)?
------------------------------------------

Problem:
--------
In scientific projects, you'll often store structured data (e.g., simulations, measurements).
Raw SQL works but gets repetitive and error-prone at scale.

Solution:
---------
Use an ORM like SQLAlchemy:
- Define database tables as Python classes
- Perform queries and updates with object methods
- Avoid writing repetitive SQL manually

First, here's a refresher on using SQLite:
------------------------------------------
This example shows:
- How to connect to an SQLite database
- Perform full CRUD operations using raw SQL
- Compare in-memory vs. file-based databases
"""

import sqlite3

# ============================
# CONNECT
# ============================

# Option 1: In-memory DB (temporary, disappears after program ends)
# conn = sqlite3.connect(":memory:")

# Option 2: File-based DB (persists between runs)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# ============================
# CREATE (setup table)
# ============================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
""")
conn.commit()

# ============================
# CREATE (insert one record)
# ============================

cursor.execute("SELECT * FROM students WHERE name=? AND age=? AND grade=?", ("Alice", 30, "A"))
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 30, "A"))
    conn.commit()
else:
    print("Record already exists.")

# ============================
# READ (query data)
# ============================

print("\nCurrent data:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# ============================
# UPDATE (change grade)
# ============================

cursor.execute("UPDATE students SET grade=? WHERE name=?", ("A+", "Alice"))
conn.commit()

# ============================
# DELETE (remove record)
# ============================

cursor.execute("DELETE FROM students WHERE name=?", ("Alice",))
conn.commit()

# ============================
# CREATE MANY (bulk insert)
# ============================

students_batch = [
    ("Bob", 21, "B"),
    ("Clara", 24, "A"),
    ("David", 28, "C")
]
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_batch)
conn.commit()

# ============================
# READ AGAIN (final contents)
# ============================

print("\nFinal table contents:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# ============================
# CLOSE CONNECTION
# ============================

conn.close()
