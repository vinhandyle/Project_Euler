# Day 14: Restroom Redoubt
# Part 1: 229980828
# Part 2: 7132

import math
import lib

def run():
    robots = process_input() 
    size = (101, 103)
    
    pos = update_map(robots, size, 100)
    q = get_safety_factor(pos, size)
    print(q)

    #data = ''
    #for i in range(10000):
    #    map = get_map(robots, size, i)
    #    data += f'{i}\n{lib.print_matrix(map)}\n'
    #lib.log('output14.txt', data)

    ans = None
    for i in range(10000):
        pos = update_map(robots, size, i)
        v = get_entropy(pos)
        if ans is None or v > ans[1]:
            ans = (i, v)   
    print(lib.print_matrix(get_map(robots, size, ans[0])))
    print(ans)



# How close together the robots are (higher score = lower entropy)
def get_entropy(pos):
    e, p = dict(), set()
    for x, y in pos:
        if (x,y) not in p:
            p.add((x,y))
            x = x // 10
            y = y // 10
            if (x,y) not in e:
                e[(x,y)] = 0
            e[(x,y)] += 1
    return max(e.values())



def get_map(robots, size, cycles):
    pos = update_map(robots, size, cycles)
    map = []
    for i in range(size[1]):
        line = []
        for j in range(size[0]):
            line.append('.')
        map.append(line)
    for x, y in pos:
        map[y][x] = '|'
    return map



def get_safety_factor(pos, size):
    q = [0] * 4
    xl, xr = size[0] // 2, size[0] // 2 + size[0] % 2
    yt, yb = size[1] // 2, size[1] // 2 + size[1] % 2
    for x, y in pos:
        if x < xl:
            if y < yt:
                q[0] += 1
            elif y >= yb:
                q[1] += 1
        elif x >= xr:
            if y < yt:
                q[2] += 1
            elif y >= yb:
                q[3] += 1
    return math.prod(q)



def update_map(robots, size, cycles):
    final_pos = []
    for p, v in robots:
        px, py = p
        vx, vy = v
        fx = (px + vx * cycles) % size[0]
        fy = (py + vy * cycles) % size[1]
        final_pos.append((fx, fy))
    return final_pos



def process_input():
    input = lib.read_input('input14.txt')
    robots = []
    for line in input:
        temp = line.split(' ')
        p = tuple(int(i) for i in temp[0][2:].split(','))
        v = tuple(int(i) for i in temp[1][2:].split(','))
        robots.append((p,v))
    return robots



if __name__ == '__main__':
    run()