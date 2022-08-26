
def tower_builder(n_floors):
    width = 2 * n_floors -1
    tower = ['*'.center(width)]
    for i in range(1,n_floors):
        new_floor = tower[i-1].strip() + '**'
        tower.append(new_floor.center(width))
    return tower

print(tower_builder(5))




