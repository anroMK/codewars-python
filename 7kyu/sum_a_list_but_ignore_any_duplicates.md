# Sum a list but ignore any duplicates

## Problem

Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.

[codewars](https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python)

```python
def sum_no_duplicates(l):
    return sum([i for i in set(l) if l.count(i) < 2])
```