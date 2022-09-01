def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def twin_prime(n):
    prime_list = [num for num in range(2,n + 2) if is_prime(num)]
    return [(prime_list[i], prime_list[i+1])  for i in range(len(prime_list) -1) if prime_list[i+1] -  prime_list[i] == 2 ]

print(twin_prime(12))
        
    


#print(twin_prime(20))

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int((num ** 0.5)) + 1):
#         if num % i == 0:
#             return False
#     return True