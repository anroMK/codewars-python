def descending_order(num):
    return int(''.join(sorted([i for i in str(num)], reverse= True)))

def descending_order_v2(num):
    return int(''.join(sorted(str(num), reverse=True)))




print(descending_order(42145))
print(descending_order_v2(42145))