# Day 23: LAN Party
# Part 1: 1330
# Part 2: hl,io,ku,pk,ps,qq,sh,tx,ty,wq,xi,xj,yp

import lib

def run():
    pairs = process_input()  
    nd = find_neighbors(pairs)

    tot, tri = 0, find_tri(nd)
    for t in tri:
        if any(c[0] == 't' in c for c in t):
            tot += 1
    print(tot)

    c = find_largest_clique(tri)
    print(','.join(sorted(c)))



# Within a clique, all vertices belonging have the same number of triangles
# 
# Vertices with many connections but part of smaller cliques will be pruned
# before vertices with fewer connections but part of larger cliques if pruning
# vertices in ascending order of how many triangles they are part of
def find_largest_clique(tri):
    d = find_tri_count(tri)
    while min(d.values()) != max(d.values()):
        v, pruned = min(d.values()), set()
        for k in d:
            if d[k] == v:
                pruned.add(k)
        for i in range(len(tri)-1,-1,-1):
            if any(c in pruned for c in tri[i]):
                tri.pop(i)
        d = find_tri_count(tri)
    return d.keys()



def find_tri_count(tri):
    d = dict()
    for t in tri:
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] += 1
    return d



def find_tri(nd):
    tri, seen = [], set()
    for c in nd:
        temp = set(nd[c]) - seen
        for n1 in temp:
            for n2 in temp:
                if n1 != n2 and n1 in nd[n2] and {c,n1,n2} not in tri:
                    tri.append({c,n1,n2})
        seen.add(c)
    return tri
                


def find_neighbors(pairs):
    nd = dict()
    for a, b in pairs:
        if a not in nd:
            nd[a] = set()
        nd[a].add(b)
        if b not in nd:
            nd[b] = set()
        nd[b].add(a)
    return nd



def process_input():
    input = lib.read_input('input23.txt')
    pairs = []
    for line in input:
        pairs.append(set(c for c in line.split('-')))
    return pairs



if __name__ == '__main__':
    run()