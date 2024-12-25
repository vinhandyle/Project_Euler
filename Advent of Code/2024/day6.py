# Day 6: Guard Gallivant
# Part 1: 4778
# Part 2: 1618

import lib

def run():
    arr = process_input()

    # Brute force trace
    print(trace_path(arr))

    # Brute force nested trace
    loops = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in '#^v<>':
                arr[i][j] = '#'
                _, loop = trace_path(arr)
                loops += 1 if loop else 0
                arr[i][j] = '.'
    print(loops)



def trace_path(map):
    rangle = {(0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0), (1,0):(0,1)}

    x, y, dx, dy = find_start(map)
    start = x, y
    pos, stops = set(), set()
    free = False

    while not free:
        while map[y][x] !='#':
            pos.add((x,y))
            x += dx
            y += dy           
            if y in (-1, len(map)) or x in (-1, len(map[0])):
                free = True
                break
        else:          
            if ((x,y,dx,dy)) in stops:
                return len(pos), True 
            stops.add((x,y,dx,dy))
            x -= dx
            y -= dy
            dx, dy = rangle[(dx,dy)]              
    return len(pos), False



def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'v':
                return x, y, 0, 1
            elif map[y][x] == '^':
                return x, y, 0, -1
            elif map[y][x] == '>':
                return x, y, 1, 0
            elif map[y][x] == '<':
                return x, y, -1, 0



def process_input():
    return list(list(line) for line in lib.read_input('input6.txt'))



if __name__ == '__main__':
    run()