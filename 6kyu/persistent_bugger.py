import numpy as np

def persistence(n):
    n = str(n)
    multiply_count = 0
    while len(n) > 1:
        n = str(np.prod([int(i) for i in n]))
        multiply_count += 1
    return multiply_count

      
    
print(persistence(999))