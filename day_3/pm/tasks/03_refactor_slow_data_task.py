"""
TASK 03 – Refactor Slow Data Script
====================================

Goal:
-----
Refactor a poorly written script that:
    - Loads a large number of ORM rows
    - Uses slow for-loops for calculations
    - Does not use vectorization or batching

Instructions:
-------------
1. Run the original script and observe the performance.
2. Refactor it using Pandas or NumPy for efficient computation.
3. (Optional) Try multiprocessing or Cython to push performance further.

Scenario:
---------
You’re computing the log of measurement values from 10,000 rows in the database.

Expected Improvements:
----------------------
- Use Pandas to vectorize math
- Avoid looping through ORM objects one-by-one
- Bonus: Profile with `time` or `cProfile`
"""

# === TODO: Add required imports (time, pandas, numpy, math, etc.) ===
from day_3.pm.utility.model_for_optermisation import Experiment, Measurement, Base

# ---------------------------------------------
# Provided: Seed 10,000 measurements into the database
# ---------------------------------------------
def setup(session):
    for i in range(10_000):
        exp = Experiment(name=f"exp_{i}")
        exp.measurements = [Measurement(value=(i + 1) / 10_000)]
        session.add(exp)
    session.commit()


# === TODO 1: Query all measurements from ORM ===
def get_measurements(session):
    """
    Return a list of Measurement ORM objects.
    BAD PRACTICE:
    - Loads full ORM objects into memory.
    - Inefficient for large datasets.

    TODO: Replace with a query that selects only 'value' as a list or uses batching.
    """
    return session.query(Measurement).all()


# === TODO 2: Compute log10 of each value using a for-loop (baseline) ===
def slow_log(measurements):
    """
    Compute log10 of each measurement using a slow Python loop.

    BAD PRACTICE:
    - Loops over each ORM object.
    - Uses math.log10() in pure Python.

    TODO: Replace with vectorized NumPy or Pandas computation after ORM query refactor.
    """
    results = []
    for m in measurements:
        results.append(math.log10(m.value))
    return results


# === MAIN WORKFLOW ===
if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    setup(session)

    print("\n--- Running Slow Loop Version ---")
    measurements = get_measurements(session)

    start = time.time()
    slow_results = slow_log(measurements)
    print(f"Slow loop took {time.time() - start:.4f} sec")

    # === TODO 4: Refactor using Pandas or NumPy ===
    # Using time in the main runner above, compare your improvements with the originals
    # Remember a raise in complexity isn't necessarliy accsicated with a rasie in computation
