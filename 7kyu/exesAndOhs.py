def xo(s):
    return s.lower().count('x')  == s.lower().count('o') 


print(xo("ooxx"))
print(xo("ooxXm"))
print(xo("zzoo"))