def counting_valleys(s): 
    level, entry = 0, 0
    for i in s:
        if level == -1 and i == 'U':
            entry += 1
            level += 1
        elif i == 'U':
            level += 1
        elif i == 'D':
            level -= 1
    return entry

print(counting_valleys('UFFDDFDUDFUFU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'))
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'))


        