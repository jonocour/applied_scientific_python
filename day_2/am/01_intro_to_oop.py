"""
01_intro_to_oop.py
==================

Intro to Object-Oriented Programming (OOP) in Python
----------------------------------------------------

Why OOP?
--------
- OOP lets us model scientific concepts with both data and behavior.
- Helps enforce valid operations on data through encapsulation.
- Makes objects behave like built-in types using special methods.

Encapsulation in Python:
------------------------
- Python doesn't enforce access control like Java/C++.
- Uses naming conventions instead:
    - public: no underscore — open access.
    - _protected: single underscore — intended for internal use.
    - __private: double underscore — name mangling to avoid accidental access.
- Python trusts the developer: conventions over strict rules.

Learning Outcomes:
------------------
- Understand encapsulation (public, protected, private).
- Use special methods for intuitive object behavior.
- Recognize Python's flexible approach to access control.
"""

# =======================================================
# 0. MOTIVATION — Let's make objects act like numbers
# =======================================================

# You want a Measurement class:
# - Can be printed nicely
# - Can be added together (if units match)
# - Protects its internal value from accidental misuse

# =======================================================
# 1. DEFINING A CLASS WITH PUBLIC, PROTECTED, AND PRIVATE
# =======================================================
class Measurement:
    """A scientific measurement with encapsulation, special methods, and property decorators."""

    def __init__(self, value, unit):
        self._value = value    # Protected by convention
        self.unit = unit       # Public
        self.__id = id(self)   # Private with name mangling

    @property
    def value(self):
        """Getter for _value (allows m.value access)."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter with validation (allows m.value = x)."""
        if new_value < 0:
            raise ValueError("Measurement cannot be negative.")
        self._value = new_value

    @property
    def id(self):
        """Read-only access to private __id."""
        return self.__id

    def __str__(self):
        return f"{self._value} {self.unit}"

    def __add__(self, other):
        if self.unit != other.unit:
            raise ValueError("Can't add measurements with different units.")
        return Measurement(self._value + other._value, self.unit)

    def __eq__(self, other):
        return self.unit == other.unit and self._value == other._value


# =======================================================
# 2. USAGE EXAMPLES
# =======================================================
m = Measurement(10, "kg")
m1 = Measurement(5, "m")
m2 = Measurement(3, "m")
total = m1 + m2

print(m1)       # 5 m
print(m2)       # 3 m
print(total)    # 8 m

# Accessing protected attribute (allowed but discouraged)
print(m1._value)  # ➔ Works, but violates encapsulation

# Accessing private attribute directly — fails
# print(m1.__id)   # ➔ Raises AttributeError!

# Correct ways to access the private attribute
print(m1.id)                 # ➔ Via property (recommended)
print(m1._Measurement__id)   # ➔ Name mangling (not recommended)

# Using property for value
print(m.value)   # ➔ Getter via @property
m.value = 15     # ➔ Setter with validation
print(m)         # ➔ 15 kg

# Attempting invalid value — raises ValueError
# m.value = -5

# Accessing read-only id
print(m.id)      # ➔ Read-only property

# =======================================================
# 3. KEY TAKEAWAYS
# =======================================================

# - Python uses naming conventions for access control.
# - _single: protected — "internal use"
# - __double: private — "name mangled" (not strictly enforced)
# - Use getters/setters when validation is needed.
# - Special methods let you define natural behavior for your objects.
