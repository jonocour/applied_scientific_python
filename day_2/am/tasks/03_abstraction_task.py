"""
TASK 03 – Abstraction with Shapes
=================================

Goal:
-----
Use abstraction to define a shared interface for geometric shapes.

Learning Outcomes:
------------------
- Understand the purpose of abstract base classes
- Enforce method implementation using @abstractmethod
- Use polymorphism to work with multiple shapes generically

Instructions:
-------------
- Create an abstract base class `Shape`:
    - Abstract methods: area(), perimeter()
    - __str__ should return the class name

- Implement 2 concrete shapes:
    1. Circle – initialized with radius
    2. Rectangle – initialized with width and height

- Use math.pi for Circle calculations
- Demonstrate polymorphic usage with a list of shapes

Example Output:
---------------
    Circle
    Area: 78.54
    Perimeter: 31.42

    Rectangle
    Area: 24.00
    Perimeter: 20.00
"""

import abc
import math

# === TODO: Define abstract base class Shape ===
# - Abstract methods: area(), perimeter()
# - __str__ should return class name only


# === TODO: Subclass – Circle ===
# - Simulate with radius = 5
# - Use math.pi for calculations


# === TODO: Subclass – Rectangle ===
# - Simulate with width = 4, height = 6


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    shapes = [
        # Circle(5),
        # Rectangle(4, 6)
    ]

    for shape in shapes:
        print(shape)
        print("Area: {:.2f}".format(shape.area()))
        print("Perimeter: {:.2f}".format(shape.perimeter()))
        print()

