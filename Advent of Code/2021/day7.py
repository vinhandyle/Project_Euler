# Day 7: The Treachery of Whales
# Part 1: 347449
# Part 2: 98039527

from collections import defaultdict

INPUT = 'input_7.txt'



def sum_n(n: int) -> int:
    '''Returns the result of the summation from 1 to n'''
    return int((n + 1) * n / 2)



def min_fuel(pos: [int], exp = False) -> int:
    '''Returns the minimum fuel used based on the crab positions'''
    u = set(range(min(pos), max(pos) + 1))
    #print('\n'.join(f'{i}: {sum((sum_n(abs(n - i)) if exp else abs(n - i)) for n in pos)}' for i in u))
    return min(sum((sum_n(abs(n - i)) if exp else abs(n - i)) for n in pos) for i in u)


    
def run():
    i = get_input()
    print(min_fuel(i))
    print(min_fuel(i, True))



def get_input() -> [int]:
    '''Parses the input file and returns an integer array'''
    with open(INPUT) as f:
        return list(int(x) for x in f.readline().rstrip().split(','))



if __name__ == '__main__':
    run()
