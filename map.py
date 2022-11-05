from dataclasses import dataclass

@dataclass
class Map:
    star_list = []
    planet_list = []
    dist_map = []
    human_colony = []
    connections = []

    new_human_colony_planets = []
    new_connections = []
    scores = []
