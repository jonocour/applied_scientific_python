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
    if std == 0:
        return [0.0 for _ in values]  # All standardized values should be 0.0
    return [(x - mean) / std for x in values]


# === TESTS ===
class TestStandardize(unittest.TestCase):

    def test_mean_zero_for_1_2_3(self):
        """Standardizing [1,2,3] should give values whose mean ≈ 0."""
        vals = [1, 2, 3]
        result = standardize(vals)
        # The mean of the result should be 0. Use assertAlmostEqual for floating point.
        mean_of_result = sum(result) / len(result)
        self.assertAlmostEqual(mean_of_result, 0.0, places=7)

    def test_single_element_all_zero(self):
        """A single-element list should standardize to [0.0]."""
        self.assertEqual(standardize([42]), [0.0])

    def test_empty_list_raises(self):
        """Passing an empty list should raise a ValueError."""
        with self.assertRaises(ValueError):
            standardize([])

    def test_values_for_10_20_30(self):
        """Check standardized values for [10,20,30] against expected z-scores."""
        vals = [10, 20, 30]
        result = standardize(vals)
        # For [10,20,30], mean=20, std≈8.1649658, so z-scores ≈ [-1.2247, 0, +1.2247]
        self.assertAlmostEqual(result[0], -1.224744871, places=6)
        self.assertAlmostEqual(result[1],  0.0,           places=6)
        self.assertAlmostEqual(result[2],  1.224744871,  places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
