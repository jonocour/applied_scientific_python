"""
TASK 02 – Solo Practice with functools
Goal: Apply partial, reduce, and lru_cache to common scientific patterns

Instructions:
- Complete each function where marked
- Test your implementation at the bottom
"""

import functools

# 1. Use partial to convert Celsius to Kelvin
def convert(temp, offset):
    """Add an offset to a temperature value."""
    return temp + offset  # This is provided for clarity

# TODO: Use functools.partial to create a function 'c_to_k' that adds 273.15
# Example: c_to_k(25) => 298.15
# Your code here:
# c_to_k = ...



# 2. Use reduce to multiply all even numbers in a list
def even_product(numbers):
    """Multiply all even numbers in a list using reduce."""
    # TODO:
    # 1. Filter only even numbers from the input
    # 2. Use functools.reduce to multiply them
    pass



# 3. Use lru_cache to memoize a recursive Fibonacci function
# TODO: Decorate this function with @lru_cache (maxsize=64)
# Then implement a standard recursive Fibonacci calculation
def fib(n):
    """Compute nth Fibonacci number with caching."""
    pass



# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    print("=== PARTIAL ===")
    # print("c_to_k(25):", c_to_k(25))  # Uncomment once implemented

    print("\n=== REDUCE ===")
    # print("even_product([2, 3, 4, 5]):", even_product([2, 3, 4, 5]))

    print("\n=== LRU_CACHE ===")
    # print("fib(10):", fib(10))
    # Optional: print("fib.cache_info():", fib.cache_info())
