# Day 20: Race Condition
# Part 1: 1395
# Part 2: 

import lib

def run():
    start, end, walls, rows, cols = process_input()  
    
    _, d = path_to_end(start, end, walls, init_map(rows, cols))

    # Brute force (very slow but feasible)
    c_walls = set(filter(lambda w: cheatable_wall(w, walls, (rows, cols)), walls))
    time_saved, tot = dict(), 0
    for w in c_walls:
        temp = walls.copy()
        temp.remove(w)
        _, cd = path_to_end(start, end, temp, init_map(rows, cols))
        ts = d - cd
        # Log
        if ts > 0:
            if ts not in time_saved:
                time_saved[ts] = 0
            time_saved[ts] += 1
            if ts >= 100:
                tot += 1
    print(tot)



def print_map(map):
    mat = []
    mx = len(str(max(max(line) for line in map)))
    for line in map:
        vec = []
        for w in line:
            s = str(w)
            s = (' ' * (mx - len(s))) + s
            vec.append(s)
        mat.append(vec)
    print('\n'.join(f'{vec}' for vec in mat))



def cheatable_wall(w, walls, lim):
    r, c = w
    free, to_check = 0, [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
    for t in to_check:
        if t not in walls and \
            t[0] >= 0 and t[1] >= 0 and \
                t[0] < lim[0] and t[1] < lim[1]:
            free += 1
    return free >= 2




def path_to_end(start, end, walls, map):
    frontier, traversed = [(start,0)], set()
    while len(frontier) > 0:
        pos, d = frontier.pop(0)
        r, c = pos
        traversed.add((r,c))
        if map[r][c] == -1:
            map[r][c] = d           
            to_check = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
            for r2, c2 in to_check:
                if (r2,c2) not in traversed and (r2,c2) not in walls and \
                    r2 >= 0 and c2 >= 0 and r2 < len(map) and c2 < len(map):                   
                    frontier.append(((r2,c2), d+1))
    return map, map[end[0]][end[1]]



def init_map(rows, cols):
    map = []
    for i in range(rows):
        line = []
        for j in range(cols):
            line.append(-1)
        map.append(line)
    return map



def process_input():
    input = lib.read_input('input20.txt')
    start, end, walls = None, None, set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            t = input[i][j]
            if t == 'S':
                start = (i,j)
            elif t == 'E':
                end = (i,j)
            elif t == '#':
                walls.add((i,j))
    return start, end, walls, len(input), len(input[0])



if __name__ == '__main__':
    run()