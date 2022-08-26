# Credit Card Mask
## Problem

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

[codewars](https://www.codewars.com/kata/5412509bd436bd33920011bc)
### Examples
```
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"

"Skippy" --> "##ippy"

"Nananananananananananananananana Batman!"
-->
"####################################man!"
```

### Solution
```python
def maskify(cc):
    newString =''
    if len(cc) > 4:
        for _ in range(len(cc)-4):
            newString += '#'
        newString += cc[-4:]
        return newString
    return cc

def maskify_v2(cc):
    return '#' * (len(cc) - 4) + cc[-4:]
```

### Test
```python
print(maskify("4556364607935616"))
print(maskify_v2("4556364607935616"))
```

