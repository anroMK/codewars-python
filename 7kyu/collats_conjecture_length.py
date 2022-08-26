def collatz(n):
    result = [n]
    while n!=1:
        if n % 2 == 0:
            n //= 2
        else: 
            n = n * 3 + 1 
        result.append(n)
    return len(result)

print(collatz(20))
print(collatz(73567465519280238573))


    
