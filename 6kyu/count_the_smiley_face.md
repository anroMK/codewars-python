# Count the smiley faces!
## Problem

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

*  Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
* A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
* Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)

Invalid smiley faces: ;( :> :} :]

[codewars](https://www.codewars.com/kata/583203e6eb35d7980400002a)

### Example
```
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
```

### Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

### Solutions
```python
import re
def count_smileys(arr):
    return len([i for i in arr if i[-1] in 'D)' if i[-2] in '-~:;'])

def count_smileys_v2(arr):
    return sum([1 for i in arr if re.match(r"[:;][-~]?[)D]", i)])
```

### Tests
```python
print(count_smileys([':)', ';(', ';}', ':-D']))       # should return 2;
print(count_smileys([';D', ':-(', ':-)', ';~)']))     # should return 3;
print(count_smileys([';]', ':[', ';*', ':$', ';-D'])) # should return 1;

print(count_smileys_v2([':)', ';(', ';}', ':-D']))       # should return 2;
print(count_smileys_v2([';D', ':-(', ':-)', ';~)']))     # should return 3;
print(count_smileys_v2([';]', ':[', ';*', ':$', ';-D'])) # should return 1;
```
