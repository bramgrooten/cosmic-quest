from planets import Planet
from map import Map
import random
from stars import Star

nr_of_planets = 0

class map_generation:
    def generate_milkyway_distribution(self, star_count):
        for i in range(star_count):
            Map.star_list.append(Star())
    
    def generate_star_system_distribution(star):
        for i in star.planet_count:
            p = Planet()
            Map.planet_list.append(p)
            star.planet_list.append(p)
            # initial positions, purely
            # sample from Gaussian distribution
            r = np.random.normal(25_0, 5_0)
            angle = np.random.uniform(0, 2*np.pi)
            if r > 100_0:  # get r back in range
                r = 100_0 - (r - 100_0)
            # convert to cartesian coordinates
            p.x = r * np.cos(angle)
            p.y = r * np.sin(angle)
    
    def generate_planet():
        TODO

    def determine_distances():
        Map.dist_map = [[-1]*nr_of_planets]*nr_of_planets
        for x in range(nr_of_planets):
            for y in range(nr_of_planets):
                # Can definitely be made more elegant, simple solution for now
                Map.dist_map[x][y] = abs(Map.planet_list[x] - Map.planet_list[y])


    def generate():
        # determine how many stars we need
        star_count = 2
        # determine where the stars are
        generate_milkyway_distribution(star_count)

        # for each star...
        for star in Map.star_list:
            # determine how many planets
            planet_count =  random.range(4) #4
            nr_of_planets += planet_count
            # for each star, determine where planets are
            generate_star_system_distribution(star, planet_count)

        # configure planets
        for p in Map.planet_list:
            generate_planet()

        # determine distances between planets
        determine_distances()
