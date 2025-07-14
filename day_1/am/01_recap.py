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
# Squares of even numbers from a list

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

def countdown(n):
    # A generator function that counts down from n to 1
    while n > 0:
        yield n   # Yield returns the next value and pauses the function here
        n -= 1    # State is preserved until the next call

# Using the generator
for num in countdown(5):
    print(num)

# Advantages of using a generator:
# - Generates numbers one at a time (lazy evaluation) — saves memory
# - You don’t need to create a full list like [5, 4, 3, 2, 1] in memory
# - Ideal for large ranges or streams of data
# - Execution can be paused and resumed — useful for pipelines
# - Cleaner and more efficient than managing state manually with a loop and a list
# Tip: You can only loop through a generator ONCE!

# ---------------------------------------------
# 5. SIMPLE FUNCTIONS & LAMBDAS
# Use case: Code reuse and clarity
# ---------------------------------------------

def add(a, b):
    """Add two numbers."""
    return a + b

# ---------------------------------------------
# Lambda Functions – inline, anonymous functions
# Often used in sorting, filtering, simple operations
# ---------------------------------------------

# Example 1 – Multiply two numbers with a lambda
multiply = lambda x, y: x * y
print("multiply (lambda):", multiply(3, 4))  # Output: 12

# Example 2 – Sort a list of tuples by the second element using lambda
data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_data = sorted(data, key=lambda item: item[1])
print("sorted data (lambda):", sorted_data)  # Output: [(3, 'a'), (1, 'b'), (2, 'c')]

# Example 3 – Filter even numbers from a list using lambda
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("even numbers (lambda):", evens)  # Output: [2, 4, 6]

# ---------------------------------------------
# Mini Challenge – Convert lambdas to named functions
# ---------------------------------------------

# Named version of multiply
def multiply_named(x, y):
    return x * y

print("multiply_named:", multiply_named(3, 4))  # Output: 12

# Named key function for sorting
def get_second(item):
    return item[1]

sorted_data_named = sorted(data, key=get_second)
print("sorted_data_named:", sorted_data_named)  # Output: [(3, 'a'), (1, 'b'), (2, 'c')]

# Named filter function for even numbers
def is_even(x):
    return x % 2 == 0

evens_named = list(filter(is_even, nums))
print("evens_named:", evens_named)  # Output: [2, 4, 6]









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
