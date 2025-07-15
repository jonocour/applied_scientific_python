"""
01_pytest_task.py – Pytest Task (After Pytest Demo)

Task:
-----
- Write tests for the `normalize` function below
- Use plain asserts first, then add exception and param tests
- Run with:
    $ pytest -v 01_pytest_task.py
"""
import pytest

def normalize(values):
    """Return a list of values scaled to sum to 1."""
    if not values:
        raise ValueError("Input list must not be empty.")
    total = sum(values)
    return [v / total for v in values]

# === TESTS ===

def test_normalize_basic():
    """[1,1,2] → [0.25, 0.25, 0.5]"""
    assert normalize([1, 1, 2]) == [0.25, 0.25, 0.5]

def test_normalize_single():
    """A single value [5] → [1.0]"""
    assert normalize([5]) == [1.0]

def test_normalize_empty():
    """Empty input should raise ValueError."""
    with pytest.raises(ValueError):
        normalize([])

@pytest.mark.parametrize("input_vals, expected", [
    ([2, 2, 6], [0.2, 0.2, 0.6]),
    ([0, 5, 5], [0.0, 0.5, 0.5]),
    ([10, 10],   [0.5, 0.5]),
])
def test_normalize_parametrized(input_vals, expected):
    """Parametrized tests for multiple input/output pairs."""
    result = normalize(input_vals)
    # Use approx for float-comparison safety
    assert result == pytest.approx(expected)

# === SAMPLE RUN ===
if __name__ == "__main__":
    print("normalize([1, 1, 2]):", normalize([1, 1, 2]))