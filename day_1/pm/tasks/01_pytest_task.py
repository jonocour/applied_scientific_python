"""
01_pytest_task.py – Pytest Task (After Pytest Demo)

Task:
-----
- Write tests for the `normalize` function below
- Use plain asserts first, then add exception and param tests
- Run with:
    $ pytest -v 01_pytest_task.py
"""

def normalize(values):
    """Return a list of values scaled to sum to 1."""
    if not values:
        raise ValueError("Input list must not be empty.")
    total = sum(values)
    return [v / total for v in values]

# === TESTS ===
# TODO: Add a basic test to check that [1, 1, 2] normalizes to [0.25, 0.25, 0.5]

# TODO: Add a test for an input with one number only

# TODO: Add a test to check if ValueError is raised when input is []

# TODO: BONUS – Use pytest.mark.parametrize to test 3 different input-output cases

# === SAMPLE RUN ===
if __name__ == "__main__":
    print("normalize([1, 1, 2]):", normalize([1, 1, 2]))
