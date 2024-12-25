# Day 15: Warehouse Woes
# Part 1: 1438161
# Part 2: 1437981

import lib

def run():
    map, moves = process_input()

    start, boxes, walls = find_elements(map)
    t_boxes = trace(start, moves, boxes, walls, len(map)-1, len(map[0])-1)
    score = get_gps_score(t_boxes)
    print(score)

    start, boxes, walls = find_wide_elements(widen_map(map))
    t_boxes = trace_wide(start, moves, boxes, walls, len(map)-1, 2*len(map[0])-1)
    score = get_wide_gps_score(t_boxes)
    print(score)



def get_gps_score(boxes):
    return sum(100 * b[0] + b[1] for b in boxes)



def get_wide_gps_score(boxes):
    return sum(100 * b[0] + b[1] for b, _ in boxes)



def trace(start, moves, boxes, walls, ev, eh):    
    pos = start
    for mv in moves:
        # Get movement direction
        d = None
        if mv == '<':
            d = (0,-1)
        elif mv == '>':
            d = (0,1)
        elif mv == '^':
            d = (-1,0)
        else:
            d = (1,0)

        # Check boxes in the way
        to_move = [pos]
        new_pos = (pos[0]+d[0], pos[1]+d[1])
        if new_pos in boxes:
            t_pos = pos
            while (t_box := (t_pos[0]+d[0], t_pos[1]+d[1])) in boxes:
                t_pos = t_box
                to_move.append(t_box)

        # Check wall in the way
        if (to_move[-1][0]+d[0], to_move[-1][1]+d[1]) in walls:
            to_move = []
        else:
            pos = new_pos

        # Move valid elements
        for t in to_move[1:]:
            boxes.remove(t)
        for t in to_move[1:]:
            boxes.add((t[0]+d[0], t[1]+d[1]))
        
        #print_boxes(pos, boxes, walls, ev, eh)
    return boxes



def trace_wide(start, moves, boxes, walls, ev, eh):
    pos = start
    for mv in moves:
        # Get movement direction
        d = None
        #print(mv)
        if mv == '<':
            d = (0,-1)
        elif mv == '>':
            d = (0,1)
        elif mv == '^':
            d = (-1,0)
        else:
            d = (1,0)

        # Check boxes in the way
        to_move = set()
        new_pos = (pos[0]+d[0], pos[1]+d[1])
        if any(new_pos in b for b in boxes):
            temp = [new_pos]
            while len(temp) > 0:
                new_temp = []
                for t in temp:
                    for b in boxes:
                        if t in b:
                            to_move.add(b)
                            # Vertical movement can affect up to 2 more boxes
                            if d[0] != 0:
                                new_temp.append((b[0][0]+d[0], b[0][1]+d[1]))
                                new_temp.append((b[1][0]+d[0], b[1][1]+d[1]))
                            elif d[1] < 0:
                                new_temp.append((b[0][0], b[0][1]+d[1]))
                            else:
                                new_temp.append((b[1][0], b[1][1]+d[1]))
                temp = new_temp

        # Check wall in the way
        to_check = [new_pos]
        for b in to_move:
            for s in b:
                to_check.append((s[0]+d[0], s[1]+d[1]))
        if all(t not in walls for t in to_check):
            # Move valid elements
            pos = new_pos
            for t in to_move:
                boxes.remove(t)
            for t in to_move:
                l = (t[0][0]+d[0], t[0][1]+d[1])
                r = (t[1][0]+d[0], t[1][1]+d[1])
                boxes.add((l,r))
        
        #print_wide_boxes(pos, boxes, walls, ev, eh)
    return boxes



def print_boxes(pos, boxes, walls, ev, eh):
    map = []
    for i in range(ev+1):
        line = []
        for j in range(eh+1):
            line.append('.')
        map.append(line)

    map[pos[0]][pos[1]] = '@'
    for r, c in boxes:
        map[r][c] = 'O'
    for r, c in walls:
        map[r][c] = '#'
    print(f'{lib.print_matrix(map)}\n')



def print_wide_boxes(pos, boxes, walls, ev, eh):
    map = []
    for i in range(ev+1):
        line = []
        for j in range(eh+1):
            line.append('.')
        map.append(line)

    map[pos[0]][pos[1]] = '@'
    for l, r in boxes:
        lr, lc = l
        rr, rc = r
        map[lr][lc] = '['
        map[rr][rc] = ']'
    for r, c in walls:
        map[r][c] = '#'
    print(f'{lib.print_matrix(map)}\n')



def find_elements(map):
    start, boxes, walls = None, set(), set()
    for i in range(len(map)):
        for j in range(len(map[i])):
            t = map[i][j]
            if t == '@':
                start = (i,j)
            elif t == 'O':
                boxes.add((i,j))
            elif t == '#':
                walls.add((i,j))
    return start, boxes, walls



def find_wide_elements(map):
    start, boxes, walls = None, set(), set()
    for i in range(len(map)):
        left = None
        for j in range(len(map[i])):
            t = map[i][j]
            if t == '@':
                start = (i,j)
            elif t == '[':
                left = (i,j)
            elif t == ']':
                boxes.add((left, (i,j)))
            elif t == '#':
                walls.add((i,j))
    return start, boxes, walls



def widen_map(map):
    w_map = []
    for line in map:
        w_line = []
        for t in line:
            if t == '#':
                w_line.append('#')
                w_line.append('#')
            elif t == 'O':
                w_line.append('[')
                w_line.append(']')
            elif t == '.':
                w_line.append('.')
                w_line.append('.')
            elif t == '@':
                w_line.append('@')
                w_line.append('.')
        w_map.append(w_line)
    return w_map



def process_input():
    input = lib.read_input('input15.txt')
    map = []
    moves = []
    for line in input:
        if len(line) > 0:
            if line[0] == '#':
                map.append(list(str(c) for c in line))
            elif line[0] in '<>^v':
                moves += list(str(c) for c in line)
    return map, moves



if __name__ == '__main__':
    run()