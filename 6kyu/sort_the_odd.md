# Sort the odd
## Problem
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

[codewars](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)

### Examples
```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

### Solutions
```python
def sort_array(source_array):
    odd_list = sorted([i for i in source_array if i%2 == 1])
    odd_place = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd_list[odd_place]
            odd_place += 1
    return source_array

def sort_array(source_array):
    odd_list = sorted([i for i in source_array if i%2 == 1], reverse= True)
    return [i if i % 2 == 0 else odd_list.pop()  for i in source_array]
```

### Test
```python
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0] ))
```