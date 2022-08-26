
def sort_array(source_array):
    odd_list = sorted([i for i in source_array if i%2 == 1])
    odd_place = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd_list[odd_place]
            odd_place += 1
    return source_array

def sort_array(source_array):
    odd_list = sorted([i for i in source_array if i%2 == 1], reverse= True)
    return [i if i % 2 == 0 else odd_list.pop()  for i in source_array]


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0] ))

