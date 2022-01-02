# Day 23: Crab Cups
# Part 1: 35827964
# Part 2:

INPUT = '219748365'
TEST = '389125467'
A = 100
B = 10000000


def shuffle_cups(cups: [int], amount: int) -> ([int], int):
    '''
    Given a list of integers, returns a list of integers after the given
    amount of Crab shuffles and the index of the integer 1 in that list.
    '''
    # Get current value -> Group next three values -> Find destination value ->
    # Move grouped values before destination value ->
    # Destination becomes current value -> Repeat
    c_index = 0
    picked_up = []
    
    for i in range(A):
        curr_val = cups[c_index] - 1
        
        for j in range(1, 4):
            picked_up.append(cups.pop(c_index + 1 if c_index + 1 < len(cups) else 0))

        while curr_val in set(picked_up):
            curr_val -= 1
            if curr_val <= 0:
                curr_val = max(cups + picked_up)

        d_index = cups.index(curr_val, c_index + 1 if c_index + 1 < len(cups) else 0)
        for j in range(3):
            cups.insert(d_index + j, picked_up.pop(0))
                
        c_index = d_index + 3 if d_index + 3 < len(cups) else 0        

    return cups, cups.index(1)

assert shuffle_cups([int(c) for c in TEST], 10) == ([5,8,3,7,4,1,9,2,6], 5)




def get_first_ans(arr: [int]) -> str:
    '''Returns the labels of the cups following cup 1 after 100 moves'''
    arr, i = shuffle_cups(arr, A)
    return ''.join(str(i) for i in arr[arr.index(i) + 1:] + arr[:arr.index(i)])

assert get_first_ans([int(c) for c in TEST]) == '67384529'
assert get_first_ans([int(c) for c in INPUT]) == '35827964'




def get_second_ans(arr: [int]) -> int:
    '''
    Returns the product of the labels of the two cups following cup 1 after
    ten million moves.
    '''
    arr += list(range(10, 10 ** 6 + 1))
    arr, i = shuffle_cups(arr, B)
    return arr[i + 1 if i + 1 < len(arr) else 0] * arr[i + 2 if i + 2 < len(arr) else 0]

assert get_second_answer([int(c) for c in TEST]) == 149245887792




def run() -> None:
    iarr = [int(c) for c in INPUT]
    print(iarr)
    #print(get_first_ans(iarr))
    #print(get_second_ans(iarr))




if __name__ == '__main__':
    run()
