
def find_even_index(arr):
    n = -1
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            n = i
            return n
    return n


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
