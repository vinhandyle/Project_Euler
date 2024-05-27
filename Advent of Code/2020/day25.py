# Day 25: Combo Breaker
# Part 1: 15217943

from pathlib import Path

pk_card = 8987316
pk_door = 14681524


def run() -> None:
    print(get_first_ans())



def get_first_ans() -> int:
    ls = brute_force_decrypt(pk_card)
    return transform(pk_door, ls)



def transform(num, loop_size):
    n = 1
    for i in range(loop_size):
        n *= num
        n %= 20201227
    return n


def brute_force_decrypt(pk):
    n, i = 1, 0
    while n != pk:
        n *= 7
        n %= 20201227
        i += 1
    return i

        

if __name__ == '__main__':
    run()
