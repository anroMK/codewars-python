# Hollow array
## Problem

An array is said to be hollow if it contains 3 or more 0s in the middle that are preceded and followed by the same number of non-zero elements. Furthermore, all the zeroes in the array must be in the middle of the array.

Write a function named isHollow/is_hollow/IsHollow that accepts an integer array and returns true if it is a hollow array,else false.

[codewars](https://www.codewars.com/kata/59b72376460387017e000062)

### Solution
```python
def is_hollow(x):
    while len(x) > 2 and x[0] != 0 and x[-1] != 0: x=x[1:-1]
    return len(x) > 2 and set(x) == {0}
```

### Test
```python
print(is_hollow([-1,0,0,0,3]))
```