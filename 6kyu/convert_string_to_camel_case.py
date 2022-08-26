
def to_camel_case(text):
    return ''.join([c if text[i-1].isalpha() else c.upper() for i, c in enumerate(text) if c.isalpha()])
    
    #return [(i,c) for i, c in enumerate(text) if not c.isalpha()]
    
    



print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("A"))