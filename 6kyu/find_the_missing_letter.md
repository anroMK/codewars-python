# Find the missing letter
## Problem

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

[codewars](https://www.codewars.com/kata/5839edaa6754d6fec10000a2)

### Examples
```
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
```


### Solution
```python
def find_missing_letter(chars):
    chars_range = [chr(ch) for ch in range(ord(chars[0]), ord(chars[-1])+1)]
    for ch in chars_range:
        if ch not in chars: 
            return ch
```

### Test
```python
print(find_missing_letter(['a','b','c','d','f']))
```