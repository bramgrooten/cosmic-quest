### Statistical-likelihood Exo-Planetary Habitability Index based on paper: https://academic.oup.com/mnras/article/471/4/4628/4096396
def SEPHI(
    p_M,  # Planet Mass (0-4200 Earth mass)
    p_r,  # Planet radius (0-15 Earth radius)
    P,    # Orbital period (Days)
    s_M,  # Star mass (0-99 Sun mass)
    s_r,  # Star radius (0-99 Sun radius)
    temp,  # Temperature (K)
    age,  # Star system age (0 - 13.8 Gy)
):
    # Telluric planet
    l1 = 1
    
    # Atmosphere and planet gravity
    l2 = 1
    
    # Surface liquid water
    l3 = 1
    
    # Magnetic field
    l4 = 1
    
    sephi = (l1 * l2 * l3 * l4 )^(-4)
    print(sephi)
    return sephi
