
def is_cubic(arr):
    sum = 0
    result = []
    for i in arr:
        for j in i:
            sum += int(j) ** 3
        if str(sum) == i:
            result.append(str(sum))
        sum = 0
    #print(f'result: {result}')
    return result
        
    


def is_sum_of_cubes(s):
    n = []
    i = 0
    while i < len(s):
        if s[i:i+3].isdigit():
            n.append(s[i:i+3])
            i +=2
        elif s[i:i+2].isdigit():
            n.append(s[i:i+2])
            i +=1
        elif s[i].isdigit():
            n.append(s[i])
        i += 1
    result = is_cubic(n)
    if len(result) == 0:
        return "Unlucky"
    else: 
        return f"{' '.join(result)} {sum(map(int, result))} Lucky"
    



print(is_sum_of_cubes("aqdf&0#1xyz!22[153(777.777")) # ['0', '1', '22', '153', '777', '777']
#print(is_sum_of_cubes("QK29a45[&erui9026315"))
print(is_sum_of_cubes("0 9026315 -827&()"))




