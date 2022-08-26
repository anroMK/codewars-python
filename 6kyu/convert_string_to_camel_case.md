# Convert string to camel case
## Problem
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
[codewars](https://www.codewars.com/kata/517abf86da9663f1d2000003)
### Examples
```
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
```

### Solution
```python
def to_camel_case(text):
    return ''.join([c if text[i-1].isalpha() else c.upper() for i, c in enumerate(text) if c.isalpha()])
```

### Test
```python
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("A"))
```