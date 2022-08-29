def sum_no_duplicates(l):
    return sum([i for i in set(l) if l.count(i) < 2])




print(sum_no_duplicates([1, 1, 2, 3]))
