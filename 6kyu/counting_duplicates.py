
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

 