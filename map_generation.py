from planets import Planet
from map import Map

nr_of_planets = 0

class map_generation:
    def generate_milkyway_distribution(star_count):
        for i in range(star_count):
            Map.star_list.append(TODO: create star class)
    
    def generate_star_system_distribution():
        for i in star.planet_count:
            p = Planet
            Map.planet_list.append(p)
    
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
            star.planet_count = 4
            nr_of_planets += star.planet_count
            # for each star, determine where planets are
            generate_star_system_distribution(star)

        # configure planets
        for p in Map.planet_list:
            generate_planet()

        # determine distances between planets
        determine_distances()