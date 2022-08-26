# Build Tower
## Problem
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
[codewars](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)

For example, a tower with 3 floors looks like this:
```
[
  "  *  ",
  " *** ", 
  "*****"
]
```
And a tower with 6 floors looks like this:
```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```
### Solution
```python
def tower_builder(n_floors):
    width = 2 * n_floors -1
    tower = ['*'.center(width)]
    for i in range(1,n_floors):
        new_floor = tower[i-1].strip() + '**'
        tower.append(new_floor.center(width))
    return tower
```

### Test
```python
print(tower_builder(5))
```