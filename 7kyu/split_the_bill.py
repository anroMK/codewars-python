def split_the_bill(x):
    average_person_bill = sum([v for _, v in x.items()])/len(x)
    return {i:round(j-average_person_bill,2) for i, j in x.items()}

print(split_the_bill({'A': 20, 'B': 15, 'C': 10}))