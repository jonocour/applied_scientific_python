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

# === Define abstract base class Shape ===
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """Return the perimeter (or circumference) of the shape."""
        pass

    def __str__(self):
        # Return just the class name
        return self.__class__.__name__


# === Define subclass – Circle ===
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# === Define subclass – Rectangle ===
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(shape)
        print("Area:      {:.2f}".format(shape.area()))
        print("Perimeter: {:.2f}".format(shape.perimeter()))
        print()
