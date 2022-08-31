# Gravity Flip (3D version)

This kata is a slightly harder version of Gravity Flip. It is recommended to do that first.

Bob is bored in his physics lessons yet again, and this time, he's brought a more complex gravity-changing box with him. It's 3D, with small cubes arranged in a matrix of n×m columns. It can change gravity to go in a certain direction, which can be 'L', 'R', 'D', and 'U' (left, right, down, and up).

Given the initial configuration of the cubes inside of the box as a 2D array, determine how the cubes are arranged after Bob switches the gravity.

See the sample tests for examples.

[codewars](https://www.codewars.com/kata/5f849ab530b05d00145b9495/train/python)

### SOlution

```python
import numpy as np

def flip(d, a):
    match d:
        case 'R':
            return [sorted(sublist) for sublist in a]
        case 'L':
            return [sorted(sublist, reverse= True) for sublist in a]
        case 'U':
            return np.sort(a, axis = 0).tolist()[::-1]
        case 'D':
            return np.sort(a, axis = 0).tolist()
```

## Test
```python
import numpy as np

a = [[1, 3, 2],
    [4, 5, 1],
    [6, 5, 3],
    [7, 2, 9]]

print(flip('R', a))
print(flip('L', a))
print(flip('U', a))
print(flip('D', a))
```