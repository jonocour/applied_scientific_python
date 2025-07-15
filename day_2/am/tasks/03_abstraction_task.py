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
- TODO: Create an abstract base class `Shape`:
    - Abstract methods: area(), perimeter()
    - __str__ should return the class name only

- TODO: Implement the subclass `Circle`:
    - Initialize with radius
    - Implement area() and perimeter() using math.pi

- TODO: Implement the subclass `Rectangle`:
    - Initialize with width and height
    - Implement area() and perimeter()

- TODO: Demonstrate polymorphic behavior:
    - Use a loop to iterate over a list of shapes
    - Call area() and perimeter() on each shape
    - Display results without type checking

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
# - __str__ returns class name only


# === TODO: Define subclass Circle ===
# - Initialize with radius
# - Implement area() and perimeter() using math.pi


# === TODO: Define subclass Rectangle ===
# - Initialize with width and height
# - Implement area() and perimeter()


# === TODO: Demonstrate polymorphic behavior in a loop ===
# - Use a loop to display area and perimeter for each shape

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
