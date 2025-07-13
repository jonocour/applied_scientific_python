"""
TASK 02 – Using Pandas with ORM Data
====================================

Goal:
-----
- Query data using SQLAlchemy ORM
- Convert ORM results into a Pandas DataFrame
- Filter, flag, and group data using Pandas

Scenario:
---------
You are collecting numeric measurements from experiments.
Each measurement belongs to an experiment.
You want to analyze the dataset:
    - Remove noise (values < 0.1)
    - Flag high values (value > 0.5)
    - Group by experiment and summarize the results

Instructions:
-------------
Complete the TODOs below to:
    1. Query measurements using the ORM
    2. Build a DataFrame with columns: 'experiment', 'value'
    3. Filter, flag, and group the data
"""

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from day_3.pm.utility.model_for_optermisation import Experiment, Measurement, Base

# ---------------------------------------------
# Provided: Seed data into in-memory SQLite
# ---------------------------------------------
def setup(session):
    for i in range(3):
        exp = Experiment(name=f"exp{i}")
        exp.measurements = [
            Measurement(value=(i + j) / 10) for j in range(3)
        ]
        session.add(exp)
    session.commit()


# === TODO 1: Query ORM and return a DataFrame ===
def orm_to_dataframe(session):
    """
    Return a DataFrame with columns:
        - experiment (name)
        - value (float)
    """
    # TODO: Query all Measurement records
    # TODO: Build a list of dicts with keys: 'experiment', 'value'
    # TODO: Convert list to a Pandas DataFrame
    pass


# === MAIN WORKFLOW ===
if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    setup(session)

    # === TODO 2: Load ORM data into DataFrame ===
    # df = ...

    # === TODO 3: Filter out values below 0.1 ===
    # df = ...

    # === TODO 4: Add 'flagged' column for values > 0.5 ===
    # df["flagged"] = ...

    # === TODO 5: Group by experiment and compute count + mean ===
    # grouped = ...

    # === TODO 6: Print cleaned DataFrame and summary ===
    # print(df)
    # print(grouped)
