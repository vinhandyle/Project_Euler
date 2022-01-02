# Day 2: Dive!
# Part 1: 1714680
# Part 2: 1963088820

INPUT = 'input_2.txt'

def p1(h: [int], d: [int]) -> int:
    '''Returns the product of the summation of the given arrays'''
    return sum(h) * sum(d)



def p2(h: [int], d: [int]) -> [int]:
    '''Returns the product of the summation of the given arrays'''
    return p1(h, d)



def run():
    print(p1(*get_input()))
    print(p2(*get_input(True)))



def get_input(aim: bool = False) -> ([int], [int]):
    '''Parses the input file and returns two integer array'''
    h, d = [], []
    a = 0
    with open(INPUT) as f:
        for line in f:
            mv, amt = line.rstrip().split(' ')
            if mv == 'forward':
                h.append(int(amt))
                if aim:
                   d.append(a * int(amt)) 
            else:
                amt = int(amt) if mv == 'down' else -int(amt)
                if not aim:
                    d.append(amt)
                else:
                    a += amt
    return h, d



if __name__ == '__main__':
    run()
