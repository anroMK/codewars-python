def find_next_power(val, pow_):
    result = 0
    number = 0
    while result < val:
        result = number ** pow_
        number += 1    
    return result


print(find_next_power(12385, 3))

for i in range(100):
    print(pow(i, 3))
