# Day 13: Claw Contraption
# Part 1: 29711
# Part 2: 

import numpy as np
import lib

def run():
    machines = process_input() 
    
    tot = 0
    for m in machines:
        tot += play_fast(m)
    print(tot)

    tot = 0
    for m in machines:
        tot += play_fastest(m)
    print(tot)

    tot = 0
    for m in machines:
        a, b, p = m
        p = (p[0] + 10000000000000, p[1] + 10000000000000)
        #tot += play_fastest((a, b, p))
    print(tot)



# Brute force: O(n^2)
def play(m):
    a, b, p = m
    n_a = max(p[0]//a[0], p[1]//a[1])
    n_b = max(p[0]//b[0], p[1]//b[1])
    wins = []
    for i in range(n_a):
        for j in range(n_b):
            x = a[0] * i + b[0] * j
            y = a[1] * i + b[1] * j
            if (x, y) == p:
                wins.append(3 * i + j)
    return 0 if len(wins) == 0 else min(wins)
    


# Optimized brute force: O(n)
def play_fast(m):
    a, b, p = m
    n = max(p[0]//b[0], p[1]//b[1])
    i, di = n, max(1, min(a[0]//b[0], a[1]//b[1]))
    while i >= 0:
        if (b[0] * i, b[1] * i) == p:
            return i
        else:
            j = (p[0] - b[0] * i) // a[0]
            if (a[0] * j + b[0] * i, a[1] * j + b[1] * i) == p:
                return 3 * j + i
        i -= di
    return 0



# Linear Algebra: O(1)?
def play_fastest(m):
    a, b, p = m
    matA = np.matrix([a, b]).transpose()
    matb = np.matrix(p).transpose()
    matx = np.linalg.lstsq(matA, matb)[0]
    return matx[0,0] * 3 + matx[1,0]



def process_input():
    input = lib.read_input('input13.txt')
    machines = []
    for line in input:
        ws = line.split(' ')
        if len(ws) == 1:
            continue
        if ws[1] == 'A:':
            machines.append([(int(ws[-2][2:-1]), int(ws[-1][2:]))])
        else:
            machines[-1].append((int(ws[-2][2:-1]), int(ws[-1][2:])))
    return machines



if __name__ == '__main__':
    run()