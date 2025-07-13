"""
03_debugging_tools.py

Debugging Scientific Python Code
================================

Goals:
- Learn to identify and investigate bugs using built-in tools
- Apply three common techniques:
    1. print() for simple tracing
    2. traceback for clean stack traces
    3. pdb for interactive, step-through debugging
"""

# =======================================================
# 1. TRACEBACK – Print a full error trace when exceptions happen
# =======================================================

def divide(a, b):
    return a / b   # Will raise ZeroDivisionError if b == 0

def wrapper():
    try:
        return divide(10, 0)  # This triggers an exception
    except ZeroDivisionError:
        import traceback
        traceback.print_exc()  #  Prints a clean, formatted traceback
        # Great for logging errors in scripts or analysis pipelines


# =======================================================
# 2. PRINT DEBUGGING – Quick sanity checks inside logic
# =======================================================

def mean(values):
    total = sum(values)
    print(f"DEBUG: total={total}, count={len(values)}")  #  Manual inspection
    return total / len(values)  #  Will raise ZeroDivisionError if list is empty

# When to use print():
# - During prototyping
# - To check assumptions (e.g., inputs, loop counters, early exits)
# - Avoid for production code — prefer logging


# =======================================================
# 3. PDB – Python Debugger for step-by-step investigation
# =======================================================

def buggy_calc(x, y):
    result = x + y
    import pdb; pdb.set_trace()  # ⏸️ Pauses execution here
    return result * 2

# Once inside the debugger:
# ▶ n  → next line
# ▶ s  → step into a function
# ▶ p  → print a variable (e.g., p result)
# ▶ c  → continue execution
# ▶ q  → quit debugger


# =======================================================
# MAIN SCRIPT EXECUTION – Try all three demos
# =======================================================

if __name__ == "__main__":
    print("== TRACEBACK DEMO ==")
    #  Should trigger a division-by-zero error with a traceback
    wrapper()

    print("\n== PRINT DEBUG DEMO ==")
    #  Will show internal state of 'mean' function
    print("mean([1, 2, 3]):", mean([1, 2, 3]))

    print("\n== PDB DEBUG DEMO ==")
    #  Will pause in the terminal — use keyboard commands (p, n, q, etc.)
    buggy_calc(5, 7)
