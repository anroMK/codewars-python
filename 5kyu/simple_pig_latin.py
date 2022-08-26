def pig_it(text):
    return ' '.join([word[1:] + word[0] + 'ay' if  word.isalpha()  else word for word in text.split()])
    


print(pig_it('Pig latin is cool'))
print(pig_it('This is my string ?'))