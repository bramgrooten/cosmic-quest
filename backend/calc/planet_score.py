from calc.ESI import calc_esi
import math

# calculates a score for a planet based on it's characteristics
# score is based on planet habitability and distance
def planet_score(dist, rad, mass, temp):
    # ESI is a measure related to habitability, to a high power to emphasise high habitability
    ESI_val = calc_esi(rad, mass, temp)

    # closer is better
    dist_val = 100*math.exp(-0.00005*dist)
    # dist_val = 10
    # if (dist < 10000):
    #     dist_val = 100
    # elif (dist < 25000):
    #     dist_val = 70
    # elif(dist < 50000):
    #     dist_val = 40

    return dist_val * ESI_val
