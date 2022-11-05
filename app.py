from flask import Flask
from map_generation import map_generation
from recommender import recommend
from planets import planet_argmax
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

        scores_and_origins[new_planet_index][0] = -1  # set score to -1, so it won't be chosen again

    # add previous move's "new" to the list of connections and planet
    galaxy_map.connections += galaxy_map.new_connections
    galaxy_map.human_colony += galaxy_map.new_human_colony_planets

    # reset the new connections and new human colony planets
    galaxy_map.new_connections = new_connections
    galaxy_map.new_human_colony_planets = new_planets

    # return the new human colony to frontend
    return map_generator.save_map_to_json(galaxy_map)



# old add best planet:
#     new_planet_index = np.argmax(scores_and_origins)
#     galaxy_map.human_colony.append(new_planet_index)



