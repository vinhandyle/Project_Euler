# Day 5: Print Queue
# Part 1: 4135
# Part 2: 5285

import lib

def run():
    rules, ordering = process_input()
    iordering = []

    # Correct order
    tot = 0
    for o in ordering:
        valid = True
        for i in range(1, len(o)):
            a, temp = o[i], o[:i]
            if a not in rules:
                continue
            for b in rules[a]:
                if b in temp:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            tot += o[len(o)//2]
        else:
            iordering.append(o)
    print(tot)  

    # Fix incorrect order
    tot = 0
    for io in iordering:
        o = []
        for a in io:
            if a not in rules:
                o.append(a)
                continue
            valid = True
            for b in o:
                if b in rules[a]:
                    o.insert(o.index(b), a)
                    valid = False
                    break
            if valid:
                o.append(a)
        tot += o[len(o)//2]
    print(tot)



def process_input():
    lines = lib.read_input('input5.txt')
    rules = dict()
    ordering = []
    b = True

    for line in lines:
        if line == "":
            b = False
            continue
        if b:
            a, b = tuple(int(i) for i in line.split('|'))
            if a not in rules:
                rules[a] = set()
            rules[a].add(b)
        else:
            ordering.append(list(int(i) for i in line.split(',')))
    
    return rules, ordering


if __name__ == '__main__':
    run()