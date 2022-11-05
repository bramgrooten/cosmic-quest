from calc.planet_score import planet_score
from map import Map
from human_colony import closest_colony_planet
from map_generation import map_generation


# takes galaxy state and returns score for each planet, the best scoring one and it's origin colony
def recommend(gmap: Map):
    planets = gmap.planet_list
    scores_and_origin = []

    # calculate scores for the planets
    for i in range(len(planets)):
        p = planets[i]
        # print("called with " + str(gmap.human_colony) +" "+ str(i) + " "+ str(gmap))
        index_origin_planet, d = closest_colony_planet(gmap.human_colony, i, gmap)
        
        if (i in gmap.human_colony):
            # already a colony, invalid
            scores_and_origin.append((
                -1,
                index_origin_planet
            ))
        else:
            # not already a colony
            scores_and_origin.append(((
                planet_score(d, p.radius, p.mass, p.temperature)),
                index_origin_planet
            ))



    # # get the planet with the best score
    # index_best = 0
    # best_score = 0
    # for i in range(len(planets)):
    #     if (scores_and_origin[i][0] > best_score):
    #         best_score = scores_and_origin[i][0]
    #         index_best = i

    return scores_and_origin

# # testing code
mg = map_generation()
galaxy = mg.generate()
galaxy = mg.determine_distances(galaxy)
r = recommend(galaxy)

# get the planet with the best score
index_best = 0
best_score = 0
for i in range(len(r)):
    if (r[i][0] > best_score):
        best_score = r[i][0]
        index_best = i

print(galaxy.dist_map[0])
print(galaxy.dist_map[1])
print(r[index_best])