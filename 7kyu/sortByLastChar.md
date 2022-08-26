# Sort by Last Char
## Problem

Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid.

[codewars](https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0)

### Solution 
```python
def last(s):
    return sorted(s.split(' '), key=lambda x: x[-1] )
```

### Test
```python
print(last("man i need a taxi up to ubud"))
```