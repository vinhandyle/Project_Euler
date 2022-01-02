# Day 9: Smoke Basin
# Part 1: 468 
# Part 2: 1280496

INPUT = 'input_9.txt'


def compare(m: [[int]], nonlow: {(int, int)}, c: (int, int), p: (int, int)):
    '''Add to the deeper point to the set'''
    if m[c[0]][c[1]] <= m[p[0]][p[1]]:
        nonlow.add(p)
    else:
        nonlow.add(c)



def get_nonlow(m: [[int]], i: int,  j: int) -> {(int, int)}:
    '''Returns the positions of non-minimum points in the area'''
    nonlow = set()
    if i != 0:
        compare(m, nonlow, (i, j), (i - 1, j))
        if j != 0:
            compare(m, nonlow, (i, j), (i - 1, j - 1))
        if j != len(m[0]) - 1:
            compare(m, nonlow, (i, j), (i - 1, j + 1))
    if i != len(m) - 1:
        compare(m, nonlow, (i, j), (i + 1, j))
        if j != 0:
            compare(m, nonlow, (i, j), (i + 1, j - 1))
        if j != len(m[0]) - 1:
            compare(m, nonlow, (i, j), (i + 1, j + 1))
    if j != 0:
        compare(m, nonlow, (i, j), (i, j - 1))
    if j != len(m[0]) - 1:
        compare(m, nonlow, (i, j), (i, j + 1))  
    return nonlow



def get_low(m: [[int]]) -> int:
    '''Returns the map's low points'''
    cells = set((i, j) for i in range(len(m)) for j in range(len(m[0])))
    low = []
    while len(cells) > 0:
        curr = cells.pop()
        nonlow = get_nonlow(m, *curr)
        if curr not in nonlow:
            low.append(curr)
        else:
            cells -= nonlow
    return low



def probe(m: [[int]], pos: (int, int), b: [(int, int)]) -> int:
    '''Returns the size of the basin (expanding in cardinal directions)'''
    i, j = pos
    if i == -1 or i == len(m) \
       or j == -1 or j == len(m[0]) \
       or m[i][j] == 9 or (i,j) in b:
        return 0
    else:
        adj = list((i + x, j + y) for x, y in [(-1,0),(1,0),(0,-1),(0,1)])
        b.append(pos)
        return 1 + sum(probe(m, (i, j), b) for i, j in adj)
        


def get_basins(m: [[int]], low: {(int, int)}) -> [int]:
    '''Returns the list of all basin sizes ordered from least to greatest'''
    b = []
    for pos in low:
        b.append(probe(m, pos, []))
    return sorted(b)

    
    
def run():
    i = get_input()
    low = get_low(i)
    
    d = list(i[j][k] for j, k in low)
    print(sum(d) + len(d))

    b = get_basins(i, low)
    print(b[-1] * b[-2] * b[-3])



def get_input() -> [int]:
    '''Parses the input file and returns an integer matrix'''
    m = []
    with open(INPUT) as f:
        for line in f:
            m.append(list(int(x) for x in line.rstrip()))
    return m



if __name__ == '__main__':
    run()
