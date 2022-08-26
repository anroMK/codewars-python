# The Supermarket Queue
## Problem 
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
* customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
* n: a positive integer, the number of checkout tills.

output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

[codewars](https://www.codewars.com/kata/57b06f90e298a7b53d000a86)

### Examples
```
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
```

Clarifications
* There is only ONE queue serving many tills, and
* The order of the queue NEVER changes, and
* The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

### Solutions
```python
def queue_time_v2(customers, n):
    tills = [0] * n
    for i in customers:
        find = tills.index(min(tills))
        tills[find] += i
    return max(tills)

 


def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    if len(customers) <= n:
        return max(customers)
    tills_left_time = [0] * n 
    time = 0
    while len(customers) >= 1:
        indices = [i for i, t in enumerate(tills_left_time) if t == 0]  
        for i in indices:       
            tills_left_time[i] = customers.pop(0) 
        tills_left_time = [i-1 if i >0 else 0 for i in tills_left_time]
        time += 1
    return time + max(tills_left_time)
```

### Tests
```python
print(queue_time([2,2,3,3,4,4], 2))  
print(queue_time([1, 2, 3, 4, 5], 1))  
print(queue_time([22, 28, 50, 4, 19, 14, 17, 41, 38, 12, 10, 44, 17, 23, 8], 3))  
print(queue_time_v2([22, 28, 50, 4, 19, 14, 17, 41, 38, 12, 10, 44, 17, 23, 8], 3))  
```

