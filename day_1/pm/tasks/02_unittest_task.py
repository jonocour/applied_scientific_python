"""
02_unittest_task.py – Unittest Task (After Unittest Demo)

Task:
-----
- Write a full test class for the function below
- Use assertEqual, assertAlmostEqual, and assertRaises
- Run with:
    $ python 02_unittest_task.py
"""

import unittest


def standardize(values):
    """Return z-scores (standardized values)."""
    if not values:
        raise ValueError("Input cannot be empty.")
    mean = sum(values) / len(values)
    std = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean) / std for x in values]


# === TESTS ===
class TestStandardize(unittest.TestCase):


# TODO: Test with [1, 2, 3]; check that result has mean 0 (approximately)
    numbers = [1,2,3] # used to ignore syntax errors
# TODO: Test with single-element list – expect all values to be zero

# TODO: Test ValueError raised for empty list

# TODO: BONUS – Add multiple assertAlmostEqual values in one test for [10, 20, 30]

if __name__ == "__main__":
    unittest.main()
