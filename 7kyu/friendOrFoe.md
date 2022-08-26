# Friend or Foe?
## Problem
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

[codewars](https://www.codewars.com/kata/55b42574ff091733d900002f)
### Example
```
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
```
```
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
```
Note: keep the original order of the names in the output.

### Solutions
```python
def friend(names):
    return list(filter(lambda x: len(x)==4, names))

def friend_v2(names):
    return [p for p in names if len(p) == 4]
```

### Test
```python
list1 = ["Ryan", "Kieran", "Mark"]

print(friend(list1))
print(friend_v2(list1))
```