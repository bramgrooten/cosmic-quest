from planets import Planet
from map import Map
import random
from stars import Star
import numpy as np
import math
import json

nr_of_planets = 0

class map_generation:
    def generate_milkyway_distribution(self, star_count):
        for i in range(star_count):
            Map.star_list.append(Star())
    
    def generate_star_system_distribution(self, star, planet_count):
        for i in range(planet_count): #planet_count
            # sample from Gaussian distribution
            r = np.random.normal(25_0, 5_0)
            angle = np.random.uniform(0, 2*np.pi)
            if r > 100_0:  # get r back in range
                r = 100_0 - (r - 100_0)
            # convert to cartesian coordinates
            x = star.x + r * np.cos(angle)
            y = star.y + r * np.sin(angle)
            p = Planet(x, y, r)
            Map.planet_list.append(p)
            star.planet_list.append(p)            

    def determine_distances(self):
        Map.dist_map = [[-1]*nr_of_planets]*nr_of_planets
        for x in range(nr_of_planets):
            for y in range(nr_of_planets):
                # Can definitely be made more elegant, simple solution for now
                Map.dist_map[x][y] = math.dist([Map.planet_list[x].x, Map.planet_list[x].y], [Map.planet_list[y].x, Map.planet_list[y].y]) #math.sqrt(pow(x,2) + pow(x,2))  abs(Map.planet_list[x] - Map.planet_list[y])

    def generate(self):
        # determine how many stars we need
        star_count = 2
        # determine where the stars are
        self.generate_milkyway_distribution(self, star_count)

        # for each star...
        for i, star in enumerate(Map.star_list):
            # determine how many planets
            planet_count = random.randint(1, 5)
            # for each star, determine where planets are
            self.generate_star_system_distribution(self, star, planet_count)

        # determine distances between planets
        self.determine_distances(self)
        # save the map to json
        star_list = []
        planet_list = []
        for s in Map.star_list:
            for p in s.planet_list:
                planet_list.append(p.__dict__)
            s.planet_list = planet_list#.__dict__
            star_list.append(s.__dict__)
        
        planet_list = []
        for p in Map.planet_list:
            planet_list.append(p.__dict__)
        json_map = {
            "star_list": star_list,#.__dict__,#Map.star_list.__dict__,
            "planet_list": planet_list#.__dict__,#Map.planet_list,#
            #"dist_map": Map.dist_map
        }
        with open("test.json", "w") as outfile:
            json.dump(json_map, outfile)

