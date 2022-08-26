# Vowel Count
## Problem

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

[codewars](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

### Solutions
```python
def get_count(sentence):
    vowels = 'aeiou'
    return len([i for i in sentence if i in vowels])

def get_count_v2(sentence):
    return sum([1 for i in sentence if i in 'aeiou'])
```

### Test
```python
print(get_count('aeiouzzzzzzz'))
print(get_count_v2('aeiouzzzzzzz'))
```
