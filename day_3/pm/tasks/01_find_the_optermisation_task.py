"""
TASK 04 – Fixing Subtle ORM Inefficiency
=========================================

Goal:
-----
Spot and fix a hidden performance issue caused by lazy-loading (N+1 queries)

Instructions:
-------------
- Complete the TODOs below.
- Run the script and observe how many SQL queries are printed.
- Refactor the ORM query to reduce unnecessary round-trips.
- Use echo=True to log SQL and confirm improvements.

Hint:
-----
Look at how .measurements is accessed inside the loop. What’s happening under the hood?

Advanced:
---------
Try setting num_experiments = 100 to exaggerate the performance cost.
"""

from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

from day_3.pm.utility.model_for_optermisation import Experiment, Measurement

# === TODO: Add any loading strategy imports you may want to try ===
# e.g., from sqlalchemy.orm import joinedload

Base = declarative_base()

# ---------------------------------------------
# SEED SAMPLE DATA
# ---------------------------------------------
def setup_data(session, num_experiments=5):
    for i in range(num_experiments):
        exp = Experiment(name=f"Exp_{i}")
        exp.measurements = [Measurement(value=i * 0.1 + j * 0.01) for j in range(i + 1)]
        session.add(exp)
    session.commit()


# ---------------------------------------------
# NAIVE VERSION (N+1 Problem)
# ---------------------------------------------
def print_experiment_measurements(session):
    """
    Print number of measurements for each experiment.

    === TODO: Refactor this query to avoid N+1 issue ===
    - Add a loading strategy to preload measurements
    - Confirm only 1 or 2 queries are issued (not N+1)
    """
    experiments = session.query(Experiment).all()  # TODO: Add .options(...) here

    for exp in experiments:
        print(f"{exp.name} has {len(exp.measurements)} measurements")


# ---------------------------------------------
# MAIN
# ---------------------------------------------
if __name__ == "__main__":
    # === TODO: Set echo=True to see SQL queries ===
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # === TODO: Try setting this to 100 to simulate larger datasets ===
    setup_data(session, num_experiments=5)

    print("\n--- Running original version (watch for N+1 queries!) ---")
    print_experiment_measurements(session)

    # === TODO: After fixing print_experiment_measurements, rerun and verify ===
    #
    # Bonus:
    # - Try timing both versions
    # - Compare with both selectinload() and joinedload()
