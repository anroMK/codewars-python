# Regex validate PIN code

## Problem

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

[codewars](https://www.codewars.com/kata/55f8a9c06c018a0d6e000132)

### Examples (Input --> Output)
```
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
```
### Solution
```python
import re

def validate_pin(pin):
    return True if re.fullmatch(r'\d{4}|\d{6}', pin) else False
```
