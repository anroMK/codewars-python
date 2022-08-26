import math
def nb_year(p0, percent, aug, p):
    current_population = p0
    years = 0
    while current_population < p:
        current_population += math.floor(current_population * percent/100) + aug
        years += 1

    return years



print(nb_year(1500000, 0.0,10000, 2000000))
