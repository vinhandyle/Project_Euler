# Day 16: Ticket Translation
# Part 1: 29019
# Part 2: 517827547723

from pathlib import Path

INPUT = Path('input_16.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the ticket scanning error rate (the sum of all invalid values)'''
    fields, tickets = _get_reference()

    nearby_tickets = tickets[1:]

    sum = 0
    for ticket in nearby_tickets:
        for i in range(len(ticket)):
            valid = False
            
            for field in fields:
                if _in_range(field, ticket[i]):
                    valid = True
                    break

            if not valid:
                sum += ticket[i]

    return sum



def get_second_ans() -> int:
    '''
    Returns the product of the values of the six fields starting with departure.
    '''
    fields, tickets = _get_reference()

    our_ticket = tickets[0]
    nearby_tickets = tickets[1:]

    # Remove invalid tickets
    for ticket in nearby_tickets:
        for i in range(len(ticket)):
            valid = False
            
            for field in fields:
                if _in_range(field, ticket[i]):
                    valid = True
                    break
                
            if not valid:
                tickets.remove(ticket)

    # Find possible fields for each value
    sort_list = []
    for index in range(len(fields)):
        potential_list = []
        for i in range(len(our_ticket)):
            correct_index = True
            for ticket in tickets:
                if not _in_range(fields[index], ticket[i]):
                    correct_index = False
            if correct_index:
                potential_list.append(i)
            else:
                continue
        sort_list.append(potential_list)

    # Sort ticket values
    sort_list = _allocate_to_best(sort_list)
    
    new_ticket = [0] * len(our_ticket)
    for index in range(len(our_ticket)):
        new_ticket[index] = our_ticket[sort_list[index]]

    our_ticket = new_ticket
       
    # Multiply first six fields
    product = 1
    for i in range(6):
        product *= our_ticket[i]

    return product
    


def _allocate_to_best(sort_list: [[int]]) -> [int]:
    '''
    Given a list of lists of possible values for each field, returns a list of
    integers representing the configuration which uses all values without
    duplicates.
    '''
    num_list = [0] * len(sort_list)
    sort_dict = dict()

    for i in range(len(sort_list)):
        sort_dict[i] = sort_list[i]

    while len(sort_dict) > 0:
        for key in sort_dict:
            if len(sort_dict[key]) == 1:
                num = sort_dict[key][0]
                num_list[key] = num
                _remove_from_all_lists(sort_dict, num)
                sort_dict.pop(key)
                break
    
    return num_list



def _remove_from_all_lists(d: {int: [int]}, n: int) -> None:
    '''Removes a number from each list in the dictionary'''
    for key in d:
        d[key].remove(n)


        
def _in_range(ranges: [int], value: int) -> bool:
    '''Returns True if the value is within the ranges. Returns False otherwise'''
    return ranges[0] <= value <= ranges[1] or \
           ranges[2] <= value <= ranges[3]



def _get_reference() -> ([[int]], [[int]]):
    '''
    Finds the text file specified by INPUT and returns its content as a tuple
    containing a list of tuples containing ranges of different fields, and a
    list of ticket values which are also lists.
    '''
    file = open(INPUT, 'r')
    fields = []
    tickets = []

    mode = 'field'

    for line in file:
        if line == 'your ticket:\n' or \
           line == 'nearby tickets:\n' or \
           line == '\n':
            mode = 'ticket'
            continue

        else:
            num_list = []
            if mode == 'ticket':
                ticket = line.split(',')
                for i in range(len(ticket)):
                    ticket[i] = int(ticket[i])
                tickets.append(ticket)
                
            elif mode == 'field':
                num = ''
                for char in line:
                    if char == '-' or \
                       char == ' ' or \
                       char == '\n':
                        if len(num) > 0:
                            num_list.append(int(num))
                            num = ''
                    
                    try:
                        int(char)
                        num += char

                    except ValueError:
                        continue
                fields.append(num_list)     

    file.close()
    return fields, tickets



if __name__ == '__main__':
    run()
