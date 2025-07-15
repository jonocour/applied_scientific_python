"""
02_using_cli_tools.py
======================

Comparing Python CLI Tools for Scientific Scripts
-------------------------------------------------

Goal:
-----
- Use CLI tools to parse scientific parameters and solve equations
- Show usage of: argparse, Click, and Typer

How to run:
-----------
(1) Argparse Example – Force
    $ python 02_using_cli_tools.py argparse --mass 2.5 --acceleration 9.8

(2) Click Example – Ohm's Law
    $ python 02_using_cli_tools.py click --current 2.0 --resistance 5.5

(3) Typer Example – Kinetic Energy
    $ python 02_using_cli_tools.py typer solve --mass 70 --velocity 3.2

Notes:
------
- Each subcommand demonstrates a different CLI tool
- Designed for scientific tasks using common equations
"""

import sys


# =======================================================
# 1. ARGPARSE EXAMPLE – F = m * a
# =======================================================

def run_argparse():
    import argparse

    parser = argparse.ArgumentParser(description="Calculate force using F = m * a")
    parser.add_argument("--mass", type=float, required=True, help="Mass in kg")
    parser.add_argument("--acceleration", type=float, required=True, help="Acceleration in m/s^2")

    args = parser.parse_args(sys.argv[2:])  # Skip first 2 CLI args: script name and 'argparse'

    force = args.mass * args.acceleration
    print(f"[Argparse] Force = {force:.2f} N")


# =======================================================
# 2. CLICK EXAMPLE – Ohm's Law: V = I * R
# =======================================================

# ...
def run_click():
    import click

    @click.command()
    @click.option("--current", type=float, required=True, help="Current in Amperes (I)")
    @click.option("--resistance", type=float, required=True, help="Resistance in Ohms (R)")
    def solve(current, resistance):
        voltage = current * resistance
        print(f"[Click] Voltage = {voltage:.2f} V")

    solve(args=sys.argv[2:], standalone_mode=False)


# =======================================================
# 3. TYPER EXAMPLE – Kinetic Energy: KE = 0.5 * m * v^2
# =======================================================

import sys
import typer

def run_typer():
    app = typer.Typer()

    @app.command()
    def solve(
        mass: float = typer.Option(..., "--mass", "-m", help="Mass in kg"),
        velocity: float = typer.Option(..., "--velocity", "-v", help="Velocity in m/s"),
    ):
        ke = 0.5 * mass * velocity ** 2
        typer.echo(f"[Typer] Kinetic Energy = {ke:.2f} J")

    app(prog_name="typer", args=sys.argv[3:])


# =======================================================
# MAIN ENTRY – Use CLI Tool Based on First Argument
# =======================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  python 02_using_cli_tools.py [argparse|click|typer] ...")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "argparse":
        run_argparse()
    elif mode == "click":
        run_click()
    elif mode == "typer":
        run_typer()
    else:
        print(f"Unknown mode '{mode}'. Use 'argparse', 'click', or 'typer'.")
