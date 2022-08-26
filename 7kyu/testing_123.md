# Testing 1-2-3
### Problem
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

[codewars](https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9)

### Examples
```
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
```

### Solution
```python
def number(lines):
    return [f"{i}: {value}" for i, value in enumerate(lines, start= 1)]

print(number(["a", "b", "c"]))
```

### Test
```python
print(number(["a", "b", "c"]))
```