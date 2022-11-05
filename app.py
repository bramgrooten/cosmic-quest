from flask import Flask
from map_generation import map_generation
import numpy as np
from recommender import recommend

app = Flask(__name__)

map_generator = map_generation()
galaxy_map = map_generator.generate()

@app.route("/init_galaxy")
def init_galaxy():
    return map_generator.save_map_to_json(galaxy_map)


@app.route("/move")
def move():
    # get recommendations for next planet to colonize
    planet_scores = recommend(galaxy_map)

    # add the best planet to human colony
    new_planet_index = np.argmax(planet_scores)
    galaxy_map.human_colony.append(new_planet_index)

    # return the new human colony to frontend
    map_generator.save_map_to_json(galaxy_map)




