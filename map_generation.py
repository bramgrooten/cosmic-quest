from temp_planet import Planet
from map import Map

nr_of_planets = 4

class map_generation:
    def determine_distances():
        Map.dist_map = [[-1]*nr_of_planets]*nr_of_planets
        for x in range(nr_of_planets):
            for y in range(nr_of_planets):
                #TODO
                Map.dist_map[x][y] = -1

    def generate():
        # determine how many stars we need

        # determine where the stars are

        # for each star, determine how many planets
        
        # for each star, determine where planets are

        # configure planets

        # determine distances between planets
        determine_distances()

