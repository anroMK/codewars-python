# Count the divisors of a number
## Task

Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

[codewars](https://www.codewars.com/kata/542c0f198e077084c0000c2e)

### Examples (input --> output)
```
4 --> 3 (1, 2, 4)
5 --> 2 (1, 5)
12 --> 6 (1, 2, 3, 4, 6, 12)
30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
```

### Solution 
```python
def divisors(n):
    return sum([1 for x in range(1,n+1) if n%x == 0])
```

### Test
```python
print(divisors(30))
```

