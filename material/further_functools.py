"""
Functools Cheat Sheet – Code Demos for Scientific Python
Each block includes:
- Tool name
- Purpose
- Example use case
"""

import functools

# ---------------------------------------------
# 1. partial – Fix some function arguments
# Use case: Predefine a specific power/exponent
# ---------------------------------------------

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print("partial – square(5):", square(5))  # 25
print("partial – cube(2):", cube(2))      # 8


# ---------------------------------------------
# 2. reduce – Fold a sequence into one value
# Use case: Product of a range, cumulative logic
# ---------------------------------------------

def factorial(n):
    return functools.reduce(lambda a, b: a * b, range(1, n + 1), 1)

print("reduce – factorial(5):", factorial(5))  # 120


# ---------------------------------------------
# 3. lru_cache – Cache expensive recursive calls
# Use case: Memoize Fibonacci or API results
# ---------------------------------------------

@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("lru_cache – fib(10):", fib(10))         # 55
print("lru_cache – cache info:", fib.cache_info())


# ---------------------------------------------
# 4. singledispatch – Type-specific function behavior
# Use case: Handle lists vs. numbers cleanly
# ---------------------------------------------

@functools.singledispatch
def describe(x):
    return f"Generic object: {x}"

@describe.register(int)
def _(x):
    return f"Integer: {x}"

@describe.register(list)
def _(x):
    return f"List of length {len(x)}"

print("singledispatch – describe(42):", describe(42))           # Integer
print("singledispatch – describe([1,2,3]):", describe([1, 2, 3])) # List


# ---------------------------------------------
# 5. wraps – Preserve function info in decorators
# Use case: Decorators for logging or timing
# ---------------------------------------------

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@logger
def analyze():
    """Simulates a data analysis step."""
    print("Analyzing data...")

analyze()
print("wraps – doc preserved:", analyze.__doc__)


# ---------------------------------------------
# 6. total_ordering – Auto-fill rich comparisons
# Use case: Sorting or filtering custom objects
# ---------------------------------------------

@functools.total_ordering
class Sample:
    def __init__(self, mass):
        self.mass = mass

    def __eq__(self, other):
        return self.mass == other.mass

    def __lt__(self, other):
        return self.mass < other.mass

s1 = Sample(1.5)
s2 = Sample(2.0)

print("total_ordering – s1 < s2:", s1 < s2)   # True
print("total_ordering – s1 >= s2:", s1 >= s2) # False
