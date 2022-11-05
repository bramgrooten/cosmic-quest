


class HumanColony:
    def __init__(self):
        self.inhabited_planets = []

    def closest_colony_planet(self, new_planet):
        min_dist = float('inf')
        closest_col_planet = None
        for colony_planet in self.inhabited_planets:
            if Map.dist_map[new_planet][colony_planet] < min_dist:
                min_dist = Map.dist_map[new_planet][colony_planet]
                closest_col_planet = colony_planet
        return closest_col_planet, min_dist

