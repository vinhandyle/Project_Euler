# Day 5: Binary Boarding
# Part 1: 951
# Part 2: 653

from pathlib import Path

import math


INPUT = Path('input_5.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the highest seat ID on a boarding pass'''
    boarding_passes = _get_boarding_passes()
    largest = 0

    for boarding_pass in boarding_passes:
        pass_id = _decrypt_boarding_pass(boarding_pass)
        if pass_id > largest:
            largest = pass_id

    return largest



def get_second_ans() -> int:
    '''Returns the missing seat ID, excluding the very front and back rows'''
    boarding_passes = _get_boarding_passes()
    id_list = []

    for boarding_pass in boarding_passes:
        pass_id = _decrypt_boarding_pass(boarding_pass)
        id_list.append(pass_id)

    id_list.sort()

    for index in range(len(id_list)):
        if id_list[index] + 1 < id_list[index + 1]:
            return id_list[index] + 1
    


def _decrypt_boarding_pass(boarding_pass: str) -> int:
    '''
    Returns the seat ID of a boarding pass given its binary space partitioning.
    '''
    num_list = [[], []]
    for index in range(len(boarding_pass)):
        char = boarding_pass[index]
        if index < 7:
            if char == 'B':
                num_list[0].append(0)
            else:
                num_list[0].append(1)
        else:
            if char == 'R':
                num_list[1].append(0)
            else:
                num_list[1].append(1)

    return _binary_to_str(num_list[0]) * 8 + _binary_to_str(num_list[1])



def _binary_to_str(num_list: [int]) -> int:
    '''Returns an integer given a list of 1s and 0s'''
    # The number of rows/cols is 2 ^ len(num_list)
    power = len(num_list)
    num = math.pow(2, power)

    # Subtracting power starts at half of the total
    # Subtracting power is applied to total if the value at that index is 1
    # Every iteration, the subtracting power is halved
    for index in range(power):
        num -= num_list[index] * math.pow(2, power - index - 1)

    return num - 1



def _get_boarding_passes() -> [str]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    strings.
    '''
    str_list = []
    file = open(INPUT, 'r')

    for line in file:
        str_list.append(line[:-1])

    file.close()
    return str_list



if __name__ == '__main__':
    run()
