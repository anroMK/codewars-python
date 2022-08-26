# Collatz Conjecture Length
## Problem

The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. If you repeat the process continuously for n, n will eventually reach 1.
[codewars](https://www.codewars.com/kata/54fb963d3fe32351f2000102)
# For example, 
if n = 20, the resulting sequence will be:
```
[ 20, 10, 5, 16, 8, 4, 2, 1 ]
```
Write a program that will output the length of the Collatz Conjecture for any given n.
In the example above, the output would be 8.

### Solution
```python
def collatz(n):
    result = [n]
    while n!=1:
        if n % 2 == 0:
            n //= 2
        else: 
            n = n * 3 + 1 
        result.append(n)
    return len(result)
```

### Test
```python
print(collatz(20))
print(collatz(73567465519280238573))
```