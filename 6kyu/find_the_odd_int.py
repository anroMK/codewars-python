
def find_it(seq):
    res = {i:seq.count(i) for i in seq}
    return sum([key for key, value in res.items() if value % 2 == 1])

def find_it_v2(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i


    
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it_v2([1,2,2,3,3,3,4,3,3,3,2,2,1]))


