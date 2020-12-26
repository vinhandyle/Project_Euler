# Problem 11: Largest product in a grid
# Answer: 70600674

from pathlib import Path

INPUT = Path('problem11.txt')
LENGTH = 4


def run() -> None:
    grid = _get_grid()
    largest = 0
    largest_in_group = [_largest_in_group(grid, 0, 1),
                        _largest_in_group(grid, 1, 0),
                        _largest_in_group(grid, 1, 1),
                        _largest_in_group(grid, 1, -1)]

    for num in largest_in_group:
        if num > largest:
            largest = num

    print(largest)



def _largest_in_group(grid: [[int]], row_delta: int, col_delta: int) -> int:
    '''Returns the largest product, given a directional grouping'''
    largest = 0
    rows = len(grid)
    cols = len(grid[0])
    start = 0

    if col_delta < 0:
        start = LENGTH - 1

    for row in range(rows - (LENGTH + 1) * row_delta):
        for col in range(start, cols - (LENGTH + 1) * abs(col_delta)):
            product = 1
            for i in range(LENGTH):
                new_row = row + i * row_delta
                new_col = col + i * col_delta
                
                product *= grid[new_row][new_col]
                
            if product > largest:
                largest = product

    return largest



def _get_grid() -> [[int]]:
    '''Returns a 2D list of integers'''
    file = open(INPUT, 'r')
    grid = []
    num_list = []

    for line in file:
        num = ''
        for char in line:
            if char == ' ' or char == '\n':
                num_list.append(int(num))
                num = ''
            else:
                num += char

        if len(num) > 0:
            num_list.append(int(num))
        grid.append(num_list)
        num_list = []

    file.close()
    return grid



if __name__ == '__main__':
    run()


