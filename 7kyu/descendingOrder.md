# Descending Order
## Task

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

[codewars](https://www.codewars.com/kata/5467e4d82edf8bbf40000155)
### Examples:
```
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
```

### Solutions
```python
def descending_order(num):
    return int(''.join(sorted([i for i in str(num)], reverse= True)))

def descending_order_v2(num):
    return int(''.join(sorted(str(num), reverse=True)))
```

### Test
```python
print(descending_order(42145))
print(descending_order_v2(42145))
```