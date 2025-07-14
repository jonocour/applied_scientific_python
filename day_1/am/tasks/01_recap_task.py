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
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # skip blank lines
                yield float(line)


# 2. Filter values greater than or equal to a given threshold
def filter_values(data, threshold):
    """Return only values >= threshold."""
    return [x for x in data if x >= threshold]


# 3. Square all values in a list
def square_all(data):
    """Return a new list with all values squared."""
    return [x * x for x in data]


# 4. Compute the average of a list of numbers
def average(data):
    """Return the average (mean) of the data."""
    if not data:
        return None  # or float('nan'), or raise ValueError
    return sum(data) / len(data)



# === MAIN PIPELINE ===
if __name__ == "__main__":
    # TEAM INSTRUCTION:
    # 1. Create a sample 'data.txt' file with ~10 float values (e.g., 5.0, 10.0, 15.5, ...)
    # 2. Adjust the threshold value if needed

    # 1. Assuming data.txt doesn't exist..
    sample_values = [5.0, 10.0, 15.5, 2.3, 9.9, 10.0, 12.1, 8.8, 20.0, 0.0]
    with open("data.txt", "w") as f:
        for v in sample_values:
            f.write(f"{v}\n")

    filename = "data.txt"
    threshold = 10

    # stream → filter → square → average
    data_stream = stream_numbers(filename)
    filtered = filter_values(data_stream, threshold)
    squared = square_all(filtered)
    avg = average(squared)

    print(f"Filtered values >= {threshold}:", filtered)
    print("Squared values:", squared)
    print("Average of squared values:", avg)
