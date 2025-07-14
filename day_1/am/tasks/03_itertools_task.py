import itertools

# 1. Use chain to flatten two lists
# Example: [1, 2] and [3, 4] → [1, 2, 3, 4]
def flatten_lists(a, b):
    """Combine two lists into one using itertools.chain."""
    return list(itertools.chain(a, b))


# 2. Use combinations to generate all unique 2-element pairs
# Example: ['A', 'B', 'C'] → [('A','B'), ('A','C'), ('B','C')]
def all_pairs(elements):
    """Return all 2-item combinations from the input list."""
    return list(itertools.combinations(elements, 2))


# 3. Use groupby to group a list of (value, label) tuples by label
# Input must be sorted by the key (label)
# Example: [('A', 1), ('A', 2), ('B', 3)] → {'A': [1, 2], 'B': [3]}
def group_by_label(pairs):
    """Group (value, label) tuples into a dict of lists."""
    # 1. Sort the input by the label (second element)
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    # 2. Use groupby on the sorted sequence, keyed by label
    result = {}
    for label, group in itertools.groupby(sorted_pairs, key=lambda x: x[1]):
        # 3. Collect all the values (first element) for this label
        result[label] = [value for value, _ in group]
    return result


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    print("=== CHAIN ===")
    print(flatten_lists([1, 2], [3, 4]))

    print("\n=== COMBINATIONS ===")
    print(all_pairs(['A', 'B', 'C']))

    print("\n=== GROUPBY ===")
    example_data = [
        ('hydrogen', 'nonmetal'),
        ('helium', 'noble gas'),
        ('lithium', 'metal'),
        ('beryllium', 'metal'),
        ('boron', 'metalloid'),
    ]
    print(group_by_label(example_data))
