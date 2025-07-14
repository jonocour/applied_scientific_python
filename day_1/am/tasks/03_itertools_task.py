"""
TASK 03 – Solo Practice with itertools
Goal: Use itertools tools for structured iteration and grouping

Focus Tools:
- chain
- combinations
- groupby

Instructions:
- Fill in the missing code below
- Use the examples to test your understanding
"""

import itertools

# 1. Use chain to flatten two lists
# Example: [1, 2] and [3, 4] → [1, 2, 3, 4]
def flatten_lists(a, b):
    """Combine two lists into one using itertools.chain."""
    # TODO: Use itertools.chain and convert to a list

    pass


# 2. Use combinations to generate all unique 2-element pairs
# Example: ['A', 'B', 'C'] → [('A','B'), ('A','C'), ('B','C')]
def all_pairs(elements):
    """Return all 2-item combinations from the input list."""
    # TODO: Use itertools.combinations
    pass


# 3. Use groupby to group a list of (label, value) tuples by label
# Input must be sorted by the key (label)
# Example: [('A', 1), ('A', 2), ('B', 3)] → {'A': [1, 2], 'B': [3]}
def group_by_label(pairs):
    """Group (label, value) tuples into a dict of lists."""
    # TODO:
    # 1. Sort the input by label
    # 2. Use itertools.groupby
    # 3. Collect results into a dictionary
    pass


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    print("=== CHAIN ===")
    # print(flatten_lists([1, 2], [3, 4]))  # Expected: [1, 2, 3, 4]

    print("\n=== COMBINATIONS ===")
    # print(all_pairs(['A', 'B', 'C']))     # Expected: [('A','B'), ('A','C'), ('B','C')]

    print("\n=== GROUPBY ===")
    example_data = [
        ('hydrogen', 'nonmetal'),
        ('helium', 'noble gas'),
        ('lithium', 'metal'),
        ('beryllium', 'metal'),
        ('boron', 'metalloid'),
    ]
    # print(group_by_label(example_data))
    # Expected: {
    #   'metalloid': ['boron'],
    #   'metal': ['lithium', 'beryllium'],
    #   'noble gas': ['helium'],
    #   'nonmetal': ['hydrogen']
    # }
