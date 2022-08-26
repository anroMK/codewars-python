
def solution(number):
    return sum([num for num in range(number) if num % 3 == 0 or num % 5 == 0])

print(solution(10))
  