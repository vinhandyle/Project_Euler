# Day 24: Crossed Wires
# Part 1: 65740327379952
# Part 2: 

import lib

def run():
    d = process_input()  

    cd = compute_mappings(d)
    z = compute_num(cd, 'z')
    print(z)

    x = compute_num(cd, 'x')
    y = compute_num(cd, 'y')
    print(x, y)
    


def compute_num(d, prefix):
    zs = list(filter(lambda x: x[0] == prefix, sorted(d, key=lambda x: x, reverse=True)))
    n, i = 0, 0
    for z in zs[::-1]:
        n += d[z] * 2**i
        i += 1
    return n



def compute_mappings(d):
    cd, mapped = dict(), set()
    while len(mapped) < len(d):
        temp = set()
        for k in filter(lambda x: x not in mapped, d):
            if type(d[k]) is int:
                cd[k] = d[k]
                mapped.add(k)
            elif d[k][0] in mapped and d[k][1] in mapped:
                cd[k] = eval(d[k][2])
                mapped.add(k)
        mapped = mapped.union(temp)
    return cd



def process_input():
    input = lib.read_input('input24.txt')
    d = dict()
    for line in input:
        if ':' in line:
            k, v = line.split(':')
            d[k] = int(v.strip())
        elif len(line) > 0:
            arr, op = line.split(' '), ''
            if arr[1] == 'AND':
                op = '&'
            elif arr[1] == 'OR':
                op = '|'
            elif arr[1] == 'XOR':
                op = '^'
            d[arr[4]] = (arr[0], arr[2], f'cd[\'{arr[0]}\'] {op} cd[\'{arr[2]}\']')
    return d



if __name__ == '__main__':
    run()