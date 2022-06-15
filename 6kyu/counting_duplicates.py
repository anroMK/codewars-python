"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""


from collections import Counter


def duplicate_count(text):
    text = text.lower()
    dict = {i:text.count(i) for i in text}
    return sum([1 for value in dict.values() if value > 1])

def duplicate_count_v2(text):
    return sum([1 for value in Counter(text.lower()).values() if value > 1])


    
     

print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("abcdeaB"))

print(duplicate_count_v2("abcde"))
print(duplicate_count_v2("aabbcde"))
print(duplicate_count_v2("abcdeaB"))

 