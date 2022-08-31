import numpy as np

a = [[1, 3, 2],
    [4, 5, 1],
    [6, 5, 3],
    [7, 2, 9]]


def flip(d, a):
    match d:
        case 'R':
            return [sorted(sublist) for sublist in a]
        case 'L':
            return [sorted(sublist, reverse= True) for sublist in a]
        case 'U':
            return np.sort(a, axis = 0).tolist()[::-1]
        case 'D':
            return np.sort(a, axis = 0).tolist()


print(flip('R', a))
print(flip('L', a))
print(flip('U', a))
print(flip('D', a))
# a = [[1, 3, 2],
#     [4, 5, 1],
#     [6, 5, 3],
#     [7, 2, 9]]

# b = np.sort(a, axis = 0, reverse = True)
# print(b)


















# box = []
# for i in range(len(a)):
#     sublist = []
#     for item in a:
#         try:
#             sublist.append(item[i])
#         except:
#             continue
#     print(sublist)
#     box.append(sublist)

# print(box)



