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
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session, selectinload
from day_3.pm.utility.model_for_optermisation import Experiment, Measurement, Base

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
# FIXED VERSION — Using selectinload() to avoid N+1
# ---------------------------------------------
def print_experiment_measurements(session):
    """
    Print number of measurements for each experiment.
    This version preloads related measurements to avoid N+1 queries.
    """
    experiments = session.query(Experiment)\
                         .options(selectinload(Experiment.measurements))\
                         .all()

    for exp in experiments:
        print(f"{exp.name} has {len(exp.measurements)} measurements")


# ---------------------------------------------
# MAIN WORKFLOW
# ---------------------------------------------
if __name__ == "__main__":
    # SQL echo enabled to see queries issued
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Try increasing this to 100 for advanced testing
    setup_data(session, num_experiments=5)

    print("\n--- Running with selectinload() (should avoid N+1 queries) ---")
    print_experiment_measurements(session)
