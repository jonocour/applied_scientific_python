"""
02_intro_to_inheritance.py
==========================

Intro to Inheritance in Python OOP
----------------------------------

Why Inheritance?
----------------
- Inheritance allows us to make new classes that reuse and extend the behavior of existing ones.
- Great for organizing scientific code: you can build general "templates" (base classes), then specialize for your problem.

Learning Outcomes:
------------------
- Understand how to create a child class that inherits from a parent class.
- Know how to override and extend methods.
- See how inheritance can keep your code DRY (Don't Repeat Yourself).

"""

# =======================================================
# 0. MOTIVATION – Why copy code if we can extend it?
# =======================================================

# Suppose you need to model different shapes: rectangles, squares, and circles.
# All have an area and perimeter—but not the same formulas!

# Instead of rewriting similar code, let's build a base class for all 2D shapes.

# =======================================================
# 1. DEFINING A BASE CLASS (Shape)
# =======================================================

class Shape:
    """Base class for 2D shapes."""

    def area(self):
        """Area formula - not known for generic shapes!"""
        raise NotImplementedError("Define area() in the subclass.")

    def perimeter(self):
        """Perimeter formula - not known for generic shapes!"""
        raise NotImplementedError("Define perimeter() in the subclass.")

# =======================================================
# 2. RECTANGLE INHERITS FROM SHAPE
# =======================================================

class Rectangle(Shape):
    """Rectangle: inherits from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# =======================================================
# 3. SQUARE: SPECIAL CASE OF RECTANGLE (Inheritance Chain)
# =======================================================

class Square(Rectangle):
    """Square: a special Rectangle with equal sides."""

    def __init__(self, side):
        # Call Rectangle's __init__ with both width and height equal to 'side'
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

# =======================================================
# 4. CIRCLE: INHERITS FROM SHAPE, HAS ITS OWN FORMULAS
# =======================================================

import math

class Circle(Shape):
    """Circle: inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

# =======================================================
# 5. USAGE & POLYMORPHISM
# =======================================================

# You can treat all shapes the same way, thanks to inheritance:
shapes = [
    Rectangle(3, 4),
    Square(5),
    Circle(2)
]

for shape in shapes:
    print(shape)
    print("  Area:", shape.area())
    print("  Perimeter:", shape.perimeter())
    print()

# =======================================================
# 6. BEST PRACTICES
# =======================================================

# - Use inheritance to capture *shared* logic (e.g., area/perimeter contract).
# - Use 'super()' to reuse parent logic if possible.
# - Don't overcomplicate—inheritance is best for real "is-a" relationships.
# - You can make abstract base classes (see ABCs) to enforce method implementation.

# Try adding a new shape (e.g., Triangle) that also inherits from Shape!

