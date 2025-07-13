"""
04_debugging_task.py

TASK: Debugging with Traceback and PDB
======================================

You are given a broken scientific function: `weighted_average`.

It currently fails one or more test cases.

Your job:
---------
1. Run this file to see the traceback errors
2. Use `pdb` or `print()` to inspect the variables and logic
3. Fix the bugs in the `weighted_average()` function

Tip:
- Uncomment the `pdb.set_trace()` line to step through the function
- Use keyboard commands: n, s, p var, q
"""

# BROKEN FUNCTION
def weighted_average(values, weights):
    """Compute the weighted average of a list of values."""
    if len(values) != len(weights):
        raise ValueError("Lists must be the same length")
    total = 0
    for i in range(len(values)):
        total += values[i] * weights[i]
    # import pdb; pdb.set_trace()  # Uncomment this to step through
    return total / sum(weights)  # May fail if weights sum to 0

# TEST CASES
def test_typical_case():
    result = weighted_average([1, 2, 3], [1, 1, 1])
    assert result == 2.0, "Expected simple average"

def test_with_zero_weights():
    try:
        weighted_average([10, 20], [0, 0])
    except ZeroDivisionError:
        print("Caught expected ZeroDivisionError (zero total weight)")
    else:
        print("Expected ZeroDivisionError not raised")

def test_mismatched_lengths():
    try:
        weighted_average([1, 2, 3], [1, 2])
    except ValueError:
        print("Caught expected ValueError (length mismatch)")
    else:
        print("Expected ValueError not raised")

# RUN TESTS
if __name__ == "__main__":
    print("== RUNNING DEBUGGING TASK ==")
    test_typical_case()
    test_with_zero_weights()
    test_mismatched_lengths()
