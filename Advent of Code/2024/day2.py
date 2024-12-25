# Day 2: Red-Nosed Reports
# Part 1: 220
# Part 2: 296

import lib

def run():
    arr = process_input()
    
    safe = 0
    for a in arr:
        safe += 1 if is_safe(a) else 0
    print(safe)

    safe = 0
    for a in arr:
        for i in range(len(a)):
            temp = a.copy()
            temp.pop(i)
            if is_safe(temp):
                safe += 1
                break
    print(safe)



def is_safe(arr):
    if arr[0] < arr[-1]:           
        for i in range(1,len(arr)):
            d = arr[i] - arr[i-1]
            if d < 1 or d > 3:
                return False
        return True
    elif arr[0] > arr[1]:
        for i in range(1,len(arr)):
            d = arr[i-1] - arr[i]
            if d < 1 or d > 3:
                return False
        return True
    else:
        return False



def process_input():
    input = lib.read_input('input2.txt')
    arr = []
    for line in input:
        arr.append(list(int(i) for i in line.split(' ')))
    return arr



if __name__ == '__main__':
    run()