"""
03_debugging_task.py – Debugging Task (After Debugging Demo)

Task:
-----
- The function `weighted_average` is currently broken in one or more ways.
- Your job is to:
    1. Run this file to see which tests fail.
    2. Use print(), traceback, or pdb to inspect and trace through the logic.
    3. Fix the implementation under the TODOs so all tests pass.

Instructions:
- Uncomment the `import pdb; pdb.set_trace()` line if you want to step through.
- Use `python 03_debugging_task.py` to run the tests.
"""

# === BROKEN FUNCTION ===
def weighted_average(values, weights):
    """Compute the weighted average of a list of values."""
    # TODO: 1) Check that values and weights are same length; if not, raise ValueError
    # TODO: 2) Compute the sum of weights; if zero, raise ZeroDivisionError
    # TODO: 3) Compute the weighted sum without using zip (index-based)
    # TODO: 4) Return weighted_sum / total_weight

    # import pdb; pdb.set_trace()  # ← uncomment to debug interactively

    # YOUR FIXED CODE GOES HERE
    pass


# === TEST CASES ===
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


# === RUN TESTS ===
if __name__ == "__main__":
    print("== RUNNING DEBUGGING TASK ==")
    test_typical_case()
    test_with_zero_weights()
    test_mismatched_lengths()
