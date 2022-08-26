# Who likes it?
## Problem

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

[codewars](https://www.codewars.com/kata/5266876b8f4bf2da9b000362)

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```
Note: For 4 or more names, the number in "and 2 others" simply increases.

### Solution
```python
def likes(names):
    length = len(names)
    match length:
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return f"{names[0]}, {names[1]} and {length - 2} others like this"
```

### Test
```python
print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"] ))
print(likes(["Max", "John", "Mark"]  ))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
```
