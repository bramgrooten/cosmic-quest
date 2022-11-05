from calc.ESI import calc_esi
import math

# calculates a score for a planet based on it's characteristics
# score is based on planet habitability and distance
def planet_score(dist, rad, mass, temp):
    # ESI is a measure related to habitability, to a high power to emphasise high habitability
    ESI_val = calc_esi(rad, mass, temp)**5

    # closer is better
    dist_val = 100*math.exp(-0.005*dist)
    return dist_val * ESI_val
