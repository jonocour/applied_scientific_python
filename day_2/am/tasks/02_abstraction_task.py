"""
TASK 03 – Compare Scientific CLI Tools
======================================

Goal:
-----
Use three different CLI tools (`argparse`, `click`, and `typer`) to solve scientific equations via the terminal.

Context:
--------
Each CLI tool is used to solve a scientific formula:

1. Argparse – Force (F = m * a)
2. Click    – Ohm’s Law (V = I * R)
3. Typer    – Kinetic Energy (KE = 0.5 * m * v²)

You will run, explore, and edit these from the existing file:
    `02_using_cli_tools.py`

How to Run:
-----------
$ python 02_using_cli_tools.py argparse --mass 10 --acceleration 9.81
$ python 02_using_cli_tools.py click --current 1.2 --resistance 4.7
$ python 02_using_cli_tools.py typer solve --mass 80 --velocity 2.5

Tasks:
------
"""

# === TODO 1: Run each CLI example from the terminal and observe the output.
#             (Do this from the terminal, not inside Python.)
#             What do you notice about the syntax differences?

# === TODO 2: Choose ONE of the three examples and replace the equation.
#             Example ideas:
#               - kinetic energy (if it wasn’t used)
#               - voltage, density, speed
#               - or anything you’re familiar with from your scientific background

# === TODO 3: Update the variable names, descriptions, and print statement accordingly.

# === TODO 4 (optional): Add a fourth CLI mode (e.g., 'custom') to handle your own formula.
#             - Add a new `def run_custom():` function
#             - Add an elif block to the mode selector
#             - Use any CLI library you like!

# === Example starter function if needed:
def calculate_density(mass, volume):
    return mass / volume

# === Note:
# You can edit just one function (e.g., run_click) if you prefer to focus on a single CLI tool.
