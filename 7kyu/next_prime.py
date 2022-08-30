def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        

def next_prime(n):
    number = n + 1
    while not is_prime(number):
        number += 1
    return number
        

print(is_prime(5))              
                
            

print(next_prime(7))
