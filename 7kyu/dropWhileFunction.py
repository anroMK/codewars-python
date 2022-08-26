def isEven(num):
  return num % 2 == 0



def drop_while(arr, pred):
    index = 0
    for i in arr:
        if pred(i) == True:
            index +=1
        else:
            return arr[index:]            
    return []
    
print(drop_while([2,6,4,10,1,5,4,3], isEven))


def drop_while_v2(arr, pred):
    for i, val in enumerate(arr):
        if pred(val):
            continue
        else:
            return arr[i:]
    return []

print(drop_while_v2([2,6,4,10,1,5,4,3], isEven))