from flask import Flask
from map_generation import map_generation
import numpy as np
from recommender import recommend
import copy

app = Flask(__name__)

global map_generator
map_generator = map_generation()
global galaxy_map
galaxy_map = map_generator.generate()
galaxy_map = map_generator.determine_distances(galaxy_map)

@app.route("/init_galaxy")
def init_galaxy():
    global galaxy_map
    global map_generator
    map = copy.deepcopy(galaxy_map)
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
    json_map2 = copy.deepcopy(json_map)
    del json_map
    return json_map2
    return map_generator.save_map_to_json(galaxy_map)


@app.route("/move")
def move():
    # get recommendations for next planet to colonize
    planet_scores, best_candidate, closest_colony = recommend(galaxy_map)

    # add the best planet to human colony
    #new_planet_index = np.argmax(planet_scores)
    #galaxy_map.human_colony.append(new_planet_index)
    #TODO: add old new's to full list

    galaxy_map.new_connections = [(closest_colony, best_candidate)]
    galaxy_map.new_human_colony_planets = [best_candidate]

    

    # return the new human colony to frontend
    map_generator.save_map_to_json(galaxy_map)




