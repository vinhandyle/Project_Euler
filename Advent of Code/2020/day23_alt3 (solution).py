# Day 23: Crab Cups
# Part 1: 35827964
# Part 2: 5403610688

INPUT = '219748365'
TEST = '389125467'
A = 100
B = 1000000
C = 10000000


def create_array(s):
    arr = [0] * (len(s) + 1)
    for i in range(len(s)):
        if i == len(s) - 1:
            arr[int(s[i])] = int(s[0])
        else:
            arr[int(s[i])] = int(s[i+1])
    return arr



def extend_array(arr, start, end):
    arr[arr.index(start)] = len(arr)
    arr += list(i+1 for i in range(len(arr), end+1))
    arr[-1] = start
    return arr



def cups(arr, moves, start):
    curr = start
    for i in range(moves):
        # Pick up cups: O(1)
        p = []
        p.append(arr[curr])
        p.append(arr[p[-1]])
        p.append(arr[p[-1]])

        # Pick destination: O(1)
        d = curr - 1
        while d in p or d == 0:
            d -= 1
            if d <= 0:
                d = len(arr) - 1

        # Insert cups: O(1)
        arr[curr] = arr[p[-1]]
        temp = arr[d]
        arr[d] = p[0]
        arr[p[-1]] = temp

        # Update current: O(1)
        curr = arr[curr]
    return arr


def run():
    target = INPUT
    start = int(target[0])
    arr = create_array(target)
    
    p1 = cups(arr, A, start)
    a1, i = [1], 0
    while i < len(arr) - 2:
        a1.append(p1[a1[-1]])
        i += 1
    print(a1[1:])

    e_arr = extend_array(create_array(target), start, B)
    p2 = cups(e_arr, C, start)
    a2 = [p2[1], p2[p2[1]]]
    print(a2[0], a2[1], a2[0] * a2[1])



if __name__ == '__main__':
    run()
