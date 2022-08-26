# Which are in?
## Problem

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
[codewars](https://www.codewars.com/kata/550554fd08b86f84fe000a58)

 ### Example 1:
 ```
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]
```

### Example 2:
```
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
```

### Notes:
* Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
* In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
* Beware: r must be without duplicates.

### Solution
```python
def in_array(array1, array2):

    return sorted(list(set([i for i in array1 for j in array2 if i in j])))
```

### Test
```python
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
```