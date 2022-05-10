'''
The aim of this kata is to split a given string into different strings of equal size (note size of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
Assumptions:

String length is always greater than 0
String has no spaces
Size is always positive

'''

def split_in_parts(s, part_length):
    return " ".join([s[x:x+part_length] for x in range(0, len(s), part_length)])

print(split_in_parts("supercalifragilisticexpialidocious", 3))