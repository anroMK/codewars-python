def remove(s):
    return ' '.join([str for str in s.split() if str.count('!') != 1])

print(remove("Hi! !Hi! Hi!"))