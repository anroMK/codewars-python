# String ends with?
## Problem

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
[codewars](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)

### Examples:
```
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```

### Solution
```python
def solution(string, ending):
    length = len(ending)
    if (string[-length:] == ending) or ending == "":
        return True
    else:
        return False

def solution_v2(string, ending):
    return string.endswith(ending)
```

### Test
```python
print(solution('abcde', ''))
print(solution_v2('abcde', 'de'))
```