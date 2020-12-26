# Day 14: Docking Data
# Part 1: 11612740949946
# Part 2: 3394509207186

from pathlib import Path

import math

INPUT = Path('input_14.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the sum of all values left in memory'''
    program = _get_program()
    sum = 0

    mem_list = dict()

    for section in program:
        bitmask, actions = section
        temp_mem = _dup_list(bitmask)
        
        for action in actions:
            address, value = action
            temp_mem = _dup_list(_int_to_binary(value))
            _mask_list(bitmask, temp_mem)
            mem_list[address] = _binary_to_int(temp_mem)

    for mem in mem_list:
        sum += mem_list[mem]

    return sum



def get_second_ans() -> int:
    '''Returns the sum of all values left in memory using version 2'''
    program = _get_program()
    sum = 0

    mem_list = dict()

    for section in program:
        bitmask, actions = section
        
        for action in actions:
            address, value = action
            temp_mem = _dup_list(_int_to_binary(value))

            masked_addresses = _mask_list2(bitmask, _int_to_binary(address))

            for masked_address in masked_addresses:
                _address = _binary_to_int(masked_address)
                mem_list[_address] = _binary_to_int(temp_mem)

    for mem in mem_list:
        sum += mem_list[mem]

    return sum



def _int_to_binary(num: int) -> int:
    '''
    Given an integer, returns a list of 1s and 0s representing the number's
    binary form.
    '''
    binary = [0] * 36

    for i in range(36):
        binary[i] = math.floor(num / math.pow(2, 35 - i))
        num -= binary[i] * math.pow(2, 35 - i)

    return binary



def _binary_to_int(num_list: [int]) -> int:
    '''Given a list of 1s and 0s, returns an integer'''
    num = 0

    for i in range(36):
        num += num_list[i] * math.pow(2, 35 - i)

    return int(num)



def _mask_list2(mask: [int, str], num_list: [int]) -> [[int]]:
    '''
    Writes 1s and Xs into num_list where they appear in the mask.
    Returns a list of binary lists for the floating bits.
    '''
    size = 0
    for i in range(36):
        if mask[i] != 0:
            num_list[i] = mask[i]
            if mask[i] == 'X':
                size += 1

    return _floating_lists(num_list, size)



def _floating_lists(num_list: [int, str], size: int) -> [[int]]:
    '''
    Returns a list of binary lists where the Xs are replaced with every
    combination of 1s and 0s.
    '''
    super_list = []

    # The combination of 1s and 0s is stored as a binary number
    # since the Xs will be replaced by those 1s and 0s
    for i in range(int(math.pow(2, size))):
        float_list = _int_to_binary(i)[36 - size:]
        sub_list = _dup_list(num_list, 'X')
        float_index = 0

        for index in range(36):
            if sub_list[index] == 'X':
                sub_list[index] = float_list[float_index]
                float_index += 1

        super_list.append(sub_list)


    return super_list



def _mask_list(mask: [int, str], num_list: [int]) -> None:
    '''Writes into num_list 1s and 0s where they appear in the mask'''
    for i in range(36):
        if mask[i] != 'X':
            num_list[i] = mask[i]



def _dup_list(num_list: [int, str], x = 0) -> [int]:
    '''Returns a copy of a list, replacing every X with a character'''
    new_list = []
    
    for num in num_list:
        if num == 'X':
            new_list.append(x)
        else:
            new_list.append(num)

    return new_list



def _get_program() -> [([int], [(int)])]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    tuples containing two lists: the mask and the actions.
    The mask is a list of integers, while the actions are a list of tuples
    containing the memory address and value.
    '''
    file = open(INPUT, 'r')
    program = []
    mask = []
    actions = []

    for line in file:
        if line[:4] == 'mask':
            if len(mask) > 0 and len(actions) > 0:
                program.append((mask, actions))
                mask = []
                actions = []

            
            for char in line[6:]:
                try:
                    mask.append(int(char))
                    
                except ValueError:
                    if char == 'X':
                        mask.append(char)
        else:
            mode = 'address'
            address = ''
            value = ''

            for char in line:
                if mode == 'address':
                    if char == '=':
                        mode = 'value'
                        address = int(address)
                    else:
                        try:
                            int(char)
                            address += char
                        except ValueError:
                            pass
                elif mode == 'value':
                    if char == '\n':
                        value = int(value)
                        actions.append((address, value))
                    else:
                        try:
                            int(char)
                            value += char
                            
                        except ValueError:
                            pass

    if len(mask) > 0 and len(actions) > 0:
        program.append((mask, actions))
        
    file.close()
    return program



if __name__ == '__main__':
    run()
