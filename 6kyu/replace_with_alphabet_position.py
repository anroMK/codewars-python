
def alphabet_position(text):
    return ' '.join([str(ord(c) - 96) for c in text.lower() if c.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))