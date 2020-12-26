# Day 6: Custom Customs
# Part 1: 6714
# Part 2: 3435

from pathlib import Path


INPUT = Path('input_6.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the sum of questions that each group answered yes to'''
    question_groups = _get_question_groups()
    sum = 0

    for group in question_groups:
        sum += len(_get_all_chars(group))

    return sum
        


def get_second_ans() -> int:
    '''
    Returns the sum of questions that every individual in each group answered
    yes to.
    '''
    question_groups = _get_question_groups()
    sum = 0

    for group in question_groups:
        sum += _common_questions(group)

    return sum



def _common_questions(group: [str]) -> int:
    '''
    Returns the number of questions that each individual in the group has in
    common.
    '''
    in_common = 0

    if len(group) == 1:
        in_common = len(group[0])
    else:
        char_list = _get_all_chars(group)
        for char in char_list:
            found = 0 # Number of strings the char appears in
            for string in group:
                if char in string:
                    found += 1
            if found == len(group):
                in_common += 1

    return in_common
    


def _get_all_chars(group: [str]) -> [str]:
    '''
    Given a list of strings, returns a list of all unique characters in those
    strings.
    '''
    char_list = []
    for string in group:
        for char in string:
            if not char in char_list:
                char_list.append(char)
    return char_list



def _get_question_groups() -> [[str]]:
    '''
    Finds the text file specified by INPUT and returns its content as a nested
    list of strings.
    '''
    file = open(INPUT, 'r')
    group_list = []
    people_list = []

    for line in file:
        if line.strip() == '':
            group_list.append(people_list)
            people_list = []
        else:
            people_list.append(line[:-1])

    file.close()
    group_list.append(people_list)
    return group_list


if __name__ == '__main__':
    run()
