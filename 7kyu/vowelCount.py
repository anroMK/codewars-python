def get_count(sentence):
    vowels = 'aeiou'
    return len([i for i in sentence if i in vowels])

def get_count_v2(sentence):
    return sum([1 for i in sentence if i in 'aeiou'])

print(get_count('aeiouzzzzzzz'))
print(get_count_v2('aeiouzzzzzzz'))


