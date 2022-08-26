
def in_array(array1, array2):

    return sorted(list(set([i for i in array1 for j in array2 if i in j])))



a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))