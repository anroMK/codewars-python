def two_sum(numbers, target):
    print(numbers)
    for i, value_i in enumerate(numbers):
        for j, value_j in enumerate(numbers[i+1:], i+1):
            print(f'i:{i} value_i:{value_i},        j:{j} value_j:{value_j}')
            if value_i + value_j == target:
                return [i, j]
                

print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))