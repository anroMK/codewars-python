# Find the unique number
## Problem
There is an array with some numbers. All numbers are equal except for one. Try to find it!
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
[codewars](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)

### Example
```
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

### Solution
```python
def find_uniq(arr):
    return [key for key, value in Counter(arr).items() if value == 1][0]
```

### Test
```python
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
```

