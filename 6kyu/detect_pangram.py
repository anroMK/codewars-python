
def is_pangram(s):
    for ch in range(ord('a'),ord('z')):
        if chr(ch) not in s.lower():
            return False
    return True
        

sentence = "The quick brown fox jumps over the lazy dog" 
print(is_pangram(sentence))

