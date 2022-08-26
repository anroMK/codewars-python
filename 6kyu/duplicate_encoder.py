
def duplicate_encode(word):
    word = word.lower()
    dict1 = {i:word.count(i) for i in word}
    return ''.join(['(' if dict1[i] == 1 else ')' for i in word])

def duplicate_encode_v2(word):
    word = word.lower()
    return ''.join(['(' if word.count(i) == 1 else ')' for i in word])


print(duplicate_encode("Success"))
print(duplicate_encode_v2("Success"))


