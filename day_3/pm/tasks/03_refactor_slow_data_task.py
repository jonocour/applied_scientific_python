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

# === TODO: Add required imports (time, pandas, etc.) ===


# === TODO 1: Query all measurements from ORM ===
def get_measurements(session):
    """
    Return a list of measurement values (floats).
    """
    # TODO: Replace with real ORM query
    return []


# === TODO 2: Compute log10 of each value using a for-loop (baseline) ===
def slow_log(values):
    # TODO: Implement loop version of log10
    pass


# === TODO 3: Vectorized version using Pandas or NumPy ===
def fast_log(values):
    # TODO: Implement vectorized version
    pass


# === MAIN WORKFLOW ===
if __name__ == "__main__":
    # TODO: Set up ORM engine/session and seed ~10,000 rows
    pass

    # TODO: Fetch raw values
    # values = get_measurements(session)

    # TODO: Time and compare both versions
    # slow_log(values)
    # fast_log(values)
