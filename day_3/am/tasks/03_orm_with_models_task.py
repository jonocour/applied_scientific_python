"""
TASK 03 – ORM with Declarative Base
=======================================================

Goal:
-----
- Use SQLAlchemy ORM to create and manage a product inventory database
- Practice defining models and performing CRUD via context‑managed sessions

Scenario:
---------
You are developing a simple inventory system. Each product record must include:
  - id       (INTEGER PRIMARY KEY AUTOINCREMENT)
  - name     (TEXT)    — product name
  - quantity (INTEGER) — units in stock
  - price    (REAL)    — unit price in USD

Instructions:
-------------
Complete the TODOs below to:
    1. Connect to a SQLite database named "inventory.db"
    2. Create a declarative Base
    3. Define an `InventoryItem` model class with:
         - `__tablename__ = "inventory_items"`
         - Columns: id, name, quantity, price
    4. Create the table in the database
    5. Create a Session class bound to the engine
    6. Open a session with `with Session() as session:`
    7. **CREATE** two records:
         - "Widget" with quantity=100, price=2.99
         - "Gadget" with quantity=50,  price=5.49
    8. **READ** and print all records
    9. **UPDATE** the quantity of "Widget" to 120
   10. **DELETE** the "Gadget" record
   11. **READ** and print remaining records

Expected Output:
----------------
Records inserted!
(1, 'Widget', 100, 2.99)
(2, 'Gadget', 50, 5.49)
Record updated!
Record deleted!
(1, 'Widget', 120, 2.99)
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# === TODO 1: Create an engine connected to "inventory.db" ===
# engine = create_engine("sqlite:///inventory.db", echo=True)

# === TODO 2: Create a declarative Base ===
# Base = declarative_base()

# === TODO 3: Define the ORM model ===
# class InventoryItem(Base):
#     __tablename__ = "inventory_items"
#     id       = Column(Integer, primary_key=True, autoincrement=True)
#     name     = Column(String,  nullable=False)
#     quantity = Column(Integer, nullable=False)
#     price    = Column(Float,   nullable=False)

# === TODO 4: Create the table ===
# Base.metadata.create_all(engine)

# === TODO 5: Create a Session class ===
# Session = sessionmaker(bind=engine)

## === TODO 6: Open a session and perform CRUD ===
# with Session() as session:
#     # === TODO 7: INSERT two inventory records
#     # session.add_all([
#     #     InventoryItem(name="Widget", quantity=100, price=2.99),
#     #     InventoryItem(name="Gadget", quantity=50, price=5.49)
#     # ])
#     # print("Records inserted!")

#     # === TODO 8: SELECT and print all records

#     # === TODO 9: UPDATE Widget’s quantity to 120

#     # === TODO 10: DELETE the Gadget record

#     # === TODO 11: SELECT and print all remaining records
