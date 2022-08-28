# Counting Valleys

## Problem

You need count how many valleys you will pass.

Start is always from zero level.

Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.

One passed valley is equal one entry and one exit of a valley.

```
s='FUFFDDFDUDFUFUF'
U=UP
F=FORWARD
D=DOWN
```
To represent string above
```
(level 1)  __
(level 0)_/  \         _(exit we are again on level 0)
(entry-1)     \_     _/
(level-2)       \/\_/
```
So here we passed one valley

### Solution
```python
def counting_valleys(s): 
    level = 0
    entry = 0
    for i in s:
        if level == -1 and i == 'U':
            entry += 1
            level += 1
        elif i == 'U':
            level += 1
        elif i == 'D':
            level -= 1
    return entry
```

### Test
```python
print(counting_valleys('UFFDDFDUDFUFU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'))
```
