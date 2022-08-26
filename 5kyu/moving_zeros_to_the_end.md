#  Moving Zeros To The End

## Problem
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

[codewars](https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python)

### Example
```
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

### Solution
```python
def move_zeros(lst):
    return [num for num in lst if num != 0] + lst.count(0) * [0]
```

### Test
```python
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
```

