"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

"""

def expanded_form(num):
    l = len(str(num))
    lst = []
    for i in str(num):
        l -= 1
        if i != '0':
            lst.append(f"{i}" + '0'*l)
    print(lst)
    return ' + '.join(lst)

def expanded_form_v2(num):
    return ' + '.join([s + '0' * (len(str(num)) - (i+1)) for i, s in enumerate(str(num)) if s != '0'])



print(expanded_form(12))
print(expanded_form_v2(12))
print(expanded_form(1204))
print(expanded_form_v2(1204))


    




