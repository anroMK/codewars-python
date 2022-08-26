
def unique_in_order(iterable):
    return [c  for i, c in enumerate(iterable) if iterable[i-1] != iterable[i] or i < 1]
    
    

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('AA'))
print(unique_in_order('A'))

