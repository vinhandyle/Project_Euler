# Day 13: Transparent Origami
# Part 1: 661 
# Part 2: PFKLKCFP

INPUT = 'input_13.txt'

    
    
def run():
    dots, folds = get_input()
    
    matrix = create_matrix(dots)
    for fold in folds:
        matrix = fold_matrix(matrix, fold)
        print(dot_count(matrix))
        #print_matrix(matrix)
    print_matrix(matrix)



def fold_matrix(matrix, fold):
    axis, pivot = fold
    new_matrix = []
    # Fold left
    if axis == 'x':
        for i in range(pivot, 0, -1):
            for j in range(len(matrix)):
                if len(new_matrix) == j:
                    new_matrix.append([])
                new_matrix[j].append(matrix[j][pivot - i] * matrix[j][pivot + i])
    # Fold up
    else:
        # Extend paper with empty space if needed
        l = pivot * 2 + 1
        if l > len(matrix):
            for i in range(l - len(matrix)):
                matrix.append([1] * len(matrix[0]))
        # Fold
        for i in range(pivot, 0, -1):
            row = list(a * b for a, b in zip(matrix[pivot - i], matrix[pivot + i]))
            new_matrix.append(row)
    return new_matrix



def create_matrix(dots):
    mx = max(dot[0] for dot in dots) + 1
    my = max(dot[1] for dot in dots) + 1
    matrix = list([1] * mx for i in range(my))

    for dot in dots:
        matrix[dot[1]][dot[0]] = 0
    return matrix



def dot_count(matrix):
    return len(matrix) * len(matrix[0]) - sum(sum(line) for line in matrix)



def print_matrix(matrix):
    for line in matrix:
        for i in line:
            print('.' if i == 1 else '#', end='')
        print()
    print()


    
def get_input():
    dots, folds = [], []
    mode = 0
    with open(INPUT) as f:
        for line in f:
            if mode == 0:
                if len(line.rstrip()) == 0:
                    mode += 1
                    continue
                dots.append(tuple(int(i) for i in line.rstrip().split(',')))
            else:
                data = line[len('fold along '):].rstrip().split('=')
                folds.append((data[0], int(data[1])))
    return dots, folds



if __name__ == '__main__':
    run()
