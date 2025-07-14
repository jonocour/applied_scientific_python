"""
TASK 01 – Build a Planet Class
Goal: Practice defining your own class with attributes and methods.

Instructions:
-------------
- Model a planet in the solar system.
- Your class should store name, mass (kg), and radius (km).
- Add a method to return a summary string.
- Add a method to compute surface gravity (g = G * M / R^2)

Constants:
    - Gravitational constant (G) = 6.67430 × 10⁻¹¹ m³/kg·s²
    - Radius must be converted to meters inside the gravity calculation.

Example:
    earth = Planet("Earth", mass=5.972e24, radius_km=6371)
    print(earth.summary())         ➞ "Planet Earth: 5.972e+24 kg, 6371 km radius"
    print(earth.surface_gravity()) ➞ ~9.81 m/s²
"""


class Planet:
    # TODO: Define __init__ with name, mass (kg), radius (km)
    pass

    # TODO: Define summary() method to describe the planet
    pass

    # TODO: Define surface_gravity() using the formula: G * M / R^2
    # Convert radius to meters inside the method
    pass

    # CHALLENGE:
    # TODO: Override __add__ so adding two Planet objects returns a new Planet
    # - Name: "CombinedPlanet"
    # - Mass: sum of both masses
    # - Radius: sum of both radii
    pass

# === TEST YOUR IMPLEMENTATION ===


if __name__ == "__main__":
    earth = Planet("Earth", mass=5.972e24, radius_km=6371)
    mars = Planet("Mars", mass=6.417e23, radius_km=3389.5)
    marth = earth + mars # in an IDE, this + is flagged (it will complain we haven't implemented __add__
    print(earth.summary())
    print("Gravity:", earth.surface_gravity(), "m/s²")

    print(mars.summary())
    print("Gravity:", mars.surface_gravity(), "m/s²")
