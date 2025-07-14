"""
02_intro_to_itertools.py
=========================

Introduction to itertools for Scientific Python Workflows

Focus Tools:
------------
- itertools.product: Cartesian product (all combinations)
- itertools.chain: combine sequences
- itertools.combinations: pairs/triples without repeats
- itertools.groupby: group consecutive items by a key

Optional (below):
-----------------
- cycle, count, islice, tee, permutations

How to run:
-----------
    $ python 02_intro_to_itertools.py
"""

import itertools

# ---------------------------------------------
# 1. product – Cartesian Product of Iterables
# Use case: Parameter sweeps, state space exploration, combinations
# ---------------------------------------------

from itertools import product

# Example 1: Spin configurations (Quantum Mechanics)
spins = ['↑', '↓']
print("Spin configurations (3 particles):")
for config in product(spins, repeat=3):
    print("Configuration:", config)

# Example 2: Parameter sweep in an experiment
learning_rates = [0.01, 0.1]
epochs = [10, 50]
print("\nParameter combinations (Grid Search):")
for lr, epoch in product(learning_rates, epochs):
    print(f"Training with lr={lr}, epochs={epoch}")

# Example 3: Cartesian product of numbers and letters
print("\nproduct – all possible (a,b) from [1,2] and [x,y]:")
print(list(product([1, 2], ['x', 'y'])))


# ---------------------------------------------
# 2. chain – Combine Multiple Iterables Into One
# Use case: Flattening multiple sequences into a single list
# ---------------------------------------------

a = [1, 2, 3]
b = [4, 5]
combined = list(itertools.chain(a, b))
print("\nchain – combined:", combined)


# ---------------------------------------------
# 3. combinations – All Possible Pairs/Triples (No Repeats)
# Use case: Pairwise comparisons, parameter grids, experiments
# ---------------------------------------------

elements = ['A', 'B', 'C']
pairs = list(itertools.combinations(elements, 2))
print("\ncombinations – pairs of 2:", pairs)


# ---------------------------------------------
# 4. groupby – Group Consecutive Items by a Key
# Use case: Summarize sorted data by category/type
# ---------------------------------------------

data = [
    ("hydrogen", "nonmetal"),
    ("helium", "noble gas"),
    ("lithium", "metal"),
    ("beryllium", "metal"),
    ("boron", "metalloid")
]

data.sort(key=lambda x: x[1])

print("\ngroupby – grouped elements:")
for group, items in itertools.groupby(data, key=lambda x: x[1]):
    print(f"{group}: {[el[0] for el in items]}")


# ================================
#  Further itertools Tools (Optional Reading)
# ================================

# cycle – Repeat items forever (or until stopped)
print("\ncycle – first 5 colors:")
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors), end=" ")  # Output: red green blue red green

# count – Infinite counting iterator (with step)
print("\n\ncount – next 3 from 10 (step=2):")
counter = itertools.count(start=10, step=2)
print(next(counter), next(counter), next(counter))  # Output: 10 12 14

# islice – Take a slice from an (even infinite) generator
print("\nislice – 5 squared numbers from generator:")
squares = (x**2 for x in itertools.count(1))
print(list(itertools.islice(squares, 5)))  # Output: [1, 4, 9, 16, 25]

# tee – Duplicate an iterator (creates independent copies)
print("\ntee – two independent iterators over the same data:")
data_iter1, data_iter2 = itertools.tee([10, 20, 30])
print("1:", list(data_iter1))
print("2:", list(data_iter2))

# permutations – All possible orderings of a collection
print("\npermutations – of [1,2,3]:")
print(list(itertools.permutations([1, 2, 3])))
