def sum_dig_pow_condition(number):
    return sum([int(value) ** i for i, value in enumerate(str(number), 1)]) == number

def sum_dig_pow(a, b):
    return [i for i in range(a,b + 1) if sum_dig_pow_condition(i)]

print(sum_dig_pow_condition(9))

print(sum_dig_pow(1,100))