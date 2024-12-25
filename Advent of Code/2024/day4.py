# Day 4: Ceres Search
# Part 1: 2644
# Part 2: 1952

import lib

def run():
    arr = process_input()
    find_xmas(arr)
    find_x_mas(arr)

def find_xmas(arr):
    o = 0

    # Vertical
    for i in range(len(arr)-3):
        for j in range(len(arr[i])):
            w = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
            if w in ('XMAS', 'SAMX'):
                o += 1

    # Horizontal
    for i in range(len(arr)):
        for j in range(len(arr[i])-3):
            w = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
            if w in ('XMAS', 'SAMX'):
                o += 1

    # Diagonal
    for i in range(len(arr)-3):
        for j in range(len(arr[i])-3):
            w = arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3]
            if w in ('XMAS', 'SAMX'):
                o += 1
    for i in range(len(arr)-3):
        for j in range(len(arr[i])-1,2,-1):
            w = arr[i][j] + arr[i+1][j-1] + arr[i+2][j-2] + arr[i+3][j-3]
            if w in ('XMAS', 'SAMX'):
                o += 1
    
    print(o)



def find_x_mas(arr):
    o = 0

    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            w1 = arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2]
            w2 = arr[i+2][j] + arr[i+1][j+1] + arr[i][j+2]
            if w1 in ('MAS', 'SAM') and w2 in ('MAS', 'SAM'):
                o += 1

    print(o)



def process_input():
    return lib.read_input('input4.txt')



if __name__ == '__main__':
    run()