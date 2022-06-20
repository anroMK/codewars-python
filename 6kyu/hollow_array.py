"""
An array is said to be hollow if it contains 3 or more 0s in the middle that are preceded and followed by the same number of non-zero elements. 
Furthermore, all the zeroes in the array must be in the middle of the array.

Write a function named isHollow/is_hollow/IsHollow that accepts an integer array and returns true if it is a hollow array,else false.

"""

def is_hollow(x):
    if len(x) < 3:
        return False
    if not 0 in x:
        return False
    if x.count(0) == len(x):
        return True
    if x.count(0) < 3:
        return False
    index = x.index(0) 
    for i in x[index:-index]:
        if i != 0:
            return False
    if 0 in x[:index] or 0 in x[-index:]:
        return False
    return True
    


print(is_hollow([-1,0,0,0,3]))