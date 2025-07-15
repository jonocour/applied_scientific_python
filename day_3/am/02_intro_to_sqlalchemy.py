from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, select

# 1. Setup: Engine and Metadata
# engine = create_engine("sqlite:///viscosity_tests.db", echo=True) - exists as a .db file
engine = create_engine("sqlite:///:memory:", echo=True) # exists "in-memory", deleted after run
metadata = MetaData()

# 2. Define the table using SQLAlchemy Core (no ORM models)
viscosity_tests = Table(
    "viscosity_tests",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("fluid", String, nullable=False),
    Column("temperature", Float, nullable=False),  # °C
    Column("viscosity", Float, nullable=False)     # Pa·s
)

# 3. Create the table
metadata.create_all(engine)

# 4. Perform CRUD inside a connection block
with engine.connect() as connection:
    # CREATE — Insert records
    connection.execute(
        viscosity_tests.insert(),
        [
            {"fluid": "Water", "temperature": 20.0, "viscosity": 0.001002},
            {"fluid": "Glycerin", "temperature": 20.0, "viscosity": 1.412}
        ]
    )
    print("Records inserted!")

    # READ — Select all records
    result = connection.execute(select(viscosity_tests))
    print("\nAll records:")
    for row in result:
        print(row)

    # UPDATE — Change Water's viscosity
    connection.execute(
        viscosity_tests.update()
        .where(viscosity_tests.c.fluid == "Water")
        .values(viscosity=0.00103)
    )
    print("Record updated!")

    # DELETE — Remove Glycerin
    connection.execute(
        viscosity_tests.delete()
        .where(viscosity_tests.c.fluid == "Glycerin")
    )
    print("Record deleted!")

    # Final check — Select remaining records
    result = connection.execute(select(viscosity_tests))
    print("\nFinal records:")
    for row in result:
        print(row)
