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
    # Gravitational constant in m^3 / (kg s^2)
    G = 6.67430e-11

    def __init__(self, name: str, mass: float, radius_km: float):
        """Initialize a planet with a name, mass (kg), and radius (km)."""
        self.name = name
        self.mass = mass
        self.radius_km = radius_km

    def summary(self) -> str:
        """Return a one‑line summary of this planet."""
        return f"Planet {self.name}: {self.mass:.3e} kg, {self.radius_km} km radius"

    def surface_gravity(self) -> float:
        """
        Compute surface gravity (m/s^2) via
            g = G * M / R^2
        where R is in meters.
        """
        radius_m = self.radius_km * 1_000  # km → m
        return Planet.G * self.mass / (radius_m ** 2)

    def __add__(self, other):
        """
        Define how to 'add' two Planets:
          - New name is "CombinedPlanet"
          - Mass and radius are summed
        """
        if not isinstance(other, Planet):
            return NotImplemented
        return Planet(
            name="CombinedPlanet",
            mass=self.mass + other.mass,
            radius_km=self.radius_km + other.radius_km
        )


# === TEST YOUR IMPLEMENTATION ===
if __name__ == "__main__":
    earth = Planet("Earth", mass=5.972e24, radius_km=6371)
    mars  = Planet("Mars",  mass=6.417e23, radius_km=3389.5)
    marth = earth + mars  # uses our __add__

    print(earth.summary())
    print("Gravity:", earth.surface_gravity(), "m/s²\n")

    print(mars.summary())
    print("Gravity:", mars.surface_gravity(), "m/s²\n")

    print(marth.summary())
    print("Gravity:", marth.surface_gravity(), "m/s²")
