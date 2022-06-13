"""
Task
Write a function that checks if two non-negative integers make an "interlocking binary pair".

Interlock ?
numbers can be interlocked if their binary representations have no 1's in the same place
comparisons are made by bit position, starting from right to left (see the examples below)
when representations are of different lengths, the unmatched left-most bits are ignored
Examples
a = 9, b = 4
Stacking representations shows how they can interlock. Here, no 1's share any position, so the function returns true.

 9    1001
 4     100
a = 3, b = 6
These representations do not interlock. Finding they both have a 1 in the same position, the function returns false.

 3      11
 6     110

"""
def interlockable(a, b):
    a, b = bin(a)[2::][::-1], bin(b)[2::][::-1]
    length = min(len(a), len(b))
    for i in range(length):
        if (a[i] == '1' and b[i] == '1'):
            return False
    return True


print(interlockable(9, 4))
print(interlockable(3, 6))

