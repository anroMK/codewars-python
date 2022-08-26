def number(lines):
    return [f"{i}: {value}" for i, value in enumerate(lines, start= 1)]

print(number(["a", "b", "c"]))
