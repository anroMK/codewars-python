# Bit Counting
## Problem

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

[codewars](https://www.codewars.com/kata/526571aae218b8ee490006f4)

### Exaple
```
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
```

### Solutions
```python
def count_bits(n):
    return len([bit for bit in bin(n) if bit == '1'])

def count_bits_v2(n):
    return bin(n).count('1')
```

### Tests
```python
print(count_bits(1234))
print(count_bits_v2(1234))
```