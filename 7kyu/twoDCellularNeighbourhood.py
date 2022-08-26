N = 5
M = 5
mat = [[j+i*N for j in range (N)] for i in range(M)]



def get_neighbourhood(n_type, mat, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    max_x = len(mat[0])
    max_y = len(mat)
    list = []
    
    for i in range(x-1, min(x+2, max_x)):
        for j in range(y-1,min(y+2, max_y)):
            if n_type == 'moore' and i >=0 and j >= 0:
                list.append(mat[i][j])
            if n_type == 'von_neumann' and (i == x or j == y) and i >= 0 and j >=0:
                list.append(mat[i][j])
                
    try:
        list.remove(mat[x][y])
    except:
        print('')
    return sorted(list)
    


print(get_neighbourhood("moore", mat, (1,1))) # [0, 1, 2, 5, 7, 10, 11, 12]
print(get_neighbourhood('moore', mat, (0,0))) #[1, 6, 5]
print(get_neighbourhood("moore", mat, (4,2))) # [21, 16, 17, 18, 23]


print(get_neighbourhood("von_neumann", mat, (1,1))) # [1, 5, 7, 11]
print(get_neighbourhood("von_neumann", mat, (0,0))) # [1, 5]
print(get_neighbourhood("von_neumann", mat, (4,2))) # [21, 17, 23]


