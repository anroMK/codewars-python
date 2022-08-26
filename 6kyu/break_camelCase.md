# Break camelCase
## Problem
Complete the solution so that the function will break up camel casing, using a space between words.
[codewars](https://www.codewars.com/kata/5208f99aee097e6552000148)

### Example
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

### Solution
```python
import re

def solution(s):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)
```

### Test
```python
print(solution("camelCasing" ))
```