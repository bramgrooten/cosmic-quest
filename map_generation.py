from planets import Planet
from map import Map
import random
from stars import Star
import numpy as np
import math
import json

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

    def determine_distances(self, galaxy_map):
        galaxy_map.dist_map = [[-1]*len(galaxy_map.planet_list)]*len(galaxy_map.planet_list)
        for a in range(len(galaxy_map.planet_list)):
            for b in range(len(galaxy_map.planet_list)):
                # Can definitely be made more elegant, simple solution for now
                galaxy_map.dist_map[a][b] = math.dist([galaxy_map.planet_list[a].x, galaxy_map.planet_list[a].y],
                                                      [galaxy_map.planet_list[b].x, galaxy_map.planet_list[b].y])
                # math.sqrt(pow(x,2) + pow(x,2))  abs(Map.planet_list[x] - Map.planet_list[y])
        return galaxy_map

    def init_human_colony(self):
        first_planet_index = random.randint(0, len(Map.planet_list))
        Map.human_colony.append(first_planet_index)

    def save_map_to_json(self, map):
        star_list = []
        planet_list = []
        for s in map.star_list:
            for p in s.planet_list:
                planet_list.append(p.__dict__)
            s.planet_list = planet_list
            planet_list = []
            star_list.append(s.__dict__)
        
        planet_list = []
        for p in map.planet_list:
            planet_list.append(p.__dict__)

        json_map = {
            "star_list": star_list,
            "planet_list": planet_list,
            #"dist_map": Map.dist_map,
            "human_colony": map.human_colony,
        }
        with open("map.json", "w") as outfile:
            json.dump(json_map, outfile)
        return json_map


    def generate(self):
        # determine how many stars we need
        star_count = 2000
        # determine where the stars are
        self.generate_milkyway_distribution(star_count)

        # for each star...
        for i, star in enumerate(Map.star_list):
            # determine how many planets
            planet_count = 3#random.randint(1, 5)
            # for each star, determine where planets are
            self.generate_star_system_distribution(star, planet_count)

        # determine distances between planets
        #self.determine_distances()

        # determine where the human colony starts
        self.init_human_colony()

        # save the map to json
        # self.save_map_to_json(Map)

        return Map

