# Day 8: Resonant Collinearity
# Part 1: 244
# Part 2: 912

import lib

def run():
    d, x, y = process_input()
    
    ap = set()
    for k in d:
        ap = ap.union(find_antipode(d[k], x, y))
    print(len(ap))

    ap = set()
    for k in d:
        ap = ap.union(find_antipode_2(d[k], x, y))
    print(len(ap))



def find_antipode(al, x, y):
    ap = set()
    for a1 in al:
        temp = al.copy()
        temp.remove(a1)
        for a2 in temp:
            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]
            a3 = (a2[0] + dx, a2[1] + dy)
            if a3[0] < 0 or a3[0] >= x or a3[1] < 0 or a3[1] >= y:
                continue
            ap.add(a3)
    return ap



def find_antipode_2(al, x, y):
    ap = set()
    for a1 in al:
        ap.add(a1)
        temp = al.copy()
        temp.remove(a1)
        for a2 in temp:
            dx = a2[0] - a1[0]
            dy = a2[1] - a1[1]
            dx, dy = lcd(dx, dy)
            a3 = (a2[0] + dx, a2[1] + dy)
            while not(a3[0] < 0 or a3[0] >= x or a3[1] < 0 or a3[1] >= y):
                ap.add(a3)
                a3 = (a3[0] + dx, a3[1] + dy)
    return ap



def lcd(a, b):
    for i in range(min(abs(a), abs(b)), 1, -1):   
        ta = a / i
        tb = b / i
        if ta - int(ta) == 0 and tb - int(tb) == 0:
            return ta, tb
    return a, b



def process_input():
    input = lib.read_input('input8.txt')
    d = dict()
    for i in range(len(input)):
        for j in range(len(input[i])):
            c = input[i][j]
            if alphanumeric(c):
                if c not in d:
                    d[c] = []
                d[c].append((i,j))
    return d, len(input), len(input[0])



def alphanumeric(c):
    o = ord(c)
    return (o >= ord('0') and o <= ord('9')) \
    or (o >= ord('A') and o <= ord('Z')) \
    or (o >= ord('a') and o <= ord('z'))



if __name__ == '__main__':
    run()