"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
Its guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique

"""

from collections import Counter


def find_uniq(arr):
    return [key for key, value in Counter(arr).items() if value == 1][0]
    


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))