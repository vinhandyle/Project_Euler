# Day 17: Chronospatial Computer
# Part 1: 6,4,6,0,4,5,7,2,7
# Part 2: 

import lib

def run():
    reg, ops = process_input() 

    out = program(reg, ops)
    print(out)

    a = reverse_program(ops, ops[::-1])
    return(a)



def reverse_program(ops, out):
    a, jumps, prints = 0, find_instr(ops, 3), find_instr(ops, 5)
    for o in out:
        for p in prints:
            v = combo(p[1])
    return a



def find_instr(ops, code):
    instr = dict()
    for i in range(len(ops)-1):
        o = ops[i]
        if o == code:
            if o not in instr:
                instr[o] = []
            instr[o].append(i)
    return instr



def brute_force(ops, s):
    a = 0
    while True:
        out = set_program(a, ops)
        if out == s:
            return a
        else:
            a += 1



def set_program(a, ops):
    reg = {'A':a, 'B':0, 'C':0}
    return program(reg, ops)



def program(reg, ops):
    i, output = 0, ''
    while i < len(ops):
        opcode, operand = ops[i], ops[i+1]
        if opcode == 0:   # adv
            reg['A'] = reg['A'] // 2 ** combo(reg, operand)
        elif opcode == 1: # bxl
            reg['B'] = reg['B'] ^ operand
        elif opcode == 2: # bst
            reg['B'] = combo(reg, operand) % 8
        elif opcode == 3: # jnz
            if reg['A'] != 0:
                i = operand
                continue
        elif opcode == 4: # bxc
            reg['B'] = reg['B'] ^ reg['C']
        elif opcode == 5: # out
            output += f'{combo(reg, operand) % 8},'
        elif opcode == 6: # bdv
            reg['B'] = reg['A'] // 2 ** combo(reg, operand)
        elif opcode == 7: # cdv
            reg['C'] = reg['A'] // 2 ** combo(reg, operand)
        i += 2
    return output[:-1]



def combo(reg, operand):
    v = None
    if operand in range(4):
        v = operand
    elif operand == 4:
        v = reg['A']
    elif operand == 5:
        v = reg['B']
    elif operand == 6:
        v = reg['C']
    return v



def process_input():
    input = lib.read_input('input17.txt')
    reg, ops = dict(), []
    for line in input:
        if 'A' in line:
            reg['A'] = int(line.split(' ')[-1])
        elif 'B' in line:
            reg['B'] = int(line.split(' ')[-1])
        elif 'C' in line:
            reg['C'] = int(line.split(' ')[-1])
        elif len(line) > 0:
            ops = list(int(i) for i in line.split(' ')[-1].split(','))
    return reg, ops



if __name__ == '__main__':
    run()