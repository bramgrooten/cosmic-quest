import json
from flask import Flask
from map_generation import map_generation
from recommender import recommend
from planets import planet_argmax
from flask_cors import CORS
import copy

app = Flask(__name__)
CORS(app)

map_generator = map_generation()
galaxy_map = map_generator.generate()
galaxy_map = map_generator.determine_distances(galaxy_map)

@app.route("/init_galaxy")
def init_galaxy():
    star_list1 = copy.deepcopy(galaxy_map.star_list)
    planet_list1 = copy.deepcopy(galaxy_map.planet_list)
    human_colony1 = copy.deepcopy(galaxy_map.human_colony)
    connections1 = copy.deepcopy(galaxy_map.connections)
    new_human_colony_planets1 = copy.deepcopy(galaxy_map.new_human_colony_planets)
    new_connections1 = copy.deepcopy(galaxy_map.new_connections)
    return map_generator.save_map_elements_to_json(star_list1, planet_list1, human_colony1, connections1,
                                                   new_human_colony_planets1, new_connections1)


@app.route("/move")
def move():
    # get recommendations for next planet to colonize
    scores_and_origins = recommend(galaxy_map)

    # add the num_to_add best planet(s) to human colony
    new_planets = []
    new_connections = []

    num_to_add = 3
    for i in range(num_to_add):
        new_planet_index = planet_argmax(scores_and_origins)
        from_planet_index = scores_and_origins[new_planet_index][1]

        new_planets.append(new_planet_index)
        new_connections.append((from_planet_index, new_planet_index))

        scores_and_origins[new_planet_index] = (-1, -1)  # set score to -1, so it won't be chosen again

    # add previous move's "new" to the list of connections and planet
    galaxy_map.connections += galaxy_map.new_connections
    galaxy_map.human_colony += galaxy_map.new_human_colony_planets

    # reset the new connections and new human colony planets
    galaxy_map.new_connections = new_connections
    galaxy_map.new_human_colony_planets = new_planets

    star_list1 = copy.deepcopy(galaxy_map.star_list)
    planet_list1 = copy.deepcopy(galaxy_map.planet_list)
    human_colony1 = copy.deepcopy(galaxy_map.human_colony)
    connections1 = copy.deepcopy(galaxy_map.connections)
    new_human_colony_planets1 = copy.deepcopy(galaxy_map.new_human_colony_planets)
    new_connections1 = copy.deepcopy(galaxy_map.new_connections)

    # return the new human colony to frontend
    return map_generator.save_map_elements_to_json(star_list1, planet_list1, human_colony1, connections1,
                                                   new_human_colony_planets1, new_connections1)


# old add best planet:
#     new_planet_index = np.argmax(scores_and_origins)
#     galaxy_map.human_colony.append(new_planet_index)
