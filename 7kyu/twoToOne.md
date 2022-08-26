# Two to One
## Problem
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

[codewars](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)

### Examples:
```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

### Solution
```python
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
```

### Test
```python
print(longest("aretheyhere","yestheyarehere"))
```