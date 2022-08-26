def split_in_parts(s, part_length):
    return " ".join([s[x:x+part_length] for x in range(0, len(s), part_length)])

print(split_in_parts("supercalifragilisticexpialidocious", 3))