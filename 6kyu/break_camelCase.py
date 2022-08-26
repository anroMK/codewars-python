
import re

def solution(s):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)

print(solution("camelCasing" ))