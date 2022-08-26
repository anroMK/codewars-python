
def narcissistic( value ):
    return value == sum([int(i) ** len(str(value)) for i in str(value)])

print(narcissistic(1652))
print(narcissistic(153))




