def open_or_senior(data):
    new_data = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            new_data.append('Senior')
        else:
            new_data.append('Open')
    return new_data

def open_or_senior_v2(data):
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]

print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior_v2([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
