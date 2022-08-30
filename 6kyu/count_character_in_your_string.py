def count(str):
    # The function code should be here
    return {i:str.count(i) for i in set(str)}


print(count('aba'))

