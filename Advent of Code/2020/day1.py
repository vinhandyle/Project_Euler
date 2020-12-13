# Day 1: Report Repair
# Part 1: 866436
# Part 2: 276650720

from pathlib import Path


INPUT = Path('input_1.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the product of the two entries in the expense report whose sum is
    2020.
    '''
    expense_report = _get_report()
    
    # Checks if the difference is in the report
    for entry in expense_report:
        partner_entry = 2020 - entry
        if partner_entry in expense_report:
            return entry * partner_entry
        else:
            expense_report.remove(entry)



def get_second_ans() -> int:
    '''
    Returns the product of the three entries in the expense report whose sum is
    2020.
    '''
    expense_report = _get_report()
    
    for entry in expense_report:
        sum_other_two = 2020 - entry
        report_copy = _copy_list(expense_report)

        # If a + b = c, then at least one (a or b)
        # is equal to or less than c / 2
        for copied_entry in report_copy:
            if copied_entry > sum_other_two / 2:
                report_copy.remove(copied_entry)

        # Checks if the report contains any entries
        # with the above description
        if len(report_copy) == 0:
            expense_report.remove(entry)
            continue

        # Checks if the sub-difference is in the report
        for copied_entry in report_copy:
            diff = sum_other_two - copied_entry
            if diff in expense_report:
                return entry * copied_entry * diff
            
        expense_report.remove(entry)        



def _get_report() -> [int]:
    '''
    Finds the text file called input_1.txt and returns its content as a list of
    integers.
    '''
    num_list = []
    file = open(INPUT, 'r')
    
    for line in file:
        num_list.append(int(line))

    file.close()
    return num_list



def _copy_list(master: [int]) -> [int]:
    '''Returns a copy of the given list of integers'''
    num_list = []
    for num in master:
        num_list.append(num)
    return num_list



if __name__ == '__main__':
    run()
