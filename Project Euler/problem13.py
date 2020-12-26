# Problem 13: Large sum
# Answer: 5537376230

from pathlib import Path

INPUT = Path('problem13.txt')

def run() -> None:
    num_list = _get_num_list()

    sum = 0

    for num in num_list:
        sum += num

    digits = list(str(sum))
    for digit in digits[:10]:
        print(digit, end = '')



def _get_num_list() -> [int]:
    file = open(INPUT, 'r')
    num_list = []

    for line in file:
            num_list.append(int(line))

    file.close()
    return num_list



if __name__ == '__main__':
    run()


