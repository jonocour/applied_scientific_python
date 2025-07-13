"""
02_intro_to_pandas.py
===========================

Intro to Pandas: Clean and Analyze Scientific Data
--------------------------------------------------

Topics:
-------
- Load tabular data into a DataFrame
- Filter, group, and transform with vectorized operations
- Compare naive `.apply()` with better Pandas idioms

Run:
----
    $ python 02_pandas_data_cleaning.py
"""

import pandas as pd

# ---------------------------------------------
# Step 1: Create synthetic data
# ---------------------------------------------
data = {
    "experiment": ["exp1", "exp1", "exp2", "exp2", "exp3", "exp3", "exp3"],
    "sample_id": [101, 102, 103, 104, 105, 106, 107],
    "value": [0.12, 0.09, 0.33, 0.25, 0.48, 0.51, 0.50],
}

df = pd.DataFrame(data)
print("Raw data:\n", df)

# ---------------------------------------------
# Step 2: Basic filtering (masking)
# ---------------------------------------------
filtered = df[df["value"] > 0.1]
print("\nFiltered (value > 0.1):\n", filtered)

# ---------------------------------------------
# Step 3: Grouped statistics
# ---------------------------------------------
grouped = df.groupby("experiment")["value"].agg(["count", "mean", "std"])
print("\nGrouped stats per experiment:\n", grouped)

# ---------------------------------------------
# Step 4: Vectorized flagging
# ---------------------------------------------
# Bad: row-wise apply (slow for big data)
# df["flagged"] = df.apply(lambda row: row["value"] < 0.15, axis=1)

# Good: vectorized boolean operation
df["flagged"] = df["value"] < 0.15
print("\nWith flagged column:\n", df)

# ---------------------------------------------
# Optional: Export to CSV or Excel
# ---------------------------------------------
# df.to_csv("processed.csv", index=False)
