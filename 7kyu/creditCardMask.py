# return masked string
def maskify(cc):
    newString =''
    if len(cc) > 4:
        for _ in range(len(cc)-4):
            newString += '#'
        newString += cc[-4:]
        return newString
    return cc

def maskify_v2(cc):
    return '#' * (len(cc) - 4) + cc[-4:]

print(maskify("4556364607935616"))
print(maskify_v2("4556364607935616"))


