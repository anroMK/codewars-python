
def digital_root(n):
    while n >= 10:
        n = sum([int(i) for i in str(n)])
    return n


print(digital_root(942))
#print(sum([int(i) for i in str(942)]))