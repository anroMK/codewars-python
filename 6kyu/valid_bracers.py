
def valid_braces(string):
    stack = []
    dict = {'[':']', ']':'[', '{':'}', '}':'{', '(':')', ')':'('}
    
    for i in string:
        if len(stack) > 0  and stack[-1] == dict[i]:
            if i in '])}':
                stack.pop()
        else:
            stack.append(i)
    return not stack


print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("(}" ))
print(valid_braces("[(])"))
print(valid_braces("[({})](]"))
print(valid_braces("([}{])"))
stack = ['([}']