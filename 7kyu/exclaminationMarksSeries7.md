# Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark

## Problem
Description:
Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.

### Examples
```
remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!"
```

### Solution
```python
def remove(s):
    return ' '.join([str for str in s.split() if str.count('!') != 1])
```

### Test
```python
print(remove("Hi! !Hi! Hi!"))
```