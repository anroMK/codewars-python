# def generate_shape(n):
#     shape_string = ''
#     for i in range(n-1):
#         shape_string += n * '+' + '\n'
#     return shape_string + n * '+' 

def generate_shape(n):

    return '\n'.join([n * '+' for i in range(n)])



print(generate_shape(3))