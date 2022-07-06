"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

"""

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

   

            

    

    
    #return True if len([1 for i in range(2,int(num/2)+1,1) if (num/i).is_integer()]) == 0 else False
  
   

print(is_prime(9))
print(is_prime(75))
print(is_prime(113))
    
