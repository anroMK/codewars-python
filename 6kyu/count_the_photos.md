# Count the photos!

## Problem
In a string we describe a road. There are cars that move to the right and we denote them with ">" and cars that move to the left and we denote them with "<". There are also cameras that are indicated by: " . ".
A camera takes a photo of a car if it moves to the direction of the camera.

## Task
Your task is to write a function such that, for the input string that represents a road as described, returns the total number of photos that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests.

[codewars](https://www.codewars.com/kata/6319dba6d6e2160015a842ed/train/python)

### Examples
```
For ">>." -> 2 photos were taken
For ".>>" -> 0 photos were taken
For ">.<." -> 3 photos were taken
For ".><.>>.<<" -> 11 photos were taken
```

### Solution
```python
def count_photos(road):
    photos_count = 0
    for i in range(len(road)):
        if road[i]  == '>':
            photos_count += road[i:].count('.')
        if road[i] == '<':
            photos_count += road[:i].count('.')
    
    return photos_count
```

