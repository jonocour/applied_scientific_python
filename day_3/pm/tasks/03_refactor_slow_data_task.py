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
import time
import math
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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


# ---------------------------------------------
# BAD EXAMPLE — Slow ORM Query & Python Loop
# ---------------------------------------------
def get_measurements(session):
    return session.query(Measurement).all()


def slow_log(measurements):
    results = []
    for m in measurements:
        results.append(math.log10(m.value))
    return results


# ---------------------------------------------
# GOOD EXAMPLE — Efficient Vectorized Approach
# ---------------------------------------------
def get_measurements_as_dataframe(session):
    """
    Query only required fields and load into a DataFrame.
    """
    results = session.query(Measurement.value).all()
    values = [v[0] for v in results]  # Extract tuples into list
    return pd.DataFrame({"value": values})


def vectorized_log(df):
    """
    Use NumPy log10 on entire column — super fast.
    """
    df["log_value"] = np.log10(df["value"])
    return df

# ---------------------------------------------
# MAIN WORKFLOW
# ---------------------------------------------
if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    setup(session)

    # --- BAD WAY ---
    print("\n--- Running Slow Loop Version ---")
    bad_start = time.time()
    measurements = get_measurements(session)
    slow_results = slow_log(measurements)
    bad_time = time.time() - bad_start
    print(f"Slow loop took {bad_time:.4f} sec")

    # --- GOOD WAY ---
    print("\n--- Running Vectorized Pandas Version ---")
    good_start = time.time()
    df = get_measurements_as_dataframe(session)
    df = vectorized_log(df)
    good_time = time.time() - good_start
    print(f"Vectorized version took {good_time:.4f} sec")

    # --- Compare Performance ---
    speedup = bad_time / good_time if good_time > 0 else float('inf')
    print(f"\nVectorized approach is {speedup:.2f}x faster than the looped version.")
