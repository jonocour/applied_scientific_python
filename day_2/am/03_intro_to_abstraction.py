"""
03_intro_to_abstraction.py
==========================

Introduction to Abstraction and ABCs in Python

Focus:
------
- What is abstraction? Why use Abstract Base Classes (ABCs)?
- How to use the abc module to define required methods
- Simple scientific example

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
# 2. Example: Measurement ABC
# ---------------------------------------------

class Measurement(abc.ABC):
    """Abstract Base Class for scientific measurements."""

    @abc.abstractmethod
    def value(self):
        """Return the measured value (must be implemented by subclasses)."""
        pass

    @abc.abstractmethod
    def units(self):
        """Return the measurement units (must be implemented)."""
        pass

# ---------------------------------------------
# 3. Implementing a Concrete Class
# ---------------------------------------------

class TemperatureMeasurement(Measurement):
    def __init__(self, temp_c):
        self.temp_c = temp_c

    def value(self):
        return self.temp_c

    def units(self):
        return "°C"

# ---------------------------------------------
# 4. Usage
# ---------------------------------------------

if __name__ == "__main__":
    t = TemperatureMeasurement(37.0)
    print("Temperature:", t.value(), t.units())

    # Uncommenting this would cause an error:
    # m = Measurement()  # TypeError: Can't instantiate abstract class

# ---------------------------------------------
# 5. Best Practices
# ---------------------------------------------
# - Use ABCs to define a shared protocol: scientists can build their own models by subclassing MathematicalModel.
# - Each model can be used in fitting, plotting, simulation, or experimental prediction—just call .evaluate(x)!
# - For more complex models, simply require more methods (e.g., "derivative", "parameters", etc.).
