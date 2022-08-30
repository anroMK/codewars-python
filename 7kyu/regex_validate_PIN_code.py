import re

# def validate_pin(pin):
#     return True if re.fullmatch(r'\d{4}', pin) or re.fullmatch(r'\d{6}', pin) else False

def validate_pin(pin):
    return True if re.fullmatch(r'\d{4}|\d{6}', pin) else False

print(validate_pin('1234'))