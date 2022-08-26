def interlockable(a, b):
    a, b = bin(a)[2::][::-1], bin(b)[2::][::-1]
    length = min(len(a), len(b))
    for i in range(length):
        if (a[i] == '1' and b[i] == '1'):
            return False
    return True


print(interlockable(9, 4))
print(interlockable(3, 6))

