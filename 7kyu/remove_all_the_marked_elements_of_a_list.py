class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]


l = List()
print(l.remove_([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1,3]))
print(l.remove_([1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8], [1, 3, 4, 2]))