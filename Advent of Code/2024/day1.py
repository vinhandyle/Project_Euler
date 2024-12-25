# Day 1: Historian Hysteria
# Part 1: 1319616
# Part 2: 27267728

import lib

def run():
    a1, a2 = process_input()
    
    diff = 0
    for i in range(len(a1)):
        diff += abs(a1[i] - a2[i])
    print(diff)

    d = dict()
    for num in a1:
        if num in d:
            continue
        d[num] = a2.count(num)

    score = 0
    for num in d:
        score += num * d[num]
    print(score)   



def process_input():
    input = lib.read_input('input1.txt')

    a1, a2 = [], []
    for line in input:
        x, y = line.split('   ')
        a1.append(int(x))
        a2.append(int(y))
    return sorted(a1), sorted(a2)



if __name__ == '__main__':
    run()