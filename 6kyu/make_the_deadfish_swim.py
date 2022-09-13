def parse(data):
    result = []
    value = 0
    for i in data:
        if i == 'i':
            value += 1
        if i == 'd':
            value -= 1
        if i == 's':
            value = value ** 2
        if i == 'o':
            result.append(value)
    return result