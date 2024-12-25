# Day 3: Mull It Over
# Part 1: 157621318
# Part 2: 79845780

import lib

def run():
    arr = process_input()

    m = mull(arr)
    print(sum(x * y for x, y in m))

    m = d_mull(arr)
    print(sum(x * y for x, y in m))



def d_mull(input):
    arr = []
    for sec in input.split('do()'):
        arr += mull(sec.split('don\'t()')[0])         
    return arr
    
    
    
def mull(input):
    arr = []
    for op in input.split('mul(')[1:]:
        try:
            x, y = op.split(',')[:2]  
            if len(y.split(')')) < 2:
                continue            
            y = y.split(')')[0]
            x = int(x)
            y = int(y)
            arr.append((x,y))
        except Exception as ex:
            continue
    return arr



def process_input():
    return ''.join(lib.read_input('input3.txt'))



if __name__ == '__main__':
    run()
