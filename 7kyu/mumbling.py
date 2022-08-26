def accum(s):
    return '-'.join([letter.upper() + count * letter.lower() for count, letter in enumerate(s) ])

print(accum("RqaEzty"))