# Day 9: Disk Fragmenter
# Part 1: 6154342787400
# Part 2: 6183632723350

import lib

def run():
    o_arr, fb = process_input()

    arr = back_fill(o_arr.copy(), fb)
    cs = checksum(arr)
    print(cs)

    arr = back_fill_2(o_arr.copy())
    cs = checksum(arr)
    print(cs)



def checksum(arr):
    tot = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            tot += i * arr[i]
    return tot



def back_fill(arr, fb):
    i, j, lf = 0, len(arr) - 1, 0

    # Find last free space to check
    for k in range(fb-1, -1, -1):
        if arr[:fb][k] == -1:
            lf = k
            break

    # Swap free and file blocks
    while arr[lf] == -1:
        if arr[i] != -1:
            i += 1
        if arr[j] == -1:
            j -= 1
        if arr[i] == -1 and arr[j] != -1:
            arr[i] = arr[j]
            arr[j] = -1
    return arr[:fb]



def back_fill_2(arr):
    files, frees = dict(), []

    # Tag each space
    free_start, free_size = 0, 0
    for i in range(len(arr)):
        b = arr[i]
        if b != -1:
            if free_size > 0:
                frees.append((free_start, free_size))
                free_start = 0
                free_size = 0
            if b not in files:
                files[b] = (0, i)
            cnt, start = files[b]
            files[b] = (cnt + 1, start)
        else:
            if free_size == 0:
                free_start = i
            free_size += 1

    # Swap free and file spaces
    for id in range(max(arr), -1, -1):
        d, start = files[id]
        for i in range(len(frees)):
            fstart, size = frees[i]
            if d <= size and start > fstart:
                for j in range(fstart, fstart + d):
                    arr[j] = id
                for j in range(start, start + d):
                    arr[j] = -1
                size -= d
                if size == 0:
                    frees.pop(i)
                else:
                    frees[i] = (fstart + d, size)
                break
    return arr



def process_input():
    input = lib.read_input('input9.txt')[0]
    arr, id, fb = [], 0, 0
    for i in range(len(input)):
        d = int(input[i])
        b = (i + 1) % 2
        for j in range(d):
            arr.append(id if i % 2 == 0 else -1)
            fb += b
        id += b
    return arr, fb



if __name__ == '__main__':
    run()