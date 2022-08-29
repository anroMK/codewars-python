
# def max_multiple(divisor, bound):
#     result = divisor
#     while result <= (bound - divisor):
#         result += divisor
#     return result

def max_multiple(divisor, bound):
    return bound // divisor * divisor

print(max_multiple(37,200))