# Unique In Order
## Problem
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
[codewars](https://www.codewars.com/kata/54e6533c92449cc251001667)

### Examples
```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```

### Solution
```python
def unique_in_order(iterable):
    return [c  for i, c in enumerate(iterable) if iterable[i-1] != iterable[i] or i < 1]
```

### Test
```python
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('AA'))
print(unique_in_order('A'))
```