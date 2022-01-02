# Day 8: Seven Segment Search
# Part 1: 237
# Part 2: 1009098

from collections import defaultdict

INPUT = 'input_8.txt'


def get_unique(entries: [([str], [str])]) -> int:
    '''Return the number of instances of unique segment digits'''
    amt = 0
    for entry in entries:
        for p in entry[1]:
            amt += 1 if len(p) in {2, 3, 4, 7} else 0
    return amt



def get_key(v: [str]) -> {str: int}:
    '''Returns key used to decode the given string array'''
    #  0    |   0: 6    5: 5    |   1, 7, 4 (2, 3, 5), (0, 6, 9), 8
    # 1 2   |   1: 2    6: 6    | 
    #  3    |   2: 5    7: 3    | 
    # 4 5   |   3: 5    8: 7    |  
    #  6    |   4: 4    9: 6    |
    seg, key = dict(), dict()
    conl, cons = sorted(v, key = len), sorted((set(c) for c in v), key = len)

    key[1] = conl[0]
    key[7] = conl[1]
    key[4] = conl[2]
    key[8] = conl[9]

    seg[0] = (cons[1] - cons[0]).pop()
    for s in cons[6:9]:
        segs = s - cons[2] - {seg[0]}
        if len(segs) == 1:
            seg[6] = segs.pop()
            key[9] = conl[cons.index(s)]
    seg[4] = (cons[9] - cons[2] - {seg[0], seg[6]}).pop()

    key[2] = list(filter(lambda x: x.count(seg[4]) == 1, conl[3:6]))[0]
    for s in cons[3:6]:
        segs = s - set(key[2])
        if len(segs) == 1:
            seg[5] = segs.pop()
            key[3] = conl[cons.index(s)]
    seg[1] = (set(key[9]) - set(key[3])).pop()
    seg[3] = (cons[2] - cons[0] - {seg[1]}).pop()
    for s in cons[6:9]:
        if seg[3] not in s:
            key[0] = conl[cons.index(s)]
    
    key = {v: k for k, v in key.items()}
    for s in cons[3:6]:
        if conl[cons.index(s)] not in key:
            key[conl[cons.index(s)]] = 5
    for s in cons[6:9]:
        if conl[cons.index(s)] not in key:
            key[conl[cons.index(s)]] = 6
            
    return {tuple(k): v for k, v in key.items()}



def decode(key: {tuple: int}, o: str) -> int:
    '''Given the key and a string, return the output value'''
    for k, v in key.items():
        if set(k) == set(c for c in o):
            return v



def get_output(entries: [([str], [str])]) -> int:
    '''Return the sum of all output values after being decoded'''
    total = 0
    for e in entries:
        key = get_key(e[0])
        for i in range(4):
            total += decode(key, e[1][i]) * 10 ** (3 - i)
    return total


    
def run():
    i = get_input()
    print(get_unique(i))
    print(get_output(i))
    


def get_input() -> [([str], [str])]:
    '''Parses the input file and returns an integer array'''
    entries = []
    with open(INPUT) as f:
        for line in f:
            entries.append(tuple(l.rstrip().lstrip().split(' ') for l in line.split('|')))
    return entries


if __name__ == '__main__':
    run()
