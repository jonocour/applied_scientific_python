"""
TASK 03 – Real-World Data Processing with a CLI Tool
====================================================

Goal:
-----
Build a command-line tool that processes a data file (CSV) using **argparse, Click, or Typer**.

Scenario:
---------
You are working with material property data stored in CSV files.
Each row contains measured or recorded values like mass, volume, density, or other properties.

You will:
1. Write a function that reads a CSV file and processes its rows
2. Perform a calculation or check on each row
3. Print meaningful results to the console

Part 1 – Provided Function (Example)
------------------------------------
- Define a function that reads a CSV file and checks each row for missing density
- If density is missing, calculate it using:
    density = mass / volume

Include basic error handling:
- Handle zero or negative volume
- Handle missing fields

Part 2 – Your Own Function (From Your Field)
---------------------------------------------
- Define your own simple processing function based on your background
- Example ideas (but pick your own):
    - Calculate BMI from weight and height
    - Convert temperature units
    - Flag unusually high readings

Part 3 – CLI Tool (You Choose)
------------------------------
- Use **argparse, Click, or Typer**
- The CLI should accept at least:
    --input   (Path to CSV file)

Optional:
- Allow users to specify which function they want to run (e.g., --mode density or --mode custom)
- Allow output to a new file

How to test:
------------
$ python 03_extra_task.py --input materials.csv

Optional Enhancements:
----------------------
- Add summary statistics (averages, counts)
- Handle multiple calculation modes
- Write results back to a file

"""

# === TODO: Define a function to process a CSV file and calculate density if missing ===
# Hint:
#   - Use csv.DictReader to read the input file row by row
#   - For each row, check if 'density_kg_m3' is missing or zero
#   - If missing, calculate density = mass_kg / volume_m3
#   - Handle cases where volume is zero or missing (skip or flag)
#   - Print each processed row with updated values (or collect them for output)


# === Example helper function (you may edit or delete) ===
import csv


def read_csv_file(file_path):
    """Reads a CSV file and returns a list of rows as dictionaries."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows

# Hint:
#   - Use read_csv_file() to load your data
#   - Loop over the rows and apply your calculations or checks
#   - You can print results directly or collect them for later output


# === TODO: Implement CLI argument parsing with argparse, Click, or Typer ===
# Hint:
#   - Accept at least --input (CSV file path) as a required argument
#   - Optional: Add --output to write results to a file
#   - Call your CSV processing function with the parsed arguments
#   - Optional: Add flags to control behavior (e.g., --summary)


# =======================================================
# Extra Goals

# === TODO: Define your own processing function based on a task YOU choose ===
# Examples (but you must choose your own):
#   - Flag values above a threshold
#   - Convert between units
#   - Apply a formula from your field


# === TODO: Set up CLI parsing with argparse, Click, or Typer ===
# Accept at least --input to specify the CSV file
# Call one or both of your processing functions based on CLI arguments


# === TODO: Test your tool with a CSV file of your choice ===
# Example:
# if __name__ == "__main__":
#     Run your CLI tool here


# =======================================================
# Sample CSV Data Format
# =======================================================
# Save as: materials.csv
#
# material,mass_kg,volume_m3,density_kg_m3
# Steel,10,1,
# Aluminum,5,2,2.5
# Copper,8,0.5,
#
# =======================================================


# =======================================================
# Further Reading – Working with Data in Python
# =======================================================
# pandas – For advanced data analysis and manipulation
# pathlib – For safer file path handling

# =======================================================
