"""
Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values. 
You want to remove the longest prefix of elements such that the predicate is true for each element. We'll call this the dropWhile function. It accepts two arguments. 
The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence.

def isEven(num):
  return num % 2 == 0

arr = [2,4,6,8,1,2,5,4,3,2]

dropWhile(arr, isEven) == [1,2,5,4,3,2] # True
Your task is to implement the dropWhile function. If you've got a span function lying around, this is a one-liner! 
Alternatively, if you have a takeWhile function on your hands, then combined with the dropWhile function, you can implement the span function in one line. 
This is the beauty of functional programming: there are a whole host of useful functions, many of which can be implemented in terms of each other.

"""

def isEven(num):
  return num % 2 == 0
"""
def drop_while(arr, pred):
    lst = list(filter(pred, arr[2:]))
    lst.remove(arr[1])
    return [x for x in arr if x not in lst]
"""




def drop_while(arr, pred):
    index = 0
    for i in arr:
        if pred(i) == True:
            index +=1
        else:
            return arr[index:]            
    return []
    


print(drop_while([2,6,4,10,1,5,4,3], isEven))


def drop_while_v2(arr, pred):
    for i, val in enumerate(arr):
        if pred(val):
            continue
        else:
            return arr[i:]
    return []

print(drop_while_v2([2,6,4,10,1,5,4,3], isEven))