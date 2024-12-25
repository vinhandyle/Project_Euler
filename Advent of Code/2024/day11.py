# Day 11: Plutonian Pebbles
# Part 1: 175006
# Part 2: 

import lib

def run():
    stones = process_input()

    s1 = blink(stones, 25)
    print(len(s1))

    s2 = blink(stones, 75)
    print(len(s2))
    


# Barely faster than single core brute force
def blink_multicore(stones, amt):
    from multiprocessing import Process
    processes = list(Process(target=blink, args=(stones[i:i+1], amt)) for i in range(len(stones))) 
    for process in processes:
        process.start()
    for process in processes:
        process.join()



def blink(stones, amt):
    for i in range(amt):
        new_stones = []
        for s in stones:
            ss = str(s)
            if s == 0:
                new_stones.append(1)
            elif len(ss) % 2 == 0:
                new_stones.append(int(ss[:len(ss)//2]))
                new_stones.append(int(ss[len(ss)//2:]))
            else:
                new_stones.append(s * 2024)
        stones = new_stones
        print(i, len(stones))
    return stones



def process_input():
    return list(int(w) for w in lib.read_input('input11.txt')[0].split(' '))



if __name__ == '__main__':
    run()