"""
05_abc_real_world_mathematical.py
==================================

Real-World Example: Abstract Base Class for Mathematical Models

Focus:
------
- How to use ABCs for reusable, extendable mathematical modeling
- Example: Abstract MathematicalModel base class for different formulas
"""

import abc

# ---------------------------------------------
# 1. Abstract Mathematical Model Framework
# ---------------------------------------------

class MathematicalModel(abc.ABC):
    """Abstract base class for mathematical models."""

    @abc.abstractmethod
    def evaluate(self, x):
        """Evaluate the model at input x. Must be implemented."""
        pass

    @abc.abstractmethod
    def __str__(self):
        """Return a string representation of the model."""
        pass

# ---------------------------------------------
# 2. Concrete Implementation: Linear Model (y = mx + b)
# ---------------------------------------------

class LinearModel(MathematicalModel):
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def evaluate(self, x):
        return self.m * x + self.b

    def __str__(self):
        return f"LinearModel: y = {self.m}x + {self.b}"

# ---------------------------------------------
# 3. Concrete Implementation: Quadratic Model (y = ax^2 + bx + c)
# ---------------------------------------------

class QuadraticModel(MathematicalModel):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x):
        return self.a * x**2 + self.b * x + self.c

    def __str__(self):
        return f"QuadraticModel: y = {self.a}x² + {self.b}x + {self.c}"

# ---------------------------------------------
# 4. Usage Example
# ---------------------------------------------

if __name__ == "__main__":
    models = [
        LinearModel(m=2.0, b=1.0),
        QuadraticModel(a=1.0, b=0.0, c=-4.0)
    ]
    xs = [0, 1, 2, 3]
    for model in models:
        print(model)
        for x in xs:
            print(f"  x={x} -> y={model.evaluate(x)}")
        print()

