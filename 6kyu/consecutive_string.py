

def longest_consec(strarr, k):
    words =[''.join(strarr[i:i+k]) for i in range(len(strarr)-(k-1))]
    return "" if k <= 0 or len(words) == 0  else max(words, key= lambda x: len(x)) 
     
    #return "" if k <= 0 or len(words) == 0  else max(words, key=len) 

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
print(longest_consec(['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], -2))

