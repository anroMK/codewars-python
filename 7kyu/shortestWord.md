# Shortest Word
# Problem 
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

[codewars](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9)

### Solution
```python
def find_short(s):
    return min([len(word) for word in s.split()])
```

### Test
```python
print(find_short("bitcoin take over the world maybe who knows perhaps"))
```