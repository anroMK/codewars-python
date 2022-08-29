
def fifo(n, reference_list):
    memory = []
    for i in reference_list:
        print(i)
        if len(memory) < n:
            memory = memory + [i] 



    return memory


print(fifo(3,[1, 2, 3, 4, 2, 5]))