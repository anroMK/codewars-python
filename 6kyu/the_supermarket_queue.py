"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

"""

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
    tills_left_time = [0] * n #left time of each till
    time = 0
    while len(customers) >= 1:
        indices = [i for i, t in enumerate(tills_left_time) if t == 0]  #indeksy dla ktorych tills_left_time jest rowne 0
        #print(indices)
        for i in indices:       #dla kazdego pustego indeksu
            tills_left_time[i] = customers.pop(0) 
        #print(tills_left_time)  
        tills_left_time = [i-1 if i >0 else 0 for i in tills_left_time]
        time += 1
        #print(f"time: {time}")
    return time + max(tills_left_time)



#print(queue_time([2,2,3,3,4,4], 2))  
#print(queue_time([1, 2, 3, 4, 5], 1))  
print(queue_time([22, 28, 50, 4, 19, 14, 17, 41, 38, 12, 10, 44, 17, 23, 8], 3))  
print(queue_time_v2([22, 28, 50, 4, 19, 14, 17, 41, 38, 12, 10, 44, 17, 23, 8], 3))  


