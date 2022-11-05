# Based on https://www.researchgate.net/publication/348759371_PESIC_Planetary_ESI_Calculator

from functools import reduce
import math

# Normalized Earth values of the quantities involved
earth = [1,   # 6.371 x 106 m
         1,   # 5.9722×1024 kg
         1,   # 11 184 m/s
         288] # K

# Weights for each quantity based on https://www.liebertpub.com/doi/10.1089/ast.2010.0592
w = [0.57, 1.07, 0.7, 5.58]

def calc_esi(radius, mass, temp):
    if mass == 0 or radius == 0:
        return 0
        
    # Calculates density in Earth units from mass and radius
    rho = mass/(radius**3)

    # Calculates escape velocity in Earth units from mass and radius
    vel = (math.sqrt(mass/radius))

    # Planet values
    values = [radius, rho, vel, temp]

    ESI = []

    # Calculate individual values
    for i in range(4): 
        ESI.append((1 - abs((values[i] - earth[i])/(values[i] + earth[i])))**(w[i]))

    c_ESI = reduce((lambda x, y: x* y), ESI)**(1/len(ESI))
    return c_ESI