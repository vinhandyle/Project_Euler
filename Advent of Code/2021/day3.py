# Day 3: Binary Diagnostic
# Part 1: 2583164
# Part 2: 2784375

INPUT = 'input_3.txt'


def to_bin(arr, inverse = False):
    '''Return an array representing the binary value'''
    b_arr = []
    for i in arr:
        b_arr.append(0 if (i > 0 if inverse else i < 0) else 1)
    return b_arr



def to_dec(b_arr):
    '''Converts the binary value (array) into a decimal value'''
    dec = 0
    for i in range(len(b_arr)):
        dec += b_arr[::-1][i] * 2 ** i
    return dec
    
    
    
def most_common_bits(arr: [str]) -> [int]:
    '''
    Returns an array of the most common bit
    for each index (0 is replace with -1).
    '''
    i_arr = []
    for n in arr:
        for i in range(len(n)):
            if i == len(i_arr):
                i_arr.append(0)
            i_arr[i] += 1 if n[i] == '1' else -1
    return i_arr



def filter_minority(arr: [str], index: int, inverse = False) -> [str]:
    '''
    Filter from the array of binary values that don't
    contain the most common bit in the given index.
    '''
    bit = 0
    if len(arr) == 1:
        return arr
    for n in arr:
        bit += 1 if n[index] == '1' else -1
        
    if inverse:
        bit = 1 if bit < 0 else 0
    else:
        bit = 0 if bit < 0 else 1
    return list(filter(lambda x: bit.__eq__(int(x[index])), arr))
        


def p1(arr: [str]) -> int:
    '''Returns the product of the gamma and epsilon rates'''
    m = most_common_bits(arr)
    return to_dec(to_bin(m)) * to_dec(to_bin(m, True))



def p2(arr: [str]) -> int:
    '''
    Returns the product of the oxygen generator and C02 scrubber ratings
    '''
    o_arr, c_arr = arr, arr
    for i in range(len(arr[0])):
        o_arr = filter_minority(o_arr, i)
        c_arr = filter_minority(c_arr, i, True)
    return to_dec(list(int(o) for o in list(o_arr[0]))) \
           * to_dec(list(int(c) for c in list(c_arr[0])))


    
def run():
    i = get_input()
    print(p1(i))
    print(p2(i))
    


def get_input() -> [str]:
    '''Parses the input file and returns a string array'''
    arr = []
    with open(INPUT) as f:
        for line in f:
            arr.append(line.rstrip())
    return arr



if __name__ == '__main__':
    run()
