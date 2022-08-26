
def solution(s):
    lst = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(lst) !=0 and len(lst[-1]) == 1:
        lst[-1] += '_'
    return lst

print(solution('abcdef'))
print(solution('abc'))
print(solution(''))


