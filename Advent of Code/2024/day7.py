# Day 7: Bridge Repair
# Part 1: 932137732557
# Part 2: 661823605105500

import lib

def run():
    d = process_input()

    tot = 0
    for v in d:
        tot += check_possible(v, d[v])
    print(tot)

    tot = 0
    for v in d:
        tot += check_possible_2(v, d[v])
    print(tot)



def check_possible(v, ns):
    def recurse(acc, left):
        if len(left) == 0:
            return acc == v
        else:
            return recurse(acc + left[0], left[1:]) \
                or recurse(acc * left[0], left[1:])
    return v if recurse(0, ns) else 0



def check_possible_2(v, ns):
    def recurse(acc, left):
        if len(left) == 0:
            return acc == v
        else:
            return recurse(acc + left[0], left[1:]) \
                or recurse(acc * left[0], left[1:]) \
                or recurse(acc * (10 ** len(str(left[0]))) + left[0], left[1:])
    return v if recurse(0, ns) else 0



def process_input():
    input = lib.read_input('input7.txt')
    d = dict()
    for line in input:
        v, ns = line.split(':')
        v = int(v)
        ns = list(int(n) for n in ns.strip().split(' '))
        d[v] = ns
    return d



if __name__ == '__main__':
    run()