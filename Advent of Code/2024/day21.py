# Day 21: Keypad Conundrum 
# Part 1: 
# Part 2: 

import lib

def run():
    lines = process_input() 

    nps = calc_shortcuts(4, 3, (3,0))  
    dps = calc_shortcuts(4, 3, (0,0))

    tot = 0
    c1, c2, c3 = 'AAA'
    for line in lines:
        c1, i1 = pad_input(c1, line, nps, numpad_shortcut)
        c2, i2 = pad_input(c2, i1, dps, dirpad_shortcut)
        c3, i3 = pad_input(c3, i2, dps, dirpad_shortcut)
        tot += len(i3) * int(line[:-1])
        print(i3)
    print(tot)



def pad_input(start, seq, nps, f):
    cur, iseq = start, ''
    for c in seq:
        iseq += f(cur, c, nps)
        cur = c
    return cur, iseq



def numpad_shortcut(start, end, nps):
    numpad = {'7':(0,0), '8':(0,1), '9':(0,2), \
              '4':(1,0), '5':(1,1), '6':(1,2), \
              '1':(2,0), '2':(2,1), '3':(2,2), \
              '0':(3,1), 'A':(3,2),}
    return nps[(numpad[start], numpad[end])] + 'A'



def dirpad_shortcut(start, end, dps):
    dirpad = {'^':(0,1), 'A':(0,2), \
              '<':(1,0), 'v':(1,1), '>':(1,2)}
    return dps[(dirpad[start], dirpad[end])] + 'A'



def calc_shortcuts(rows, cols, wall):
    sdict, tiles = dict(), set()
    for i in range(rows):
        for j in range(cols):
            if (i,j) != wall:
                tiles.add((i,j))

    for t1 in tiles:
        frontier, traversed, map = [(t1, '')], set(), init_map(rows, cols)
        while len(frontier) > 0:
            pos, d = frontier.pop(0)
            r, c = pos
            traversed.add((r,c))
            if map[r][c] == -1:
                map[r][c] = d
                to_check = [(r-1,c,d+'^'), (r+1,c,d+'v'), (r,c-1,d+'<'), (r,c+1,d+'>')]
                for r2, c2, d2 in to_check:
                    if (r2,c2) not in traversed and (r2,c2) != wall and \
                        r2 >= 0 and c2 >= 0 and r2 < len(map) and c2 < len(map[0]):
                        frontier.append(((r2,c2), d2))
        for t2 in tiles:
            sdict[(t1,t2)] = map[t2[0]][t2[1]]
    return sdict
        


def init_map(r, c):
    map = []
    for i in range(r):
        line = []
        for j in range(c):
            line.append(-1)
        map.append(line)
    return map



def process_input():
    return list(line for line in lib.read_input('input21.txt'))



if __name__ == '__main__':
    run()