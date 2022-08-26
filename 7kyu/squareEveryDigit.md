# Square Every Digit
## Problem

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
[codewars](https://www.codewars.com/kata/546e2562b03326a88e000020)
### For example,
```
if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
```

Note: The function accepts an integer and returns an integer

### Solutions
```python
def square_digits(num):
    strNum = ''
    num = str(num)
    for i in num:
        strNum += str(int(i)**2)
    return int(strNum)

def square_digits_v2(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))
```

### Test
```python
print(square_digits(9119))
print(square_digits_v2(9119))
```