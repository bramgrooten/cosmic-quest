import numpy as np
import matplotlib.pyplot as plt


class Star:
    def __init__(self):
        self.x, self.y = generate_star()
        self.planet_list = []


# diameter of milky way galaxy: 100,000 light years. Center is (0,0)
def generate_star():
    r = np.random.normal(25_000, 7_000)
    angle = r/10000 + np.random.random_integers(0, 1) * np.pi#np.random.uniform(0, 2*np.pi)
    angle += np.random.normal(np.pi*r/40000, np.pi*r/180000)


    if r > 100_000:  # get r back in range
        r = 100_000 - (r - 100_000)
    # convert to cartesian coordinates
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y





if __name__ == '__main__':

    stars = []
    for i in range(2000):
        x, y = generate_star()
        stars.append((x, y))

    # make a scatter plot of the stars
    x, y = zip(*stars)
    plt.scatter(x, y)
    plt.show()
