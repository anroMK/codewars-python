# Split Strings
## Problem
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
[codewars](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001)

### Examples
```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

### Solution
```python
def solution(s):
    lst = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(lst) !=0 and len(lst[-1]) == 1:
        lst[-1] += '_'
    return lst
```

### Test
```python
print(solution('abcdef'))
print(solution('abc'))
print(solution(''))
```