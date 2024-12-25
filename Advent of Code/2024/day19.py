# Day 19: Linen Layout
# Part 1: 265
# Part 2: 752461716635602

import lib

def run():
    towels, designs = process_input() 

    d_towels = dict()
    for t in sorted(towels, key = lambda x: len(x)):
        if t[0] not in d_towels:
            d_towels[t[0]] = []
        d_towels[t[0]].append(t)
    
    tot = 0
    for d in designs:
        if valid_design(d_towels, d):
            tot += 1
    print(tot)

    mem, tot = dict(), 0
    for d in designs:
        tot += unique_designs(mem, d_towels, d)
    print(tot)



def unique_designs(mem, towels, d):
    if len(d) == 0:
        return 1
    elif d in mem:
        return mem[d]  
    head = d[0]
    if head not in towels:
        return 0
    else:
        u = 0
        for t in towels[head]:
            if d[:len(t)] == t:
                u += unique_designs(mem, towels, d[len(t):])
        mem[d] = u
        return u



def valid_design(towels, d):
    if len(d) == 0:
        return True 
    head = d[0]
    if head not in towels:
        return False
    else:
        for t in towels[head]:
            if d[:len(t)] == t:
                v = valid_design(towels, d[len(t):])
                if v:
                    return True
    return False



def process_input():
    input = lib.read_input('input19.txt')
    towels, designs = [], []
    for line in input:
        if ',' in line:
            towels = line.split(', ')
        elif len(line) > 0:
            designs.append(line)
    return towels, designs



if __name__ == '__main__':
    run()