# Day 22: Monkey Market
# Part 1: 18694566361
# Part 2: 

import lib

def run():
    arr = process_input()  

    # Calculate and save secret nums
    sdict, tot = dict(), 0
    for n in arr:
        tot += secret_num(n, 2000, sdict)
    print(tot)

    # Get all price change sequences grouped by end price, for each buyer
    prices, deltas, chains = [], [], []
    for s in sdict.values():
        prices.append(get_price(s))
    for p in prices:
        deltas.append(get_delta(p))
    for i in range(len(deltas)):
        chains.append(get_chains(prices[i], deltas[i]))

    # Algo
    tot = 0
    print(tot)



def merge_chains(chains):
    merge = set()
    for c in chains:
        for v in c.values():
            merge = merge.union(v)
    return merge



def get_chains(prices, deltas):
    d = dict()
    for i in range(4, len(prices)):
        if prices[i] not in d:
            d[prices[i]] = set()
        d[prices[i]].add((deltas[i-3], deltas[i-2], deltas[i-1], deltas[i]))
    return d



def get_delta(prices):
    arr = [0]
    for i in range(1, len(prices)):
        arr.append(prices[i] - prices[i-1])
    return arr



def get_price(seq):
    arr = []
    for n in seq:
        arr.append(n % 10)
    return arr



def secret_num(n, i, sdict):
    s = n
    sdict[n] = [n]
    for j in range(i):
        s = prune(mix(s, s * 64))
        s = prune(mix(s, s // 32))
        s = prune(mix(s, s * 2048))
        sdict[n].append(s)
    return s



def mix(a, b):
    return a ^ b

assert mix(42, 15) == 37



def prune(a):
    return a % 16777216

assert prune(100000000) == 16113920



def process_input():
    return list(int(line) for line in lib.read_input('input22.txt'))



if __name__ == '__main__':
    run()