# Next Prime

## Problem
Get the next prime number!

You will get a numbern (>= 0) and your task is to find the next prime number.

Make sure to optimize your code: there will numbers tested up to about 10^12.

### Examples
```
5   =>  7
12  =>  13
```

## Solution
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        

def next_prime(n):
    number = n + 1
    while not is_prime(number):
        number += 1
    return number
```