# CamelCase Method
## Problem

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

[codewars](https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python)

For instance:
```
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
```

### Solution
```python
def camel_case(string):
    return ''.join([w.capitalize() for w in string.split()])
```