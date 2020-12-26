# Problem 18: Maximum path sum I
# Answer: 1074

from pathlib import Path

INPUT = Path('problem18.txt')
DEBUG = False


def run() -> None:
    triangle = _get_triangle()
    largest = _brute_force(triangle)
    print(largest)



def _brute_force(triangle: [[int]]) -> int:
    '''
    Traverses and takes the sum of each branch, comparing it to the current
    largest value.
    Branches are stored as a list of 1s and 0s where the value at each index
    indicates the distance horizontal between the current and previous nodes
    (0 = directly beneath, 1 = one column to the right).
    '''
    rows = len(triangle)
    indexes = [0] * rows
    largest = 0

    while True:
        sum = 0

        # Update place values (can only be 0 or 1)
        for i in range(len(indexes) - 1, 0, -1):
            if indexes[i] > 1:
                indexes[i - 1] += 1
                indexes[i] = 0

        if indexes[0] > 0:
            break

        # Sum branch
        for row in range(rows):
            col = _sum_up_to(indexes, row)
            sum += triangle[row][col]

        if sum > largest:
            largest = sum

        if DEBUG:
            print(indexes, largest)
        indexes[-1] += 1

    return largest



def _sum_up_to(num_list: [int], index: int) -> int:
    '''
    Returns the sum of every integer in the given list up to the one in the
    given index.
    '''
    sum = 0
    for i in range(index):
        sum += num_list[i]
    return sum + num_list[index]



def _get_triangle() -> [[int]]:
    '''Returns a nested list of integers representing a triangle'''
    triangle = []
    file = open(INPUT, 'r')

    for line in file:
        section = []
        chunk = ''
        for char in line:
            if char == ' ':
                section.append(int(chunk))
                chunk = ''
            else:
                chunk += char
        section.append(int(chunk))
        triangle.append(section)

    file.close()
    return triangle
                


if __name__ == '__main__':
    run()
