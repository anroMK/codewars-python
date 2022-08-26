def extra_perfect(n):
    return [x for x in range(1, n+1) if x%2 == 1]

def extra_perfect_v2(n):
    return list(range(1, n+1, 2))

print(extra_perfect(7))
print(extra_perfect_v2(7))