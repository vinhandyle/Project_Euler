# Day 6: Lanternfish
# Part 1: 386755
# Part 2: 1732731810807

from collections import defaultdict

INPUT = 'input_6.txt'


def age_day(lfs: {int: int}) -> {int: int}:
    '''Returns the lanternfish dict aged by one day'''
    n_lfs = defaultdict(int)
    for k, v in lfs.items():
        if k == 0:
            n_lfs[8] += v
            n_lfs[6] += v
        else:
            n_lfs[k - 1] += v
    return n_lfs



def age(lfs: [int], days: int) -> [int]:
    '''Returns the number of lanternfish after the given number of days'''
    lfs = {n: lfs.count(n) for n in set(lfs)}
    for i in range(days):
        lfs = age_day(lfs)
    return sum(lfs.values())


    
def run():
    i = get_input()
    print(age(i, 80))
    print(age(i, 256))
    


def get_input() -> [int]:
    '''Parses the input file and returns an integer array'''
    with open(INPUT) as f:
        return list(int(x) for x in f.readline().rstrip().split(','))



if __name__ == '__main__':
    run()
