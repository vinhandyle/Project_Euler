# Day 5: Hydrothermal Venture
# Part 1: 7142
# Part 2: 20012

import re
from collections import defaultdict

INPUT = 'input_5.txt'


def deepen(holes: dict, vent: (int), diagonal: bool = False):
    '''Increases the depth of each point in the vent by 1'''
    if vent[0] == vent[2]:
        step = 1 if vent[1] < vent[3] else -1
        for i in range(vent[1], vent[3] + step, step):
            holes[(vent[0], i)] += 1
            
    elif vent[1] == vent[3]:
        step = 1 if vent[0] < vent[2] else -1
        for i in range(vent[0], vent[2] + step, step):
            holes[(i, vent[1])] += 1
            
    elif diagonal and (abs(vent[0] - vent[2]) == abs(vent[1] - vent[3])):
        stepX = 1 if vent[0] < vent[2] else -1
        stepY = 1 if vent[1] < vent[3] else -1
        for i in range(abs(vent[0] - vent[2]) + 1):
            holes[(vent[0] + stepX * i, vent[1] + stepY * i)] += 1
        
    return holes



def find_overlap(vents: [(int)], diagonal: bool = False) -> int:
    '''Returns the number of overlapping points'''
    holes = defaultdict(int)
    for v in vents:
        deepen(holes, v, diagonal)
    return len(list(filter(lambda v: v > 1, holes.values())))


    
def run():
    i = get_input()
    print(find_overlap(i))
    print(find_overlap(i, True))
    


def get_input() -> [(int)]:
    '''Parses the input file and returns an integer tuple array'''
    floor = []
    with open(INPUT) as f:
        for line in f:
            floor.append(tuple(int(i) for i in re.split(r",| -> ", line.rstrip())))           
    return floor



if __name__ == '__main__':
    run()
