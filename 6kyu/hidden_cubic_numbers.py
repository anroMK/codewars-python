"""
We search non-negative integer numbers, with at most 3 digits, such as the sum of the cubes of their digits is the number itself; we will call them "cubic" numbers.

153 is such a "cubic" number : 1^3 + 5^3 + 3^3 = 153
These "cubic" numbers of at most 3 digits are easy to find, even by hand, so they are "hidden" with other numbers and characters in a string.

The task is to find, or not, the "cubic" numbers in the string and then to make the sum of these "cubic" numbers found in the string, if any, and to return a string such as:

"number1 number2 (and so on if necessary) sumOfCubicNumbers Lucky" 
if "cubic" numbers number1, number2, ... were found.

The numbers in the output are to be in the order in which they are encountered in the input string.

If no cubic numbers are found return the string: `"Unlucky"``.

Examples:
 - s = "aqdf&0#1xyz!22[153(777.777" 
   the groups of at most 3 digits are 0 and 1 (one digit), 22 (two digits), 153, 777, 777 (3 digits)
   Only 0, 1, 153 are cubic and their sum is 154
   Return: "0 1 153 154 Lucky"

- s = "QK29a45[&erui9026315"
  the groups are 29, 45, 902, 631, 5. None is cubic.
  Return: "Unlucky"
Notes
In the string "001234" where 3 digits or more follow each other the first group to examine is "001" and the following is "234". If a packet of at most three digits has been taken, whether or not "cubic", it's over for that packet.

When a continuous string of digits exceeds 3, the string is split into groups of 3 from the left. The last grouping could have 3, 2 or 1 digits.

e.g "24172410" becomes 3 strings comprising "241", "724" and "10"

e.g "0785" becomes 2 strings comprising "078" and "5".

"""

def is_cubic(arr):
    sum = 0
    result = []
    for i in arr:
        for j in i:
            sum += int(j) ** 3
        if str(sum) == i:
            result.append(str(sum))
        sum = 0
    #print(f'result: {result}')
    return result
        
    


def is_sum_of_cubes(s):
    n = []
    i = 0
    while i < len(s):
        if s[i:i+3].isdigit():
            n.append(s[i:i+3])
            i +=2
        elif s[i:i+2].isdigit():
            n.append(s[i:i+2])
            i +=1
        elif s[i].isdigit():
            n.append(s[i])
        i += 1
    result = is_cubic(n)
    if len(result) == 0:
        return "Unlucky"
    else: 
        return f"{' '.join(result)} {sum(map(int, result))} Lucky"
    



print(is_sum_of_cubes("aqdf&0#1xyz!22[153(777.777")) # ['0', '1', '22', '153', '777', '777']
#print(is_sum_of_cubes("QK29a45[&erui9026315"))
print(is_sum_of_cubes("0 9026315 -827&()"))



