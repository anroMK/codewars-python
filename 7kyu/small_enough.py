def small_enough(array, limit):
    return all([i <= limit for i in array ])

print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))