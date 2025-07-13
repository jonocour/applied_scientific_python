"""
03_compare_perf_numpy_vs_loop.py
=================================

Goal:
-----
Compare the performance of three approaches to a large numerical task:
    - Pure Python loop (slow)
    - NumPy vectorized (fast)
    - Multiprocessing with Pool.map()

Why This Matters:
-----------------
In scientific computing and data analysis, code performance is often critical.
Looping over millions of rows in Python can be painfully slow.
This tutorial helps you decide:
    - When to use NumPy
    - When to parallelize
    - When to consider Cython

What is Vectorization?
----------------------
Vectorization means applying an operation to an entire array or column
**without writing a loop yourself**. Under the hood, NumPy calls fast C code.

What is Multiprocessing?
------------------------
The `multiprocessing` module lets you **parallelize CPU-bound tasks** across multiple CPU cores.
A `Pool` manages worker processes. You can:
    - Use `.map()` to apply a function to all items in parallel
    - Use `.starmap()` to handle multiple arguments
    - Use `.apply_async()` for async job handling

What Is the GIL? (Global Interpreter Lock)
------------------------------------------
Python's GIL prevents **multiple native threads** from executing Python bytecode at the same time.
This means:
    - Threads are great for IO-bound tasks (e.g., file reads, HTTP)
    - Threads are *bad* for CPU-bound work like math or simulations
    - Multiprocessing avoids the GIL by spawning new processes instead of threads

What is Cython? (Preview)
--------------------------
Cython compiles Python-like code to C for performance.
It's ideal when:
    - You’ve profiled and found a hot loop
    - NumPy can't vectorize what you need
    - You want to interoperate with C/C++ libraries

We'll focus here on NumPy and multiprocessing — Cython comes next.

How to Run:
-----------
    $ python 03_compare_perf_numpy_vs_loop.py

What to Expect:
---------------
    - Python loop: 5–15 seconds
    - NumPy: under 0.1 second
    - Multiprocessing: better than loop, slower than NumPy
"""

import time
import numpy as np
from multiprocessing import Pool

# ---------------------------------------------
# SETUP: Create synthetic data
# ---------------------------------------------
# We'll square 10 million random floats between 0 and 1
N = 10_000_000
data = np.random.rand(N)

# ---------------------------------------------
# METHOD 1: Pure Python loop (slowest)
# ---------------------------------------------
def slow_square(arr):
    """
    Loop through values one by one and square them.
    Python is slow because:
        - No native optimization
        - Runs in interpreted mode
        - High loop overhead
    """
    out = []
    for x in arr:
        out.append(x ** 2)
    return out

# ---------------------------------------------
# METHOD 2: NumPy vectorized (fastest baseline)
# ---------------------------------------------
def numpy_square(arr):
    """
    NumPy uses fast C loops under the hood.
    Entire arrays are processed at once with no Python loop.
    """
    return arr ** 2

# ---------------------------------------------
# METHOD 3: Multiprocessing (spread Python loop across cores)
# ---------------------------------------------
def square(x):
    return x ** 2

def parallel_square(arr):
    """
    Uses multiprocessing.Pool to parallelize the loop.
    Slower than NumPy, but faster than pure Python in some cases.

    Notes:
    - Multiprocessing adds overhead for splitting and collecting work.
    - Not great for small tasks; best when each unit of work is heavy.
    """
    with Pool() as pool:
        return pool.map(square, arr)

# ---------------------------------------------
# BENCHMARKING TOOL
# ---------------------------------------------
def benchmark(func, *args):
    """
    Time how long a function takes.
    """
    print(f"\nRunning: {func.__name__}")
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__:<20} took {end - start:.4f} sec")
    return result

# ---------------------------------------------
# RUN BENCHMARKS
# ---------------------------------------------
if __name__ == "__main__":
    print("Benchmarking different approaches to squaring 10 million values...")

    # Convert NumPy to list for fair test with slow/parallel
    python_data = data.tolist()

    # === TEST 1: Pure Python loop
    benchmark(slow_square, python_data)

    # === TEST 2: NumPy vectorized (fastest baseline)
    benchmark(numpy_square, data)

    # === TEST 3: Multiprocessing over Python loop
    benchmark(parallel_square, python_data)

    print("\nSummary:")
    print("- NumPy is almost always the best first step.")
    print("- Multiprocessing helps when you're stuck in Python loops.")
    print("- Cython can be considered when both of the above aren't enough.")
