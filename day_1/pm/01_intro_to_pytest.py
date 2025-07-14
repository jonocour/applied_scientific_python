"""
01_intro_to_pytest.py
======================

Intro to Pytest – A Lightweight Testing Tool for Scientific Python

Why pytest?
-----------
- Simple and readable syntax
- No boilerplate or test classes required
- Ideal for testing functions in scientific scripts

How to Run:
-----------
    $ pytest 01_intro_to_pytest.py
    $ pytest -v 01_intro_to_pytest.py  # Verbose output

Installation (if needed):
-------------------------
    pip install pytest
"""

# =====================================
# FUNCTION TO TEST
# =====================================
def c_to_k(temp_c):
    """Convert Celsius to Kelvin."""
    if not isinstance(temp_c, (int, float)):
        raise TypeError("Temperature must be a number.")
    return temp_c + 273.15




def calculate_force(mass, acceleration):
    return mass * acceleration

def test_calculate_force():
    result = calculate_force(5, 9.81)
    assert result == pytest.approx(49.05, rel=1e-4)



# =====================================
#  1. BASIC ASSERT TESTS
# =====================================

def test_c_to_k_zero():
    assert c_to_k(0) == 273.15

def test_c_to_k_boiling():
    assert c_to_k(100) == 373.15

def test_c_to_k_negative():
    assert c_to_k(-273.15) == 0

# =====================================
#  2. ASSERTING EXCEPTIONS
# =====================================

# Old-school way with try/except
def test_invalid_input_try():
    try:
        c_to_k("cold")  # Should raise TypeError
    except TypeError:
        pass
    else:
        assert False, "Expected a TypeError for string input"

# Modern and cleaner: using pytest.raises
import pytest

def test_invalid_input_pytest_raises():
    with pytest.raises(TypeError):
        c_to_k("twenty")

# =====================================
#  3. ASSERTING MULTIPLE THINGS IN ONE TEST
# =====================================

def test_multiple_asserts():
    assert c_to_k(0) == 273.15
    assert c_to_k(100) == 373.15
    assert round(c_to_k(-50), 2) == 223.15  # rounding due to float precision

#  Best practice:
# - OK to put several asserts in one test if they're related
# - But split into separate test functions if they serve distinct behaviors

# =====================================
#  4. PARAMETRIZED TESTING (ADVANCED)
# =====================================

@pytest.mark.parametrize("temp_c, expected_k", [
    (0, 273.15),
    (100, 373.15),
    (-273.15, 0),
    (25, 298.15),
])
def test_c_to_k_param(temp_c, expected_k):
    assert c_to_k(temp_c) == expected_k

# =====================================
#  SUMMARY NOTES
# =====================================

# ▶ All test functions must start with `test_`
# ▶ Use plain `assert` to compare values
# ▶ Use `pytest.raises` to test exceptions
# ▶ Parametrize when testing lots of cases
# ▶ You can group related tests into one function with multiple asserts

# Extra:
# ▶ To test only a specific function:
#       $ pytest -k "test_c_to_k_zero"
# ▶ To see detailed tracebacks:
#       $ pytest -v
