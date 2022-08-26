
#x = ['n','s','n','s','n','s','n','s','n','s']


def is_valid_walk(walk):
    directions = ['n', 's', 'w', 'e']
    steps = {c:walk.count(c) for c in directions for i in walk}
    return len(walk) == 10 and steps['w'] - steps['e'] == 0 and steps['n'] - steps['s'] == 0 


def is_valid_walk_v2(walk):
    return len(walk) == 10 and walk.count('n') - walk.count('s') == 0 and walk.count('w') - walk.count('e') == 0

print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk_v2(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk_v2(['w','e','w','e','w','e','w','e','w','e']))

