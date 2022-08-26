from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    prime = [True for i in range(num+1)]
    prime[0] = prime[1] = False
    for i in range(2,int(sqrt(num))+1):
        #print(f'i: {i}')
        if prime[i] == True:
            for j in range(i+i, num+1, i):
                #print(f'j:{j}')
                prime[j] = False
    return True if num in [i for i in range(num+1) if prime[i] == True] else False


print(is_prime(9))
print(is_prime(75))
print(is_prime(113))
    
