from dataclasses import dataclass
import numpy as np


class Planet:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.dist_to_star = r
        self.generate_planet_properties()

    def generate_planet_properties(self):
        self.radius = np.random.gamma(shape=2, scale=2)  # in earth radii (max around 20)
        self.mass = np.random.gamma(shape=2, scale=400)  # in earth mass (max around 3000)
        self.temperature = np.random.gamma(shape=2, scale=150)  # in kelvin (max around 1000)

        # old (uniform distribution)
        # self.radius = np.random.uniform(0, 100_000)  # in km (jupiter radius = 69_911 km)
        # self.density = np.random.uniform(0, 10)  # in g/cm^3 (earth density = 5.5 g/cm^3)
        # self.surface_temperature = np.random.uniform(0, 1000)  # in Kelvin (earth surface temperature = 288 K)


    def generate_realistic_planet_properties(self):
        # sample from a heavy-tailed distribution
        self.radius = np.random.normal(69_911, 10_000)

    # version with 7 properties
    # def generate_planet_properties(self):
    #     # right-tailed distribution for mass of the planet, mean 1, tail until 4000
    #     self.mass = np.random.uniform(1, 4000)  # in Earth masses
    #     self.radius = np.random.uniform(0, 15)  # in Earth radii
    #     self.orbital_period = np.random.uniform(0, 100_000)  # in days
    #     self.star_mass = np.random.uniform(0, 99)  # in solar masses
    #     self.star_radius = np.random.uniform(0, 99)  # in solar radii
    #     self.star_temperature = np.random.uniform(0, 40_000)  # in Kelvin
    #     # see https://link.springer.com/referenceworkentry/10.1007/978-3-642-11274-4_487
    #     self.star_age = np.random.uniform(0, 13.8)  # in Gy (billion years)






if __name__ == '__main__':

    # import matplotlib.pyplot as plt
    # masses = []
    # for i in range(1000):
    #     masses.append(np.random.lognormal(0, 5))
    # # plot log-normal distribution
    # plt.hist(masses, bins=100)
    # plt.show()

    import matplotlib.pyplot as plt
    s = np.random.gamma(shape=2, scale=400, size=1000)
    plt.hist(s, 70, density=True)
    plt.show()


# self.temperature = config.get('temperature', None)
# self.min_temperature = config.get('min_temperature', None)
# self.max_temperature = config.get('max_temperature', None)
#
# self.atmospheric_pressure = config.get('atmospheric_pressure', None)
# self.atmospheric_composition = config.get('atmospheric_composition', None)
# self.atmosphere_height = config.get('atmosphere_height', None)
#
# self.solid_surface_fraction = config.get('solid_surface_fraction', None)
# self.surface_composition = config.get('surface_composition', None)
# self.surface_water = config.get('surface_water', None)
# self.surface_ice = config.get('surface_ice', None)
#
# self.avg_distance_from_star = config.get('avg_distance_from_star', None)
# self.gravity = config.get('gravity', None)
# # self.radius = config.get('radius', None)
#
# # self.orbital_period = config.get('orbital_period', None)
# self.length_of_day = config.get('length_of_day', None)
# self.orbital_eccentricity = config.get('orbital_eccentricity', None)
# self.orbital_inclination = config.get('orbital_inclination', None)


# temperature  # in K, average temperature (Kelvin, 0 K = -273.15 C)
# min_temperature  # in K
# max_temperature  # in K
#
# # atmosphere_properties
# atmospheric_pressure  # in Pa (Pascal, 1 Pa = 1 N/m^2)
# atmospheric_composition  # list of gases in the atmosphere (oxigen, nitrogen, carbon dioxide, etc.)
# atmosphere_height  # in km
#
# # surface_properties
# solid_surface_fraction  # how much of the surface (%) is covered by solid material
# surface_composition  # list of elements on the surface (iron, silicon, oxygen, etc.)
# surface_water  # in %, how much of the surface is covered by water (percentage)
# surface_ice  # in %, how much of the surface is covered by ice (percentage)
#
# avg_distance_from_star  # in AU (astronomical units, 1 AU ~ 150 million km = distance from Earth to Sun)
# gravity  # in m/s^2
# radius  # size of the planet
#
# orbital_period  # time it takes to orbit the star
# length_of_day  # time it takes to rotate on its axis
# orbital_eccentricity  # how much the orbit is elliptical
# orbital_inclination  # how much the orbit is tilted
