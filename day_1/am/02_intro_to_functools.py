"""
02_intro_to_functools.py
=========================

Introduction to functools for Reusable Scientific Code

Topics:
-------
- functools.partial: create functions with fixed arguments
- functools.reduce: accumulate values in a sequence
- functools.lru_cache: memoization for performance

How to run:
-----------
    $ python 02_intro_to_functools.py
"""

import functools

# ---------------------------------------------
# 1. PARTIAL FUNCTIONS – Fix Some Arguments Now, Fill in the Rest Later
# Use case: Create reusable function "templates" for later
# ---------------------------------------------

def power(base, exponent):
    """Raise base to the given exponent."""
    return base ** exponent

# Create new functions with the 'exponent' argument pre-filled:
square = functools.partial(power, exponent=2)
cube   = functools.partial(power, exponent=3)

# Example: Fixing parameters is handy for scientific curve fits, custom normalizations, etc.

# ---------------------------------------------
# 2. REDUCE – Accumulate Values in a Sequence
# Use case: Combine a list into a single result (product, sum, etc.)
# ---------------------------------------------

def factorial(n):
    """Compute factorial (product of all integers from 1 to n) using reduce."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    return functools.reduce(lambda a, b: a * b, range(1, n + 1), 1)

# ✅ Good for mathematical operations: cumulative sums, products, logical AND/OR, etc.

# Mini Challenge:
# Replace the lambda in reduce with a named function called multiply(a, b).
# Try:
# def multiply(a, b): return a * b
# Then: functools.reduce(multiply, ...)

# ---------------------------------------------
# 3. LRU CACHE – Remember Function Results (Memoization)
# Use case: Speed up recursive or expensive calculations
# ---------------------------------------------

@functools.lru_cache(maxsize=128)
def fib(n):
    """Compute Fibonacci number efficiently by caching previous results."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Great for recursive algorithms (Fibonacci, pathfinding), or when querying slow data sources.
# Use with care for large inputs – watch memory usage!

# Mini Challenge:
# Add print(f"fib({n})") inside fib() to see how often it’s called.
# Compare output with and without @lru_cache to see the effect.

# Bonus Tip:
# Clear the cache anytime with: fib.cache_clear()

# ---------------------------------------------
# MAIN EXECUTION BLOCK (Sample Usage & Output)
# ---------------------------------------------

if __name__ == "__main__":
    print("== partial() ==")
    print("square(5):", square(5))    # 25
    print("cube(4):", cube(4))        # 64

    print("\n== reduce() ==")
    print("factorial(6):", factorial(6))  # 720

    print("\n== lru_cache() ==")
    print("fib(10):", fib(10))        # 55

    # Bonus: Check cache statistics (hits/misses)
    print("fib.cache_info():", fib.cache_info())

    # Uncomment for Mini Challenge:
    # def multiply(a, b): return a * b
    # print(functools.reduce(multiply, range(1, 7), 1))

    # To reset Fibonacci cache (if experimenting):
    # fib.cache_clear()
