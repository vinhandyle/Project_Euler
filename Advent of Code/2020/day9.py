# Day 9: Encoding Error
# Part 1: 23278925
# Part 2: 4011064

from pathlib import Path

INPUT = Path('input_9.txt')
PAST_LENGTH = 25


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the first number in the list that is not the sum of two of previous
    x numbers.
    '''
    num_list = _get_num_list()

    for index in range(PAST_LENGTH, len(num_list)):
        summable_list  = num_list[index - PAST_LENGTH:index]
        summable = False

        # If the number is summable, its difference
        # must be contained in the list of previous numbers
        for num in summable_list:
            diff = num_list[index] - num
            if diff in summable_list:
                summable = True
                break
            
        if not summable:
            return num_list[index]



def get_second_ans() -> int:
    '''
    Returns the sum of the smallest and largest numbers in the contiguous set of
    numbers whose sum is the first invalid number in list.
    '''
    num_list = _get_num_list()
    invalid_num = get_first_ans()
    ans_list = []

    for index in range(len(num_list)):
        i = 0
        diff = invalid_num

        # Check value of current number and next number
        # If difference - current number >= next_number: keep going
        while index + i < len(num_list) - 1:
            num = num_list[index + i]
            next_num = num_list[index + i + 1]
            
            diff -= num
            ans_list.append(num)
            i += 1
            
            if diff < next_num:
                break

        # There are atleast two elements
        # and no remainder
        if i < 2 or diff != 0:
            ans_list = []
        else:
            break

    ans_list.sort()
    return ans_list[0] + ans_list[-1] 



def _get_num_list() -> [int]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    integers.
    '''
    file = open(INPUT, 'r')
    num_list = []

    for line in file:
        if line[-1] == '\n':
            num = int(line[:-1])
        else:
            num = int(num)
        num_list.append(num)
    
    file.close()
    return num_list



if __name__ == '__main__':
    run()
