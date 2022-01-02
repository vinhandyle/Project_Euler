# Day 1: Sonar Sweep
# Part 1: 1316
# Part 2: 1344

INPUT = 'input_1.txt'

def p1(arr: [int]) -> int:
    '''
    Returns the number of elements in the array
    that are greater than their predecessor.
    '''
    i = 0
    for n in range(1, len(arr)):
        if arr[n] > arr[n - 1]:
            i += 1
    return i



def p2(arr: [int]) -> [int]:
    '''
    Returns the number of 3-element sliding windows
    in the array that are greater than their predecessor.
    '''
    arr2 = []
    for i in range(1, len(arr) - 1):
        arr2.append(arr[i - 1] + arr[i] + arr[i + 1])
    return p1(arr2)



def run():
    i = get_input()
    print(p1(i))
    print(p2(i))



def get_input() -> [int]:
    '''Parses the input file and returns an integer array'''
    arr = []
    with open(INPUT) as f:
        for line in f:
            arr.append(int(line.rstrip()))
    return arr



if __name__ == '__main__':
    run()
