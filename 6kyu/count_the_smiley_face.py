
import re
def count_smileys(arr):
    return len([i for i in arr if i[-1] in 'D)' if i[-2] in '-~:;'])

def count_smileys_v2(arr):
    return sum([1 for i in arr if re.match(r"[:;][-~]?[)D]", i)])



print(count_smileys([':)', ';(', ';}', ':-D']))       # should return 2;
print(count_smileys([';D', ':-(', ':-)', ';~)']))     # should return 3;
print(count_smileys([';]', ':[', ';*', ':$', ';-D'])) # should return 1;

print(count_smileys_v2([':)', ';(', ';}', ':-D']))       # should return 2;
print(count_smileys_v2([';D', ':-(', ':-)', ';~)']))     # should return 3;
print(count_smileys_v2([';]', ':[', ';*', ':$', ';-D'])) # should return 1;