
def delete_nth(order,max_e):
    dict = {i:(order.count(i)- max_e) for i in set(order) if order.count(i) > max_e}
    to_remove = []
    for key, value in dict.items():
        for _ in range(value):
            to_remove.append(key)
    order.reverse()
    for i in to_remove:
        order.remove(i)
    order.reverse()
    return order

def delete_nth_v2(order,max_e):
    dict = {}
    lst = []
    for i in order:
        n = dict.get(i, 0)
        if n < max_e:
            lst.append(i)
            dict[i] = n +1
    return lst


print(delete_nth([20,37,20,21], 1))
print(delete_nth([44,21,21,21,44,44,44,21,21,21,49,32,44,44,44,21,44,49,44,21,44], 3))

print(delete_nth_v2([20,37,20,21], 1))
print(delete_nth_v2([44,21,21,21,44,44,44,21,21,21,49,32,44,44,44,21,44,49,44,21,44], 3))




