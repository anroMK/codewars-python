# Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
[codewars](https://www.codewars.com/kata/54ba84be607a92aa900000f1)
### Example: (Input --> Output)
'''
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''

### Solution
```python
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```

### Test
```python
print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
```