"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""





def to_camel_case(text):
    return ''.join([c if text[i-1].isalpha() else c.upper() for i, c in enumerate(text) if c.isalpha()])
    
    #return [(i,c) for i, c in enumerate(text) if not c.isalpha()]
    
    



print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("A"))