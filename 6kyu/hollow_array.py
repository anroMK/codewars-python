
def is_hollow(x):
    while len(x) > 2 and x[0] != 0 and x[-1] != 0: x=x[1:-1]
    return len(x) > 2 and set(x) == {0}


print(is_hollow([-1,0,0,0,3]))