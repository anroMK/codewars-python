def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    list = []
    index = 1
    for letter in word.lower():
        if letter in vowels:
            list.append(index)
        index+=1
    return list

def vowel_indices_v2(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [i for i, letter in enumerate(word, start = 1) if letter.lower() in vowels]

print(vowel_indices("apple"))
print(vowel_indices("UNDISARMED"))

print(vowel_indices_v2("apple"))
print(vowel_indices_v2("UNDISARMED"))

