# Day 18: Operation Order
# Part 1: 9535936849815
# Part 2: 472171581333710

from pathlib import Path

INPUT = Path('input_18.txt')
DEBUG = False


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the sum of the results of each line of calculation'''
    calcs = _get_calcs()

    sum = 0
    for calc in calcs:
        sum += _perform_calc(calc)[0]

    return sum



def get_second_ans() -> int:
    '''Returns the sum of the results of each line of calculation'''
    calcs = _get_calcs()

    sum = 0
    for calc in calcs:
        sum += _perform_calc2(calc)

    return sum


def _perform_calc2(calc: str) -> int:
    '''
    Given a calculation in string form, returns its result.
    The order of operations goes: () -> + -> *, Left-to-right
    '''
    calc = _turn_into_list(calc)
    calc = _add_parens(calc)
    calc = _unpack_list(calc)

    new_calc = ''
    for char in calc:
        new_calc += char

    if DEBUG:
        print(new_calc)
    
    return _perform_calc(new_calc)[0]


def _turn_into_list(calc: str) -> 'nested list of str':
    '''Returns a nested list of strings representing the given calculation'''
    calc_list = []

    index = 0
    while index < len(calc):
        char = calc[index]
        if char == '(':
            sub_list, index_delta = _turn_into_list(calc[index + 1:])
            calc_list.append(sub_list)
            index += index_delta + 1

        elif char == ')':
            return calc_list, index

        else:
            calc_list.append(char)
            
        index += 1

    return calc_list



def _add_parens(calc: 'nested list of str') -> [str]:
    '''Adds sets of parentheses around summations'''
    calc_list = [] # Stores the end results
    temp_list = [] # Stores fragments for use in priority
    
    prev_num = None
    bind = None

    index = 0
    while index < len(calc):
        element = calc[index]

        # Parentheses
        if type(element) == list:
            sub_list = _add_parens(element)
            
            if bind:
                grouped_add = bind(prev_num, sub_list)
                temp_list.append(grouped_add)
                bind = None
            else:
                prev_num = sub_list
                temp_list.append(sub_list)
            
        else:
            # Priority Addition
            if element == '+':
                bind = lambda a, b: ['('] + a + ['+'] + b + [')']
                
                # If the temporary list has elements,
                # Interact with and then empty it
                if len(temp_list) > 0:
                    # If the temporary list has only one element,
                    # that means it stores a single number
                    # or a single group of numbers
                    if len(temp_list) == 1:
                        prev_num = temp_list

                    # If the temporary list has multiple elements,
                    # take the last element
                    else:
                        calc_list += temp_list[:-1]
                        prev_num == temp_list[-1]
                        
                    temp_list = []
        
            elif element == '*':
                temp_list.append(element)

            # Group numbers using addition
            else:
                if bind:
                    grouped_add = bind(prev_num, [element])
                    temp_list.append(grouped_add)
                    bind = None
                else:
                    prev_num = [element]
                    temp_list.append(element)               

        index += 1

    calc_list += temp_list
    return ['('] + calc_list + [')']



def _unpack_list(l: 'nested list') -> list:
    '''Returns a list given a nested list'''
    new_list = []
    for element in l:
        if type(element) == list:
            new_list += _unpack_list(element)
        else:
            new_list.append(element)
    return new_list



def _perform_calc(calc: str) -> int:
    '''
    Given a calculation in string form, returns its result.
    The order of operations goes: () -> + or *, Left-to-right
    '''
    result = 0
    operation = None

    index = 0
    while index < len(calc):
        char = calc[index]
        if char == '(':
            sub_result, index_delta = _perform_calc(calc[index + 1:])
            if operation:
                result = operation(result, sub_result)
            else:
                result = sub_result
            index += index_delta + 1

        elif char == ')':
            return result, index

        elif char == '+':
            operation = lambda x, y: x + y

        elif char == '*':
            operation = lambda x, y: x * y

        else:
            if index == 0:
                result = int(char)
            else:
                result = operation(result, int(char))
        
        index += 1

    return result, index



def _get_calcs() -> [str]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    strings.
    '''
    file = open(INPUT, 'r')
    calcs = [line[:-1].replace(' ', '') for line in file]
    file.close()
    return calcs


    
if __name__ == '__main__':
    run()
