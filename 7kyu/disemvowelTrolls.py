def disemvowel(str):
    vowels = 'aeiou'
    return ''.join([i for i in str if i.lower() not in vowels])


print(disemvowel("This website is for losers LOL!"))