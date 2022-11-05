from calc.planet_score import planet_score
from map import Map


# takes galaxy state and returns best option
def recommend(map: Map):
    planets = map.planet_list
    scores = []
    dist = map.dist_map

    # calculate scores for the planets
    for i in range(len(planets)):
        p = planets[i]
        scores.append(planet_score(
            min(dist[i]), p.radius, p.mass, p.temperature))

    # get the planet with the best score
    index_best = 0
    best_score = 0
    for i in range(len(planets)):
        if (scores[i] > best_score):
            best_score = scores[i]
            index_best = i

    return scores, planets[index_best]