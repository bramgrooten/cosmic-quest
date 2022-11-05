import numpy as np


class Star:
    def __init__(self):
        self.x, self.y = generate_star()
        self.planet_list = []


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
