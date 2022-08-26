def sum_of_n(n):
    current = 0
    list = []
    if n > 0:
        for i in range(n+1):
            current +=i
            list.append(current)
    else:
        for i in range(-n+1):
            current -=i
            list.append(current)
      
    return list

def sum_of_n_v2(n):
    current = 0
    list = []
    sign = 1
    if n < 0: sign = -1
    for i in range(abs(n)+1):
        current +=(i*sign)
        list.append(current)
    return list

#print(sum_of_n(5))
#print(sum_of_n(-5))

print(sum_of_n_v2(5))
print(sum_of_n_v2(-5))






