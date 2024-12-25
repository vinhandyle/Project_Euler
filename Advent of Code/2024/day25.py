# Day 25: Code Chronicle
# Part 1: 2978

import lib

def run():
    locks, keys = process_input()  

    lock_pins = list(get_pins(lock, False) for lock in locks)
    key_pins = list(get_pins(key, True) for key in keys)
    tot = 0
    for pin in lock_pins:
        tot += find_fit(pin, key_pins)
    print(tot)



def find_fit(lock, keys):
    fits = 0
    for key in keys:
        if all(lock[i] < key[i] for i in range(len(lock))):
            fits += 1
    return fits



def get_pins(schema, reverse):
    pins = []
    rows = range(len(schema)-1,-1,-1) if reverse else range(0, len(schema))
    for col in range(0, len(schema[0])):
        for row in rows:
            if schema[row][col] == '.':
                pins.append(row + (1 if reverse else -1))
                break
    return pins



def process_input():
    input = lib.read_input('input25.txt')
    locks, keys, schema = [], [], []
    for line in input:
        if len(line) == 0:
            if schema[0][0] == '#':
                locks.append(schema)
            elif schema[0][0] == '.':
                keys.append(schema)
            schema = []
        else:
            schema.append(line)
    if schema[0][0] == '#':
        locks.append(schema)
    elif schema[0][0] == '.':
        keys.append(schema)
    return locks, keys
             


if __name__ == '__main__':
    run()