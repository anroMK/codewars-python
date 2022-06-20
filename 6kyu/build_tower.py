"""
Build Tower
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

"""

def tower_builder(n_floors):
    width = 2 * n_floors -1
    tower = ['*'.center(width)]
    for i in range(1,n_floors):
        new_floor = tower[i-1].strip() + '**'
        tower.append(new_floor.center(width))
    return tower

print(tower_builder(5))




