
def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    a = signature[0]
    b = signature[1]
    c = signature[2]
    new_list = [a,b,c]
    n = n-3
    while n > 0:
        d = a + b + c
        a, b, c = b, c, d
        new_list.append(c)
        n -= 1
    return new_list

def tribonacci_v2(signature, n):
   lst = signature[:n]
   for i in range(n-3):
        lst.append(sum(lst[-3:]))
   return lst

print(tribonacci([1, 1, 1], 10))
print(tribonacci_v2([1, 1, 1], 10))
print(tribonacci_v2([1, 1, 1], 1))


    