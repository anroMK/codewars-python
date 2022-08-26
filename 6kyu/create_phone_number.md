# Create Phone Number
## Problem
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
[codewars](https://www.codewars.com/kata/525f50e3b73515a6db000b83)

### Example
```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

### Solution
```python
def create_phone_number(n):
    n = ''.join([str(i) for i in n])
    return f"({n[0:3]}) {n[3:6]}-{n[6:]}"
```

### Test
```python
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
```