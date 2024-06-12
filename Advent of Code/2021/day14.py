# Day 14: Extended Polymerization
# Part 1: 3259
# Part 2: 

INPUT = 'input_14.txt'

    
    
def run():
    p, d = get_input()
    cl, cr = find_cycles(d,True), find_cycles(d,False)
    print('\n'.join(str(i) for i in cl.items()))
    print()
    print('\n'.join(str(i) for i in cr.items()))
    
    #print(divide_and_conquer(p, d, 10))
    #print(divide_and_conquer(p, d, 40))

    #o = dict()
    #def get_branch(pair):
        



def find_cycles(d, left):
    # Max length of a cycle is len(d) which is O(1)
    c = dict()
    for pair in d:
        cur, path = pair, []
        while cur not in path:
            path.append(cur)
            cur = cur[0] + d[cur] if left else d[cur] + cur[1]
        i = path.index(cur)
        c[pair] = (path[:i], path[i:])
    return c
    


def divide_and_conquer(p, d, max_depth):
    o = dict()

    # Log input string
    for c in p:
        if c not in o:
            o[c] = 0
        o[c] += 1
    
    def recurse(pair, depth):
        if depth < max_depth:
            # Log insertion
            insert = d[pair]
            if insert not in o:
                o[insert] = 0
            o[insert] += 1
            # Check self-cycle in first half
            if pair == pair[0] + insert:
                o[insert] += max_depth - depth
            else:
                recurse(pair[0] + insert, depth + 1)
            # Check self-cycle in second half
            if pair == insert + pair[1]:
                o[insert] += max_depth - depth
            else:
                recurse(insert + pair[1], depth + 1)

    for i in range(0, len(p) - 1):
        recurse(p[i] + p[i + 1], 0)

    return max(o.values()) - min(o.values())

            
    
def naive(p, d):
    # Time & Space: O(2^n)
    for i in range(40):
        p = pair_insertion(p, d)
        p += p
        if i == 10 or i == 40:
            o = get_occurrences(p)
            print(max(o.values()) - min(o.values()))


            
def pair_insertion(p, d):
    np = ''
    for i in range(0, len(p) - 1):
        np += p[i]
        np += d[f'{p[i]}{p[i+1]}']
    np += p[-1]
    return np



def get_occurrences(p):
    d = dict()
    for c in p:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d


    
def get_input():
    p, d = None, dict()
    mode = 0
    with open(INPUT) as f:
        for line in f:
            if len(line.rstrip()) == 0:
                mode += 1
                continue
            
            if mode == 0:
                p = line.rstrip()
            else:
                pair, insert = line.rstrip().split(' -> ')
                d[pair] = insert
    return p, d



if __name__ == '__main__':
    run()
