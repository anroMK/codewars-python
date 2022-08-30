def find_lowest_int(k):
    n = 1
    while True:
        k1 = k * n
        k2 = (k+1) * n
        if sorted(str(k1)) == sorted(str(k2)):
            break
        n += 1
    return n


print(find_lowest_int(100))
