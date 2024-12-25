# Day 18: RAM Run
# Part 1: 234
# Part 2: 58,19

import lib

def run():
    walls = process_input()  
    size, w = 71, 1024

    map, dist = shortest_path(init_map(size), walls[:w])
    print(dist)

    for i in range(w, len(walls)):
        map, dist = shortest_path(init_map(size), walls[:i])
        if dist == -1:
            print(i, walls[i-1])
            break



# Since all edges are the same weight, Dijkstra becomes BFS
def shortest_path(map, walls):
    start, end = (0,0), (len(map)-1, len(map)-1)
    walls, frontier, traversed = set(walls), [(start,0)], set()
    while len(frontier) > 0:
        pos, d = frontier.pop(0)
        r, c = pos
        traversed.add((r,c))
        if map[r][c] == -1:
            map[r][c] = d
            to_check = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
            for r2, c2 in to_check:
                if (r2,c2) not in traversed and (c2,r2) not in walls and \
                    r2 >= 0 and c2 >= 0 and r2 < len(map) and c2 < len(map):
                    frontier.append(((r2,c2), d+1))
    return map, map[end[0]][end[1]]



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



def init_map(size):
    map = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(-1)
        map.append(line)
    return map



def process_input():
    input = lib.read_input('input18.txt')
    walls = []
    for line in input:
        walls.append(tuple(int(i) for i in line.split(',')))
    return walls



if __name__ == '__main__':
    run()