# This module contains tools that can be used for many different problems.



# Special
def fibonacci_num(index: int) -> int:
    '''Returns the nth fibonacci number'''
    if index == 0 or index == 1:
        return 1
    else:
        return fibonacci_num(index - 1) + fibonacci_num(index - 2)



# Utility
def is_prime_number(num: int) -> bool:
    '''Returns whether a number is a prime number'''
    num = int(num)

    # Easy filter for even numbers
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    for index in range(3, num, 2):
        if num % index == 0:
            return False

    return True



def list_unique_factors(num: int) -> [int]:
    '''Given a number, returns a list of its factors'''
    num_list = []
    
    for index in range(1, num):
        # If we encounter a repeat, that means we've found all factors
        if index in num_list:
            break
        else:
            # If a factor is found, add it and its partner to the list
            if num % index == 0:
                num_list.append(index)
                partner = int(num / index)
                if not partner in num_list:
                    num_list.append(partner)

    return num_list



def duplicate_list(l: list) -> list:
    '''Returns a copy of the given list'''
    new_list = []
    for element in l:
        new_list.append(element)
    return new_list


