"""
01_recap.py
==========================

Recap of Python Basics for Scientific Computing

Topics:
-------
- Variables & basic types
- Core collections & comprehensions
- Simple functions & lambdas
- Generator expressions

How to run:
-----------
    $ python 01_recap_python_basics.py
"""

# ---------------------------------------------
# 1. VARIABLES & BASIC TYPES
# Use case: Storing different types of data
# ---------------------------------------------

int_var = 42                   # Integer
float_var = 3.14               # Float
str_var = "Science"            # String (immutable)
bool_var = True                # Boolean (for conditionals, logic)

# Python is dynamically typed (type is set by assignment), but strongly typed (won't auto-convert types!)
# Try this and see what happens:
# print(int_var + str_var)   # Raises a TypeError

# ---------------------------------------------
# 2. COLLECTIONS
# Use case: Grouping related data
# ---------------------------------------------

# Lists – mutable, ordered
data_list = [1, 2, 3, 4]

# Tuples – immutable, ordered
data_tuple = (1, 2, 3, 4)

# Sets – unordered, unique elements
data_set = {1, 2, 3, 4, 4}     # Duplicate 4 will be dropped

# Dictionaries – key-value store
data_dict = {"H": 1, "He": 2}

# Mini Challenge:
# Add another element to data_dict, then print keys and values
# Example:
# data_dict["Li"] = 3
# print("dict keys:", list(data_dict.keys()))
# print("dict values:", list(data_dict.values()))

# ---------------------------------------------
# 3. COMPREHENSIONS
# Use case: Build new collections in a single readable line
# ---------------------------------------------

# List comprehension – create list of squares
squares = [x ** 2 for x in data_list]

# Dictionary comprehension – map number to its square
square_map = {x: x ** 2 for x in data_list}

# Set comprehension – filter for even numbers only
even_set = {x for x in data_list if x % 2 == 0}

# Best Practice: Prefer comprehensions over for-loops for clarity and conciseness!

# ---------------------------------------------
# 4. GENERATORS
# Use case: Efficient, lazy iteration (memory-friendly)
# ---------------------------------------------

# Generator expression – does NOT build the full list in memory
square_gen = (x ** 2 for x in data_list)

# Tip: You can only loop through a generator ONCE!

# ---------------------------------------------
# 5. SIMPLE FUNCTIONS & LAMBDAS
# Use case: Code reuse and clarity
# ---------------------------------------------

def add(a, b):
    """Add two numbers."""
    return a + b

# Lambda function – inline, anonymous function (often used in sorting, filtering, etc.)
multiply = lambda x, y: x * y

# Mini Challenge:
# Convert the lambda above to a named function:
# def multiply(x, y):
#     return x * y

# ---------------------------------------------
# MAIN EXECUTION BLOCK – Examples & Output
# ---------------------------------------------

if __name__ == "__main__":
    print("squares:", squares)
    print("square_map:", square_map)
    print("even_set:", even_set)

    # Using next() to get the first value from the generator
    print("first of gen:", next(square_gen))

    # Reminder: Generators are consumed once!
    print("remaining from gen:", list(square_gen))

    print("add(2, 3):", add(2, 3))
    print("multiply(2, 3):", multiply(2, 3))

    # Mini Challenge:
    # Write a function that takes a list of numbers and returns only the odd values squared
    # Example starter:
    # def odd_squares(nums):
    #     return [x ** 2 for x in nums if x % 2 == 1]
    # print("odd squares:", odd_squares([1,2,3,4,5]))
