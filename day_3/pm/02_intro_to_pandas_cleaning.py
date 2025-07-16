"""
02_intro_to_pandas_cleaning.py
===========================

Intro to Pandas: Clean and Analyze Scientific Data
--------------------------------------------------

Topics:
-------
- Load tabular data into a DataFrame
- Filter, group, and transform with vectorized operations
- Compare naive `.apply()` with better Pandas idioms
- Sort and rank data with `.sort_values()`
- Merge datasets with `pd.merge()`
- Reshape and aggregate with `.pivot_table()`


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
# Step 5: Sorting values (by descending value)
# ---------------------------------------------
sorted_df = df.sort_values("value", ascending=False)
print("\nSorted by value (descending):\n", sorted_df)

# ---------------------------------------------
# Step 6: Merging with another DataFrame
# ---------------------------------------------
# Create a synthetic lookup table for sample metadata
meta_data = pd.DataFrame({
    "sample_id": [101, 102, 103, 104, 105, 106, 107],
    "type": ["A", "A", "B", "B", "C", "C", "C"],
})

merged_df = pd.merge(df, meta_data, on="sample_id")
print("\nMerged DataFrame with metadata:\n", merged_df)

# ---------------------------------------------
# Step 7: Pivot Table (average value per experiment and type)
# ---------------------------------------------
pivot = merged_df.pivot_table(
    index="experiment",
    columns="type",
    values="value",
    aggfunc="mean"
)
print("\nPivot Table (mean value per experiment and type):\n", pivot)

# ---------------------------------------------
# Optional: Export to CSV or Excel
# ---------------------------------------------
# df.to_csv("processed.csv", index=False)
