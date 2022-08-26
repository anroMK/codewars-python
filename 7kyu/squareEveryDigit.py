def square_digits(num):
    strNum = ''
    num = str(num)
    for i in num:
        strNum += str(int(i)**2)
    return int(strNum)

def square_digits_v2(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))

print(square_digits(9119))
print(square_digits_v2(9119))