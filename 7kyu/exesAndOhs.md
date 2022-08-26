# Exes and Ohs
## Problem

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

[codewars](https://www.codewars.com/kata/55908aad6620c066bc00002a)
### Examples input/output:
```
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```

### Solution
```python
def xo(s):
    return s.lower().count('x')  == s.lower().count('o') 
```

### Test
```python
print(xo("ooxx"))
print(xo("ooxXm"))
print(xo("zzoo"))
```