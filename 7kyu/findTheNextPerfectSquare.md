# Find the next perfect square!
## Problem
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

[codewars](https://www.codewars.com/kata/56269eb78ad2e4ced1000013)
### Examples:(Input --> Output)
```
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```

### Solution
```python
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    return int((root+1) ** 2) if root.is_integer() else -1
```

### Test
```python
print(find_next_square(121))
```