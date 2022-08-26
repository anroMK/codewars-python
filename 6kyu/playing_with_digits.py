
def dig_pow(n, p):
    number = 0
    for i in str(n):
        number+=int(i) ** p
        p += 1
    return int(number/n) if (number/n).is_integer() else -1

print(dig_pow(92, 1))
print(dig_pow(46288, 3))