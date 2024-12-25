# Day 16: Reindeer Maze
# Part 1: 
# Part 2: 

import lib

def run():
    start, end, walls, map = process_input()

    mcp, move_map = min_cost_path(start, walls, map)
    print_map(mcp)
    print(lib.print_matrix(move_map))
    print(mcp[end[0]][end[1]])



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

    

# Basic DP didn't work due to turns (min cost to end doesn't equate to min cost for every step in the path)
def min_cost_path(start, walls, map):
    move_map, d = blank_map(map, start, walls), {-2:'<', -1:'^', 1:'v', 2:'>'}
    frontier, traversed = [(start,0)], set()
    while len(frontier) > 0:
        t = frontier.pop(0)
        traversed.add(t)
        pos, dir = t
        r, c = pos
        check = [((r-1, c), -1), ((r+1, c), 1), \
                 ((r, c-1), -2), ((r, c+1), 2)]
        for tc in check:
            if tc[0] not in walls:               
                cost = map[r][c] + (1 if dir == 0 or dir == tc[-1] else 1001)               
                tcr, tcc = tc[0]
                if map[tcr][tcc] == -1:
                    map[tcr][tcc] = cost       
                else:
                    map[tcr][tcc] = min(map[tcr][tcc], cost)
                if map[tcr][tcc] == cost and tc not in traversed:
                    frontier.insert(0, tc)
                    move_map[tcr][tcc] = d[tc[-1]]
    return map, move_map



def blank_map(ref, start, walls):
    map = []
    for i in range(len(ref)):
        line = []
        for j in range(len(ref[0])):
            t = (i,j)
            if t == start:
                line.append('S')
            else:
                line.append('#' if t in walls else '')
        map.append(line)
    return map



def process_input():
    input = lib.read_input('input16.txt')
    start, end, walls, map = None, None, set(), []
    for i in range(len(input)):
        line = []
        for j in range(len(input[0])):
            t = input[i][j]
            if t == 'S':
                start = (i,j)
                line.append(0)
            else:
                line.append(-1)
                if t == 'E':
                    end = (i,j)
                elif t == '#':
                    walls.add((i,j))
        map.append(line)
    return start, end, walls, map



if __name__ == '__main__':
    run()