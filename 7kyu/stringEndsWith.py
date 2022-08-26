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
    