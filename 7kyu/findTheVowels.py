
"""
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
NOTES
Vowels in this context refers to: a e i o u y (including upper case)
This is indexed from [1..n] (not zero indexed!)
"""

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

