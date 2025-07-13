"""
TASK 04 – Build Your Own Scientific CLI Tool
============================================

Goal:
-----
Practice creating your own command-line interface for a scientific function.

Instructions:
-------------
You will:
1. Define a simple scientific function: `density(mass, volume)`
2. Wrap it in a CLI using a tool of your choice (argparse, Click, or Typer)
3. Run the tool from the terminal with custom parameters

Part 1 – The Function
---------------------
Define a function that computes density using:
    density = mass / volume

Include error handling:
- Raise ValueError if volume is zero or negative

Part 2 – CLI Tool
-----------------
- Let users specify mass and volume via command-line arguments
- Choose a CLI tool you’re comfortable with
    - argparse: basic usage
    - click: nice syntax & validation
    - typer: modern, type-hinted

How to test (once implemented):
-------------------------------
    $ python 04_cli_your_own_tool_task.py --mass 10 --volume 2.5

Or for Click/Typer:
    $ python 04_cli_your_own_tool_task.py calculate --mass 10 --volume 2.5

Optional:
---------
- Format the result with units (e.g., "Density = 4.0 kg/m³")
- Add more features: auto-detect units, scientific notation, etc.
"""

# === TODO: Define a function called `density(mass, volume)` ===
# It should return mass / volume, and raise an error if volume <= 0


# === TODO: Choose a CLI tool (argparse, click, or typer)
# Set up CLI argument parsing for --mass and --volume
# Call the density() function and print the result nicely


# === Example stub (edit this or delete) ===
def density(mass, volume):
    if volume <= 0:
        raise ValueError("Volume must be greater than zero.")
    return mass / volume


# === TODO: Implement your CLI entry point below
# Hint: For argparse, use argparse.ArgumentParser
#       For click, decorate a function with @click.command()
#       For typer, use @app.command() with type hints


# === TEST YOUR TOOL ===
# if __name__ == "__main__":
#     Run your CLI tool





























# =======================================================
# Further Reading – Scientific Packages for Density
# =======================================================
# These libraries go beyond basic density = mass / volume
# and are useful in real scientific and engineering work:

# 1. pint
#    - Handles unit-aware calculations (e.g., kg/L, g/cm³)
#    - Ensures correctness of units and conversions
#    - Example: (10 * ureg.kg) / (2 * ureg.liter)

# 2. scipy.constants
#    - Provides physical constants (e.g., Avogadro, liter, atmosphere)
#    - Useful for conversions and precise scientific computation
#    - Example: Convert liters to cubic meters using `scipy.constants.liter`

# 3. CoolProp
#    - Advanced library for fluid properties (density, enthalpy, etc.)
#    - Used in thermodynamics, chemical engineering
#    - Example: Look up the density of water at a specific temperature and pressure

# These are not needed for this task, but worth exploring!
# =======================================================
