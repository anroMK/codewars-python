def camel_case(string):
    return ''.join([w.capitalize() for w in string.split()])


print(camel_case("hello case"))
print(camel_case("camel case word"))

