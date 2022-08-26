# Mumbling
## Problem

This time no story, no theory. The examples below show you how to write function accum:

[codewars](https://www.codewars.com/kata/5667e8f4e3f572a8f2000039)
### Examples:
```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```
The parameter of accum is a string which includes only letters from a..z and A..Z.

### Solution
```python
def accum(s):
    return '-'.join([letter.upper() + count * letter.lower() for count, letter in enumerate(s) ])
```

### Test
```python
print(accum("RqaEzty"))
```