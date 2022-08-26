
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


    




