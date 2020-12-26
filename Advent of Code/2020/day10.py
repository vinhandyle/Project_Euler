# Day 10: Adapter Array
# Part 1: 2470
# Part 2: 1973822685184

from pathlib import Path

INPUT = Path('input_10.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the product of all 1-jolt and 3-jolt difference connections if all
    adapters were used.
    '''
    jolt_list = _get_adapters()
    one_jolts = 0
    three_jolts = 0

    for index in range(len(jolt_list) - 1):
        curr = jolt_list[index]
        next = jolt_list[index + 1]
        
        if curr + 1 == next:
            one_jolts += 1
        elif curr + 3 == next:
            three_jolts += 1

    return one_jolts  * three_jolts 



def get_second_ans() -> int:
    '''Returns the number of unique ways to arrange the adapters'''
    jolt_list = _get_adapters()
    all_connections = _get_all_connections(jolt_list)

    # Iterates, from the bottom-up, through the list
    # of adapter-connections tuples.
    # The number of connections of each adapter is replaced by the total
    # number of connections of the adapters it can connect to.
    for index in range(len(all_connections) - 2, -1, -1):
        jolt, connections = all_connections[index]
        new_connections = 0
        for _index in range(index + 1, index + connections + 1):
            new_connections += all_connections[_index][1]
        all_connections[index] = (jolt, new_connections)

    return all_connections[0][1]



def _get_all_connections(jolt_list: [int]) -> [(int, int)]:
    '''
    Returns a list of tuples containing the joltage of each adapter and the
    number of adapters that can be connected to it.
    '''
    all_connections = []
    
    for index in range(len(jolt_list) - 1):
        curr = jolt_list[index]
        connections = 0

        for jolt in jolt_list[index + 1:]:
            if jolt > curr + 3:
                break
            else:
                connections += 1
        all_connections.append((curr, connections))

    return all_connections


    
def _brute_force(jolt_list) -> int:
    '''Traverses through all branches to find the answer'''
    return _sum_branches(jolt_list[:-1], 0)



def _sum_branches(jolt_list: [int], start: int) -> int:
    '''
    Returns the total number of different arrangements with the adapter at.
    '''
    sum = 0
    curr = jolt_list[start]

    # Checks each number whose index is greater than the current number
    # Stops if the checked number is > current number + 3
    # If the checked number is in the ideal range, call the function
    # on that number's index
    # If the checked number is the last number, add 1 to the total
    for index in range(start + 1, len(jolt_list)):
        jolt = jolt_list[index]
        
        if jolt > curr + 3:
            break
        else:
            if jolt == jolt_list[-1]:
                sum += 1
            else:
                sum += _sum_branches(jolt_list, index)
            
    return sum


def _get_adapters() -> [int]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    integers, ordered from least to greatest.
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

    # Orders then adds to the ends
    num_list.sort()
    num_list.append(num_list[-1] + 3)
    num_list.append(0)
    num_list.sort()
    
    return num_list


if __name__ == '__main__':
    run()
