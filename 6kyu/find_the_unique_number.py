
from collections import Counter


def find_uniq(arr):
    return [key for key, value in Counter(arr).items() if value == 1][0]
    


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))