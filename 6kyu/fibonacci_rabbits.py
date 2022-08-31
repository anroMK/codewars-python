def fib_rabbits(n, b):
    immmature, mature = 1, 0
    for i in range(n):
        remember_immature = immmature
        immmature = mature * b
        mature += remember_immature
        print(f'month: {i}')
        print(f'immature:{immmature}, mature{mature}')
    return mature

print(fib_rabbits(5,3))



