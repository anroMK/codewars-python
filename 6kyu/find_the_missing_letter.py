
def find_missing_letter(chars):
    chars_range = [chr(ch) for ch in range(ord(chars[0]), ord(chars[-1])+1)]
    for ch in chars_range:
        if ch not in chars: 
            return ch


print(find_missing_letter(['a','b','c','d','f']))


