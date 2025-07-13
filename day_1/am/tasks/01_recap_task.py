"""
TASK 01 – Team Exercise: Data Processing Pipeline
Goal: Practice generators, functions, and comprehensions
File: data.txt (one float per line)
Instructions:
- Fill in the missing code under each function stub
- Work as a team: discuss design choices and edge cases
"""

# 1. Write a generator function to stream numbers from a file
def stream_numbers(filename):
    """Yield float values from each line in a file."""
    # TODO: Open the file and yield each number as a float
    pass


# 2. Filter values greater than or equal to a given threshold
def filter_values(data, threshold):
    """Return only values >= threshold."""
    # TODO: Use a list comprehension
    pass


# 3. Square all values in a list
def square_all(data):
    """Return a new list with all values squared."""
    # TODO: Use a list comprehension
    pass


# 4. Compute the average of a list of numbers
def average(data):
    """Return the average (mean) of the data."""
    # TODO: Return sum / count; watch for divide-by-zero!
    pass


# === MAIN PIPELINE ===
if __name__ == "__main__":
    # TEAM INSTRUCTION:
    # 1. Create a sample 'data.txt' file with ~10 float values (e.g., 5.0, 10.0, 15.5, ...)
    # 2. Adjust the threshold value if needed

    filename = "data.txt"
    threshold = 10

    data_stream = stream_numbers(filename)
    filtered = filter_values(data_stream, threshold)
    squared = square_all(filtered)
    avg = average(squared)

    print(f"Filtered values >= {threshold}:", filtered)
    print("Squared values:", squared)
    print("Average of squared values:", avg)
