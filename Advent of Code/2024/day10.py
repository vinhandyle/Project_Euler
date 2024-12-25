# Day 10: Hoof It
# Part 1: 816
# Part 2: 1960

import lib

def run():
    map = process_input() 

    score, rating = 0, 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                s, r = find_trail_score((i,j), map)
                score += s
                rating += r
    print(score)
    print(rating)



def find_trail_score(start, map):
    end = set()
    rating = 0
    def recurse(pos, h):
        nonlocal end, rating
        if h == 9:         
            end.add(pos)
            rating += 1
        else:
            row, col = pos
            nxt = [(row-1,col), (row+1,col), \
                   (row,col-1), (row,col+1)]
            for n_pos in nxt:
                if n_pos[0] < 0 or n_pos[0] >= len(map) or n_pos[1] < 0 or n_pos[1] >= len(map[0]):
                    continue
                if map[n_pos[0]][n_pos[1]] == h + 1:
                    recurse(n_pos, h + 1)
    recurse(start, 0)
    return len(end), rating



def process_input():
    return list(list(int(c) for c in line) for line in lib.read_input('input10.txt'))



if __name__ == '__main__':
    run()