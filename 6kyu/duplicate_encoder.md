# Duplicate Encoder
## Problem

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

[codewars](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c)

### Examples
```python
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
```
### Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

### Solutions
```python
def duplicate_encode(word):
    word = word.lower()
    dict1 = {i:word.count(i) for i in word}
    return ''.join(['(' if dict1[i] == 1 else ')' for i in word])

def duplicate_encode_v2(word):
    word = word.lower()
    return ''.join(['(' if word.count(i) == 1 else ')' for i in word])
```

### Tests
```python
print(duplicate_encode("Success"))
print(duplicate_encode_v2("Success"))
```