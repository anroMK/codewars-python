# Consecutive strings
## Problem

You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

[codewars](https://www.codewars.com/kata/56a5d994ac971f1ac500003e)

### Examples
```
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
```
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

### Note
consecutive strings : follow one after another without an interruption

### Solution
```python
def longest_consec(strarr, k):
    words =[''.join(strarr[i:i+k]) for i in range(len(strarr)-(k-1))]
    return "" if k <= 0 or len(words) == 0  else max(words, key= lambda x: len(x)) 
```
### Tests
```python
print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
print(longest_consec(['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], -2))
```
