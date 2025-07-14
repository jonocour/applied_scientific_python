"""
TASK 02 – Build Your Own Scientific CLI Tool (Argparse)
=======================================================

Goal:
-----
Practice creating your own command-line interface using **argparse** for a basic calculation.

Instructions:
-------------
You will:
1. Define a function: `pressure(force, area)`
2. Wrap it in a CLI using **argparse**
3. Run the tool from the terminal with custom parameters

Part 1 – The Function
---------------------
Define a function that computes pressure using:
    pressure = force / area

Include error handling:
- Raise ValueError if area is zero or negative

Part 2 – CLI Tool
-----------------
- Use argparse to let users specify:
    --force  (float)
    --area   (float)

- Parse the arguments, call the `pressure()` function, and print the result nicely

How to test (once implemented):
-------------------------------
    $ python 02_create_your_own_argparse_task.py --force 100 --area 5

Expected output example:
------------------------
    Pressure = 20.00 Pascals (Pa)

Optional:
---------
- Format result with scientific notation if appropriate
- Add input validation for negative force
"""

# === TODO: Define a function called `pressure(force, area)` ===
# It should return force / area, and raise an error if area <= 0


# === TODO: Use argparse.ArgumentParser to set up CLI arguments for --force and --area
# Call the pressure() function with the parsed arguments and print the result


# === Example stub (edit or delete as needed) ===
def pressure(force, area):
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    return force / area


# === TODO: Implement your CLI entry point below ===
# Hint: Use argparse.ArgumentParser(description="...")
#       Add --force and --area as required arguments with type=float
#       Call the pressure() function and print the result formatted nicely


# === TEST YOUR TOOL ===
# if __name__ == "__main__":
#     Run your CLI tool here



























# =======================================================
# Further Reading – Scientific Packages for Pressure
# =======================================================
# These libraries go beyond basic pressure = force / area:

# 1. pint
#    - Handles units and conversions for pressure (Pa, bar, atm)
#    - Example: (100 * ureg.newton) / (2 * ureg.square_meter)

# 2. scipy.constants
#    - Provides constants like atmosphere, Pascal, etc.
#    - Useful for scientific accuracy and conversions

# These are optional but great for advanced work!
# =======================================================
