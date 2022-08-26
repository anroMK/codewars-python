def last(s):
    return sorted(s.split(' '), key=lambda x: x[-1] )

print(last("man i need a taxi up to ubud"))


