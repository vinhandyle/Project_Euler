# Day 15: Chiton
# Part 1: 609
# Part 2: 2925

INPUT = 'input_15.txt'
TEST = 'input_15_test.txt'

    
    
def run():
    i = get_input(INPUT)
    path = get_best_path(i)
    print(sum(path[1:]))

    i = expand_matrix(i)
    path = get_best_path(i)
    print(sum(path[1:]))



def expand_matrix(matrix):
    n = len(matrix)
    m = 5 * n
    e_matrix = list([0] * m for i in range(m))
    for i in range(m):
        for j in range(m):
            e_matrix[i][j] = (matrix[i % n][j % n] + (i+j)//n) % 9
            e_matrix[i][j] = 9 if e_matrix[i][j] == 0 else e_matrix[i][j]
    return e_matrix



def get_best_path(matrix):
    path = []
    for i, j in dp(matrix):
        path.append(matrix[i][j])
    return path



def dp(matrix):
    n = len(matrix) - 1
    p_matrix = list([0] * (n+1) for i in range(n+1))

    # Forward fill matrix: O(n^2)
    for i in range(n+1):
        for j in range(n+1):
            if p_matrix[i][j] == 0:
                p_matrix[i][j] = matrix[i][j]
            if i < n:
                temp = p_matrix[i][j] + matrix[i+1][j]
                if p_matrix[i+1][j] == 0 or p_matrix[i+1][j] > temp:
                    p_matrix[i+1][j] = temp
            if j < n:
                temp = p_matrix[i][j] + matrix[i][j+1]
                if p_matrix[i][j+1] == 0 or p_matrix[i][j+1] > temp:
                    p_matrix[i][j+1] = temp

    # Backtrack find shortest path: O(n)
    i, j, path = n, n, [(n, n)]
    while (i, j) != (0, 0):
        if i == 0:
            path.append((i, j := j-1))
        elif j == 0:
            path.append((i := i-1, j))
        else:
            if p_matrix[i][j-1] < p_matrix[i-1][j]:
                path.append((i, j := j-1))
            else:
                path.append((i := i-1, j))
    return path[::-1]



def greedy(matrix):
    n = len(matrix) - 1
    i, j, path = 0, 0, [(0,0)]
    while (i, j) != (n, n):
        if i == n:
            path.append((i, j := j+1))
        elif j == n:
            path.append((i := i+1, j))
        else:
            if matrix[i][j+1] < matrix[i+1][j]:
                path.append((i, j := j+1))
            else:
                path.append((i := i+1, j))
    return path



def print_matrix(matrix):
    for line in matrix:
        print(''.join(str(i) for i in line))



def get_input(path) -> [int]:
    '''Parses the input file and returns an integer matrix'''
    arr = []
    with open(path) as f:
        for line in f:
            arr.append(list(int(c) for c in line.rstrip()))
    return arr



if __name__ == '__main__':
    run()
