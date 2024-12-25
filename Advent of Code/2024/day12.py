# Day 12: Garden Groups
# Part 1: 1371306
# Part 2: 805880

import lib

def run():
    map = process_input() 
    regions = find_regions(map)

    price = 0
    for i in regions:
        f = calc_fences(regions[i])
        price += len(regions[i] * f)
    print(price)

    price = 0
    for i in regions:
        s = calc_sides(regions[i])
        price += len(regions[i] * s)
    print(price)

    

def calc_fences(region):
    f = 0
    for r, c in region:
        if (r-1, c) not in region:
            f += 1
        if (r+1, c) not in region:
            f += 1
        if (r, c-1) not in region:
            f += 1
        if (r, c+1) not in region:
            f += 1
    return f



def calc_sides(region):
    sides = []

    # Get fences
    for r, c in region:
        temp = []
        if (r-1, c) not in region:
            temp.append((r, c, -1))
        if (r+1, c) not in region:
            temp.append((r, c, 1))
        if (r, c-1) not in region:
            temp.append((r, c, -2))
        if (r, c+1) not in region:
            temp.append((r, c, 2))

        # Build sides
        for s in temp:
            if len(sides) == 0:
                sides.append([s])
            else:
                v = False
                for side in sides:
                    if side[0][-1] == s[-1]:
                        for t in side:
                            tr, tc, dir = t
                            cv = abs(dir) == 1 and tr == r and abs(tc - c) == 1
                            ch = abs(dir) == 2 and tc == c and abs(tr - r) == 1
                            if ch or cv:
                                side.append(s)
                                v = True
                                break
                    if v:
                        break
                if not v:
                    sides.append([s])
    
        # Merge sides
        temp = []
        for side in sides:
            if len(temp) == 0:
                temp.append(side)
            else:
                v = False
                for tside in temp:
                    if tside[0][-1] == side[0][-1]:
                        for ts in tside:
                            tr, tc, dir = ts
                            for s in side:
                                r, c, _ = s
                                cv = abs(dir) == 1 and tr == r and abs(tc - c) == 1
                                ch = abs(dir) == 2 and tc == c and abs(tr - r) == 1 
                                if cv or ch:
                                    tside += side
                                    v = True
                                    break
                            if v:
                                break
                    if v:
                        break
                if not v:
                    temp.append(side)
    return len(temp)



def find_regions(map):
    traversed = set()
    regions = dict()

    def fill_region(r, c, i):
        if (r,c) in traversed or \
            r < 0 or c < 0 or r >= len(map) or c >= len(map[0]):
            return       
        if i not in regions:
            regions[i] = [(r,c)]
            traversed.add((r,c))
        else:
            nr, nc = regions[i][0]
            if map[r][c] == map[nr][nc]:
                regions[i].append((r,c))
                traversed.add((r,c))
            else:
                return
        fill_region(r-1, c, i)
        fill_region(r+1, c, i)
        fill_region(r, c-1, i)
        fill_region(r, c+1, i)
        
    for r in range(len(map)):
        for c in range(len(map[r])):
            if (r,c) in traversed:
                continue
            fill_region(r, c, len(regions))

    return regions



def process_input():
    return list(list(c for c in line) for line in lib.read_input('input12.txt'))



if __name__ == '__main__':
    run()