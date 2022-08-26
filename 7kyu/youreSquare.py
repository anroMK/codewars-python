def is_square(n):    
    return  n>= 0  and (n ** 0.5).is_integer() 

print(is_square(-1))
print(is_square(25))
print(is_square(26))