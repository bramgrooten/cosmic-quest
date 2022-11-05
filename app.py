import json
import random
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
timestep = 0

@app.route("/init_galaxy")
def init_galaxy():
    star_list1 = copy.deepcopy(galaxy_map.star_list)
    planet_list1 = copy.deepcopy(galaxy_map.planet_list)
    human_colony1 = copy.deepcopy(galaxy_map.human_colony)
    connections1 = copy.deepcopy(galaxy_map.connections)
    new_human_colony_planets1 = copy.deepcopy(galaxy_map.new_human_colony_planets)
    new_connections1 = copy.deepcopy(galaxy_map.new_connections)
    scores1 = copy.deepcopy(galaxy_map.scores)
    return map_generator.save_map_elements_to_json(star_list1, planet_list1, human_colony1, connections1,
                                                   new_human_colony_planets1, new_connections1, scores1)


@app.route("/move")
def move():
    global timestep
    timestep += 1

    # get recommendations for next planet to colonize
    scores_and_origins = recommend(galaxy_map)
    scores = []
    for s in scores_and_origins:
        scores.append(s[0])
    galaxy_map.scores = scores

    # add the num_to_add best planet(s) to human colony
    new_planets = []
    new_connections = []

    num_to_add = set_num_planets_to_add(timestep)
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
    scores1 = copy.deepcopy(galaxy_map.scores)

    # return the new human colony to frontend
    return map_generator.save_map_elements_to_json(star_list1, planet_list1, human_colony1, connections1,
                                                   new_human_colony_planets1, new_connections1, scores1)


# old add best planet:
#     new_planet_index = np.argmax(scores_and_origins)
#     galaxy_map.human_colony.append(new_planet_index)

@app.route("/reset")
def reset():
    galaxy_map.human_colony = []
    first_planet_index = random.randint(0, len(galaxy_map.planet_list))
    galaxy_map.human_colony.append(first_planet_index)
    galaxy_map.connections = []
    galaxy_map.new_human_colony_planets = []
    galaxy_map.new_connections = []
    galaxy_map.scores = []


def set_num_planets_to_add(timestep):
    if timestep < 3:
        return 1
    elif timestep < 7:
        return 2
    elif timestep < 12:
        return 3
    else:
        return 4