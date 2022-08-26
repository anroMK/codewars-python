def friend(names):
    return list(filter(lambda x: len(x)==4, names))

def friend_v2(names):
    return [p for p in names if len(p) == 4]

list1 = ["Ryan", "Kieran", "Mark"]

print(friend(list1))
print(friend_v2(list1))
#print(list(filter(lambda x: (len(x)==4), list1)))