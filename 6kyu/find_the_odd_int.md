# Find the odd int
## Problem
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

[codewars](https://www.codewars.com/kata/54da5a58ea159efa38000836)

### Examples
```
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
```

### Solutions
```python
def find_it(seq):
    res = {i:seq.count(i) for i in seq}
    return sum([key for key, value in res.items() if value % 2 == 1])

def find_it_v2(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i
```

### Tests
```python
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it_v2([1,2,2,3,3,3,4,3,3,3,2,2,1]))
```


