from flask import Flask
from map_generation import map_generation
import numpy as np
from recommender import recommend

app = Flask(__name__)

map_generator = map_generation()
galaxy_map = map_generator.generate()
galaxy_map = map_generator.determine_distances(galaxy_map)

@app.route("/init_galaxy")
def init_galaxy():
    global galaxy_map
    
    galaxy_map = map_generator.generate()
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




