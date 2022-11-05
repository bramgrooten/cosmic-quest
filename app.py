from flask import Flask
from map_generation import map_generation
import numpy as np

app = Flask(__name__)

map2 = map_generation()
map = map2.generate()

@app.route("/state")
def test():
    return map

@app.route("/move")
def move():
    # get recommendations for next planet to colonize
    planet_scores = recommender.get_planet_scores()

    # add best planet to human colony
    new_planet_index = np.argmax(planet_scores)
    galaxy_map.human_colony.append(new_planet_index)

    # return the new human colony to frontend
    galaxy_map.save_map_to_json(galaxy_map)




