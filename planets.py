from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Planet:
    def __init__(self, config):
        self.x = config['x']
        self.y = config['y']

        self.temperature = config.get('temperature', None)
        self.min_temperature = config.get('min_temperature', None)
        self.max_temperature = config.get('max_temperature', None)

        self.atmospheric_pressure = config.get('atmospheric_pressure', None)
        self.atmospheric_composition = config.get('atmospheric_composition', None)
        self.atmosphere_height = config.get('atmosphere_height', None)

        self.solid_surface_fraction = config.get('solid_surface_fraction', None)
        self.surface_composition = config.get('surface_composition', None)
        self.surface_water = config.get('surface_water', None)
        self.surface_ice = config.get('surface_ice', None)

        self.avg_distance_from_star = config.get('avg_distance_from_star', None)
        self.gravity = config.get('gravity', None)
        self.radius = config.get('radius', None)

        self.orbital_period = config.get('orbital_period', None)
        self.length_of_day = config.get('length_of_day', None)
        self.orbital_eccentricity = config.get('orbital_eccentricity', None)
        self.orbital_inclination = config.get('orbital_inclination', None)




# diameter of milky way galaxy: 100,000 light years. Center is (0,0)
def generate_star():
    # sample from Gaussian distribution
    r = np.random.normal(25_000, 5_000)
    angle = np.random.uniform(0, 2*np.pi)
    if r > 100_000:  # get r back in range
        r = 100_000 - (r - 100_000)
    # convert to cartesian coordinates
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y

def generate_planet():
    pass




if __name__ == '__main__':

    stars = []
    for i in range(1000):
        x, y = generate_star()
        stars.append((x, y))

    # make a scatter plot of the stars
    x, y = zip(*stars)
    plt.scatter(x, y)
    plt.show()







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
