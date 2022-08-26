def are_coprime(n,m):
    n_divisors = [x for x in range(2,n+1) if n%x == 0]
    m_divisors = [x for x in range(2,m+1) if m%x == 0]
    return len(list(set(n_divisors) & set(m_divisors))) == 0

print(are_coprime(20,27))
print(are_coprime(12,39))

