def move_zeros(lst):
    return [num for num in lst if num != 0] + lst.count(0) * [0]

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))