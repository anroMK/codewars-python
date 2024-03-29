# Categorize New Member
## Problem
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

### Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

### Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

[codewars](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa)

### Example
```
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
```

### Solution
```python
def open_or_senior(data):
    new_data = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            new_data.append('Senior')
        else:
            new_data.append('Open')
    return new_data

def open_or_senior_v2(data):
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]
```

### Test
```python
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior_v2([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
```