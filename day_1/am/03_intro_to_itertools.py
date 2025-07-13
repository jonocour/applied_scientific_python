"""
02_intro_to_itertools.py
=========================

Introduction to itertools for Scientific Python Workflows

Focus Tools:
------------
- itertools.chain: combine sequences
- itertools.combinations: pairs/triples without repeats
- itertools.groupby: group consecutive items by a key

Optional (see below):
---------------------
- cycle, count, islice, tee, product, permutations

How to run:
-----------
    $ python 02_intro_to_itertools.py
"""

import itertools

# ---------------------------------------------
# 1. chain – Combine Multiple Iterables Into One
# Use case: Flattening multiple sequences into a single list
# ---------------------------------------------

a = [1, 2, 3]
b = [4, 5]

combined = list(itertools.chain(a, b))
print("chain – combined:", combined)  # [1, 2, 3, 4, 5]

# Useful when merging data chunks, reading many files, or appending data.


# ---------------------------------------------
# 2. combinations – All Possible Pairs/Triples (No Repeats)
# Use case: Pairwise comparisons, parameter grids, experiments
# ---------------------------------------------

elements = ['A', 'B', 'C']
pairs = list(itertools.combinations(elements, 2))
print("combinations – pairs of 2:", pairs)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Great for exploring parameter spaces, testing all unique pairs, or drawing lots.


# ---------------------------------------------
# 3. groupby – Group Consecutive Items by a Key
# Use case: Summarize sorted data by category/type
# ---------------------------------------------

# Data should be sorted by the same key function
data = [
    ("hydrogen", "nonmetal"),
    ("helium", "noble gas"),
    ("lithium", "metal"),
    ("beryllium", "metal"),
    ("boron", "metalloid")
]

# Sort first by type (the groupby key)
data.sort(key=lambda x: x[1])
for group, items in itertools.groupby(data, key=lambda x: x[1]):
    print(f"groupby – {group}: {[el[0] for el in items]}")

# Ideal for log analysis, grouped results, or quick category summaries.


# ================================
#  Further itertools Tools (Optional Reading)
# ================================

# cycle – Repeat items forever (or until stopped)
print("\ncycle – first 5 colors:")
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors), end=" ")  # red green blue red green

# count – Infinite counting iterator (with step)
print("\n\ncount – next 3 from 10 (step=2):")
counter = itertools.count(start=10, step=2)
print(next(counter), next(counter), next(counter))  # 10 12 14

# islice – Take a slice from an (even infinite) generator
print("\nislice – 5 squared numbers from generator:")
squares = (x**2 for x in itertools.count(1))
print(list(itertools.islice(squares, 5)))  # [1, 4, 9, 16, 25]

# tee – Duplicate an iterator (creates independent copies)
print("\ntee – two independent iterators over the same data:")
data_iter1, data_iter2 = itertools.tee([10, 20, 30])
print("1:", list(data_iter1))  # [10, 20, 30]
print("2:", list(data_iter2))  # [10, 20, 30]

# product – Cartesian product of iterables (all combinations)
print("\nproduct – all possible (a,b) from [1,2] and [x,y]:")
print(list(itertools.product([1, 2], ['x', 'y'])))

# permutations – All possible orderings of a collection
print("\npermutations – of [1,2,3]:")
print(list(itertools.permutations([1, 2, 3])))
