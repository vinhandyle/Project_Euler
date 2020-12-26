# Day 13: Shuttle Search
# Part 1: 138
# Part 2: 226845233210288

from pathlib import Path

import math

INPUT = Path('input_13.txt')

# Simple brute force increments in multiples of the first number (super slow)
#
# Better brute force goes directly to the next multiple of the number which
# broke the chain (faster but still too slow)
#
# Fastest algorithm goes directly to the next multiple of the first number which
# satisfies the relation which the previous numbers in the chain (super fast)
SIMPLE = False 
TIME = False


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the product of the ID of the earliest bus takeable and the number of
    minutes needed to wait for that bus.
    '''
    my_time, time_list = _get_time_stamps()
    smallest = (0, my_time)

    for time in time_list:
        diff = time[0] - my_time % time[0]
        if diff < smallest[1]:
            smallest = (time[0], diff)

    return smallest[0] * smallest[1]



def get_second_ans() -> int:
    '''
    Returns the earliest timestamp such that all of the listed bus IDs depart
    at offsets matching their index.
    '''
    my_time, time_list = _get_time_stamps()

    x = _brute_force
    y = _fastest_algorithmn

    return y(time_list)



def _fastest_algorithmn(time_list: [(int, int)]) -> int:
    '''
    Calculates the smallest number which satisfies the offset time criteria for
    every number in the chain before adding the next number to the chain.
    Returns the number resulting from a full chain.
    '''
    multiplier = 1
    time_list_index = 0
    
    starts = dict()
    base_time = time_list[0][0]

    while time_list_index < len(time_list):
        start = base_time * multiplier
        bus_info = time_list[time_list_index]
        bus_time, bus_index = bus_info
        

        # Next multiplier = Current mulitplier + x * i
        # x = The product of every bus time up to but not including the
        # current one and the base time
        # i = unknown factor

        # Finds x
        time_multiplier = 1
        for i in range(1, time_list_index):
            time_multiplier *= time_list[i][0]

        # Finds i
        while (base_time * multiplier + bus_index) % bus_time != 0:
            multiplier += time_multiplier

        time_list_index += 1

    return base_time * multiplier
        



def _brute_force(time_list: [(int, int)]) -> int:
    '''
    Checks each multiple of the first bus' ID and sees if the correct sequence
    is formed with the other bus' IDs.
    '''
    multiplier = 1
    starting_points = dict()
    
    while True:    
        start = time_list[0][0] * multiplier
        broken_chain = () # bus_time, bus_index

        for time in time_list:
            time_stamp, index = time
            next = start + index
            remainder = next % time_stamp

            if remainder > 0:
                if not SIMPLE:
                    broken_chain = time
                break

            if time == time_list[-1]:
                return start

        if SIMPLE:
            multiplier += 1
        else:
            multiplier = jump_to_next_multiplier(
                time_list[0][0], multiplier, broken_chain, starting_points)
            
    

def jump_to_next_multiplier(base_time: int, multiplier: int, bus_info: (int, int), starting_points: {int: int}) -> int:
    '''
    Returns the next multiplier, calculated by finding the next mutiple of the
    other number that is also a multiple of the first number.
    '''
    bus_time, bus_index = bus_info

    # Determine starting points:
    if not bus_time in starting_points:
        starting_mult = _find_starting_point(base_time, bus_info)
        starting_points[bus_time] = starting_mult
    else:
        starting_mult = starting_points[bus_time]
        
    number_of_mults = math.floor(multiplier / bus_time)

    # Smallest {bus_mult} such that:
    # {bus_time} * {bus_mult} > {next_in_sequence}
    bus_mult = starting_mult + base_time * number_of_mults

    # Given that:
    # {base_time} * {multiplier} + {bus_index} = {bus_time} * {bus_mult}
    # Rearrange and solve for {multiplier}:
    new_mult = int((bus_time * bus_mult - bus_index) / base_time)

    # If the resulting multiplier is lower, get the next one
    cycles = 1
    while new_mult < multiplier:
        number_of_mults = math.floor(multiplier / bus_time) + cycles
        bus_mult = starting_mult + base_time * number_of_mults
        new_mult = int((bus_time * bus_mult - bus_index) / base_time)
        cycles += 1

    return new_mult



def _find_starting_point(base_time: int, bus_info: (int, int)) -> int:
    bus_time, bus_index = bus_info
    index = 0
    
    while True:
        start = (base_time * index + bus_index) / bus_time
        if start == math.floor(start):
            return int(start)
        else:
            index += 1


    
def _get_time_stamps() -> (int, [(int, int)]):
    '''
    Finds the text file specified by INPUT and returns its content as a tuple
    containing our earliest departure time and a list of tuples containing the
    timestamps for each bus and their index in the list (includes x's).
    '''
    file = open(INPUT, 'r')
    my_time = 0
    bus_times = []

    my_time = int(file.readline())
    data = file.readline().split(',')
    index = 0

    for time in data:
        try:
            bus_times.append((int(time), index))
            
        except ValueError:
            pass
        index += 1

    file.close()
    return my_time, bus_times



if __name__ == '__main__':
    run()
