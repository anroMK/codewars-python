
def find_outlier(integers):
    odd = [i for i in integers if i %2 == 1]
    even = [i for i in integers if i %2 == 0]
    return odd[0] if len(odd) == 1 else even[0]
    

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

