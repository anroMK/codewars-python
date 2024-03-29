# Delete occurrences of an element if it occurs more than n times

## Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

### Task
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.

[codewars](https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python)

### Example
```
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
```

### Solution
```python
def delete_nth(order,max_e):
    dict = {i:(order.count(i)- max_e) for i in set(order) if order.count(i) > max_e}
    to_remove = []
    for key, value in dict.items():
        for _ in range(value):
            to_remove.append(key)
    order.reverse()
    for i in to_remove:
        order.remove(i)
    order.reverse()
    return order

def delete_nth_v2(order,max_e):
    dict = {}
    lst = []
    for i in order:
        n = dict.get(i, 0)
        if n < max_e:
            lst.append(i)
            dict[i] = n +1
    return lst
```

### Tests
```python
print(delete_nth([20,37,20,21], 1))
print(delete_nth([44,21,21,21,44,44,44,21,21,21,49,32,44,44,44,21,44,49,44,21,44], 3))

print(delete_nth_v2([20,37,20,21], 1))
print(delete_nth_v2([44,21,21,21,44,44,44,21,21,21,49,32,44,44,44,21,44,49,44,21,44], 3))
```