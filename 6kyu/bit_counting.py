

def count_bits(n):
    return len([bit for bit in bin(n) if bit == '1'])

def count_bits_v2(n):
    return bin(n).count('1')



print(count_bits(1234))
print(count_bits_v2(1234))

