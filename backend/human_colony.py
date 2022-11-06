def closest_colony_planet(colony_planets,   # indices
                          new_planet,       # index
                          map):
    min_dist = float('inf')
    closest_col_planet = None

    for colony_planet in colony_planets:
        if map.dist_map[new_planet][colony_planet] < min_dist:

            min_dist = map.dist_map[new_planet][colony_planet]
            closest_col_planet = colony_planet

    return closest_col_planet, min_dist

