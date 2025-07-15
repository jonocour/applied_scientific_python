"""
02_create_your_own_argparse_task.py
===================================

Build Your Own Scientific CLI Tool (Argparse)

Usage:
    python 02_create_your_own_argparse_task.py --force 100 --area 5
"""

import argparse
import sys

# === Part 1: The Function ===
def pressure(force, area):
    """Compute pressure = force / area, with error checks."""
    if area <= 0:
        raise ValueError("Area must be greater than zero.")
    if force < 0:
        raise ValueError("Force must be non-negative.")
    return force / area


# === Part 2: CLI Entry Point ===
def main():
    parser = argparse.ArgumentParser(
        description="Calculate pressure using P = force / area"
    )
    parser.add_argument(
        "--force", "-f",
        type=float,
        required=True,
        help="Force in Newtons (N)"
    )
    parser.add_argument(
        "--area", "-a",
        type=float,
        required=True,
        help="Area in square meters (m²)"
    )

    args = parser.parse_args()

    try:
        p = pressure(args.force, args.area)
    except ValueError as e:
        parser.error(str(e))

    if abs(p) >= 1e4 or (abs(p) > 0 and abs(p) < 1e-2):
        out = f"{p:.2e}"
    else:
        out = f"{p:.2f}"

    print(f"Pressure = {out} Pascals (Pa)")


if __name__ == "__main__":
    main()
