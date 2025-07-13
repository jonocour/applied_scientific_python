
"""
TASK 02 – Build Your Own ORM Model: Viscosity Tests
===================================================

Goal:
-----
Design and implement a SQLAlchemy ORM model for fluid viscosity data
and exercise full CRUD operations via context-managed sessions.

Scenario:
---------
You need to record viscosity test results for various fluids at different
temperatures. Each record must include:
  - id             (INTEGER PRIMARY KEY)
  - fluid          (TEXT)       — name of the fluid tested
  - temperature    (REAL)       — in degrees Celsius
  - viscosity      (REAL)       — in Pascal·seconds (Pa·s)

Instructions:
-------------
1. Import or create an Engine and declarative Base.
2. Define a class `ViscosityTest` with:
     __tablename__ = "viscosity_tests"
     Columns: id, fluid, temperature, viscosity
3. Create the table using `Base.metadata.create_all(engine)`.
4. Open a session using the SQLAlchemy 1.4+ context manager:
     Session = sessionmaker(bind=engine)
     with Session() as session:
         ...
5. **CREATE** two sample records:
     - fluid="Water", temperature=20.0, viscosity=0.001002
     - fluid="Glycerin", temperature=20.0, viscosity=1.412
6. **READ**: Query and print all ViscosityTest rows.
7. **UPDATE**: Change Water’s viscosity to 0.00103.
8. **DELETE**: Remove the Glycerin test.
9. Exit the session block and verify only the Water record remains.

Hints:
------
- Use `session.add_all([...])` to insert both records at once.
- Query with `session.query(ViscosityTest).all()` or `.filter_by(...)`.
- No explicit `commit()` or `close()` needed—context manager handles it.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# === TODO 1: Setup engine & Base ===
# engine = create_engine("sqlite:///viscosity.db", echo=True)
# Base = declarative_base()

# === TODO 2: Define the ORM model ===
# class ViscosityTest(Base):
#     __tablename__ = "viscosity_tests"
#     id = Column(Integer, primary_key=True)
#     fluid = Column(String, nullable=False)
#     temperature = Column(Float, nullable=False)  # °C
#     viscosity = Column(Float, nullable=False)    # Pa·s

# === TODO 3: Create the table ===
# Base.metadata.create_all(engine)

# === TODO 4: Open a session and perform CRUD ===
# Session = sessionmaker(bind=engine)
# with Session() as session:
#     # 5. CREATE two records
#     # session.add_all([...])
#
#     # 6. READ and print all rows
#
#     # 7. UPDATE Water’s viscosity
#
#     # 8. DELETE the Glycerin row
#
#     # 9. Exiting the block commits changes automatically
