# Sum of a sequence
## Problem

Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

If begin value is greater than the end, function should returns 0

[codewars](https://www.codewars.com/kata/586f6741c66d18c22800010a)

### Examples
```
2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
```

### Solution
```python
def sequence_sum(begin_number, end_number, step):
    return sum(list(range(begin_number, end_number+1, step)))
```

### Test
```python
print(sequence_sum(2,6,2))
print(sequence_sum(2,2,2))
print(sequence_sum(1,5,1))
print(sequence_sum(1,5,3))
```
