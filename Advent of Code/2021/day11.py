# Day 11: Dumbo Octopus
# Part 1: 1665
# Part 2: 235

INPUT = 'input_11.txt'

    
    
def run():
    matrix, flashes = get_input(), 0
    #print_matrix(matrix)
    for i in range(100):
        matrix, f = update_step(matrix)
        flashes += f
        #print_matrix(matrix)
    print(flashes)

    matrix, i = get_input(), 0
    while True:
        i += 1
        matrix, _ = update_step(matrix)
        if sum(sum(line) for line in matrix) == 0:
            print(i)
            break


def update_step(matrix):
    # Increase energy levels
    mx, my = len(matrix[0]), len(matrix)
    for i in range(my):
        for j in range(mx):
            matrix[i][j] += 1
            
    # Check flash    
    f, flashes = 0, None
    while f != flashes:
        flashes = f
        for i in range(my):
            for j in range(mx):
                if matrix[i][j] > 9:
                    f += 1
                    flash(matrix, mx, my, i, j)               

    # Reset energy levels
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0

    return matrix, flashes



def flash(matrix, mx, my, row, col):
    matrix[row][col] = -100
    x, y = {-1, 0, 1}, {-1, 0, 1}
    
    if row == 0:
        y.remove(-1)
    elif row == my - 1:
        y.remove(1)
    if col == 0:
        x.remove(-1)
    elif col == mx - 1:
        x.remove(1)

    for dx in x:
        for dy in y:
            matrix[row + dy][col + dx] += 1



def print_matrix(matrix):
    for line in matrix:
        print(''.join(str(i) for i in line))
    print()


        
def get_input() -> [int]:
    '''Parses the input file and returns an integer matrix'''
    matrix = []
    with open(INPUT) as f:
        for line in f:
            matrix.append(list(int(c) for c in line.rstrip()))
    return matrix



if __name__ == '__main__':
    run()
