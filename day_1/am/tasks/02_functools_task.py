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
    return temp + offset

# Create c_to_k by fixing offset = 273.15
c_to_k = functools.partial(convert, offset=273.15)


# 2. Use reduce to multiply all even numbers in a list
def even_product(numbers):
    """Multiply all even numbers in a list using reduce."""
    evens = [n for n in numbers if n % 2 == 0]
    # Identity for multiplication is 1
    return functools.reduce(lambda x, y: x * y, evens, 1)


# 3. Use lru_cache to memoize a recursive Fibonacci function
@functools.lru_cache(maxsize=64)
def fib(n):
    """Compute nth Fibonacci number with caching."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    print("=== PARTIAL ===")
    print("c_to_k(25):", c_to_k(25))

    print("\n=== REDUCE ===")
    print("even_product([2, 3, 4, 5]):", even_product([2, 3, 4, 5]))

    print("\n=== LRU_CACHE ===")
    print("fib(10):", fib(10))
    print("fib.cache_info():", fib.cache_info())
