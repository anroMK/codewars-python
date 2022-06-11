"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""

def solution(string, ending):
    length = len(ending)
    if (string[-length:] == ending) or ending == "":
        return True
    else:
        return False
    

print(solution('abcde', ''))


def solution_v2(string, ending):
    return string.endswith(ending)

print(solution_v2('abcde', 'de'))
    