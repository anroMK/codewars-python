# Build a square

## Problem

I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer will be a whole number between 1 and 50.

### Example
n = 3, so I expect a 3x3 square back just like below as a string:
```
+++
+++
+++
```

### Solution
```python
def generate_shape(n):
    shape_string = ''
    for i in range(n-1):
        shape_string += n * '+' + '\n'
    return shape_string + n * '+' 


def generate_shape(n):
    return '\n'.join([n * '+' for i in range(n)])
```

