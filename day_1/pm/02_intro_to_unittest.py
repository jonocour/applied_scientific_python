"""
02_intro_to_unittest.py
========================

Introduction to unittest – Python's Built-in Test Framework

Why unittest?
-------------
- Part of the Python Standard Library (no install needed)
- More structured than pytest: ideal for larger, more formal projects
- Uses test classes and method-based assertions

 How to run:
    $ python 02_intro_to_unittest.py
    OR:
    $ python -m unittest 02_intro_to_unittest.py
"""

import unittest

# ============================================
# FUNCTION TO TEST
# ============================================
def mean(values):
    """Compute the mean of a list of numbers."""
    if not values:
        raise ValueError("List must not be empty")
    return sum(values) / len(values)

# ============================================
#1. BASIC ASSERT TESTS
# ============================================
class TestMeanBasic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mean([1, 2, 3]), 2.0)

    def test_single_element(self):
        self.assertEqual(mean([42]), 42.0)

    def test_floats(self):
        self.assertAlmostEqual(mean([0.1, 0.2, 0.3]), 0.2, places=6)

# ============================================
#2. ASSERT RAISES FOR EXCEPTIONS
# ============================================
class TestMeanExceptions(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            mean(["a", "b", "c"])

# ============================================
#3. MULTIPLE ASSERTS IN ONE TEST
# ============================================
class TestMeanMultiple(unittest.TestCase):

    def test_various_inputs(self):
        self.assertEqual(mean([2, 2, 2]), 2.0)
        self.assertEqual(mean([5, 10, 15]), 10.0)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.0]), 2.33333, places=4)

# ============================================
# Best Practices
# ============================================
# - Inherit from unittest.TestCase
# - Group related tests into classes
# - Use self.assert* methods:
#     - assertEqual, assertAlmostEqual
#     - assertTrue, assertFalse
#     - assertRaises for exceptions
# - Use setUp/tearDown to prep state (optional for advanced use)

# ============================================
#  ENTRY POINT
# ============================================
if __name__ == "__main__":
    unittest.main()
