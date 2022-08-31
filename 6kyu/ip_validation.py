# def is_valid_IP(strng):
#     if len(strng) == 0:
#         return False
#     return len([i for i in strng.split('.') if i.isdigit() and int(i) <= 255 and not (len(i) != 1 and i[0] == '0')]) == 4

def is_valid_IP(strng):
    if len(strng) == 0:
        return False
    return len([i for i in strng.split('.') if i.isdigit() and int(i) <= 255 and str(int(i)) == i]) == 4

# print(is_valid_IP('123.045.067.089'))
# print(is_valid_IP('123.456.78.90'))
# print(is_valid_IP('1.2.3.4.5'))
# print(is_valid_IP('1.2.3.4'))

print(is_valid_IP('12.255.56.1'))
print(is_valid_IP('123.045.067.089'))





