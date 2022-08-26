def robber_encode(sentence):
    vovels = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    for ch in sentence:
        if ch.isalpha() and ch.lower() not in vovels:
            if ch.islower():
                new_string += ch + 'o' + ch
            else:
                new_string += ch + 'O' + ch
        else:
            new_string+= ch
    return new_string


print(robber_encode('Hello world'))



