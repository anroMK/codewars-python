# Find the smallest power higher than a given a value

## Problem

We have the number 12385. We want to know the value of the closest cube but higher than 12385. The answer will be 13824.

Now, another case. We have the number 1245678. We want to know the 5th power, closest and higher than that number. The value will be 1419857.

We need a function find_next_power ( findNextPower in JavaScript, CoffeeScript and Haskell), that receives two arguments, a value val, and the exponent of the power, pow_, and outputs the value that we want to find.

[codears](https://www.codewars.com/kata/56ba65c6a15703ac7e002075)

Let'see some cases:
```
find_next_power(12385, 3) == 13824

find_next_power(1245678, 5) == 1419857
```
The value, val will be always a positive integer.

The power, pow_, always higher than 1.

Happy coding!!

### Solution
```python
def find_next_power(val, pow_):
    result = 0
    number = 0
    while result < val:
        result = number ** pow_
        number += 1    
    return result
```