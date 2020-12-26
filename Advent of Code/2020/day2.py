# Day 2: Password Philosophy
# Part 1: 383
# Part 2: 272

from pathlib import Path


INPUT = Path('input_2.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    database = _get_database()
    num_valid = 0
    
    for entry in database:
        if _is_valid(entry):
            num_valid += 1
            
    return num_valid



def get_second_ans() -> int:
    database = _get_database()
    num_valid = 0

    for entry in database:
        if _is_more_valid(entry):
            num_valid += 1

    return num_valid



def _is_more_valid(entry: (int, int, str, str)) -> bool:
    '''
    Returns True if the entry is valid. Returns False otherwise.
    An entry is valid if a given character appears within one of the two (and
    not both) given indexes of a given string.
    '''
    index1, index2, letter, password = entry
    if (password[index1 - 1] == letter or password[index2 - 1] == letter) and \
       password[index1 - 1] != password[index2 - 1]:
        return True
    else:
        return False


    
def _is_valid(entry: (int, int, str, str)) -> bool:
    '''
    Returns True if the entry is valid. Returns False otherwise.
    An entry is valid if a given character appears within a given number of
    times in a given string.
    '''
    min, max, letter, password = entry
    occurences = _times_appeared_in(letter, password)

    if min <= occurences <= max:
        return True
    else:
        return False



def _times_appeared_in(c: str, s: str) -> int:
    '''
    Returns the number of times a given character appears in a given string.
    '''
    times = 0
    for char in s:
        if char == c:
            times += 1
    return times


    
def _get_database() -> [(int, int, str, str)]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    tuples containing (a, b, c, d) where a and b are the minimum and maximum
    number of occurences of c in d.
    '''
    data_list = []
    file = open(INPUT, 'r')

    for line in file:
        min, max, letter, password = (0, 0, '', '')
        index = 0
        chunk = ''

        while index < len(line):
            char = line[index]
            if char == '-':
                min = int(chunk)
                chunk = ''
                
            elif char == ' ':
                max = int(chunk)
                chunk = ''

            elif char == ':':
                letter = chunk
                chunk = ''
                index += 1

            elif char == '\n':
                password = chunk

            else:
                chunk += char  
            index += 1
            
        data_list.append((min, max, letter, password))

    file.close()
    return data_list



if __name__ == '__main__':
    run()
