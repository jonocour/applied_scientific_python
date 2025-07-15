"""
03_intro_to_abstraction.py
==========================

Introduction to Abstraction and ABCs in Python

Focus:
------
- What is abstraction? Why use Abstract Base Classes (ABCs)?
- How to use the abc module to define required methods
- Simple example

"""

import abc

# ---------------------------------------------
# 1. What is Abstraction? Why Use ABCs?
# ---------------------------------------------
# Abstraction means defining a common interface for a group of related objects, hiding implementation details.
# An Abstract Base Class (ABC) is a "template" for other classes:
#   - Can't be instantiated directly
#   - Forces child classes to implement certain methods

# ---------------------------------------------
# 2. What is @abstractmethod?
# ---------------------------------------------
# An @abstractmethod marks a method that MUST be implemented by any subclass.
# The method is defined in the abstract base class (ABC) without a real body.

# - Any class inheriting from Shape MUST define its own area() method.
# - If it doesn't, Python will raise a TypeError when you try to instantiate it.
#
# Why use @abstractmethod?
#   - Enforces a shared contract between all subclasses.
#   - Prevents incomplete implementations.
#   - Supports polymorphism: every subclass will have those methods.

# ---------------------------------------------
# 3. Example: Measurement ABC
# ---------------------------------------------

class Measurement(abc.ABC):
    """Abstract Base Class for measurements."""

    @abc.abstractmethod
    def value(self):
        """Return the measured value (must be implemented by subclasses)."""
        pass

    @abc.abstractmethod
    def units(self):
        """Return the measurement units (must be implemented)."""
        pass

# ---------------------------------------------
# 4. Implementing a Concrete Class
# ---------------------------------------------

class TemperatureMeasurement(Measurement):
    def __init__(self, temp_c):
        self.temp_c = temp_c

    def value(self):
        return self.temp_c

    def units(self):
        return "°C"

# ---------------------------------------------
# 5. Usage
# ---------------------------------------------

if __name__ == "__main__":
    t = TemperatureMeasurement(37.0)
    print("Temperature:", t.value(), t.units())

    # Uncommenting this would cause an error:
    # m = Measurement()  # TypeError: Can't instantiate abstract class

# ---------------------------------------------
# 5. Best Practices
# ---------------------------------------------
# - Use ABCs to define a shared protocol: you can build your own models by subclassing MathematicalModel.
# - Each model can be used in fitting, plotting, simulation, or experimental prediction, just call .evaluate(x)!
# - For more complex models, add more methods (e.g., "derivative", "parameters", etc.).
