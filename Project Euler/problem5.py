# Problem 5: Smallest multiple
# Answer: 232792560

import euler


UPPER_BOUND = 20


def run() -> None:
    factor_list = []
    for i in range(2, UPPER_BOUND + 1):
        prime_list = deconstruct_into_prime_factors(i)
        create_super_set(factor_list, prime_list)

    total = 1
    for f in factor_list:
        total *= f
    print(total)
    


def create_super_set(super_set: [int], sub_set: [int]) -> None:
    '''
    Makes sure the first list contains all elements in the second list, including
    repeats (super: [1, 2], sub: [1, 1] -> super: [1, 2, 1])
    '''
    super_copy = euler.duplicate_list(super_set)

    for num in sub_set:
        if num in super_copy:
            super_copy.remove(num)
        else:
            super_set.append(num)



def deconstruct_into_prime_factors(num: int) -> [int]:
    '''
    Given a number, returns a list of prime numbers which multiplied together
    equals the given number.
    '''
    num_list = []

    prime, ambig = first_factor_pair(num)
    num_list.append(prime)
    
    while not euler.is_prime_number(ambig):
        prime, ambig = first_factor_pair(ambig)
        num_list.append(prime)

    num_list.append(ambig)
    
    return num_list



def first_factor_pair(num: int) -> (int, int):
    '''
    Returns the first factor pair for a given number:
    xy = num, where x is the smallest factor of num greater than 1
    '''
    index = 2
    while num % index != 0:
        index += 1

    return (index, int(num / index))
    


if __name__ == '__main__':
    run()
