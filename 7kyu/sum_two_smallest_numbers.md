# Sum of two lowest positive integers
## Problem

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

[codewars](https://www.codewars.com/kata/558fc85d8fd1938afb000014)

### For example, 
```
when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
```

### Solution
```python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
```

### Test
```python
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
```
