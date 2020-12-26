# Problem 8: Largest product in a series
# Answer: 23514624000

from pathlib import Path


INPUT = Path('problem8.txt')
RANGE = 13

def run() -> None:
    num_list = _get_num_list()
    largest = 0
    for index in range(len(num_list) - RANGE):
        product = 1
        for i in range(RANGE):
            product *= num_list[index + i]
        if product > largest:
            largest = product
    print(largest)



def _get_num_list() -> [int]:
    '''Returns the 1000 digit number as a list of integers'''
    num_list = []
    file = open(INPUT, 'r')

    for line in file:
        for char in line:
            try:
                num_list.append(int(char))
            except:
                pass

    file.close()
    return num_list



if __name__ == '__main__':
    run()
